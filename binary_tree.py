# coding: utf-8
__author__ = 'polly'


'''
значения = [1, 4, 5, 10, 16, 17, 21]
'''


class Vertex(object):
    left_child = None
    right_child = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'value={0}, left={1}, right={2}'.format(self.value, self.left_child, self.right_child)


class Tree(object):
    def __init__(self, source):
        self.source = source
        self.root = Vertex(source[-1])

    def Prepare(self):
        for val in self.source:
            self.Build(self.root, Vertex(val))

    def Build(self, root, vertex):
        if root.value <= vertex.value:
            if root.right_child is None:
                root.right_child = vertex
            else:
                self.Build(root.right_child, vertex)
        else:
            if root.left_child is None:
                root.left_child = vertex
            else:
                self.Build(root.left_child, vertex)

    def __str__(self):
        return str(self.root)


lst = [1, 4, 5, 10, 16, 17, 21]
a = Tree(lst)
a.Prepare()
print a
