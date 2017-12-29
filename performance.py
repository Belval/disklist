import time

from timeit import default_timer as timer
from disklist import DiskList

def main():
    """
        Compare disklists and lists
    """

    # Instantiation
    print('|---------- Instanciation ----------|')
    # List
    start = timer()
    for _ in range(0, 1000):
        l = []
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for _ in range(0, 1000):
        dl = DiskList()
    end = timer()
    print('DiskList: {:.10f} sec'.format((end - start) / 1000))

    # Append
    print('|---------- Appending ----------|')
    # List
    start = timer()
    for i in range(0, 1000):
        l.append(i)
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for i in range(0, 1000):
        dl.append(i)
    end = timer()
    print('DiskList: {:.10f} sec'.format((end - start) / 1000))

    # Inserting
    print('|---------- Inserting ----------|')
    # List
    start = timer()
    for i in range(0, 1000):
        l.insert(i, i)
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for i in range(0, 1000):
        dl.insert(i, i)
    end = timer()
    print('DiskList: {:.10f} sec'.format((end - start) / 1000))

    # Getting with index
    print('|------ Getting with index ------|')
    # List
    start = timer()
    for i in range(0, 1000):
        l[i]
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for _ in range(0, 1000):
        dl[i]
    end = timer()
    print('DiskList: {:.10f} sec'.format((end - start) / 1000))

    # Setting with index
    print('|------ Setting with index ------|')
    # List
    start = timer()
    for i in range(0, 1000):
        l[i] = i
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for _ in range(0, 1000):
        dl[i] = i
    end = timer()
    print('DiskList: {:.10f} sec'.format((end - start) / 1000))

    # Iterating
    print('|---------- Iterating ----------|')
    # List
    start = timer()
    for i in range(0, 1000):
        for item in l:
            continue
    end = timer()
    print('List: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    start = timer()
    for _ in range(0, 1000):
        for item in dl:
            continue
    end = timer()
    print('DiskList without cache: {:.10f} sec'.format((end - start) / 1000))
    # DiskList
    dl = DiskList(cache_size=256) # 256 items
    for i in range(0, 1000):
        dl.append(i)
    start = timer()
    for _ in range(0, 1000):
        for item in dl:
            continue
    end = timer()
    print('DiskList with cache: {:.10f} sec'.format((end - start) / 1000))

if __name__=='__main__':
    main()
