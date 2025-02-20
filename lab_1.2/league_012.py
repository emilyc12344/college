#!/usr/bin/env python3

import sys

pos = ['POS']
c = ['CLUB']
p = ['P']
w = ['W']
d = ['D']
l = ['L']
gf = ['GF']
ga = ['GA']
gd = ['GD']
pts = ['PTS']

for i in sys.stdin:
	i = i.strip().split()
	pos.append(i[0])
	c.append(' '.join(i[1:-8]))
	p.append(i[-8])
	w.append(i[-7])
	d.append(i[-6])
	l.append(i[-5])
	gf.append(i[-4])
	ga.append(i[-3])
	gd.append(i[-2])
	pts.append(i[-1])

low = 0
for i in c:
	if len(i) > low:
		low = len(i)

x = 0
while x < len(pos):
	print(f'{pos[x]: >3} {c[x]: <{low}} {p[x]: >2} {w[x]: >3} {d[x]: >3} {l[x]: >3} {gf[x]: >3} {ga[x]: >3} {gd[x]: >3} {pts[x]: >3}')
	x += 1