class MyList:

    def __init__(self, mylist):
        self.mylist = mylist

    def __str__(self):
        return 'Object: {}'.format(self.mylist)

    def add(self, item):
        self.mylist[len(self.mylist):] = [item]
        return self.mylist

    def pop(self):
        self.mylist = self.mylist[:-1]
        return self.mylist

    def remove(self, item):
        for i in range(len(self.mylist)):
            if item == self.mylist[i]:
                if i == 0:
                    self.mylist = self.mylist[1:]

    def __len__(self):
        return len(self.mylist)

    def __contains__(self, item):
        if item in self.mylist:
            return True
        else:
            return False

    def __setitem__(self, index, item):
        self.mylist[index] = item

    def __getitem__(self, index):
        return self.mylist[index]


if __name__ == '__main__':

    my_list = MyList([6, 5, 2, 3])
    my_list.add(5)
    #print(my_list)
    #print(my_list[2])
    my_list[0] = "hola"
    print(my_list)
    my_list.pop()
    print(my_list)
    print(len(my_list))
    #
    for el in my_list:
         print(el)
    #
    print(type(my_list))
    