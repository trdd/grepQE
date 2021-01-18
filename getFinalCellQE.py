#!/usr/bin/env python
import re
import sys
with open(sys.argv[1], 'r') as f:
    s = f.read()
    c = re.findall('(?<=Begin final coordinates)[\S\s]*(?=End final coordinates)',
            s)
    print('\n'.join(c[0].split('\n')[4:]))
