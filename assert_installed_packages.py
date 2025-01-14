import sys
import importlib

for check in sys.argv[1:]:
    module, status = check.split('=')
    status = int(status)
    try:
        importlib.import_module(module)
    except ImportError:
        if status == 1:
            print(f"{module} was not installed but was expected")
            sys.exit(1)
    else:
        if status == 0:
            print(f"{module} was installed but was not expected")
            sys.exit(1)
