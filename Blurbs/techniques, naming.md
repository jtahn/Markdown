# when does a technique get its own heading
- imo it needs to be a significant 'big idea/insight' FOR THAT PROBLEM, it should be relative
	- ie for [242. Valid Anagram](../LeetCode/242.%20Valid%20Anagram.md): 
		- i think its worth having headings for all the 3 diff ways you do hashmaps in python to count stuff, and also how you compare them
			- for standard dict, include 2 variants for how to deal with absent keys
	- similarly [704. Binary Search](../LeetCode/704.%20Binary%20Search.md)
		- this is where i should put discussion on 2 vs 3 cases, and also the while condition allowing equality or being strict
- don't think about this too much imo..when it's borderline whether it's "big enough", its nbd if i pick to use a heading or not
	- [238. Product of Array Except Self](../LeetCode/238.%20Product%20of%20Array%20Except%20Self.md) is a good example of where the 'optimizations' are borderline..so nbd if i do a heading or not

- a technique is useful if:
	- it achieves optimal asymptotic complexity in either time/space, and the constant isnt ‘far worse’
	- is significantly easier to understand/write
	- becomes a uniquely optimal technique if a ‘finite’ constraint becomes ‘infinite’
		- and ‘spirit of the problem’ was for the constraint to indeed be finite
		- see [complexity analysis wrt "spirit of the problem"](complexity%20analysis%20wrt%20"spirit%20of%20the%20problem".md)
		- ie [36. Valid Sudoku](../LeetCode/36.%20Valid%20Sudoku.md)




- for now: keep all code examples for ‘useful techniques’
	- it’s good practice
- however in the future:
	- i might have enough problems, to the point where might not be worth including code examples
	- ie:
		- every technique has examples where it is truly the optimal technique
		- and the examples cover all the possible ways i should know how to use the technique



# should i add more than a 'name'?
- ie should i add descriptors to indicate in what way it might be an 'improvement' to other techniques? or maybe it should just be the first bullet
	- likely brownie points if i explain why it's not a strict improvement; ie time/space tradeoff



# descriptors for space complexity
- terminology i use to summarize how it's an improvement?
	- O(1) space and in-place should probly mean different things
		- [space complexity](space%20complexity.md)