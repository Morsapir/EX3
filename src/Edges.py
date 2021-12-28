class Edges:

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight
