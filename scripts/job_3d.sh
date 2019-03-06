#!/bin/bash

#SBATCH -J 3d
#SBATCH --time=2:00:00
#SBATCH -N 1
#SBATCH --ntasks 64
#SBATCH -p development

# The following commands will be executed when this script is run.
module load gcc
module load python3

export DIR=$SCRATCH/parSgTurb/data/prodRuns/

python3 multi_plots3d.py 11? $DIR

#python3 plots3d_multiPanel.py 1.e-3 0.1 $DIR
#python3 plots3d_par.py 64 $DIR
#python3 plots3d.py   $DIR
#python3 pspec.py     $DIR
#python3 pspec_timeEvo.py $DIR
#python3 acf.py       $DIR
#python3 slices3d.py  $DIR
#python3 gas_multiPanelAnimation.py $DIR 1.e-4







#
