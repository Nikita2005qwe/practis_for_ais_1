"""Модуль "заглушка" для тестов"""


class LinkedListItem:
    """Узел связного списка"""

    def __init__(self, value, next=None, previous=None):
        self.data = value
        self.next = next
        self.previous = previous

    @property
    def next_item(self):
        """Следующий элемент"""
        return self.next

    @next_item.setter
    def next_item(self, value):
        self.next = value
        if value is not None:
            value.previous = self

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self.previous

    @previous_item.setter
    def previous_item(self, value):
        self.previous = value
        if value is not None:
            value.next = self

    def __repr__(self):
        return f"LinkedListItem({self.data})"


class LinkedList:
    """Связный список"""




    def __init__(self, first_item=None):
        self.first_item = first_item
        self.length = 0
        if first_item:
            current = first_item
            while True:
                self.length += 1
                if current.next_item == first_item:
                    break
                current = current.next_item
            current.next_item = first_item
            first_item.previous_item = current

    @property
    def last(self):
        """Получение последнего элемента"""
        if self.first_item is None:
            return None
        last = self.first_item.previous
        return last

    def append_left(self, data):
        """Добавление слева"""
        new_item = LinkedListItem(data)
        if len(self) == 0:
            self.first_item = new_item
            new_item.next = self.first_item
            new_item.previous = self.first_item
        else:
            last = self.first_item.previous
            last.next = new_item
            new_item.previous = last
            new_item.next = self.first_item
            self.first_item.previous = new_item
            self.first_item = new_item
        self.length += 1


    def append_right(self, data):
        """Добавление справа"""
        new_item = LinkedListItem(data)
        if len(self) == 0:
            self.first_item = new_item
            new_item.next = self.first_item
            new_item.previous = self.first_item
        else:
            last = self.first_item.previous
            last.next = new_item
            new_item.previous = last
            new_item.next = self.first_item
            self.first_item.previous = new_item
        self.length += 1

    def append(self, data):
        """Добавление справа"""
        self.append_right(data)

    def remove(self, data):
        """Удаление"""
        if self.first_item is None:
            raise ValueError()
        current_item = self.first_item
        for i in range(len(self)):
            if current_item.data == data:
                if len(self) == 1:
                    self.first_item = None
                else:
                    previous_item = current_item.previous_item
                    next_item = current_item.next_item
                    previous_item.next_item = next_item
                    next_item.previous_item = previous_item
                    if current_item == self.first_item:
                        self.first_item = next_item
                self.length -= 1
                return None
            current_item = current_item.next_item
        raise ValueError()



    def insert(self, previous_item_data, new_item):
        """Вставка справа"""
        if self.first_item is None:
            raise ValueError()
        current = self.first_item
        for i in range(self.length):
            if current.data == previous_item_data:
                new_item.next = current.next
                new_item.previous = current
                current.next.previous = new_item
                current.next = new_item
                self.length += 1
                return None
            current = current.next
        raise ValueError("Элемент с такими данными не найден в списке.")




    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        raise NotImplementedError()
