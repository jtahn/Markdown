---
created: 2024-05-01T15:20:47 (UTC -04:00)
tags: []
source: https://realpython.com/python-heapq-module/
author: Real Python
---

# The Python heapq Module: Using Heaps and Priority Queues – Real Python

> ## Excerpt
> In this step-by-step tutorial, you'll explore the heap and priority queue data structures. You'll learn what kinds of problems heaps and priority queues are useful for and how you can use the Python heapq module to solve them.

---
**Heaps** and **priority queues** are little-known but surprisingly useful data structures. For many problems that involve finding the best element in a dataset, they offer a solution that’s easy to use and highly effective. The Python `heapq` module is part of the standard library. It implements all the low-level heap operations as well as some high-level common uses for heaps.

A [priority queue](https://realpython.com/queue-in-python/#priority-queue-sorted-from-high-to-low) is a powerful tool that can solve problems as varied as writing an email scheduler, finding the shortest path on a map, or merging log files. Programming is full of [optimization problems](https://en.wikipedia.org/wiki/Optimization_problem) in which the goal is to find the best element. Priority queues and the functions in the Python `heapq` module can often help with that.

**In this tutorial, you’ll learn**:

-   What **heaps** and **priority queues** are and how they relate to each other
-   What kinds of **problems** can be solved using a heap
-   How to use the Python **`heapq` module** to solve those problems

This tutorial is for Pythonistas who are comfortable with [lists](https://realpython.com/python-lists-tuples/), [dicts](https://realpython.com/python-dicts/), [sets](https://realpython.com/python-sets/), and [generators](https://realpython.com/introduction-to-python-generators/) and are looking for more sophisticated [data structures](https://realpython.com/python-data-structures/).

## What Are Heaps?

Heaps are **concrete** data structures, whereas priority queues are **abstract** data structures. An abstract data structure determines the [interface](https://realpython.com/python-interface/), while a concrete data structure defines the implementation.

Heaps are commonly used to implement priority queues. They’re the most popular concrete data structure for implementing the priority queue abstract data structure.

Concrete data structures also specify **performance guarantees**. Performance guarantees define the relationship between the _size_ of the structure and the _time_ operations take. Understanding those guarantees allows you to predict how much time the program will take as the size of its inputs change.

### Data Structures, Heaps, and Priority Queues

Abstract data structures specify operations and the relationships between them. The priority queue abstract data structure, for example, supports three operations:

1.  **is\_empty** checks whether the queue is empty.
2.  **add\_element** adds an element to the queue.
3.  **pop\_element** pops the element with the highest priority.

Priority queues are commonly used for optimizing task execution, in which the goal is to work on the task with the highest priority. After a task is completed, its priority is lowered, and it’s returned to the queue.

There are two different conventions for determining the priority of an element:

1.  The _largest_ element has the highest priority.
2.  The _smallest_ element has the highest priority.

These two conventions are equivalent because you can always reverse the effective order. For example, if your elements consist of [numbers](https://realpython.com/python-numbers/), then using negative numbers will flip the conventions around.

The Python `heapq` module uses the second convention, which is generally the more common of the two. Under this convention, the _smallest_ element has the highest priority. This might sound surprising, but it’s often quite useful. In the real-life examples you’ll see later, this convention will simplify your code.

> [!note]
> The Python `heapq` module, and the heap data structure in general, is _not_ designed to allow finding any element except the smallest one. For retrieval of any element by size, a better option is a [binary search tree](https://realpython.com/binary-search-python/).

Concrete data structures implement the operations defined in an abstract data structure and further specify performance guarantees.

The heap implementation of the priority queue guarantees that both pushing (adding) and popping (removing) elements are **logarithmic time** operations. This means that the time it takes to do push and pop is proportional to the **base-2 logarithm** of the number of elements.

[Logarithms](https://en.wikipedia.org/wiki/Logarithm) grow slowly. The base-2 logarithm of fifteen is about four, while the base-2 logarithm of a trillion is about forty. This means that if an algorithm is fast enough on fifteen elements, then it’s going to be only ten times slower on a trillion elements and will probably still be fast enough.

In any discussion of performance, the biggest caveat is that these abstract considerations are less meaningful than actually measuring a concrete program and learning where the [bottlenecks](https://en.wikipedia.org/wiki/Bottleneck_(software)) are. General performance guarantees are still important for making useful predictions about program behavior, but those predictions should be confirmed.

### Implementation of Heaps

A heap implements a priority queue as a **complete binary tree**. In a [binary tree](https://en.wikipedia.org/wiki/Binary_tree), each node will have at most two children. In a _complete_ binary tree, all levels except possibly the deepest one are full at all times. If the deepest level is incomplete, then it will have the nodes as far to the left as possible.

The **completeness property** means that the depth of the tree is the base-2 logarithm of the number of elements, rounded up. Here’s an example of a complete binary tree:

![[../../../!assets/attachments/Pasted image 20240501152358.png]]

In this particular example, all levels are complete. Each node except for the deepest ones has exactly two children. There are a total of seven nodes in three levels. Three is the base-2 logarithm of seven, rounded up.

The single node at the base level is called the **root** node. It might seem weird to call the node at the top of the tree the root, but this is the common convention in programming and computer science.

The performance guarantees in a heap depend on how elements percolate up and down the tree. The practical result of this is that the number of comparisons in a heap is the base-2 logarithm of the size of the tree.

> [!note]
> Comparisons sometimes involve calling user-defined code using `.__lt__()`. Calling user-defined methods in Python is a relatively slow operation compared with other operations done in a heap, so this will usually be the bottleneck.

In a heap tree, the value in a node is always smaller than both of its children. This is called the **heap property**. This is different from a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree), in which only the left node will be smaller than the value of its parent.

The algorithms for both pushing and popping rely on temporarily violating the heap property, then fixing the heap property through comparisons and replacements up or down a single branch.

For example, to push an element onto a heap, Python adds the new node to the next open slot. If the bottom layer isn’t full, then the node is added to the next open slot at the bottom. Otherwise, a new level is created and then the element is added to the new bottom layer.

Once the node is added, Python compares it to its parent. If the heap property is violated, then the node and its parent are switched, and the check begins again at the parent. This continues until the heap property holds or the root has been reached.

Similarly, when popping the smallest element, Python knows that, because of the heap property, the element is at the root of the tree. It replaces the element with the last element at the deepest layer and then checks if the heap property is violated down the branch.

### Uses of Priority Queues

A priority queue, and a heap as an implementation of a priority queue, is useful for programs that involve finding an element that is extreme in some way. For example, you can use a priority queue for any of the following tasks:

-   Getting the three most popular blog posts from hit data
-   Finding the fastest way to get from one point to the other
-   Predicting which bus will be the first to arrive at a station based on arrival frequency

Another task for which you could use a priority queue is scheduling emails. Imagine a system that has several kinds of emails, each of which needs to be sent at a certain frequency. One kind of email needs to go out every fifteen minutes, and another needs to be sent every forty minutes.

A scheduler could add both types of email to the queue with a **timestamp** indicating when the email next needs to be sent. Then the scheduler could look at the element with the smallest timestamp—indicating that it’s next in line to be sent—and calculate how long to sleep before sending.

When the scheduler wakes up, it would process the relevant email, take the email out of the priority queue, calculate the next timestamp, and put the email back in the queue at the correct location.

## Heaps as Lists in the Python `heapq` Module

Although you saw the heap described earlier as a tree, it’s important to remember that it’s a _complete_ binary tree. Completeness means that it’s always possible to tell how many elements are at each layer except the last one. Because of this, heaps can be implemented as a [list](https://realpython.com/courses/lists-tuples-python/). This is what the Python `heapq` module does.

There are three rules that determine the relationship between the element at the index `k` and its surrounding elements:

1.  Its first child is at `2*k + 1`.
2.  Its second child is at `2*k + 2`.
3.  Its parent is at `(k - 1) // 2`.

> [!note]
> The `//` symbol is the **integer division** operator. It always rounds down to an integer.

The rules above tell you how to visualize a list as a complete binary tree. Keep in mind that an element always has a parent, but some elements don’t have children. If `2*k` is beyond the end of the list, then the element doesn’t have any children. If `2*k + 1` is a valid index but `2*k + 2` is not, then the element has only one child.

The heap property means that if `h` is a heap, then the following will never be `False`:

```python
h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
```

It might raise an `IndexError` if any of the indices is beyond the length of the list, but it will never be `False`.

In other words, an element must always be smaller than the elements that are at twice its index plus one and twice its index plus two.

Here’s a visual of a list that satisfies the heap property:

![[../../../!assets/attachments/Pasted image 20240501152527.png]]

The arrows go from element `k` to elements `2*k + 1` and `2*k + 2`. For example, the first element in a Python list has the index `0`, so its two arrows point at indices `1` and `2`. Notice how the arrows always go from a smaller value to a bigger value. This is how you can check that the list satisfies the heap property.

### Basic Operations

The Python `heapq` module implements heap operations on lists. Unlike many other modules, it does _not_ define a custom class. The Python `heapq` module has functions that work on lists directly.

Usually, as in the email example above, elements will be inserted into a heap one by one, starting with an empty heap. However, if there’s already a list of elements that needs to be a heap, then the Python `heapq` module includes `heapify()` for turning a list into a valid heap.

The following code uses `heapify()` to turn `a` into a **heap**:

```python
>>> import heapq
>>> a = [3, 5, 1, 2, 6, 8, 7]
>>> heapq.heapify(a)
>>> a
[1, 2, 3, 5, 6, 8, 7]
```

You can check that even though `7` comes after `8`, the list `a` still obeys the heap property. For example, `a[2]`, which is `3`, is less than `a[2*2 + 2]`, which is `7`.

As you can see, `heapify()` modifies the list in place but doesn’t sort it. A heap doesn’t have to be sorted to satisfy the heap property. However, since every sorted list _does_ satisfy the heap property, running `heapify()` on a sorted list won’t change the order of elements in the list.

The other basic operations in the Python `heapq` module assume that the list is already a heap. It’s useful to note that an empty list or a list of length one will always be a heap.

Since the root of the tree is the first element, you don’t need a dedicated function to read the smallest element nondestructively. The first element, `a[0]`, will always be the smallest element.

To pop the smallest element while preserving the heap property, the Python `heapq` module defines `heappop()`.

Here’s how to use `heappop()` to pop an element:

```python
>>> import heapq
>>> a = [1, 2, 3, 5, 6, 8, 7]
>>> heapq.heappop(a)
1
>>> a
[2, 5, 3, 7, 6, 8]
```

The function returns the first element, `1`, and preserves the heap property on `a`. For example, `a[1]` is `5` and `a[1*2 + 2]` is `6`.

The Python `heapq` module also includes `heappush()` for pushing an element to the heap while preserving the heap property.

The following example shows pushing a value to a heap:

```python
>>> import heapq
>>> a = [2, 5, 3, 7, 6, 8]
>>> heapq.heappush(a, 4)
>>> a
[2, 5, 3, 7, 6, 8, 4]
>>> heapq.heappop(a)
2
>>> heapq.heappop(a)
3
>>> heapq.heappop(a)
4
```

After pushing `4` to the heap, you pop three elements from it. Since `2` and `3` were already in the heap and are smaller than `4`, they’re popped first.

The Python `heapq` module also defines two more operations:

1.  **`heapreplace()`** is equivalent to `heappop()` followed by `heappush()`.
2.  **`heappushpop()`** is equivalent to `heappush()` followed by `heappop()`.

These are useful in some algorithms since they’re more efficient than doing the two operations separately.

### A High-Level Operation

Since priority queues are so often used to merge sorted sequences, the Python `heapq` module has a ready-made function, `merge()`, for using heaps to merge several iterables. `merge()` assumes its input iterables are already sorted and returns an **iterator**, not a list.

As an example of using `merge()`, here’s an implementation of the email scheduler described earlier:

```python
import datetime
import heapq

def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details

fast_email = email(datetime.timedelta(minutes=15), "fast email")
slow_email = email(datetime.timedelta(minutes=40), "slow email")

unified = heapq.merge(fast_email, slow_email)
```

The inputs to `merge()` in this example are [infinite generators](https://realpython.com/introduction-to-python-generators/#example-2-generating-an-infinite-sequence). The return value assigned to the [variable](https://realpython.com/python-variables/) `unified` is also an infinite iterator. This iterator will yield the emails to be sent in the order of the future timestamps.

To debug and confirm that the code is merging correctly, you can print the first ten emails to be sent:

```python
>>> for _ in range(10):
...    print(next(element))
(datetime.datetime(2020, 4, 12, 21, 27, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 21, 42, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 21, 52, 20, 305360), 'slow email')
(datetime.datetime(2020, 4, 12, 21, 57, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 22, 12, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 22, 27, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 22, 32, 20, 305360), 'slow email')
(datetime.datetime(2020, 4, 12, 22, 42, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 22, 57, 20, 305358), 'fast email')
(datetime.datetime(2020, 4, 12, 23, 12, 20, 305358), 'fast email')
```

Notice how the `fast email` is scheduled every `15` minutes, the `slow email` is scheduled every `40`, and the emails are properly interleaved so that they’re arranged in the order of their timestamps.

`merge()` doesn’t read all the input, but rather it works dynamically. Even though both inputs are infinite iterators, printing the first ten items finishes quickly.

In a similar way, when used to merge sorted sequences like log file lines arranged by timestamp, even if the logs are big, this will take reasonable amounts of memory.

## Problems Heaps Can Solve

As you saw above, heaps are good for incrementally merging sorted sequences. Two applications for heaps that you’ve already considered are scheduling periodic tasks and merging log files. However, there are many more applications.

Heaps can also help identify the top _n_ or bottom _n_ things. The Python `heapq` module has high-level functions that implement this behavior.

For example, this code gets as input the times from the [women’s 100 meters final](https://www.olympic.org/rio-2016/athletics/100m-women) at the 2016 Summer Olympics and prints the medalists, or top three finishers:

```python
>>> import heapq
>>> results="""\
... Christania Williams      11.80
... Marie-Josee Ta Lou       10.86
... Elaine Thompson          10.71
... Tori Bowie               10.83
... Shelly-Ann Fraser-Pryce  10.86
... English Gardner          10.94
... Michelle-Lee Ahye        10.92
... Dafne Schippers          10.90
... """
>>> top_3 = heapq.nsmallest(
...     3, results.splitlines(), key=lambda x: float(x.split()[-1])
... )
>>> print("\n".join(top_3))
Elaine Thompson          10.71
Tori Bowie               10.83
Marie-Josee Ta Lou       10.86
```

This code uses `nsmallest()` from the Python `heapq` module. `nsmallest()` returns the smallest elements in an iterable and accepts three arguments:

1.  **`n`** indicates how many elements to return.
2.  **`iterable`** identifies the elements or dataset to compare.
3.  **`key`** is a callable function that determines how elements are compared.

Here, the `key` function splits the line by whitespace, takes the last element, and converts it to a [floating-point number](https://realpython.com/python-data-types/#floating-point-numbers). This means the code will sort the lines by running time and return the three lines with the smallest running times. These correspond to the three fastest runners, which gives you the gold, silver, and bronze medal winners.

The Python `heapq` module also includes `nlargest()`, which has similar parameters and returns the largest elements. This would be useful if you wanted to get the medalists from the javelin throw competition, in which the goal is to throw the javelin as far as possible.

## How to Identify Problems

A heap, as an implementation of a priority queue, is a good tool for solving problems that involve extremes, like the most or least of a given metric.

There are other words that indicate a heap might be useful:

-   Largest
-   Smallest
-   Biggest
-   Smallest
-   Best
-   Worst
-   Top
-   Bottom
-   Maximum
-   Minimum
-   Optimal

Whenever a problem statement indicates that you’re looking for some extreme element, it’s worthwhile to think about whether a priority queue would be useful.

Sometimes the priority queue will be only _part_ of the solution, and the rest will be some variant on [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming). This is the case with the full example that you’ll see in the next section. Dynamic programming and priority queues are often useful together.

## Example: Finding Paths

The following example serves as a realistic use case for the Python `heapq` module. The example will use a classic algorithm that, as one part of it, requires a heap.

Imagine a robot that needs to navigate a two-dimensional maze. The robot needs to go from the origin, positioned at the top-left corner, to the destination at the bottom-right corner. The robot has a map of the maze in its memory, so it can plan out the whole path before setting out.

The goal is to have the robot finish the maze as quickly as possible.

Our algorithm is a variant of [Dijkstra’s algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). There are three data structures that are kept and updated throughout the algorithm:

1.  **`tentative`** is a map of a tentative path from the origin to a position, `pos`. The path is called _tentative_ because it’s the shortest _known_ path, but it might be improved upon.
    
2.  **`certain`** is set of points for which the path that `tentative` maps is _certain_ to be the shortest possible path.
    
3.  **`candidates`** is a heap of positions that have a path. The **sorting key** of the heap is the length of the path.
    

At each step, you perform up to four actions:

1.  Pop a candidate from `candidates`.
    
2.  Add the candidate to the `certain` set. If the candidate is already a member of the `certain` set, then skip next two actions.
    
3.  Find the shortest known path to the current candidate.
    
4.  For each of the current candidate’s immediate neighbors, see if going through the candidate gives a shorter path than the current `tentative` path. If so, then update the `tentative` path and the `candidates` heap with this new path.
    

The steps are run in a loop until the destination is added to the `certain` set. When the destination is in the `certain` set, you’re done. The output of the algorithm is the `tentative` path to the destination, which is now `certain` to be the shortest possible path.

### Top-Level Code

Now that you understand the algorithm, it’s time to write code to implement it. Before implementing the algorithm itself, it’s useful to write some support code.

First, you need to [import](https://realpython.com/absolute-vs-relative-python-imports/#a-quick-recap-on-imports) the Python `heapq` module:

```python
import heapq
```

You’ll use the functions from the Python `heapq` module to maintain a heap that will help you find the position with the shortest known path at each iteration.

The next step is to define the map as a variable in the code:

```python
map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""
```

The map is a [triple-quoted string](https://realpython.com/python-data-types/#triple-quoted-strings) that shows the area in which the robot can move as well as any obstacles.

Though a more realistic scenario would have you reading the map from a file, for teaching purposes it’s easier to define a variable in the code using this simple map. The code will work on any map, but it’s easier to understand and debug on a simple map.

This map is optimized to be easy to understand for a human reader of the code. The dot (`.`) is light enough that it looks empty, but it has the advantage of showing the dimensions of the allowed area. The `X` positions mark obstacles that the robot can’t go through.

### Support Code

The first function will convert the map to something easier to parse in code. `parse_map()` gets a map and analyzes it:

```python
def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination
```

The function takes a map and returns a tuple of three elements:

1.  A list of `lines`
2.  The `origin`
3.  The `destination`

This allows the rest of the code to work on data structures designed for computers, not for humans’ ability to visually scan.

The list of `lines` can be indexed by `(x, y)` coordinates. The expression `lines[y][x]` returns the value of the position as one of two characters:

1.  **A dot (`"."`)** indicates the position is an empty space.
2.  **The letter `"X"`** indicates the position is an obstacle.

This will be useful when you want to find which positions the robot can occupy.

The function `is_valid()` calculates whether a given `(x, y)` position is valid:

```python
def is_valid(lines, position):
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    if lines[y][x] == "X":
        return False
    return True
```

This function takes two arguments:

1.  **`lines`** is the map as a list of lines.
2.  **`position`** is the position to check as a two-tuple of integers indicating the `(x, y)` coordinates.

To be valid, a position has to be inside the boundaries of the map and not an obstacle.

The function checks that `y` is valid by checking the length of the `lines` list. The function next checks that `x` is valid by making sure it’s inside `lines[y]`. Finally, now that you know both coordinates are inside the map, the code checks that they’re not an obstacle by looking at the character in this position and comparing the character to `"X"`.

Another useful helper is `get_neighbors()`, which finds all the neighbors of a position:

```python
def get_neighbors(lines, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position
```

The function returns all the valid positions surrounding the current position.

`get_neighbors()` is careful to avoid identifying a position as its own neighbor, but it does allow diagonal neighbors. This is why at least one of `dx` and `dy` must not be zero, but it’s okay for both of them to be non-zero.

The final helper function is `get_shorter_paths()`, which finds shorter paths:

```python
def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path
```

`get_shorter_paths()` yields positions for which the path that has `through` as its last step is shorter than the current known path.

`get_shorter_paths()` has three parameters:

1.  **`tentative`** is a dictionary mapping a position to the shortest known path.
2.  **`positions`** is an iterable of positions to which you want to shorten the path.
3.  **`through`** is the position through which, perhaps, a shorter path to the `positions` can be found.

The assumption is that all elements in `positions` can be reached in one step from `through`.

The function `get_shorter_paths()` checks if using `through` as the last step will make a better path for each position. If there’s no known path to a position, then any path is shorter. If there is a known path, then you only yield the new path if its length is shorter. In order to make the API of `get_shorter_paths()` easier to use, part of the `yield` is also the shorter path.

All helper functions were written to be **pure functions**, meaning they don’t modify any data structures and only return values. This makes it easier to follow the core algorithm, which does all the data structure updates.

### Core Algorithm Code

To recap, you’re looking for the shortest path between the origin and the destination.

You keep three pieces of data:

1.  **`certain`** is the set of certain positions.
2.  **`candidates`** is the heap of candidates.
3.  **`tentative`** is a dictionary mapping nodes to the current shortest known path.

A position is in `certain` if you can be certain that the shortest known path is the shortest possible path. If the destination is in the `certain` set, then the shortest known path to the destination is unquestionably the shortest possible path, and you can return this path.

The heap of `candidates` is organized by the length of the shortest known path and is managed with the help of the functions in the Python `heapq` module.

At each step, you look at the candidate with the shortest known path. This is where the heap is being popped with `heappop()`. There is no shorter path to this candidate—all other paths go through some other node in `candidates`, and all of these are longer. Because of that, the current candidate can be marked `certain`.

You then look at all neighbors that have not been visited, and if going through the current node is an improvement, then you add them to the `candidates` heap using `heappush()`.

The function `find_path()` implements this algorithm:

```python
def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")
```

`find_path()` receives a `map` as a string and returns the path from the origin to the destination as a list of positions.

This function is a little long and complicated, so let’s walk through it one bit at a time:

-   **Lines 2 through 5** set up the variables that the loop will look at and update. You already know a path from the origin to itself, which is the empty path, of length 0.
    
-   **Line 6** defines the loop’s termination condition. If there are no `candidates`, then no paths can be shortened. If `destination` is in `certain`, then the path to `destination` can’t be made shorter.
    
-   **Lines 7 through 10** get a candidate using `heappop()`, skip the loop if it’s already in `certain`, and otherwise add the candidate to `certain`. This makes sure every candidate will be processed by the loop at most once.
    
-   **Lines 11 through 15** use `get_neighbors()` and `get_shorter_paths()` to find shorter paths to neighboring positions and update the `tentative` dictionary and `candidates` heap.
    
-   **Lines 16 through 19** deal with returning the correct result. If a path was found, then the function will return it. Although computing the paths _without_ the final position made implementing the algorithm simpler, it’s a nicer API to return it _with_ the destination. If no path is found, then an exception is raised.
    

Breaking the function into separate sections lets you understand it one part at a time.

### Visualization Code

If the algorithm was actually used by a robot, then the robot would probably perform better with a list of positions that it should travel through. However, to make the result better looking to humans, it would be nicer to visualize them.

`show_path()` draws a path on a map:

```python
def show_path(path, map):
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"
```

The function takes the `path` and `map` as parameters. It returns a new map with the path indicated by the at symbol (`"@"`).

### Running the Code

Finally, you need to call the functions. This can be done from the [Python interactive interpreter](https://realpython.com/interacting-with-python/#using-the-python-interpreter-interactively).

The following code will run the algorithm and show a pretty output:

```python
>>> path = find_path(map)
>>> print(show_path(path, map))
@@.....X..
..@....X..
...@XXXX..
....@@@@@.
.........@
```

First you get the shortest path from `find_path()`. Then you pass it to `show_path()` to render a map with the path marked on it. Finally, you `print()` the map to the standard output.

The path moves one step to the right, then a few diagonal steps toward the bottom-right, then several more steps to the right, and it finally finishes with a diagonal step to the bottom-right.

Congratulations! You’ve solved a problem using the Python `heapq` module.

These kinds of pathfinding problems, solvable by a combination of dynamic programming and priority queues, are common in [job interviews](https://realpython.com/python-coding-interview-tips/) and programming challenges. For example, the 2019 Advent of Code [included a problem](https://adventofcode.com/2019/day/18) that could be solved with the techniques described here.

## Conclusion

You now know what the **heap** and **priority queue** data structures are and what kinds of problems they’re useful in solving. You learned how to use the Python `heapq` module to use Python lists as heaps. You also learned how to use the high-level operations in the Python `heapq` module, like `merge()`, which use a heap internally.

**In this tutorial, you’ve learned how to:**

-   Use the **low-level functions** in the Python `heapq` module to solve problems that need a heap or a priority queue
-   Use the **high-level functions** in the Python `heapq` module for merging sorted iterables or finding the largest or smallest elements in an iterable
-   Recognize **problems** that heaps and priority queues can help solve
-   Predict the **performance** of code that uses heaps

With your knowledge of heaps and the Python `heapq` module, you can now solve many problems in which the solution depends on finding the smallest or largest element.