class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":
    arr = [2, 5, 8, 7]

    # Create first node
    y = Node(arr[0])

    # Print memory reference of node
    print(y)

    # Print data stored in node
    print(y.data)