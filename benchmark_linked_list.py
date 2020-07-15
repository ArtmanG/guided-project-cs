import time
from singly_linked_list import LinkedList

n = 100000

# l = [i for i in range(n)]
l = []
ll = LinkedList()


start_time = time.time()
for i in range(n):
    ll.add_to_tail(i)
end_time = time.time()
print(f"Linked List add to list through range(n) took {end_time - start_time} seconds at n = {n}")

start_time = time.time()
for i in range(n):
    l.append(i)
end_time = time.time()
print(f"List (array) append to list through range(n) took {end_time - start_time} seconds at n = {n}")

start_time = time.time() 
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked List remove from head through range(n) took {end_time - start_time} seconds at n = {n}")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"List (array) remove from head through range(n) took {end_time - start_time} seconds at n = {n}")