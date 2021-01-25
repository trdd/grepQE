#!/bin/env python

from ase import io
from ase import units
import sys
import argparse
import glob
import matplotlib.pyplot as plt
import os.path as path
import numpy as np

# command line arguments
parser = argparse.ArgumentParser('Quickly get some cell info from several qe calcs')
parser.add_argument('-p', '--pre', type=str, default='', help='directory prefix to look for outfiles')
parser.add_argument('-f', '--file', type=str, default='*.out', help='outfile wildcard')
parser.add_argument('--plot', action='store_true')
parser.add_argument('-m', '--mode', default='cell', choices=['cell', 'to_cif'])
parser.add_argument('--units', default='eV', choices=['eV', 'Ry'])
args = parser.parse_args()
dirs = glob.glob(args.pre+'*/')
vals = [d.lstrip(args.pre).rstrip('/') for d in dirs]
vals = [float(t) if t.isdigit() else t for t in vals]
ind = np.argsort(vals)

if args.mode == 'cell':
    if args.units == 'eV':
        fac = 1.
    elif args.units == 'Ry':
        fac = units.create_units('2006')['Ry']   #CODATA 2006 is hard coded in ase.
    ostr = '{:<10.6} '+7*'{:>10.6} '+'{:>20.15}'
    print(ostr.format('# '+args.pre, 'a', 'b', 'c', 'al', 'be', 'ga', 'V', 'energy'))
    for i in ind:
        outf = glob.glob(path.join(dirs[i],args.file))
        for f in outf:
            try:
                out = io.read(f, format='espresso-out')
                print(ostr.format(vals[i], *out.cell.cellpar(), out.cell.volume, out.get_total_energy()/fac))
            except Exception as e:
                pass

elif args.mode == 'to_cif':
    for i in ind:
        outf = glob.glob(path.join(dirs[i],args.file))
        for f in outf:
            try:
                out = io.read(f, format='espresso-out')
                io.write(args.pre+str(vals[i])+'_result.cif', out)
            except Exception as e:
                pass
