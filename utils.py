from os import error
import sys 



PY2 = sys.version_info[0] == 2 
PY3 = sys.version_info[0] == 3



if PY2:
    def is_valid_string(var):
        return isinstance(var, basestring)

elif PY3:
    def is_valid_string(var):
        return isinstance(var, str)

else:
    raise SystemError("Python version wrong pyrohn")
