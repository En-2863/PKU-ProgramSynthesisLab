#!/bin/sh
python3 -u main.py $1 training_data.sl
#pypy3 -u main.py $1 # it will be 50%-200% slower than python3 unless you optimize it :(
