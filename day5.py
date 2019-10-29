#!/usr/bin/env python
import sys
import json
import pip
import site
import yaml
from pip._internal.utils.misc import get_installed_distributions


def vers_python():
    p_vers = sys.version[0:5]
    v_env = sys.prefix
    p_exe = sys.executable
    pi_vers = pip.__version__
    s_pack = site.getsitepackages()
    p = get_installed_distributions()
    j = 0
    dict1 = {}
    for i in p:
        dict1[p[j].key] = p[j].version
        j += 1
    dict2 = {}
    dict2['python vers'] = p_vers
    dict2['virtualenv'] = v_env
    dict2['exec location'] = p_exe
    dict2['pip version'] = pi_vers
    dict2['site packages location'] = s_pack
    dict2['installed packages'] = dict1
    return dict2


with open('data.json', 'w') as outfile:
    json.dump(vers_python(), outfile, indent=4)

with open('data.yaml', 'w') as file:
    yaml.dump(vers_python(), file)
