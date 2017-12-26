# DiskList [![TravisCI](https://travis-ci.org/Belval/disklist.svg?branch=master)](https://travis-ci.org/Belval/disklist) [![PyPI version](https://badge.fury.io/py/disklist.svg)](https://badge.fury.io/py/disklist)
A python list implementation that uses the disk to handle very large collections

## How does it work?

DiskList will create a file on disk and store your objects in it. The most commonly used list methods and operators are implemented so you can use it as an almost drop-in replacement.

Here's an example!

```
from disklist import DiskList

dl = DiskList()

for i in range(0, 1000):
    dl.append(i)

dl[0] # Boring indexing works!
dl[0:2] # So does slicing!

Concatenation is functional too

dl2 = DiskList()
dl2.append(4)

dl = dl + dl2

Why not iterate through it?

for item in dl:
    print(dl) # 1, 2, 3, 4, 5, 6... You get the point

```

Anything that you can do with a list that is impossible with a DiskList deserves an issue!

## Speed

As with anything that uses the disk, expect every action to 2+ order of magnitude slower than a regular list. Here are some benchmarks:

```
|---------- Instanciation ----------|
List: 0.0000000372 sec
DiskList: 0.0000248346 sec
|---------- Appending ----------|
List: 0.0000000934 sec
DiskList: 0.0000045466 sec
|------ Accessing with index ------|
List: 0.0000000391 sec
DiskList: 0.0000038139 sec
|---------- Iterating ----------|
List: 0.0000072625 sec
DiskList without cache: 0.0021884149 sec
DiskList with cache: 0.0021451381 sec
```

## When should you use it?

Excellent question! My honest answer would be "as rarely as possible". It is slow, not scalable (like a database would be for example). My only legitimate use right now is for machine learning to store my training batches until I need them. If you feel like your usecase is legitimate send me an email at github@belval.org. I am very curious!
