# thoughts v2
- summary
	- the longer i think about [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md), the more i think: this blurb should not be about how 'brute force methods are valuable'; bc i'm realizing, actually they're not
	- actually tbh this blurb is useless imo
	- instead, i should have a blurb about how imo leetcode problems: dont put any focus on 'figuring out the natural inspiration/story behind a technique'
		- instead focus on
			- how to implement the technique (both high level and python code)
			- why it works (like be able to PROVE it; lots of solutions don't do this)
			- and then inductively/indirectly, over time i'll recognize patterns and then know when to apply a technique...i hope
- another aspect of brute force: determining equivalent characterizations of solutions, so that you can simplify the 'main routine' until it is a 'simple routine'
	- problems have added fluff to make them seem more complicated than they actually are
	- so this problem has a lot of added fluff to make it seem more complicated than it actually is
		- all we are doing is finding the largest $m$ where:
			- there exists a substring of length $m$ with $m-k$ letters are the same
	- note we actually don't have to replace anything:
		- the question just asks for the length; doesnt ask for the string
		- so whatever algo we do, doesnt need to do a replacement...
- finding the 'equivalent characterization' and/or 'simple routine': i don't think it's helpful to try to find a 'natural' way to 'discover it yourself'
	- imo more reliable is just: look at as many problems as possible and be aware of as many tricks/patterns as possible
	- so need to try to come up with a story of 'how to find the simple routine'
	- just provide the equivalent characterization
- the most 'brutal' brute force method..maybe this should be the brute force method
	- there needs to be some kind of distinguishing btwn how 'brutal' a brute force method is...
	- like there's various efficiencies to make on the brutal force method described above:
		- we dont actually have to replace chars; bc we know equivalent characterization of solution from the key idea above
			- also problem doesnt ask for an actual string; just asks for max length...so this should hint that actually going through the process of replacing characters, is a waste
		- we dont have to loop through every possible substring
			- this is what leads to two pointer
		- counter chars can be done efficiently via hashing
	- maybe the conclusion here is:
		- there are parts of the algo that you optimize at each step:
			- so starting at the most brutal brute force:
				- find an 'equivalence' with what it means to be a solution
					- for example: [235. Lowest Common Ancestor of a Binary Search Tree](235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md)
					- this should help simplify the 'inner' routine
					- ie "candidate satisfies property" IFF "candidate is a solution"
				- then: find a better way to loop
					- usually is based on the 'inner routine', so probably want to simplify this first..ie understand what an 'equivalent formulation/definition' of a solution is
	- another similar conclusion:
		- leetcode is about how to optimize a problem
		- as you learn more problem: you realize problems are composed of smaller subproblems that are themselves leetcode problems; and so when you first see these larger problems, the approach is basically trying to optimize pieces of it at a time, based on concepts encountered before, and maybe some new concepts
		- so maybe one goal of leetcode: being able to optimize larger and larger problems at once; ie make pieces look smaller
- basically: brute force method: the routine does not always generate a solution
	- but: the cases where it DOES generate a solution: usually there's some key piece of info that exactly determines/equivalent to whether the routine generates a solution or not; and this key piece of info is part of what contributes to an efficient optimization
- ie another example of optimizing from brute force:
	- atm, i suspect two pointer is just 'efficiently iterated brute force'
		- aka: the 'actual routine' is identical to brute force; but we handle the iteration in a way that adaptively throws away any future cases/subsets that you alrdy no there's no point checking (ie bc the result will be 'useless' in terms of updating your 'current best solution')
- Actually, i don't think it make sense to come up with a brute force every problem
	- because the most 'brutal' brute force is so ugly, that it's so obviously not going to work
	- imo when this happens: probly just immediately suggests that you need to think of an equivalent formulation of the problem
	- ie here, the most brutal would be like:
		- for every substring
			- for each possible letter A-Z
				- replace first k non-matching letters
				- compute length of longest substring of that letter
	- again, making me think: stop trying to come up with a story/inspo. this is really difficult (and i've spent so much time on this problem)
		- i need to just cleanly explain WHY something work
		- get good at understanding/memorizing tricks
		- also story/inspiration is not natural, and it's not realistic either tbh...
			- like in practice, this is just very rarely how i'm going to problem solve. you problem solve by remembering and applying patterns; by chaining them together, bc you understand how/why they work and when to use them
- yea nvm, the more i look at this problem: the more i think there's no connection btwn brute force and 'optimal method'
	- main reason is bc: brute force isn't even well defined; that's not why it's pointed out
	- during interviews: imo only worth mentioning brute force if its very obvious how to do it
		- otherwise, just jump straight into the pattern trick
			- this isnt just memorization: need to actually understand how to apply it
			- its hard (if not impossible) to memorize how to apply the trick for hundreds of problems (aka be able to recall it fairly effortlessly during an interview), unless you actually understand it very well
				- probly similar to how lebron can just rattle off exactly how happened during a 5 minute sequence of basketball...he just understands the game so well





# meta/thoughts v1
- this file is inspired by the following problems
	- [424. Longest Repeating Character Replacement](../LeetCode/424.%20Longest%20Repeating%20Character%20Replacement.md)
- imo wait until i have a longer list of examples where the brute force method is 'interesting'; and then seeing if i can draw some connections
	- by 'interesting': i mean that the brute force technique is...
		- harder to devise
		- seems to contribute heavily to understanding the optimal technique
		- the 'simple routine' and the 'key idea' do not seem that related (but imo: for brute force, they should be...so the idea is figuring out what the pattern is here)
			- by 'key idea'...i think i mean, 'what does a solution to this problem look like'
- try to find a real resource for this...but i can't seem to find one...
	- see if anybody below has stuff i can build off of...this is just first 2 pages of bing search results
		* [Brute Force | LeetCode The Hard Way](https://leetcodethehardway.com/tutorials/basic-topics/brute-force)
		* [terminology - What is meant by the term " BruteForce " in programming? - Stack Overflow](https://stackoverflow.com/questions/71786124/what-is-meant-by-the-term-bruteforce-in-programming)
		* [Brute Force Approach and its pros and cons - GeeksforGeeks](https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/)
		* [Brute Force Algorithms Explained](https://www.freecodecamp.org/news/brute-force-algorithms-explained/)
		* [Brute force approach - javatpoint](https://www.javatpoint.com/brute-force-approach)
		* [How to optimise if brute force uses entirely different algorithm? : leetcode](https://www.reddit.com/r/leetcode/comments/xpkkfz/how_to_optimise_if_brute_force_uses_entirely/)
		* [Algorithmic Paradigms - Brute Force – Study Algorithms – Theory](https://studyalgorithms.com/theory/algorithmic-paradigms-brute-force/)


---

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





