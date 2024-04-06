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



# 'true understanding' means i know the steps?

- it does seem like: true understanding of the problem happens when:
	- i actually do understand how to ‘come up with the solution’ myself, and i can see how there are clear steps
	- similar to how in calculus: when i see a problem, i immediately know the general steps i need to take (and the ‘jargon names’ for them), and ‘why’ (ie the ‘inspo’..ie ‘problem asks for slope of tangent line, so i immediately know i need to take a derivative; so lets do a derivative; and now we see to derive, we need to use product/chain rule’)

- yea imo the mindset i need to take with leetcode:
	- it’s exactly how i study calculus
	- the ‘difficulty’ here is that calculus, seems there’s a lot more ways to practice the abstract formulation (ie not word problems) to build confidence with the mechanical/drilling/computation aspect (which for leetcode imo: is the ‘implementation’ aka ‘writing code’ part)
		- well idk, we’ll see..wait until later to think of ‘similarities btwn calc and leetcode’
	- but for now: just keep doing what i’m doing. it’s definitely working, and based on gold medal competitive programmers, is close to the ‘right’ way to do things
	- none of this will ever be a waste of time, bc leetcode is the most important thing for the ‘road to 500k tc’..ie if there was anything to ‘maximize’ (ie go over 80/20 rule), it should be leetcode
		- and swe seems like the most consistent/’highest EV’ way to hit 500k tc
		- i suspect im nearing the end of the bubble tho, so this is kinda urgent..like atm i’m probly lucky cuz it seems ‘american being lazy/not having time to do leetcode’ and ‘internationals grinding leetcode but not having enough spots at companies’...but surely one of these will change in the next few years
			- ie companies outsourcing even more of their work
			- or: at some point, bc of how many americans are switching over to swe: even if most arent doing much leetcode: there are enough that are doing it, that i now have serious competition
	- also: it’s like max 250 problems that i ‘need to do’, before surely im at like 99pct mastery, and by that point: steps/etc/connections/’blurbs’ will become soooo obvious



# name variables when i cite a fundy

- when i say ‘name variables’:
	- i mean like: ‘fundamental technique’ is very general and should be interpreted as acting on ‘general problem’ that involves ‘general objects’...ie variables
		- but bc im using specific problems: then the objects in that problems should be interpreted as ‘variables’
	- so then: when i apply technique from one problem to another problem: maybe briefly describe what objects in current problem are associated with objects in the og/fundamental problem..ie naming variables


# ideal level of 'explanation'
- ideal level of ‘explanation’ is:
	- heading uses ‘jargon’ for the technique
	- sometimes, a oneliner that more specifically describes ‘naming the variables’ used in the technique, for each fundamental technique that is cited
	- oneliner comments for each block/subroutine in the code, if not immediately obvious what’s happening

- goal: practice:
	- reading code
	- associating ‘jargon’ with techniques
	- practice applying ‘techniques’ to specific situations (ie how to ‘name variables’)

- having long explanation after the code, is actually annoying to understand
	- bc i have to keep scrolling back and forth, unless super vertical display

- no point explaining step by step in prose, when python is already so readable

- imo the goal here is: to be able to develop the skill in performing the following steps:
	- identify global technique to use (ie the jargon heading)
	- identify how to name variables to use for that fundamental/global technique
	- recall what the typical steps are (ie comments for each subroutine in code)
	- know finer details of implementation (aka writing the actual python code)

- probably move complexity at the very top, ie before i provide actual code
	- bc i think it should possible (and would be a good skill) to be able to quickly estimate/recall the probably complexity, based on the global technique


- maybe: always put a oneliner comment for every subroutine (“aka step”), even if its obvious
	- bc imo makes it easier to remember/understand this process

- simply put: the explanation is made so that reading/understanding solutions is the right balance of ‘easy’ yet ‘feels efficient’
	- and imo, the above format is basically the best template
	- ‘no comments’ are harder to understand; but too much prose/detail feels like a slog
	- the best is clearly, going from general to specific, in a very organized/efficient way (ie minimize scrolling/jumping around)



# fundy: it's not the structure, it's the approach?
- future possible blurb:
	- common reason to use a structure: save things you need for later computations
		- ie: when you typically choose stack for this:
			- the decision on:
				- whether you can do a computation now
				- or need to wait/save it for later
				- and/or whether an element isnt needed for future computations
			- you can phrase this decision to depend on an inequality
				- more precisely: the decision is equivalent to an inequality
			- example: [42. Trapping Rain Water](../LeetCode/42.%20Trapping%20Rain%20Water.md)


