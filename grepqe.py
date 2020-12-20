#!/bin/env python

from ase import io
import sys
import argparse
import glob
import matplotlib.pyplot as plt
import os.path as path

parser = argparse.ArgumentParser('Quickly get some cell info from several qe calcs')
parser.add_argument('--pre', metavar=p, type=str, nargs=1,* default='', help='directory prefix to look for outfiles')
parser.add_argument('--file', metavar=fn, type=str, nargs=1, default='*.out', help='directory prefix to look for outfiles')
parser.add_argument('--plot', action='store_true')
parser
args = parser.parse_args()

dirs = glob.glob(args.pre+'*/')
ostr = 7*'{:10.6} '+'\n'
for d in dirs:
    curr = d.lstrip(args.pre)
    outf = glob.glob(path.join(d,args.fn))
    for f in outf:
        try:
            out = io.read(f, format='espresso-out')
            print(ostr.format(curr, *out.cell.cellpar())
        except Exception as e:
            pass
