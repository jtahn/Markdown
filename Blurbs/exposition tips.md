# citing fundamental techniques
- give a brief explanation that describes how to phrase current problem in terms of technique i'm citing
	- analogy: like 'assigning variables' when you're writing a formula in math to describe a word problem





# 'equivalent' vs 'best'
- intuition/inspiration is ideal
	- there's almost certainly a 'perfect concise' way to write it
	- just try my best, but don't spend more than 5-10 minutes
		- come back later when i have more experience/background
	- similarly, if i can't even figure out the intuition/inspo: that's fine too
		- then figure out concise way to describe the algo
			- ie why it is true, what are the subroutines doing
- there's a difference btwn intuition/inspiration versus 'this is true'
	- ie 'largest rectangle in histogram'
		- its true that the 1 pass approach: the stack is holding all currently valid rectangles
		- but this doesnt seem like the 'true inspo' for why the stack is created
		- ie equivalent definitions versus 'best' definition
		- 'best definition' = matches up best with intuition/inspiration
- by intuition/inspo:
	- i mean, 'you could come up with solution yourself'
		- this isn't absolutely necessary: the number of leetcode problems is small enough that tbh its fine to just straight memorize for short term 1-3 months
		- but same argument: there's so few problems, i might as well do this, to achieve more 'mastery'
			- and it should significantly help with very long term memorization..like years and decades
			- so ultimately, this is necessary if i want to job hop imo
- possible way to figure out key intuition/inspo
	- there's usually a key idea/observation that the method is using, that other techniques do not
	- maybe the 'best definition' is the one that most directly use this idea/observation
- this also applies more generally to much of the exposition i do
	- there's many 'equivalent ways' to explain what's happening
	- try to find the 'best' way...depends on situation...as i get more background, i'll get better at figuring/identifying this
		- bc 'best way' probly is a pattern among other problems
		- ie i'll inductively make connections / observe patterns
- examples
	- when explaining (nested) loops:
		- sometimes, what the implementation is directly doing, is not the "best" way to understand what we are iteration over
		- instead: consider the loops to be a chosen 'implementation' of a 'way to iterate over candidates'
			- and so our task is to find the "best definition/explanation" for this "way"
		- example: many two pointer methods
			- there is an underlying 'full iteration' that we optimized from
			- ie [11. Container With Most Water](../LeetCode/11.%20Container%20With%20Most%20Water.md)


# minimize prose



- prose adds more load during reviewing/revisions
	- should only be done when there’s a significant benefit
	- aka the ‘inspiration’ is a major jump from the implementation
- if implementation aligns almost exactly with the ‘inspiration’
	- try to only have:
		- brief description of inspo
		- no discussion of implementation
		- instead: clean code + one-liner comments for each block/subroutine
- getting better at reading code is a valuable skill




# how rigorous do proofs need to be
- there a few solutions where the proof assumes a solution exists 
	- do not give big details to prove this; do not need to prove this, brief keyword/statement is usually enough, bc existence is usually bc either:
		- problem states a solution exists
		- solution exists bc you're finding an 'maximal elemen't of a finite set (of possibilities), ie finite search space
			- there's definitely a 'jargon' keyword that says the above...find the correct jargon





# rough is fine, but have a good workflow to deal with it
- many cards being incredibly rough + surely way too much info, and having lots of loose ends, is natural when i’m first exposed to a subject
	- point is that it will likely be far more efficient to make significant adjustments on the second/third pass, when i’ve been exposed to way more stuff
- having tons of rough cards early: consider it like: rapidly expose myself to as much background/concepts as possible; kinda like ‘skimming’ a textbook

- writing cards in a way that allows for efficient voice memo revisions
	- lots of headings
	- ‘label screenies’ with numbers before them


- revision workflow when i’ve caught up on anki reviews:
- in general: typical workflow will be to view the card in anki on ipad, and then voice memo the desired edits
- then once im back at my workstation: make the edits within a day (so i don’t forget)
- ie: anki -> voice memos -> obsidian + github -> anki -> ...


- revision workflow when i’m behind on anki reviews:	- 
- typically: initial exposure to a new field; so need to make a bunch of cards, ie “skimming”
- safari ipad (browse github repo) -> voice memos -> obsidian + github -> (repeat...)

- it’s fine for anki reading cards to require significant edits
	- remember: the scheduling/repetitions are more about active revising, rather than ‘passively reading a perfect solution’


