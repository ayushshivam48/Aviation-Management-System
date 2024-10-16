class Node:
    def __init__(self, key):
        """Initialize a node with the given key and no children."""
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        """Helper method to insert a new key recursively."""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        """Search for a key in the BST. Return True if found, else False."""
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        """Helper method to search for a key recursively."""
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        """Helper method to delete a key recursively."""
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.value:
            node.right = self._delete_recursively(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursively(node.right, min_larger_node.value)

        return node

    def _find_min(self, node):
        """Find the node with the minimum value."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self):
        """Perform in-order traversal of the BST and return the values in sorted order."""
        return self._in_order_recursively(self.root)

    def _in_order_recursively(self, node):
        """Helper method for in-order traversal."""
        values = []
        if node:
            values += self._in_order_recursively(node.left)
            values.append(node.value)
            values += self._in_order_recursively(node.right)
        return values


# Example usage of the Binary Search Tree
def main():
    bst = BinarySearchTree()

    # Insert nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # In-order traversal
    print("In-order Traversal:", bst.in_order_traversal())

    # Search for a value
    print("Search for 40:", bst.search(40))  # Output: True
    print("Search for 100:", bst.search(100))  # Output: False

    # Delete a node
    bst.delete(20)
    print("In-order Traversal after deleting 20:", bst.in_order_traversal())

    bst.delete(30)
    print("In-order Traversal after deleting 30:", bst.in_order_traversal())

    bst.delete(50)
    print("In-order Traversal after deleting 50:", bst.in_order_traversal())


if __name__ == "__main__":
    main()
