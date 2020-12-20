#!/bin/env python

from ase import io
import sys
import argparse
import glob
import matplotlib.pyplot as plt
import os.path as path
import numpy as np

parser = argparse.ArgumentParser('Quickly get some cell info from several qe calcs')
parser.add_argument('--pre', type=str, default='', help='directory prefix to look for outfiles')
parser.add_argument('--file', type=str, default='*.out', help='directory prefix to look for outfiles')
parser.add_argument('--plot', action='store_true')
args = parser.parse_args()
dirs = glob.glob(args.pre+'*/')
vals = [d.lstrip(args.pre).rstrip('/') for d in dirs]
vals = [float(t) if t.isdigit() else t for t in vals]
ind = np.argsort(vals)

ostr = 7*'{:10.6} '
for i in ind:
    outf = glob.glob(path.join(dirs[i],args.file))
    for f in outf:
        try:
            out = io.read(f, format='espresso-out')
            print(ostr.format(vals[i], *out.cell.cellpar()))
        except Exception as e:
            pass

