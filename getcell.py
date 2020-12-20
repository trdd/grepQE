#!/bin/env python

from ase import io
import sys
import argparse
import glob
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser('Quickly get some cell info from several qe calcs')
parser.add_argument('--pre', metavar=fn, type=str, nargs=1, default='', help='directory prefix to look for outfiles')
parser.add_argument('--plot', action='store_true')
parser
args = parser.parse_args()

dirs = 


for f in sys.argv[1:]:
    out = io.read(f, format='espresso-out')
    print(f, out.cell.cellpar())
