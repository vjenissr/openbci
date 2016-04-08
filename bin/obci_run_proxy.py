#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

import sys
import os
import os.path
import importlib


def lchop(astring, trailing):
    thelen = len(trailing)
    if astring[:thelen] == trailing:
        return astring[thelen:]
    return astring


def rchop(astring, trailing):
    thelen = len(trailing)
    if astring[-thelen:] == trailing:
        return astring[:-thelen]
    return astring


def sanitize_module_name(name):
    digits = '0123456789'
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_' + digits
    name = str(name)
    name_filtered = ''
    for ch in name:
        if ch in allowed_chars:
            name_filtered += ch
    name = name_filtered
    while len(name) > 0 and name[0] in digits:
        name = name[1:]
    return name


def sanitize_path(path):
    path = str(path).strip()
    path = os.path.expanduser(path)
    path = os.path.realpath(path)
    return path


def try_local_path_file():
    try:
        if sys.platform.startswith('win'):
            fname = os.path.expanduser('~user/obci/local_path')
        else:
            fname = os.path.expanduser('~/.obci/local_path')

        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                return f.read().strip()
        else:
            return None
    except Exception as ex:
        print(ex)
        return None


def try_env_variable():
    try:
        if 'OBCI_INSTALL_DIR' in os.environ:
            return os.environ['OBCI_INSTALL_DIR']
    except Exception as ex:
        print(ex)
        return None


if __name__ == '__main__':
    opt_name = '--obci-run-module='
    for v in sys.argv:
        if v.startswith(opt_name):
            bin_name = lchop(v, opt_name).strip()
            sys.argv.remove(v)
            break
    else:
        # this mode assumes this file is symlinked from a file with module name
        bin_name = os.path.basename(__file__)
        bin_name = rchop(bin_name, '.py')
        bin_name = rchop(bin_name, '.pyc')
        bin_name = rchop(bin_name, '.pyo')

    bin_name = sanitize_module_name(bin_name)

    try_list = [try_local_path_file, try_env_variable]

    for try_func in try_list:
        local_path = try_func()
        if local_path is None:
            continue
        local_path = sanitize_path(local_path)
        if local_path and os.path.isdir(local_path):
            sys.path.insert(1, os.path.realpath(local_path))
            break

    try:
        if bin_name == 'obci':
            import obci.cmd.obci as module
        elif bin_name == 'obci_gui':
            import obci.cmd.obci_gui as module
        elif bin_name == 'obci_tray':
            import obci.cmd.obci_tray as module
        elif bin_name == 'obci_server':
            import obci.cmd.obci_server as module
        elif bin_name == 'obci_experiment':
            import obci.cmd.obci_experiment as module
        else:
            module_name = 'obci.cmd.{}'.format(bin_name)
            module = importlib.import_module(module_name)
        sys.exit(module.run())
    except ImportError as ie:
        print('OpenBCI Run Proxy Script')
        print('Couldn\'t import \'obci.cmd.{}\' module.'.format(bin_name))
        print('Script location: {}'.format(os.path.abspath(__file__)))
        print('ImportError exception: {}'.format(ie))
        print('Import path:')
        print('\n'.join(sys.path))
        sys.exit(1)