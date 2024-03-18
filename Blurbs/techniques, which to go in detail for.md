# index of foundational techniques (and dicussions)
- [704. Binary Search](../LeetCode/704.%20Binary%20Search.md)
	- binary search
- [242. Valid Anagram](../LeetCode/242.%20Valid%20Anagram.md)
	- counting and comparing counts
- [703. Kth Largest Element in a Stream](../LeetCode/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md)
	- heaps

# looking for fundamental problem
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




# only the 'best' technique
- if a technique is strictly asymptotically suboptimal in either/both time/space, and asymptotically equal for the other/none
	- then imo, it's not worth going into big detail
	- point is, there's something about this problem that makes it so: even tho these techniques for other problems, it's not optimal here because we have extra structure
	- definitely worth mentioning these 'suboptimal' techniques
		- important to be reminded to watch out for: what about this problem (ie some kind of extra structure/condition) allows us to use the asymptotically better techniques
	- maybe even add the code
		- bc it's good to see implementations of techniques in more examples; might as well
	- but point is, no point going into detail about 'why you can use this technique'
		- just do a brief one-liner for the strategy
		- i can just say: if you want more explanation, see X problems
		- (it should be p easy to find those problems, because neetcode/grind75 seem to organizes problems by 'most optimal data structure to use')
		- also generally: can understand the details of the strategy by looking at the 'optimal' solution
- aka the only time to go into detail about technique, is if it the asymptotically optimal
	- furthermore: this problem becomes an example of a 'fundamental problem' for this technique, if it is the only asymptotically optimal solution for this problem

# examples
- we have a strict hierarchy for available techniques for the following problems
	- [703. Kth Largest Element in a Stream](../LeetCode/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md)
		- heaps
	- [973. K Closest Points to Origin](../LeetCode/973.%20K%20Closest%20Points%20to%20Origin.md)
		- can also use quick select
	- [347. Top K Frequent Elements](../LeetCode/347.%20Top%20K%20Frequent%20Elements.md)
		- can also use bucket sort
			- strictly better time complexity than above techniques
			- asymptotically equivalent space complexity
			- so that's why other techniques, imo no reason to go in detail; i should know how to explain them if necessary, because i review the other problems
