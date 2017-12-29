import os
import pickle
import tempfile

class DiskList(object):
    def __init__(self, cache_size=-1):
        """
            Init a new diskfile object.
        """

        self.item_offsets = []
        self.item_sizes = []
        self.cache = []
        self.cache_size = cache_size
        self.cache_index = 0
        self.tempfile = tempfile.TemporaryFile()

    def __del__(self):
        """
            Destructor that closes the tempfile (which destorys it)
        """

        self.tempfile.close()

    def __add__(self, disklist2):
        """
            Add the second DiskList to the first one
        """

        self.item_offsets.extend(disklist2.item_offsets)
        self.item_sizes.extend(disklist2.item_sizes)
        self.tempfile.write(disklist2.tempfile.read())
        return self

    def __iter__(self):
        """
            Return the DiskList's iterator
        """

        self.index = 0
        self.cache_index = 0
        self.cache = []
        return self

    def __next__(self):
        """
            Return the next item in the iteration
        """

        if self.index >= len(self.item_sizes):
            raise StopIteration
        if self.index >= self.cache_index - self.cache_size and self.index < self.cache_index:
            self.index += 1
            return self.cache[(self.index - 1) % self.cache_size]
        else:
            if self.cache_size > 0:
                self.__refresh_cache()
            self.index += 1
            return self[self.index - 1]

    def __refresh_cache(self):
        """
            Refresh our cache with the current iteration index
        """

        self.cache_index = self.index + self.cache_size
        self.cache = self[self.index:self.index+self.cache_size]

    def __getitem__(self, index):
        """
            Get an item at the given index or slice
        """

        if isinstance(index, slice):
            l = []
            for i in range(
                index.start if index.start is not None else 0,
                index.stop if index.stop is not None and not index.stop > len(self.item_sizes) else len(self.item_sizes),
                index.step if index.step is not None else 1):
                self.tempfile.seek(self.item_offsets[i])
                l.append(pickle.loads(self.tempfile.read(self.item_sizes[i])))
            return l
        else:
            self.tempfile.seek(self.item_offsets[index])
            return pickle.loads(self.tempfile.read(self.item_sizes[index]))

    def __setitem__(self, index, item):
        """
            Replace an item at a given position
        """

        self.tempfile.seek(0, 2)
        data = pickle.dumps(item)
        self.item_offsets[index] = self.tempfile.tell()
        self.item_sizes[index] = len(data)
        self.tempfile.write(data)

    def __len__(self):
        """
            Return the length of the DiskList
        """

        return len(self.item_offsets)

    def insert(self, index, item):
        """
            Insert an item at the given index
        """

        self.tempfile.seek(0, 2) # Seek the EOF
        data = pickle.dumps(item)
        self.item_offsets.insert(index, self.tempfile.tell())
        self.item_sizes.insert(index, len(data))
        self.tempfile.write(data)


    def append(self, item):
        """
            Appends an item at the end of the list
        """

        self.tempfile.seek(0, 2) # Seek the EOF
        data = pickle.dumps(item)
        self.item_offsets.append(self.tempfile.tell())
        self.item_sizes.append(len(data))
        self.tempfile.write(data)
