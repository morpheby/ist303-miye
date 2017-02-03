"""
 pyinstaller_hack.py
 ist303-miye
 
Copyright (C) 2017 

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version. 
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA 
"""
        

"""
Hack to make PyInstaller work with Venusian using some very deep-hidden APIs
of Python itself and internals of the PyInstaller. Based on
pkgutil._iter_file_finder_modules code.

Links:
https://hg.python.org/cpython/file/3.6/Lib/pkgutil.py
http://stackoverflow.com/questions/1466676/create-a-wrapper-class-to-call-a-pre-and-post-function-around-existing-functions
http://stackoverflow.com/questions/1647586/is-it-possible-to-change-an-instances-method-implementation-without-changing-al
https://docs.python.org/3/library/importlib.html
https://docs.python.org/3/library/pkgutil.html
"""

_nofix = True
try:
    from pyimod03_importers import (FrozenImporter, FrozenPackageImporter,
                                         SYS_PREFIX, SYS_PREFIXLEN)
    import pyimod01_os_path as pyi_os_path
    from pkgutil import iter_importer_modules
    import sys
    import types
    
    _nofix = False
except Exception as e:
    pass

if not _nofix:

    class FrozenImporterWrapper(object):
        def __init__(self, fi, path = None, fullname = None):
            self._fi = fi
            if path:
                if path.startswith(SYS_PREFIX):
                    self.path = path[SYS_PREFIXLEN+1:].replace(pyi_os_path.os_sep, '.')
                else:
                    raise
            else:
                self.path = None
            self._fullname = fullname
            self.iter_modules = types.MethodType(_frozen_importer_iter_modules, self)

        def load_module(self, fullname):
            return self._fi.load_module(fullname, self._fullname)
    
        def __getattr__(self,attr):
            attr = self._fi.__getattribute__(attr)
            if callable(attr):
                def hooked(*args, **kwargs):
                    result = attr(*args, **kwargs)
                    # prevent wrapped_class from becoming unwrapped
                    if result == self._fi:
                        return self
                    return result
                return hooked
            else:
                return attr
    
        def __call__(self, path):
            result = self._fi(path)
            if result == self._fi:
                return FrozenImporterWrapper(self._fi, path)
            elif isinstance(result,FrozenPackageImporter):
                return FrozenPackageImporter(self._fi, path, result._fullname)
            else:
                raise
                
    
    def new_call_factory(old_call):
        def new_call(self, path):
            result = old_call(path)
            if result == self:
                return FrozenImporterWrapper(self, path)
            elif isinstance(result,FrozenPackageImporter):
                return FrozenPackageImporter(self, path, result._fullname)
            else:
                raise
        return new_call
    
    def _frozen_importer_iter_modules(importer, prefix):

        yielded = {}
        modules = list(importer.toc)
        modules.sort()  # handle packages before same-named modules

        for modname in modules:
            if modname=='__init__' or modname in yielded:
                continue
                
            fullname = None
            module_imp = importer.find_module(modname)
            if hasattr(module_imp, '_fullname'):
                fullname = module_imp._fullname
                
            if not fullname:
                fullname = modname
            
            if not hasattr(importer, 'path'):
                continue
            
            if importer.path and not fullname.startswith(importer.path + '.'):
                continue
            else:
                modname = fullname[len(importer.path)+1:]
                
            ispkg = importer.is_package(importer.path + '.' + modname)

            if modname and '.' not in modname:
                yielded[modname] = 1
                yield prefix + modname, ispkg

    iter_importer_modules.register(FrozenImporter, _frozen_importer_iter_modules)
    
    # Replace FrozenImporter with our wrapper
    def wrap_importer():
        for fr_imp in [x for x in set(sys.meta_path + sys.path_hooks) if isinstance(x,FrozenImporter)]:
            oldcall = fr_imp.__call__
            oldclass = type(fr_imp)
            methods = dict(oldclass.__dict__)
            methods['__call__'] = types.MethodType(new_call_factory(oldcall), fr_imp)
            newclass = type(oldclass.__name__,oldclass.__bases__,methods)
            fr_imp.__class__ = newclass
            fr_imp.iter_modules = types.MethodType(_frozen_importer_iter_modules, fr_imp)
    wrap_importer()
    
    

