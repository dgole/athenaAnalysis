#!/bin/bash

#SBATCH -J acf34
#SBATCH --time=48:00:00
#SBATCH -N 1
#SBATCH --ntasks 1
#SBATCH -p normal

# The following commands will be executed when this script is run.

module load gcc python3

export DIR=../../turbTest/run34/bin/

python3 acf_fullCalc.py $DIR




#
