class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

    def getid(self) -> int:
        return self.id

    def getpos(self) -> tuple:
        return self.pos