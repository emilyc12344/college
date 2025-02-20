#!/usr/bin/env python3

import sys; lines = [i.strip() for i in sys.stdin]; print(f"Words with q but no u: {[i for i in lines if i.lower().count('qu') != i.lower().count('q')]}")
