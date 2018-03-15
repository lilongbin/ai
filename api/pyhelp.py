#! /usr/bin/env python
# coding=utf-8

import sys
try:
    input = raw_input
except:
    pass
def show_help_info():
    msg = "\033[01mHelp: \033[0m"
    module = input(msg).strip()
    if not module:
        return
    if module.lower() == 'quit' or module.lower() == 'q':
        sys.exit(0)
    #try:
    #    table = str.maketrans({'.':None, '_':None})
    #except:
    #    import string
    #    table = string.maketrans('._', '00')
    #if not module.translate(table).isalnum():
    digits = '0123456789'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    valid_chars = digits + letters + "._"
    for chr in module:
        if chr not in valid_chars:
            print('ERROR: %s: invalid module or function name' % module)
            return
    try:
        import_module = 'import %s' % module
        exec(import_module)
        print('import %s' % module)
    except ImportError as reason:
        # import function name would cause ImportError
        # goto call help function name
        pass
    except Exception as reason:
        print(reason)
    try:
        help('%s' % module)
    except Exception as reason:
        print(reason)

if __name__ == '__main__':
    version = '.'.join([str(v) for v in sys.version_info[:3]])
    print('Python %s' % version)
    while True:
        show_help_info()
