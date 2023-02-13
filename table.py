class Table:
    __slots__ = ('tg', 'head', 'sh', 'abc', 'count', 'count2')

    def __init__(self, tg, head, sh, abc='ABCDEFG', count=2, count2=0):
        self.head = head
        self.sh = sh
        self.abc = abc
        self.count = count
        self.count2 = count2
        self.tg = tg

    def update_head(self):
        for h in self.head:
            text = h.text
            self.sh.sheet1.update(f'{self.abc[self.count2]}1', text)
            self.count2 += 1
        self.count2 = 0

    def update_values(self):
        for quote in self.tg:
            text = quote.text
            if text.isdigit():
                self.sh.sheet1.update(f'A{self.count}', text)
            else:
                self.sh.sheet1.update(f'B{self.count}', text)
                self.count += 1
        self.count = 2
