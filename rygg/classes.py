from uuid import uuid4


class Item:
    desire = 0

    def __init__(self, *specs, _id=None):
        if not id:
            self.id = uuid4()
        else:
            self.id = _id
        self.value = int(specs[0])
        self.size = int(specs[1])
        self.desire = self.value / self.size

    def __repr__(self):
        return f"<\x1b[1;34mItem\x1b[0m#\x1b[31m{self.id}\x1b[0m \x1b[1;30m$\x1b[0m{self.value} \x1b[1;30msize=\x1b[0m{self.size}>"
