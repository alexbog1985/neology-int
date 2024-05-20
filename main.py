""" Стек — абстрактный тип данных, представляющий список элементов, организованных по принципу LIFO
(англ. last in — first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают со стопкой
тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии: стрельба начнётся
с патрона, заряженного последним.

Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке. """


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item) -> list:
        self.items.append(item)
        return self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self) -> int:
        if not self.is_empty():
            return len(self.items)
        else:
            return 0
