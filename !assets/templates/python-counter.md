---
created: 2024-05-01T00:02:31 (UTC -04:00)
tags: []
source: https://realpython.com/python-counter/
author: Real Python
---

# Python's Counter: The Pythonic Way to Count Objects – Real Python

> ## Excerpt
> In this step-by-step tutorial, you'll learn how to use Python's Counter to count several repeated objects at once.

---

Counting several repeated objects at once is a common problem in programming. Python offers a bunch of tools and techniques you can use to approach this problem. However, Python’s **`Counter`** from [`collections`](https://docs.python.org/3/library/collections.html#module-collections) provides a clean, efficient, and Pythonic solution.

This [dictionary](https://realpython.com/python-dicts/) subclass provides efficient counting capabilities out of the box. Understanding `Counter` and how to use it efficiently is a convenient skill to have as a Python developer.

**In this tutorial, you’ll learn how to:**

-   Count **several repeated objects** at once
-   Create counters with Python’s **`Counter`**
-   Retrieve the **most common objects** in a counter
-   Update **object counts**
-   Use `Counter` to facilitate **further computations**

You’ll also learn about the basics of using `Counter` as a [multiset](https://en.wikipedia.org/wiki/Multiset), which is an additional feature of this class in Python.

## Counting Objects in Python

Sometimes you need to count the objects in a given data source to know how often they occur. In other words, you need to determine their **frequency**. For example, you might want to know how often a specific item appears in a list or sequence of values. When your list is short, counting the items can be straightforward and quick. However, when you have a long list, counting things can be more challenging.

To count objects, you typically use a **counter**, which is an [integer variable](https://realpython.com/python-numbers/#integers) with an initial value of zero. Then you increment the counter to reflect the number of times a given object appears in the input data source.

When you’re counting the occurrences of a single object, you can use a single counter. However, when you need to count several different objects, you have to create as many counters as unique objects you have.

To count several different objects at once, you can use a Python dictionary. The dictionary **keys** will store the objects you want to count. The dictionary **values** will hold the number of repetitions of a given object, or the object’s **count**.

For example, to count the objects in a sequence using a dictionary, you can loop over the sequence, check if the current object isn’t in the dictionary to initialize the counter (key-value pair), and then increment its count accordingly.

Here's an example that counts the letters in the word "Mississippi":

```python
>>> word = "mississippi"
>>> counter = {}

>>> for letter in word:
...     if letter not in counter:
...         counter[letter] = 0
...     counter[letter] += 1
...

>>> counter
{'m': 1, 'i': 4, 's': 4, 'p': 2}
```

The [`for` loop](https://realpython.com/python-for-loop/) iterates over the letters in `word`. In each iteration, the [conditional statement](https://realpython.com/python-conditional-statements/) checks if the letter at hand isn’t already a key in the dictionary you’re using as `counter`. If so, it creates a new key with the letter and initializes its count to zero. The final step is to increment the count by one. When you access `counter`, you see that the letters work as keys and the values as counts.

> [!note]
> When you’re counting several repeated objects with Python dictionaries, keep in mind that they must be [hashable](https://docs.python.org/3/glossary.html#term-hashable) because they’ll work as dictionary keys. Being **hashable** means that your objects must have a hash value that never changes during their lifetime. In Python, [immutable](https://docs.python.org/3/glossary.html#term-immutable) objects are also hashable.

Another way to count objects with a dictionary is to use [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) with `0` as a default value:

```python
>>> word = "mississippi"
>>> counter = {}

>>> for letter in word:
...     counter[letter] = counter.get(letter, 0) + 1
...

>>> counter
{'m': 1, 'i': 4, 's': 4, 'p': 2}
```

When you call `.get()` this way, you get the current count of a given `letter`, or `0` (the default) if the letter is missing. Then you increment the count by `1` and store it under the corresponding `letter` in the dictionary.

You can also use [`defaultdict`](https://realpython.com/python-defaultdict/) from [`collections`](https://docs.python.org/3/library/collections.html#module-collections) to count objects within a loop:

```python
>>> from collections import defaultdict

>>> word = "mississippi"
>>> counter = defaultdict(int)

>>> for letter in word:
...     counter[letter] += 1
...

>>> counter
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
```

This solution is more concise and readable. You first initialize the `counter` using a `defaultdict` with [`int()`](https://docs.python.org/3/library/functions.html#int) as a default factory function. This way, when you access a key that doesn’t exist in the underlying `defaultdict`, the dictionary automatically creates the key and initializes it with the value that the factory function returns.

In this example, since you’re using `int()` as a [factory function](https://realpython.com/factory-method-python/), the initial value is `0`, which results from calling `int()` without arguments.

Like with many other frequent tasks in programming, Python provides a better way to approach the counting problem. In `collections`, you’ll find a class specially designed to count several different objects in one go. This class is conveniently called [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter).

## Getting Started With Python’s `Counter`

`Counter` is a subclass of `dict` that’s specially designed for counting hashable objects in Python. It’s a dictionary that stores objects as keys and counts as values. To count with `Counter`, you typically provide a sequence or [iterable](https://docs.python.org/3/glossary.html#term-iterable) of hashable objects as an argument to the class’s constructor.

`Counter` internally iterates through the input sequence, counts the number of times a given object occurs, and stores objects as keys and the counts as values. In the next section, you’ll learn about different ways to construct counters.

### Constructing Counters

There are a few ways for you to create `Counter` instances. However, if your goal is to count several objects at once, then you need to use a sequence or iterable to initialize the counter. For example, here’s how you can rewrite the Mississippi example using `Counter`:

```python
>>> from collections import Counter

>>> # Use a string as an argument
>>> Counter("mississippi")
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

>>> # Use a list as an argument
>>> Counter(list("mississippi"))
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

`Counter` iterates over `"mississippi"` and produces a dictionary with the letters as keys and their frequency as values. In the first example, you use a string as an argument to `Counter`. You can also use [lists, tuples](https://realpython.com/python-lists-tuples/), or any iterables with repeated objects, as you see in the second example.

> [!note]
> In `Counter`, a highly optimized C function provides the counting functionality. If this function isn’t available for some reason, then the class uses an equivalent but less efficient Python function.

There are other ways to create `Counter` instances. However, they don’t strictly imply counting. For example, you can use a dictionary containing keys and counts like this:

```python
>>> from collections import Counter

>>> Counter({"i": 4, "s": 4, "p": 2, "m": 1})
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

The counter now has an initial group of key-count pairs. This way to create a `Counter` instance is useful when you need to provide initial counts of an existing group of objects.

You can also produce similar results by using keyword arguments when you call the class’s constructor:

```python
>>> from collections import Counter

>>> Counter(i=4, s=4, p=2, m=1)
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

Again, you can use this approach to create a `Counter` object with a specific initial state for its keys and counts pairs.

In practice, if you’re using `Counter` to count things from scratch, then you don’t need to initialize the counts since they have a zero value by default. Another possibility might be to initialize the counts to `1`. In that case, you can do something like this:

```python
>>> from collections import Counter

>>> Counter(set("mississippi"))
Counter({'p': 1, 's': 1, 'm': 1, 'i': 1})
```

Python [sets](https://realpython.com/python-sets/) store unique objects, so the call to `set()` in this example throws out the repeated letters. After this, you end up with one instance of each letter in the original iterable.

`Counter` inherits the interface of regular dictionaries. However, it doesn’t provide a working implementation of [`.fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys) to prevent ambiguities, such as `Counter.fromkeys("mississippi", 2)`. In this specific example, each letter would have a default count of `2` despite of its current number of occurrences in the input iterable.

There are no restrictions on the objects you can store in the keys and values of a counter. The keys can store hashable objects, whereas the values can store any objects. However, to work as counters, the values should be integer numbers representing counts.

Here's an example of a `Counter` instance that holds negative and zero counts:

```python
>>> from collections import Counter

>>> inventory = Counter(
...     apple=10,
...     orange=15,
...     banana=0,
...     tomato=-15
... )
```

In this example, you may ask, “Why do I have `-15` tomatoes?” Well, that could be an internal convention to signal that you have a client’s order for `15` tomatoes, and you don’t have any in your current inventory. Who knows? `Counter` allows you to do this, and you can probably find a few use cases for the feature.

### Updating Object Counts

Once you have a `Counter` instance in place, you can use `.update()` to update it with new objects and counts. Rather than replacing values like its `dict` counterpart, the [`.update()`](https://docs.python.org/3/library/collections.html#collections.Counter.update) implementation provided by `Counter` adds existing counts together. It also creates new key-count pairs when necessary.

You can use `.update()` with both iterables and mappings of counts as arguments. If you use an iterable, the method counts its items and updates the counter accordingly:

```python
>>> from collections import Counter

>>> letters = Counter({"i": 4, "s": 4, "p": 2, "m": 1})

>>> letters.update("missouri")
>>> letters
Counter({'i': 6, 's': 6, 'p': 2, 'm': 2, 'o': 1, 'u': 1, 'r': 1})
```

Now you have `6` instances of `i`, `6` instances of `s`, and so on. You also have some new key-count pairs, such as `'o': 1`, `'u': 1`, and `'r': 1`. Note that the iterable needs to be a sequence of items rather than a sequence of `(key, count)` pairs.

> [!note]
> As you already know, there are no restrictions on the values (counts) that you can store in a counter.
> 
> Using objects other than integer numbers for the counts breaks common counter features:
> ```python
> >>> from collections import Counter
>
>>>> letters = Counter({"i": "4", "s": "4", "p": "2", "m": "1"})
>
>>>> letters.update("missouri")
Traceback (most recent call last):
  ...
>TypeError: can only concatenate str (not "int") to str
>```
>
> In this example, the letter counts are strings instead of integer values. This breaks `.update()`, resulting in a `TypeError`.

The second way to use `.update()` is to provide another counter or a mapping of counts as an argument. In that case, you can do something like this:

```python
>>> from collections import Counter
>>> sales = Counter(apple=25, orange=15, banana=12)

>>> # Use a counter
>>> monday_sales = Counter(apple=10, orange=8, banana=3)
>>> sales.update(monday_sales)
>>> sales
Counter({'apple': 35, 'orange': 23, 'banana': 15})

>>> # Use a dictionary of counts
>>> tuesday_sales = {"apple": 4, "orange": 7, "tomato": 4}
>>> sales.update(tuesday_sales)
>>> sales
Counter({'apple': 39, 'orange': 30, 'banana': 15, 'tomato': 4})
```

In the first example, you update an existing counter, `sales`, using another counter, `monday_sales`. Note how `.update()` adds the count from both counters.

> [!note]
> You can also use `.update()` with keyword arguments. So, for example, doing something like `sales.update(apple=10, orange=8, banana=3)` works the same as `sales.update(monday_sales)` in the example above.

Next, you use a regular dictionary containing items and counts. In this case, `.update()` adds the counts of existing keys and creates the missing key-count pairs.

### Accessing the Counter’s Content

As you already know, `Counter` has almost the same interface as `dict`. You can perform nearly the same actions with counters as you can with standard dictionaries. For example, you can access their values using dictionary-like key access (`[key]`). You can also iterate over the keys, values, and items using the usual techniques and methods:

```python
>>> from collections import Counter

>>> letters = Counter("mississippi")
>>> letters["p"]
2
>>> letters["s"]
4

>>> for letter in letters:
...     print(letter, letters[letter])
...
m 1
i 4
s 4
p 2

>>> for letter in letters.keys():
...     print(letter, letters[letter])
...
m 1
i 4
s 4
p 2

>>> for count in letters.values():
...     print(count)
...
1
4
4
2

>>> for letter, count in letters.items():
...     print(letter, count)
...
m 1
i 4
s 4
p 2
```

In these examples, you access and iterate over the keys (letters) and values (counts) of your counter using the familiar dictionary interface, which includes methods such as `.keys()`, `.values()`, and `.items()`.

> [!note]
> If you want to dive deeper into how to iterate through a dictionary, then check out How to Iterate Through a Dictionary in Python.

A final point to note about `Counter` is that if you try to access a missing key, then you get zero instead of a [`KeyError`](https://realpython.com/python-keyerror/):

```python
>>> from collections import Counter

>>> letters = Counter("mississippi")
>>> letters["a"]
0
```

Since the letter `"a"` doesn’t appear in the string `"mississippi"`, the counter returns `0` when you try to access the count for that letter.

### Finding Most Common Objects

If you need to list a group of objects according to their frequency, or the number of times they appear, then you can use [`.most_common()`](https://docs.python.org/3/library/collections.html#collections.Counter.most_common). This method returns a list of `(object, count)` sorted by the objects’ current count. Objects with equal counts come in the order they first appear.

If you supply an integer number `n` as an argument to `.most_common()`, then you get the `n` most common objects. If you omit `n` or set it to `None`, then `.most_common()` returns all the objects in the counter:

```python
>>> from collections import Counter
>>> sales = Counter(banana=15, tomato=4, apple=39, orange=30)

>>> # The most common object
>>> sales.most_common(1)
[('apple', 39)]

>>> # The two most common objects
>>> sales.most_common(2)
[('apple', 39), ('orange', 30)]

>>> # All objects sorted by count
>>> sales.most_common()
[('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]

>>> sales.most_common(None)
[('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]

>>> sales.most_common(20)
[('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]
```

In these examples, you use `.most_common()` to retrieve the most frequent objects in `sales`. With no argument or with [`None`](https://realpython.com/null-in-python/), the method returns all the objects. If the argument to `.most_common()` is greater than the current counter’s length, then you get all the objects again.

You can also get the least-common objects by [slicing](https://docs.python.org/dev/whatsnew/2.3.html#extended-slices) the result of `.most_common()`:

```python
>>> from collections import Counter
>>> sales = Counter(banana=15, tomato=4, apple=39, orange=30)

>>> # All objects in reverse order
>>> sales.most_common()[::-1]
[('tomato', 4), ('banana', 15), ('orange', 30), ('apple', 39)]

>>> # The two least-common objects
>>> sales.most_common()[:-3:-1]
[('tomato', 4), ('banana', 15)]
```

The first slicing, `[::-1]`, returns all the objects in `sales` in reverse order according to their respective counts. The slicing `[:-3:-1]` extracts the last two objects from the result of `.most_common()`. You can tweak the number of least-common objects you get by changing the second offset value in the slicing operator. For example, to get the three least-frequent objects, you can change `-3` to `-4`, and so on.

> [!note]
> Check out Reverse Python Lists: Beyond .reverse() and reversed() for hands-on examples of using the slicing syntax.

If you want `.most_common()` to work correctly, then make sure that the values in your counters are sortable. This is something to keep in mind because, as mentioned, you can store any data types in a counter.

## Putting `Counter` Into Action

So far, you’ve learned the basics of creating and using `Counter` objects in your code. You now know how to count the number of times each object appears in a given sequence or iterable. You also know how to:

-   Create counters with initial values
-   Update existing counters
-   Get the most frequent objects in a given counter

In the following sections, you’ll code some practical examples so you can get a better idea of how useful Python’s `Counter` can be.

### Counting Letters in a Text File

Say you have a file that contains some text. You need to count the number of times each letter appears in the text. For example, say you have a file called `pyzen.txt` with the following content:

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Yes, this is [The Zen of Python](https://realpython.com/zen-of-python/), a list of guiding principles that define the core philosophy behind Python’s design. To count the number of times each letter appears in this text, you can take advantage of `Counter` and [write a function](https://realpython.com/defining-your-own-python-function/) like this:

```python
# letters.py

from collections import Counter

def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            letter_counter.update(Counter(line_letters))
    return letter_counter
```

Here’s how this code works:

-   **Line 5** defines `count_letters()`. This function takes a string-based file path as an argument.
-   **Line 6** creates an empty counter for counting the letters in the target text.
-   **Line 7** [opens the input file for reading](https://realpython.com/read-write-files-python/) and creates an iterator over the file content.
-   **Line 8** starts a loop that iterates through the file content line by line.
-   **Lines 9 to 11** define a list comprehension to exclude nonletter characters from the current line using [`.isalpha()`](https://docs.python.org/3/library/stdtypes.html#str.isalpha). The comprehension lowercases the letters before filtering them to prevent having separate lowercase and uppercase counts.
-   **Line 12** calls `.update()` on the letters counter to update the counts of each letter.

To use `count_letters()`, you can do something like this:

```python
>>> from letters import count_letters
>>> letter_counter = count_letters("pyzen.txt")

>>> for letter, count in letter_counter.items():
...     print(letter, "->", count)
...
t -> 79
h -> 31
e -> 92
z -> 1
  ...
k -> 2
v -> 5
w -> 4

>>> for letter, count in letter_counter.most_common(5):
...     print(letter, "->", count)
...
e -> 92
t -> 79
i -> 53
a -> 53
s -> 46
```

Great! Your code counts the frequency of every letter in a given text file. Linguists often use [letter frequency](https://en.wikipedia.org/wiki/Letter_frequency) for [language identification](https://en.wikipedia.org/wiki/Language_identification). In English, for example, studies on the average letter frequency have revealed that the five most common letters are “e,” “t,” “a,” “o,” and “i.” Wow! That almost matches your results!

### Plotting Categorical Data With ASCII Bar Charts

[Statistics](https://en.wikipedia.org/wiki/Statistics) is another field in which you can use `Counter`. For example, when you’re working with [categorical](https://en.wikipedia.org/wiki/Categorical_variable) data, you might want to create [bar charts](https://en.wikipedia.org/wiki/Bar_chart) to visualize the number of observations per category. Bar charts are especially handy for plotting this type of data.

Now say you want to create a function that allows you to create ASCII bar chart on your terminal. To do that, you can use the following code:

```python
# bar_chart.py

from collections import Counter

def print_ascii_bar_chart(data, symbol="#"):
    counter = Counter(data).most_common()
    chart = {category: symbol * frequency for category, frequency in counter}
    max_len = max(len(category) for category in chart)
    for category, frequency in chart.items():
        padding = (max_len - len(category)) * " "
        print(f"{category}{padding} |{frequency}")
```

In this example, `print_ascii_bar_chart()` takes some categorical `data`, counts the number of times each unique category appears in the data (`frequency`), and generates an ASCII bar chart that reflects that frequency.

Here’s how you can use this function:

```python
>>> from bar_chart import print_ascii_bar_chart

>>> letters = "mississippimississippimississippimississippi"
>>> print_ascii_bar_chart(letters)
i |################
s |################
p |########
m |####

>>> from collections import Counter
>>> sales = Counter(banana=15, tomato=4, apple=39, orange=30)

>>> print_ascii_bar_chart(sales, symbol="+")
apple  |+++++++++++++++++++++++++++++++++++++++
orange |++++++++++++++++++++++++++++++
banana |+++++++++++++++
tomato |++++
```

The first call to `print_ascii_bar_chart()` plots the frequency of each letter in the input string. The second call plots sales per fruit. In this case, you use a counter as input. Also, note that you can use `symbol` to change the character for the bars.

> [!note]
> In the example above, `print_ascii_bar_chart()` doesn’t normalize the frequency values when it draws the charts. If you use data with high frequency values, then your screen will look like a mess of symbols.

When you’re creating bar charts, using horizontal bars allows you to have enough room for the category labels. Another helpful feature of bar charts is the possibility of sorting the data according to their frequency. In this example, you sort the data using `.most_common()`.

### Plotting Categorical Data With Matplotlib

It’s nice to know how to create ASCII bar charts from scratch using Python. However, in the Python ecosystem, you can find several tools for plotting data. One of those tools is [Matplotlib](https://realpython.com/python-matplotlib-guide/).

Matplotlib is a third-party library for creating statical, animated, and interactive visualizations in Python. You can [install](https://matplotlib.org/stable/users/installing.html) the library from [PyPI](https://realpython.com/pypi-publish-python-package/) using [`pip`](https://realpython.com/what-is-pip/) as usual:

```shell
$ python -m pip install matplotlib
```

This command installs Matplotlib in your Python [environment](https://realpython.com/effective-python-environment/). Once you’ve installed the library, you can use it to create your bar charts and more. Here’s how you can create a minimal bar chart with Matplotlib:

```python
>>> from collections import Counter
>>> import matplotlib.pyplot as plt

>>> sales = Counter(banana=15, tomato=4, apple=39, orange=30).most_common()
>>> x, y = zip(*sales)
>>> x
('apple', 'orange', 'banana', 'tomato')
>>> y
(39, 30, 15, 4)

>>> plt.bar(x, y)
<BarContainer object of 4 artists>
>>> plt.show()
```

Here, you first do the required [imports](https://realpython.com/absolute-vs-relative-python-imports/). Then you create a counter with some initial data about fruit sales and use `.most_common()` to sort the data.

You use [`zip()`](https://realpython.com/python-zip-function/) to unzip the content of `sales` into two variables:

1.  **`x`** holds a list of fruits.
2.  **`y`** holds the corresponding units sold per fruit.

Then you create a bar chart using [`plt.bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar). When you run [`plt.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show), you get a window like the following on your screen:

![[../../../!assets/attachments/Pasted image 20240501000711.png]]

In this chart, the horizontal axis shows the name of each unique fruit. Meanwhile, the vertical axis indicates the number of units sold per fruit.

### Finding the Mode of a Sample

In statistics, the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) is the most frequent value (or values) in a sample of data. For example, if you have the sample `[2, 1, 2, 2, 3, 5, 3]`, then the mode is `2` because it appears most frequently.

In some cases, the mode isn’t a unique value. Consider the sample `[2, 1, 2, 2, 3, 5, 3, 3]`. Here you have two modes, `2` and `3`, because both appear the same number of times.

You’ll often use the mode to describe categorical data. For example, the mode is useful when you need to know which category is the most common in your data.

To find the mode with Python, you need to count the number of occurrences of each value in your sample. Then you have to find the most frequent value (or values). In other words, the value with the highest number of occurrences. That sounds like something you can do using `Counter` and `.most_common()`.

> [!note]
> Python’s `statistics` module in the standard library provides functions for calculating several statistics, including the mode of unimodal and multimodal samples. The example below is just intended to show how useful Counter can be.

Here’s a function that computes the mode of a sample:

```python
# mode.py

from collections import Counter

def mode(data):
    counter = Counter(data)
    _, top_count = counter.most_common(1)[0]
    return [point for point, count in counter.items() if count == top_count]
```

Inside `mode()`, you first count the number of times each observation appears in the input `data`. Then you use `.most_common(1)` to get the frequency of the most common observation. Since `.most_common()` returns a list of tuples in the form `(point, count)`, you need to retrieve the tuple at index `0`, which is the most common in the list. Then you unpack the tuple into two variables:

1.  **`_`** holds the most common object. Using an [underscore](https://realpython.com/python-double-underscore/) to name a variable suggests that you don’t need to use that variable in your code, but you need it as a placeholder.
2.  **`top_count`** holds the frequency of the most common object in `data`.

The list comprehension compares the `count` of each object with the count of the most common one, `top_count`. This allows you to identify multiple modes in a given sample.

To use this function, you can do something like this:

```python
>>> from collections import Counter
>>> from mode import mode

>>> # Single mode, numerical data
>>> mode([2, 1, 2, 2, 3, 5, 3])
[2]

>>> # Multiple modes, numerical data
>>> mode([2, 1, 2, 2, 3, 5, 3, 3])
[2, 3]

>>> # Single mode, categorical data
>>> data = [
...     "apple",
...     "orange",
...     "apple",
...     "apple",
...     "orange",
...     "banana",
...     "banana",
...     "banana",
...     "apple",
... ]

>>> mode(data)
['apple']

>>> # Multiple modes, categorical data
>>> mode(Counter(apple=4, orange=4, banana=2))
['apple', 'orange']
```

Your `mode()` works! It finds the mode of numerical and categorical data. It also works with single-mode and multimode samples. Most of the time, your data will come in a sequence of values. However, the final example shows that you can also use a counter to provide the input data.

### Counting Files by Type

Another interesting example involving `Counter` is to count the files in a given directory, grouping them by file extension or file type. To do that, you can take advantage of [`pathlib`](https://realpython.com/python-pathlib/):

```python
>>> import pathlib
>>> from collections import Counter

>>> entries = pathlib.Path("Pictures/").iterdir()
>>> extensions = [entry.suffix for entry in entries if entry.is_file()]
['.gif', '.png', '.jpeg', '.png', '.png', ..., '.png']

>>> Counter(extensions)
Counter({'.png': 50, '.jpg': 11, '.gif': 10, '.jpeg': 9, '.mp4': 9})
```

In this example, you first create an iterator over the entries in a given directory using [`Path.iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir). Then you use a list comprehension to build a list containing the extensions ([`.suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix)) of all the files in the target directory. Finally, you count the number of files using the file extension as the grouping criteria.

If you run this code on your computer, then you’ll get a different output depending on the content of your `Pictures/` directory, if it exists at all. So, you’ll probably need to use another input directory for this code to work.

## Using `Counter` Instances as Multisets

In math, a [multiset](https://en.wikipedia.org/wiki/Multiset) represents a variation of a [set](https://en.wikipedia.org/wiki/Set_(mathematics)) that allows multiple instances of its [elements](https://en.wikipedia.org/wiki/Element_(mathematics)). The number of instances of a given element is known as its **multiplicity**. So, you can have a multiset like {1, 1, 2, 3, 3, 3, 4, 4}, but the set version will be limited to {1, 2, 3, 4}.

Just like in math, regular Python [sets](https://realpython.com/python-sets/) allow unique elements only:

```python
>>> # A Python set
>>> {1, 1, 2, 3, 3, 3, 4, 4}
{1, 2, 3, 4}
```

When you create a set like this, Python removes all the repeated instances of each number. As a result, you get a set with unique elements only.

Python supports the concept of multisets with `Counter`. The keys in a `Counter` instance are unique, so they’re equivalent to a set. The counts hold the multiplicity, or the number of instances, of each element:

```python
>>> from collections import Counter

>>> # A Python multiset
>>> multiset = Counter([1, 1, 2, 3, 3, 3, 4, 4])
>>> multiset
Counter({3: 3, 1: 2, 4: 2, 2: 1})

>>> # The keys are equivalent to a set
>>> multiset.keys() == {1, 2, 3, 4}
True
```

Here, you first create a multiset using `Counter`. The keys are equivalent to the set you saw in the example above. The values hold the multiplicity of each element in the set.

`Counter` implements a bunch of multiset features that you can use to solve several problems. A common use case for a multiset in programming is a shopping cart because it can contain more than one instance of each product, depending on the client’s needs:

```python
>>> from collections import Counter

>>> prices = {"course": 97.99, "book": 54.99, "wallpaper": 4.99}
>>> cart = Counter(course=1, book=3, wallpaper=2)

>>> for product, units in cart.items():
...     subtotal = units * prices[product]
...     price = prices[product]
...     print(f"{product:9}: ${price:7.2f} × {units} = ${subtotal:7.2f}")
...
course   : $  97.99 × 1 = $  97.99
book     : $  54.99 × 3 = $ 164.97
wallpaper: $   4.99 × 2 = $   9.98
```

In this example, you create a shopping cart using a `Counter` object as a multiset. The counter provides information about a client’s order, which includes several learning resources. The `for` loop iterates through the counter and computes the `subtotal` for each `product` and [prints](https://realpython.com/python-print/) it to your screen.

To reinforce your knowledge of using `Counter` objects as multisets, you can expand the box below and complete the exercise. When you’re finished, expand the solution box to compare your results.

> [!note]
> As an exercise, you can modify the example above to calculate the total amount to pay at checkout.
>
> Here’s a possible solution:
> 
> ```python
> >>> from collections import Counter
>
>>>> prices = {"course": 97.99, "book": 54.99, "wallpaper": 4.99}
>>>> cart = Counter(course=1, book=3, wallpaper=2)
>>>> total = 0.0
>
>>>> for product, units in cart.items():
>...     subtotal = units * prices[product]
>...     price = prices[product]
>...     print(f"{product:9}: ${price:7.2f} × {units} = ${subtotal:7.2f}")
>...     total += subtotal
>...
>course   : $  97.99 × 1 = $  97.99
>book     : $  54.99 × 3 = $ 164.97
>wallpaper: $   4.99 × 2 = $   9.98
>
>>>> total
>272.94
> ```
> 
> In the first highlighted line, you add a new variable to hold the total cost of all the products you ordered. In the second highlighted line, you use an [augmented assignment](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements) to accumulate every `subtotal` in `total`.

Now that you have an idea of what a multiset is and how Python implements them, you can take a look at some of the multiset features that `Counter` provides.

### Restoring Elements From a Counter

The first multiset feature of `Counter` that you’re going to learn about is [`.elements()`](https://docs.python.org/3/library/collections.html#collections.Counter.elements). This method returns an iterator over the elements in a multiset (`Counter` instance), repeating each of them as many times as its count says:

```python
>>> from collections import Counter

>>> for letter in Counter("mississippi").elements():
...     print(letter)
...
m
i
i
i
i
s
s
s
s
p
p
```

The net effect of calling `.elements()` on a counter is to restore the original data you used to create the counter itself. The method returns the elements—letters in this example—in the same order they first appear in the underlying counter. Since [Python 3.7](https://realpython.com/python37-new-features/), `Counter` remembers the insertion order of its keys as a feature inherited from `dict`.

> [!note]
> As you already know, you can create counters with zeroed and negative counts. If an element’s count is less than one, then `.elements()` ignores it.

The [docstring](https://realpython.com/documenting-python-code/) of `.elements()` in the [source code file](https://github.com/python/cpython/blob/150af7543214e1541fa582374502ac1cd70e8eb4/Lib/collections/__init__.py#L607) provides an interesting example of using this method to compute a number from its [prime factors](https://en.wikipedia.org/wiki/Prime_number#Unique_factorization). Since a given prime factor may occur more than once, you might end up with a multiset. For example, you can express the number 1836 as the product of its prime factors like this:

1836 = 2 × 2 × 3 × 3 × 3 × 17 = 2<sup>2</sup> × 3<sup>3</sup> × 17<sup>1</sup>

You can write this expression as a multiset like {2, 2, 3, 3, 3, 17}. Using a Python’s `Counter`, you’ll have `Counter({2: 2, 3: 3, 17: 1})`. Once you have this counter in place, you can compute the original number using its prime factors:

```python
>>> from collections import Counter

>>> # Prime factors of 1836
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> product = 1

>>> for factor in prime_factors.elements():
...     product *= factor
...

>>> product
1836
```

The loop iterates over the elements in `prime_factors` and multiplies them to compute the original number, `1836`. If you’re using [Python 3.8](https://realpython.com/python38-new-features/) or beyond, then you can use [`prod()`](https://realpython.com/python-math-module/#new-additions-to-the-math-module-in-python-38) from [`math`](https://realpython.com/python-math-module/) to get a similar result. This function calculates the product of all elements in the input iterable:

```python
>>> import math
>>> from collections import Counter

>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> math.prod(prime_factors.elements())
1836
```

In this example, the call to `.elements()` restores the prime factors. Then `math.prod()` computes `1836` from them in one go, which saves you from writing a loop and from having a few intermediate variables.

Using `.elements()` provides a way to restore the original input data. Its only drawback is that, in most cases, the order of items in the input won’t match the order in the output:

```python
>>> from collections import Counter

>>> "".join(Counter("mississippi").elements())
'miiiisssspp'
```

In this example, the resulting string doesn’t spell the original word, `mississippi`. However, it has the same content in terms of letters.

### Subtracting the Elements' Multiplicity

Sometimes you need to subtract the multiplicity (count) of the elements in a multiset or counter. In that case, you can use `.subtract()`. As its name implies, this method subtracts the counts supplied in an iterable or mapping from the counts in the target counter.

Say you have a multiset with your current fruit inventory and you need to keep it up to date. Then you can run some of the following operations:

```python
>>> from collections import Counter

>>> inventory = Counter(apple=39, orange=30, banana=15)

>>> # Use a counter
>>> wastage = Counter(apple=6, orange=5, banana=8)
>>> inventory.subtract(wastage)
>>> inventory
Counter({'apple': 33, 'orange': 25, 'banana': 7})

>>> # Use a mapping of counts
>>> order_1 = {"apple": 12, "orange": 12}
>>> inventory.subtract(order_1)
>>> inventory
Counter({'apple': 21, 'orange': 13, 'banana': 7})

>>> # Use an iterable
>>> order_2 = ["apple", "apple", "apple", "apple", "banana", "banana"]
>>> inventory.subtract(order_2)
>>> inventory
Counter({'apple': 17, 'orange': 13, 'banana': 5})
```

Here, you use several ways to provide the input data to `.subtract()`. In all cases, you update the counts of each unique object by subtracting the counts provided in the input data. You can think of `.subtract()` as the counterpart of `.update()`.

### Doing Arithmetic With Elements’ Multiplicity

With `.subtract()` and `.update()`, you can combine counters by subtracting and adding corresponding element counts. Alternatively, Python provides handy operators for addition (`+`) and subtraction (`-`) of element counts, as well as operators for intersection (`&`) and union (`|`). The **intersection** operator returns the minimum of corresponding counts, while the **union** operator returns the maximum of counts.

Here are a few examples of how all these operators work:

```python
>>> from collections import Counter

>>> # Fruit sold per day
>>> sales_day1 = Counter(apple=4, orange=9, banana=4)
>>> sales_day2 = Counter(apple=10, orange=8, banana=6)

>>> # Total sales
>>> sales_day1 + sales_day2
Counter({'orange': 17, 'apple': 14, 'banana': 10})

>>> # Sales increment
>>> sales_day2 - sales_day1
Counter({'apple': 6, 'banana': 2})

>>> # Minimum sales
>>> sales_day1 & sales_day2
Counter({'orange': 8, 'apple': 4, 'banana': 4})

>>> # Maximum sales
>>> sales_day1 | sales_day2
Counter({'apple': 10, 'orange': 9, 'banana': 6})
```

Here, you first add two counters together using the addition operator (`+`). The resulting counter contains the same keys (elements), while their respective values (multiplicities) hold the sum of counts from both involved counters.

The second example shows how the subtraction operator (`-`) works. Note that negative and zero counts result in not including the key-count pair in the resulting counter. So, you don’t see `orange` in the output because 8 - 9 = -1.

The intersection operator (`&`) extracts the objects with lower counts from both counters, whereas the union operator (`|`) returns the objects with higher counts from both involved counters.

> [!note]
> For further details on how Counter handles arithmetic operations, check out the class documentation.

`Counter` also supports some **unary operations**. For example, you can get the items with positive and negative counts using the plus (`+`) and minus (`-`) signs, respectively:

```python
>>> from collections import Counter

>>> counter = Counter(a=2, b=-4, c=0)

>>> +counter
Counter({'a': 2})

>>> -counter
Counter({'b': 4})
```

When you use the plus sign (`+`) as a unary operator on an existing counter, you get all the objects whose counts are greater than zero. On the other hand, if you use the minus sign (`-`), you get the objects with negative counts. Note that the result excludes objects whose counts are equal to zero in both cases.

## Conclusion

When you need to count several repeated objects in Python, you can use `Counter` from `collections`. This class provides an efficient and Pythonic way to count things without the need for using traditional techniques involving loops and nested data structures. This can make your code cleaner and faster.

**In this tutorial, you learned how to:**

-   Count **several repeated objects** using different Python tools
-   Create quick and efficient counters with Python’s **`Counter`**
-   Retrieve the **most common objects** in a particular counter
-   Update and manipulate **object counts**
-   Use `Counter` to facilitate **further computations**

You also learned the basics of using `Counter` instances as multisets. With all this knowledge, you’ll be able to quickly count objects in your code and also to perform math operations with multisets.