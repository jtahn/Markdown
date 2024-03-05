(this is all just current thoughts based on observations...go find a real resource for this)


# todo
see if anybody below has stuff i can build off of...this is just first 2 pages of bing search results
* [Brute Force | LeetCode The Hard Way](https://leetcodethehardway.com/tutorials/basic-topics/brute-force)
* [terminology - What is meant by the term " BruteForce " in programming? - Stack Overflow](https://stackoverflow.com/questions/71786124/what-is-meant-by-the-term-bruteforce-in-programming)
* [Brute Force Approach and its pros and cons - GeeksforGeeks](https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/)
* [Brute Force Algorithms Explained](https://www.freecodecamp.org/news/brute-force-algorithms-explained/)
* [Brute force approach - javatpoint](https://www.javatpoint.com/brute-force-approach)
* [How to optimise if brute force uses entirely different algorithm? : leetcode](https://www.reddit.com/r/leetcode/comments/xpkkfz/how_to_optimise_if_brute_force_uses_entirely/)
* [Algorithmic Paradigms - Brute Force – Study Algorithms – Theory](https://studyalgorithms.com/theory/algorithmic-paradigms-brute-force/)


# what is a brute force method
- i.e. how to design them?
- perform a 'simple' routine with every possible case/subset
	- what is "simple"
		- doesn't necessarily mean 'one line of code'
		- rather: can very easily be explained what you're doing in a sentence or two
	- "simple" doesn't need to be "optimal"/'correct"
		- ie for that case: this routine doesn't need to be 'solving the original problem' for this case
			- ie don't need to find 'find local solution'
	- what we do need:
		- should be "obvious" that by performing this 'simple' routine on every case, one of these outputs will be the global solution

# why do we care, when they're basically never optimal?
- for a lot of problems, it seems that:
	- understanding the 'simple routine' is basically the key step
	- once you understand it: there is often a straightforward observation about that routine, that leads to an efficient algo. 
	- examples: of such observations
		- this simple routine doesn't need to be run on all cases
			- i.e.: there are some cases where we obviously don't need to run it, bc the global solution won't be here
		- the bottleneck in the simple routine can be optimized via typical leetcode tricks (ie hashing)
- so the benefit of brute force is that:
	- you don't have to worry about 'optimizing for subsets' or 'optimizing the simple routine'
	- instead, we just focus on the 'simple routine', which usually involves observing/understanding something about the problem on a 'fundamental level'
		- aka observing patterns
	- and so by reviewing brute force for every problem, i'm hoping: i start making connections with these patterns

# Examples
- examples where a brute force technique is harder to devise
	- [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md)

