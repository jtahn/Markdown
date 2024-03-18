# two pointer vs sliding window
- is sliding window a subset of two-pointer?
	- [76. Minimum Window Substring](76.%20Minimum%20Window%20Substring.md) makes me think so
	- apparently [567. Permutation in String](567.%20Permutation%20in%20String.md) made me think not? ie my reflection was: 
		- sliding window seems to be: you still have to iterate through all the cases; and you want to compute the type of 'output'/'solution' for each case; but the 'output' from the previous case lets you very efficiently compute the 'output' of the current case
	- also apparently [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md) made me think not?
		- ppl called it sliding window, but i was thinking it should be called 2 pointer?
 - i feel like two pointer is about: 'why you can ignore certain states'
	 - ie [42. Trapping Rain Water](42.%20Trapping%20Rain%20Water.md), or [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md)
	 - this also means: imo [141. Linked List Cycle](141.%20Linked%20List%20Cycle.md) isn't 2 pointer; or at least, doesn't feel related to most of the other 'two pointer techniques'
	 - make sure for two pointer, i always discuss why we can move the pointers!
		 - this is actually very obvious that i need to do that, if i want to 'prove' correctness. bc when i move a pointer, it means ignore a bunch of cases/states, so i need to explain why that's okay

		- (meta: ohh...ok so i tihnk 'moving the pointer' is the only time we need to discuss why states dont matter; ie this is what we did in other two pointer solutions where they were both moving inward)
			- aka: i dont think 'why we can ignore lower max count' actually has much to do with 'states'...i mean i guess it does...wait yea:
			- moving right pointer is the fact that:
				- if we have alrdy found length m, then we dont need to check for that length anymore; we check for m+1
		- (i'm trying to say that for any kind of two pointer method, for correctness, any time you move a pointer, it implies you're throwing away states, so i need to explain why this is allowed; ie in [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md), moving right pointer here means you're throwing away certain substring lengths; and moving left pointer means you're throwing away certain 'starting' points)
			- (i feel like these metas arent helpful...the whole point of my leetcode deck was that i would inductively/indirectly get a feel for the situations where things work, without getting to vague/broad/theory (which honestly makes understanding it harder); having a writeup describing this is too vague and honestly unhelpful; if it want to get a sense of how these techniques are related, then i just look in my ToC and read all the problems that use a similar technique)
				- specifically: i DO need to discuss why i can move pointers, bc that is how i prove correctness
				- i DONT have to mention like: "all two pointer solutions do this stuff all the time"...i should inductively realize this bc all my two pointer methods do this...


