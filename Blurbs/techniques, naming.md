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
		- ie matches optimal complexity in either time or space
	- or is significantly easier to understand/write
	- or becomes a uniquely optimal technique if a ‘finite’ constraint becomes ‘infinite’
		- and ‘spirit of the problem’ was for the constraint to indeed be finite
		- see [complexity analysis wrt "spirit of the problem"](complexity%20analysis%20wrt%20"spirit%20of%20the%20problem".md)
		- ie [36. Valid Sudoku](../LeetCode/36.%20Valid%20Sudoku.md)


- add to above list: i think more complicated techniques are still useful 
	- but really think about the 'key idea'...often, it actually is something i already have, just implemented in a more complicated/equivalent way
		- ie remember to separate 'implementation' from 'inspiration'
		- example: [143. Reorder List](../LeetCode/143.%20Reorder%20List.md)
			- i thought recursion was a genuinely diff approach..but i realized it wasnt; its a diff implementation, but same 'main idea' as other stuff i had
	- but point still stands: can be worth having more complicated stuff, as long as its genuinely diff
		- even if an approach is more ‘complicated to understand’/’harder to implement’, and doesnt have strictly better complexity: it can still be worth keeping
		- it just has to be a genuinely different approach that is sensible, and at least match optimal complexity in space or time
		- when i say ‘best approach’, is mean ‘best version of the inspo’ for that approach
		- example (well not anymore, bc it wasnt actually diff): [143. Reorder List](../LeetCode/143.%20Reorder%20List.md)
			- the recursion approach isnt strictly better in time/space, and it’s harder to understand
			- but imo atm, its still worth keeping, bc it matches optimal time complexity; and is a genuinely diff and sensible approach to the problem
				- ie its not like ‘equivalent approach but uses a diff definition’











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



# name should be based on structure?


- naming approaches / what is actually the key idea wrt data structure
	- it seems approaches: i should think about ‘what i want to compute and store’
	- and then from there: becomes ‘clear’ what data structure i should use
	- i suspect: the converse is basically true: every data structure has like a few types ‘things to store’ that is associated/optimal for
	- for the interest of brevity/understanding: i think it’s probs better to name approaches based on data structure
	- and then have a oneliner immediately under, that describes what we are going to compute/store
	- i suspect: as i approach ‘mastery’, this order of things will be fine
		- even tho technically, ‘what do i want to store’ comes before the ‘what data structure we should use’
		- i think what will happen is that, once i’m a ‘master’:
			- once i read problem, i’ll immediately have a sense of what things i might want to store
			- and then that is confirmed when i see data structure heading
	- regardless, i think better to use data structures as heading, bc more ‘efficient’/consistent for naming things
		- and since oneliner for ‘what i store’ is immediately under, it’s basically like i’m seeing both at the same time, so it doesnt actually matter which one i see ‘first’ in terms of understanding
		- so choosing to put the data structure as heading, is more for aesthetics/convenience
			- ie sometimes i cant fit that oneliner all in a heading

