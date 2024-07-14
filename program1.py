
class MaxHeap:
    def __init__(self):
        self.heap = [];

    def parent(self, index):
        return (index - 1) // 2;

    def leftchild(self, index):
        return 2 * index + 1;

    def rightchild(self, index):
        return 2 * index + 2;

    def heapify_up(self, index):
        parentindex = self.parent(index);
        if index > 0 and self.heap[index] > self.heap[parentindex]:
            self.heap[index], self.heap[parentindex] = self.heap[parentindex], self.heap[index];
            self.heapify_up(parentindex);

    def heapify_down(self, index):
        largest = index;
        lc_index = self.leftchild(index);
        rc_index = self.rightchild(index);

        if lc_index < len(self.heap) and self.heap[lc_index] > self.heap[largest]:
            largest = lc_index;

        if rc_index < len(self.heap) and self.heap[rc_index] > self.heap[largest]:
            largest = rc_index;

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest);

    def insert(self, value):
        self.heap.append(value);
        self.heapify_up(len(self.heap) - 1);

    def delete(self):
        if len(self.heap) == 0:
            print("Heap is empty");
        if len(self.heap) == 1:
            return self.heap.pop();
        root = self.heap[0];
        self.heap[0] = self.heap.pop();
        self.heapify_down(0);
        return root;

    def get_max(self):
        if len(self.heap) == 0:
            print("Heap is Empty");
        return self.heap[0];

max_heap = MaxHeap();
max_heap.insert(10);
max_heap.insert(15);
max_heap.insert(20);
max_heap.insert(17);

print("Max element:", max_heap.get_max()) ;
print("Deleted element:", max_heap.delete());
print("Max element after deletion:", max_heap.get_max());