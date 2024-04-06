# alternative descriptions of this blurb
- 'what parts of the algo should i go into detail about; vs what parts should i just wave hands and cite stuff'

# index of foundational techniques
- meta
	- these aren't necessarily the 'only problem' that is fundamental for this technique
	- it's just currently, the first one that was at that 'lowest level found so far', and i haven't found a problem that is 'more fundamental' for that technique
	- so that problem is currently where the discussion for this technique is located
- [704. Binary Search](../LeetCode/704.%20Binary%20Search.md)
	- binary search
- [242. Valid Anagram](../LeetCode/242.%20Valid%20Anagram.md)
	- counting freqs wrt a finite char set
	- comparing counts once
- [703. Kth Largest Element in a Stream](../LeetCode/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md)
	- heaps
- [567. Permutation in String](../LeetCode/567.%20Permutation%20in%20String.md)
	- sliding window
	- repeatedly comparing counts wrt a finite char set
- [150. Evaluate Reverse Polish Notation](../LeetCode/150.%20Evaluate%20Reverse%20Polish%20Notation.md)
	- transforming conditional subroutines into a dict + general subroutine
- [235. Lowest Common Ancestor of a Binary Search Tree](../LeetCode/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md)
	- wlog
- 

# todo: looking for fundamental problem
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



# when to include 'tricks'
- oneliner tricks that don't result in notable improvements to efficiency or understanding
	- if i can't put it in without comments/exposition
		- then it isn't readable
		- so it shouldn't be included
		- aka this trick is essentially useless, bc it has no real pros, other than 'shorter code'
	- otherwise, just put it in right above commented-out 'more standard code'



# when is a problem 'fundamental' for a technique



- make sure that the discussion is actually relevant to the problem
	- ie the problem needs to be an example for the discussion
	- it’s harder to understand discussion if i don’t see an example
	- examples
		- while [1. Two Sum](../LeetCode/1.%20Two%20Sum.md) should discuss hashing: it’s completely inappropriate to discuss why/how python hashes pointers/references (this should be saved for [138. Copy List with Random Pointer](../LeetCode/138.%20Copy%20List%20with%20Random%20Pointer.md))
		- [235. Lowest Common Ancestor of a Binary Search Tree](../LeetCode/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md) involves BST, but it shouldn't be fundamental for it, bc all it does is a traversal
			- there are no real 'operations'
			- any 'fundamental problem' for a data structure, needs to discuss complexity of common operations (ie searching, adding, deleting)




# meta/todo
- actions
	- keep an index of 'fundamental problems' for 'fundamental techniques'
	- cite other problems for as many steps as possible
		- particularly for suboptimal solutions
		- side benefit:
			- i'm not constantly rewriting the same justification/reasoning
			- reduces edits
				- if i want to edit a justification..then i'd have had to edit it in every problem where i used it; versus now, can just edit the few places where that discussion exists (aka, in the the fundamental problem for that technique)
			- active recall
				- citation/keyword forces me to recall how it works / what it means
				- aka: this is how 'reading solutions' should over time, help me memorize/recognize patterns when i face new problems
		- don't worry about 'forgetting the explanation'
			- these problems are small and 'easy'
			- i figured it out once: i can figure it out again, especially now that i have a hint via citation
	- ideally: current problem exposition only needs to discuss one 'key idea' used in the optimal solution
		- ie consider this problem a 'fundamental example/problem' for a 'fundamental technique'
		- note: multiple problems can be 'fundamental problem' for a 'fundamental technique'
			- that's fine: good to see many examples of how to use a technique
			- but if the usage is not that diff, then just site other problems
	- if you think about it:
		- there's really no other way to do this in a manageable way
			- without citations: writing, reading, revising would be an absurd hassle





# use fundamental techniques, if they're just a step of the overall solution
- make sure to add a reference to the technique
	- for [strategy when reviewing cards](strategy%20when%20reviewing%20cards.md)


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


# why
- fundamental techniques seems similar to how you’ll actually approach problems in practice
	- once you get really good at recognizing patterns; you start already guessing that there are certain obvious/classic steps you should take to simplify the problem, and already having a general sense of what that technique will do; maybe not specifics, but in a broad way (aka the specific implementation details don’t immediately matter atm)
