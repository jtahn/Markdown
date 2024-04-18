

# assorted
- hashing/existence
- stacks/queues
- bucket sort
	- candidate [347. Top K Frequent Elements](../LeetCode/347.%20Top%20K%20Frequent%20Elements.md)
- quick select
	- candidate [973. K Closest Points to Origin](../LeetCode/973.%20K%20Closest%20Points%20to%20Origin.md)
- monotone stacks/queues
	- current candidate is [84. Largest Rectangle in Histogram](../LeetCode/84.%20Largest%20Rectangle%20in%20Histogram.md)
		- is this is the fundamental problem tho; bc 'array jumping' still works
			- and 'array jumping' 
		- otoh: seems 'array jumping' is equivalent to monotone stacks/queues? ie same space complexity
		- [739. Daily Temperatures](../LeetCode/739.%20Daily%20Temperatures.md) is NOT the fundamental problem
			- bc there is an in-place technique iirc; aka there's something about this problem that is different
			- however this problem raises an interesting observation about how it matters for space complexity, which direction you iterate through; i highly suspect this should go into the discussion for this technique
- recursion
	- it seems recursion typically needs an aux function, so i don't need to say this
		- for one of the easier problems where recursion is "the" solution, i should have a discussion about why we can define functions inside functions in python
			- and maybe also, whether it's better to define aux function as a class method instead, ie outside the 'main' function

- extreme value problem technique
	- when solving an extreme value problem:
		- a very common and general technique: interpret solution as an extreme of keys over a search space
			- so the main questions become:
				- determining what key to compute, so that an extreme value is a solution
				- is there a way to iterate through search space efficiently
				- is there a way to compute keys efficiently
	- examples
		- iterate efficiently
			- [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md)
		- compute key efficiently
			- [84. Largest Rectangle in Histogram](../LeetCode/84.%20Largest%20Rectangle%20in%20Histogram.md)
	






# evaluation order


![](../!assets/attachments/Pasted%20image%2020240417134948.png)


# operator precedence

![](../!assets/attachments/Pasted%20image%2020240417135116.png)




# assignment statement evaluation


![](../!assets/attachments/Pasted%20image%2020240417135441.png)


# which reference
- understanding when i'm having a confusion about the 'library' vs the 'syntax'
- ie whether i should look in the 'library reference' or the 'language reference'

- [The Python Standard Library — Python 3.12.3 documentation](https://docs.python.org/3/library/index.html)
- [The Python Language Reference — Python 3.12.3 documentation](https://docs.python.org/3/reference/index.html)





