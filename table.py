
class Table:
    __slots__ = ('gs', 'head', 'go', 'abc', 'string', 'column')

    def __init__(self, gs, head, go, abc: str = 'ABCDEFG', string: int = 2, column: int = 0):
        self.head = head
        self.go = go
        self.abc = abc
        self.string = string
        self.column = column
        self.gs = gs

    def update_head(self) -> None:
        for h in self.head:
            text = h.text
            self.go.sheet1.update(f'{self.abc[self.column]}1', text)
            self.column += 1
        self.column = 0

    def update_values(self) -> None:
        for quote in self.gs:
            text = quote.text
            if text.isdigit():
                self.go.sheet1.update(f'A{self.string}', text)
            else:
                self.go.sheet1.update(f'B{self.string}', text)
                self.string += 1
        self.string = 2
