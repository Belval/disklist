# DiskList [![TravisCI](https://travis-ci.org/Belval/disklist.svg?branch=master)](https://travis-ci.org/Belval/disklist) [![PyPI version](https://badge.fury.io/py/disklist.svg)](https://badge.fury.io/py/disklist)
A python list implementation that uses the disk to handle very large collections of pickle-able objects.

Now as a PyPi package: `pip install disklist`!

## How does it work?

DiskList will create a unamed temporary file on disk and store your objects in it. The most commonly used list methods and operators are implemented so you can use it as an almost drop-in replacement.

Here's an example!

```
from disklist import DiskList

dl = DiskList()

for i in range(0, 1000):
    dl.append(i)

dl[0] # Boring indexing works!
dl[0:2] # So does slicing!

What if you want to insert something?

dl.insert(0, 2)

...or setting an element

dl[0] = 2

Concatenation is functional too

dl2 = DiskList()
dl2.append(4)

dl = dl + dl2

Why not iterate through it?

for item in dl:
    print(dl) # 1, 2, 3, 4, 5, 6... You get the point

```

Anything that you can do with a list that is impossible with a DiskList deserves an issue!

## Setting an index to a new value

Mostly for speed concerns, setting an index to something doesn't clean the old object in the TemporaryFile so while the "list" will dereference it, the space on your disk will still be used. While this will not have any real impacts in most usecases, avoid doing stuff like this:

```
for i in range(1000000):
    dl[0] = i
```

Because while `dl[0]` will be equal to `999999`, you effectively created 7.868 MB (yes I did the math) of useless data on your disk.

## Speed

As with anything that uses the disk, expect every action to 2+ order of magnitude slower than a regular list. Here are some benchmarks:

```
|---------- Instanciation ----------|
List: 0.0000000671 sec
DiskList: 0.0000138546 sec
|---------- Appending ----------|
List: 0.0000001158 sec
DiskList: 0.0000027095 sec
|---------- Inserting ----------|
List: 0.0000004970 sec
DiskList: 0.0000045391 sec
|------ Getting with index ------|
List: 0.0000000514 sec
DiskList: 0.0000034319 sec
|------ Setting with index ------|
List: 0.0000000647 sec
DiskList: 0.0000034748 sec
|---------- Iterating ----------|
List: 0.0000154976 sec
DiskList without cache: 0.0035845941 sec
DiskList with cache: 0.0015620445 sec
```

**Full disclosure, these tests were done using an SSD**

## When should you use it?

Excellent question! My honest answer would be "as rarely as possible". It is slow, not scalable (like a database would be for example). My only legitimate use right now is for machine learning to store my training batches until I need them. If you feel like your usecase is legitimate send me an email at github@belval.org. I am very curious!
