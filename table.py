
class Table:
    __slots__ = ('tg', 'head', 'sh', 'abc', 'string', 'column')

    def __init__(self, tg, head, sh, abc: str = 'ABCDEFG', string: int = 2, column: int = 0):
        self.head = head
        self.sh = sh
        self.abc = abc
        self.string = string
        self.column = column
        self.tg = tg

    def update_head(self) -> None:
        for h in self.head:
            text = h.text
            self.sh.sheet1.update(f'{self.abc[self.column]}1', text)
            self.column += 1
        self.column = 0

    def update_values(self) -> None:
        for quote in self.tg:
            text = quote.text
            if text.isdigit():
                self.sh.sheet1.update(f'A{self.string}', text)
            else:
                self.sh.sheet1.update(f'B{self.string}', text)
                self.string += 1
        self.string = 2
