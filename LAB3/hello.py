#!/usr/bin/env python3
import os
import sys

for key in os.environ:
    print(f'{key}={os.environ[key]}')

for key in sys.argv:
    print(f'{key}')