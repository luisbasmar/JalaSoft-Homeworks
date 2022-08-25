class MyList:
    def __init__(self, *args) -> None:
        self.__node = None
        self.__next = None
        self.size = 0
        if len(args) > 0:
            for item in args:
                self.add(item)
            self.size = len(args)

    def empty(self):
        return self.__node == None

    def add(self, item):
        if self.__node == None:
            self.__node = item
            self.size += 1
            self.__next = MyList()
        else:
            self.__next.add(item)
            self.size += 1

    def __getitem__(self, index):
        if index == 0:
            return self.__node
        else:
            return self.__next[index - 1]

    def __setitem__(self, index, item):
        if index == 0:
            self.__node = item
        else:
            self.__next[index - 1] = item

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.__node
        next_item = self.__next 
        while node is not None:
            yield node
            node = next_item.__node
            next_item = next_item.__next

