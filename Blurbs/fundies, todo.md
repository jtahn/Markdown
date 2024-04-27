# textbook sections
- (move some of these to actual problems/fundies)
- [adm 2.2: big oh](_private/pdfs/adm.pdf#page=51)
- [adm 2.6-2.8: sums and logs](_private/pdfs/adm.pdf#page=63)
- adm 4.6 quicksort
- clrs
	- 2
		- sorting jargon (p 17-18)
		- insertion sort
		- subarray
			- a contiguous portion of the array
		- loop invariants
		- objects, atributes
		- pseudocode conventions/jargon
	- 2.2
		- complexity jargon
	- 2.3
		- algorithmic technique jargon
		- solving/analyzing recurrence relations
	- part II intro
	- 6.3 building a heap
	- 6.5 priority queues
	- 7.2-7.3 quicksort
	- 12.1 BST
		- bst property
		- pre/in/postorder tree walk
	- 16 amortized analysis
	- 20.2 bfs
	- 20.3 dfs
	- 14.1, 14.3 dp
- knuth
	- [6.2.1 searching an ordered table](_private/pdfs/taocp%203.pdf#page=427&annotation=5576R)
		- [variation](_private/pdfs/taocp%203.pdf#page=432&selection=51,0,51,23)


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





