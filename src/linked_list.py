from typing import Any, Union


class LinkedList:
    """Кольцевой двусвязный список"""

    def __init__(self, first_item=None) -> None:
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
    def last(self) -> object:
        """Получение последнего элемента списка"""
        if self.first_item is None:
            return None
        last = self.first_item.previous
        return last

    def append_left(self, data: Any) -> None:
        """Добавление элемента в начало списка"""
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

    def append_right(self, data: Any) -> None:
        """Добавление элемента в конец списка"""
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

    def append(self, data: Any) -> None:
        """Элиас для append_right"""
        self.append_right(data)

    def remove(self, data: Any) -> None:
        """Удаление элемента, при его отсутствии в списке
        должно возбуждать исключение ValueError"""
        if self.first_item is None:
            raise ValueError()
        current_item = self.first_item
        for _ in range(len(self)):
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

    def insert(self, previous_item_data: Any, new_item: object) -> None:
        """Вставка нового узла после узла с определёнными данными"""
        if self.first_item is None:
            raise ValueError("Список пуст.")
        current = self.first_item
        for _ in range(self.length):
            if current.data == previous_item_data:
                new_item.next = current.next
                new_item.previous = current
                current.next.previous = new_item
                current.next = new_item
                self.length += 1
                return None
            current = current.next
        raise ValueError("Элемент с такими данными не найден в списке.")

    def __len__(self) -> int:
        """Длина списка"""
        return self.length

    def __iter__(self) -> object:
        self.iter_current = self.first_item
        if self.iter_current is not None:
            self.iter_start = self.iter_current
        return self

    def __next__(self) -> Any:
        if self.iter_current is None:
            raise StopIteration
        current_data = self.iter_current
        self.iter_current = self.iter_current.next_item
        if self.iter_current == self.iter_start:
            self.iter_current = None
        return current_data

    def __getitem__(self, index: int) -> Any:
        """Получение элемента по индексу"""
        if self.first_item is None:
            raise IndexError()
        current_item = self.first_item

        if index >= 0:
            for i in range(len(self)):
                if i == index:
                    return current_item.data
                current_item = current_item.next
            else:
                raise IndexError()

        else:
            for i in range(-len(self), 0):
                if i == index:
                    return current_item.data
                current_item = current_item.next
            else:
                raise IndexError()

    def __contains__(self, item: object) -> Union[bool, None]:
        """Поддержка оператора in"""
        current_item = self.first_item
        for _ in range(len(self)):
            if current_item.data == item:
                return True
            current_item = current_item.next
        return False

    def __reversed__(self) -> None:
        """Поддержка оператора reversed"""
        if not self.first_item:
            return
        current = self.first_item.previous_item
        while True:
            yield current.data
            current = current.previous_item
            if current == self.first_item.previous_item:
                break


class LinkedListItem:
    """Класс, который будет содержать ссылки на следующий и предыдущий элементы,
а также данные в виде экземпляра Composition"""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.previous = None

    @property
    def next_item(self) -> object:
        """Следующий элемент"""
        return self.next

    @next_item.setter
    def next_item(self, item: object) -> None:
        self.next = item
        if item is not None:
            item.previous = self

    @property
    def previous_item(self) -> object:
        """Предыдущий элемент"""
        return self.previous

    @previous_item.setter
    def previous_item(self, item: object) -> None:
        self.previous = item
        if item is not None:
            item.next = self

    def __repr__(self) -> str:
        return f"LinkedListItem({self.data})"
