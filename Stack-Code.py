class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        """Remove and return the top item of the stack. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, else False."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def display(self):
        """Display the items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)


# Example usage of the Stack class
def main():
    stack = Stack()

    # Push items to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display the stack
    stack.display()

    # Peek at the top item
    print("Top item:", stack.peek())

    # Pop items from the stack
    print("Popped item:", stack.pop())
    print("Popped item:", stack.pop())

    # Display the stack after popping
    stack.display()

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())

    # Pop the last item
    stack.pop()

    # Try to pop from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
