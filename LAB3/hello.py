#!/usr/bin/env python3
import os

for key in os.environ:
    print(f'{key}={os.environ[key]}')