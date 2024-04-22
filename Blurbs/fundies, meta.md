# why connect with an algo/DS textbook
- understanding general idea is helpful
	- probly makes it easier to understand specific ideas, bc they're like small tweaks/variants..ie instead of understanding the entire thing every time: just understand general idea, and then understand why the tweak/specific thing happens
	- ie skiena is definitely important to do at the same time as leetcode. neither is more important the other. i need examples/implementations to actually fully understand the nuances of the general theory; i need skiena/epi to actually become aware of the general theory and understand the 'big picture' of the general theory. for interviews, i probly don't really need more than skiena/epi.
- which algo/DS textbook
	- just pick a memed/reputable one
	- i chose skiena bc it seemed to be most applicable out of the memed stuff
		- doesn't seem like you need to be any more general than this, for interviews
	- take a look at EPI...tho imo EPI doesn't seem to explain the general stuff as much
		- also it doesn't seem as polished
		- BUT imo epi will be very helpful for understanding some implementations...ie their discussion of divide&conquer was very valuable imo, see [53. Maximum Subarray](../LeetCode/53.%20Maximum%20Subarray.md)
			- versus skiena 5.6 covers this problem, but does not emphasize the difficulty/importance of 'stitching/merging' solutions; ie i like how EPI emphasizes how this is lowkey kind of subtle (but extremely important..ie the basically the meat of the problem) 


# jargon: 'fundy'
- ‘fundy’ as an abbreviation for any of fundamental problem/technique/idea
	- ie ‘big fundy’ the yankee player, lol
	- obvious from the context, whether i’m referring to problem/technique/idea
	- instead of ‘fp’...cuz kinda confusing what that acronym is for..also is only ‘fundametnal problem’

# jargon: in writeups
- references
	- list all fundies that are cited, and briefly explain why
- results
	- list all fundies introduced/discussed by this problem/writeup



# alternative descriptions of this blurb
- 'what parts of the algo should i go into detail about; vs what parts should i just wave hands and cite stuff'


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



