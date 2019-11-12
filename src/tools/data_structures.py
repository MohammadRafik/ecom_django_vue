class Tree():
    class Node():
        def __init__(self, value, parent=None):
            self._value = value
            self._parent = parent
            self._children = []
        

    def __init__(self, value):
        self._root = self.Node(value)
    
    def add_child(self, parent_node, child_node_value):
        self._node = self.Node(child_node_value, parent_node)
        parent_node._children.append(self._node)