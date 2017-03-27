#!/usr/bin/env bash

# Copyright (C) 2016
# Ilya Mikhaltsou
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA

### Script settings ###

# Template for temporary file
properties_script_template="$(basename $0).sed.XXXX"
properties_script=

### Function: cleanup ###
# Synopsis: Removes temporary files
function cleanup () {
    if [ -n ${properties_script} ]; then
        rm -f ${properties_script}
    fi
}

### Function: build_error ###
# Synopsis: Reports error to stderr and exits script
function build_error() {
    echo "$0: Error: $1" >&2
    cleanup
    exit 1
}

# Properties template file
input_file=$1
properties=$2
if [[ $# == 2 || ( $# > 2 && $3 == '-h' ) ]]; then
    output_file="$(echo "$input_file" | sed -E 's/^(.*)\.[a-zA-Z0-9_]+$/\1/g')"
elif [[ $# == 3 || ( $# > 3 && $4 == '-h' ) ]]; then
    output_file=$3
else
    build_error "Wrong arguments. Usage: \n$0 input_file {properties|-} [output_file] [-h [string]]"
fi

# Disable header output
if [[ ( $# == 3 && x$3 == x'-h' ) || ( $# == 4 && x$4 == x'-h' ) ]]; then
	no_header=1
else
	no_header=0
fi

if [[ $# == 4 && x$3 == x'-h' ]]; then
	header=$4
elif  [[ $# == 5 && x$4 == x'-h' ]]; then
	header=$5
else
	header='//'
fi

### Function: prepare_settings ###
# Synopsis: Reads configuration files and transforms them into a sed script to apply
# Input: settings_file_name output_file
function prepare_settings() {
    if [ $# -lt 2 ]; then
        build_error "Wrong use of function prepare_settings - no arguments supplied"
    fi

    if [ ! -e $2 ]; then
        touch $2
    fi

    if [ ! -w $2 ]; then
        build_error "Unable to write to temporary file"
    fi

    # Escapes all metacharacters and creates sed script
    cat $1 | sed -E															\
        -e 's/^\/\/.*$//g'													\
        -e 's/^\#.*$//g'													\
        -e 's/^[  ]+$//g' | perl												\
        -e 'while (!eof(*STDIN)) { print quotemeta(<STDIN>); }' | sed -E		\
        -e 's/\\$//g'														\
        -e 's:^([a-zA-Z0-9_]+)\\=(.*)$:s/@\1@/\2/g:g'					\
    >> $2																	\
    || build_error "Unexpected error while parsing settings. Check syntax"
}

### main ###

if [ ${input_file} != "-" -a ! -r ${input_file} ]; then
    build_error "Unable to access ${input_file}"
fi

# Check if we actually need to update properties
if [ -e ${output_file}                                       \
  -a ${output_file} -nt ${input_file}                      \
  -a ${output_file} -nt ${properties}                      \
  -a ${output_file} -nt $0 ]; then
    cleanup
    exit 0
fi

rm -f ${output_file}
touch ${output_file}

# Create temp file to store sed script
properties_script=`mktemp ${properties_script_template}`

# Get settings
prepare_settings ${properties} ${properties_script}


# Print header
if [[ ${no_header} == 0 ]]; then
	header_sed="$(echo ${header} | sed -E 's@([#_\\])@\\\1@g')"
	sed -E "s:@:${header_sed}:g" >> ${output_file} <<EOF
@ DON'T EDIT THIS FILE.
@ THIS FILE IS AUTOGENERATED FROM
@ ${input_file} FILE WITH CONFIGURATION
@ FROM ${properties}. EDIT THESE FILES
@ INSTEAD.

EOF
fi

# Now run sed on input
cat ${input_file} | sed -f ${properties_script} >> ${output_file} \
    || build_error "Unexpected error while generating properties file: $(cat ${properties_script})"

cleanup
