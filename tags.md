# todo

## #/meta 


- refs
	- fundy overviews
		- usaco guides
- classes
	- https://courses.csail.mit.edu/6.851/spring12/lectures/
- solutions
	- naukri seems to have nice editorials? 
		- ie https://www.naukri.com/code360/problem-details/count-palindromic-pairs_3210217
	- https://discuss.codechef.com/c/editorial/5
- problems
	- https://www.naukri.com/code360
	- https://csforall.in/algomaster-sheet/
		- and also, they list a bunch of 'code submission' websites
			- ie maybe i should start trying geeksforgeeks and hackerrank

- clrs solutions
	- 3rd ed
		- https://walkccc.me/CLRS/
			- https://github.com/walkccc/CLRS




# #binary_search
- https://usaco.guide/silver/binary-search?lang=py







# assorted

- concepts
	- https://usaco.guide/silver/prefix-sums?lang=py


- port [[_private/Drafts/todo, fundies|todo, fundies]] into here or other todos


- try to find the 'traversal on graphs' template in CLRS (i found it in skiena) - Search

- two pointer meta
	- maybe call it: 'pruning iterations'
	- kinda like pruning in backtracking
	- better:
		- just find the two pointer problems in skiena/epi, and see what jargon they use
		- they surely have these?


- confirm jargon:
	- 'complexity' generally means 'asymptotic complexity' (ie no constants)
	- 'better complexity' means 'strictly better asymptotic complexity'
	- aka only using clarifying/descriptors for other cases:
		- ie 'better constant', 'or equal'
		- confirm what the jargon is for 'better constant'



- skiena 8.1.4
	- find fundies for these variations on min spanning trees
		- negated weights
			- fundy: if you know a strat to find max, but now you're asked to find min:
				- can sometimes just use same strat with negated keys
		- min product
			- fundy: 'products' can be turned to sums via log
				- which allows you to use techniques where you sum stuff


- should this index be for leetcode only?
	- or for the entire vault?
	- atm, seems index should be for all tags...but tags are global over vault
	- so seems like this index should be for entire vault




# #dynamic_programming 



- [[_refs/02 algorithms/kt.pdf#page=287|kt, 6.3 Segmented Least Squares: Multi-way Choices]]
	- multi-way choices
- [[_refs/01 competitive programming/epi.pdf#page=314&offset=-115,647,0|epi, Dynamic programming boot camp]]
	- caching
	- recycling cache space
	- 'make choices'
	- counting problems
	- decision problems
- [[_refs/02 algorithms/clrs.pdf#page=385|clrs, 14.1 Rod cutting]]
	- optimal substructure
	- time-memory tradeoff
	- top-down
	- memoization
	- bottom-up
	- subproblem graph
- [[_refs/02 algorithms/clrs.pdf#page=404|clrs, 14.3 Elements of dynamic programming]]
	- really good explanation of optimal substructure, overlapping subproblems, 
- [[_refs/02 algorithms/skiena.pdf#page=354|skiena, 10.9.1 When is Dynamic Programming Correct?]]
	- principle of optimality
	- state
	- partial solution
- [[_refs/02 algorithms/skiena.pdf#page=321|skiena, Chapter 10 Dynamic Programming]]
	- consequences
	- caching
	- [[_refs/02 algorithms/skiena.pdf#page=323|skiena, 10.1.2 Fibonacci Numbers by Caching]]
		- memoization
		- caching (or tabling)
	- [[_refs/02 algorithms/skiena.pdf#page=329|skiena, 10.2.1 Edit Distance by Recursion]]
		- the recursion branches three ways
	- [[_refs/02 algorithms/skiena.pdf#page=332|skiena, 10.2.3 Reconstructing the Path]]
		- wait this is very important..aka reconstructing the solution is actually a very general procedure
			- this was mentioned by other resources as well
				- ie [[_refs/unfiled/nutshell.pdf#page=183&selection=36,0,61,62|nutshell, page 183]]
				- and there was another i swear...
	- [[_refs/02 algorithms/skiena.pdf#page=355|skiena, 10.9.2 When is Dynamic Programming Efficient?]]
		- size of the state space
		- combinatorial objects
- [[_refs/02 algorithms/dpv.pdf#page=167|dpv, 6 Dynamic programming]]
	- algorithmic paradigm
	- implicit dag
		- nodes are subproblems
		- edges are dependencies
			- if to solve subproblem B we need the answer to subproblem A, then there is a (conceptual) edge from A to B
			- ie A is a smaller subproblem than B
	- [[_refs/02 algorithms/dpv.pdf#page=174&selection=266,0,266,18|dpv, page 174]]
		- underlying dag structure
	- [[_refs/02 algorithms/dpv.pdf#page=176&selection=6,0,6,18|dpv, page 176]]
		- common subproblems
	- [[_refs/02 algorithms/dpv.pdf#page=180&selection=6,0,6,11|dpv, page 180]]
		- dpv say memoization is NOT dynamic programming
			- but most other authors seem to say that memoization is a type of DP
	- [[_refs/02 algorithms/dpv.pdf#page=186&selection=1,0,6,18|dpv, page 186]]
		- memory can be released
- [[_refs/01 competitive programming/cses2.pdf#page=82&offset=-3,136|cses2, 6.2.4 From Permutations to Subsets]]
	- can also think of dp as turning 'permutations' into 'subsets '
- [[_refs/02 algorithms/clrs.pdf#page=439|clrs, 15 Greedy Algorithms]]
	- optimization problem
	- sequence of steps
	- set of choices at each step



- seems subproblem IS the state
	- it's just sometimes, you have to solve a different problem instead.
	- and now it maybe becomes obvious why 'subproblems' includes all 'candidates'. aka it's just 'all valid (partial) candidates for the subproblem'
- for 'candidates':
	- see what they use for backtracking
- i bet: all these problems where DP works: then backtracking would work too. but the key is: many candidates lead to the same state/consequences, which is all we care about
	- see skiena




# #greedy
- EPI seems to consider them 'greedy' algorithms...but for various reasons, either consensus or me disagrees
	- [[_refs/01 competitive programming/epi.pdf#page=352&offset=-115,373,0|epi, 18.7 Compute the maximum water trapped by a pair of vertical lines]]
		- this is [[LeetCode/11. Container With Most Water|11. Container With Most Water]]
	- [[_refs/01 competitive programming/epi.pdf#page=354&offset=-115,505,0|epi, 18.8 Compute the largest rectangle under the skyline]]
		- this is [[LeetCode/84. Largest Rectangle in Histogram|84. Largest Rectangle in Histogram]]
	- [[_refs/01 competitive programming/epi.pdf#page=350&offset=-115,417,0|epi, 18.6 The gasup problem]]
		- this is [[LeetCode/134. Gas Station|134. Gas Station]]
		- this didn't feel 'greedy' to me

- seems like a lot 'two pointer' stuff is in greedy



---


- finding greedy problems on neetcode
	- examples provided by texts (aka likely the classic problems)
	- [[_refs/02 algorithms/skiena.pdf#page=361&selection=6,0,6,17|skiena, page 361]]
	- 


- both clrs and dpv describe greedy in very specific terms, as building up solutions by piece from subproblems
	- [[_refs/02 algorithms/dpv.pdf#page=138|dpv, 5 Greedy algorithms]]
	- kt does not
		- "It is hard, if not impossible, to define precisely what is meant by a greedy algorithm."
	- so i think 'greedy algo' kinda depends on what ppl mean...seems there are ppl who take a very general/broad/loose definition for it
	- imo, use the definition in clrs/dpv...it's more helpful to be more specific about it imo
- [[_refs/02 algorithms/kt.pdf#page=141|kt, 4 Greedy Algorithms]]
	- some of the phrases here are interesting, and i do want to use it
		- "When a greedy algorithm succeeds in solving a nontrivial problem opti- mally, it typically implies something interesting and useful about the structure of the problem itself; there is a local decision rule that one can use to con- struct optimal solutions."
	- but i don't want to use them to describe greedy
	- 

- the reputable cp resources seem to agree with ctci
	- ie
		- [[_refs/01 competitive programming/sannemo2018.pdf#page=153&offset=72,537.222|sannemo2018, Greedy Algorithms]]
		- [[_refs/01 competitive programming/halim1.pdf#page=185|halim1, 3.4 Greedy]]
		- [[_refs/01 competitive programming/cses1.pdf#page=67&offset=93.543,756.85|cses1, Greedy algorithms]]
	- conclusions
		- greedy has a very specific definition, and is typically difficult to prove correctness
			- if you can prove connectness: it's typically done similar to the standard 'greedy algo' examples
		- essentially a subset of dp
	- aka
		- if 'greedy algo' for a leetcode problems seems very obvious...then it probly isnt actually 'greedy'
		- its more like: 'we understand something about the problem that leads to a very easy way to compute it'
			- aka kinda like what kt is saying
- ohhhhhh
	- epi combines greedy and invariants into one section
		- so a lot of times when consensus says 'greedy'...likely the better word is 'invariant'
			- [[_refs/01 competitive programming/epi.pdf#page=346&offset=-115,403,0|epi, Invariants]]
			- aka something about the structure of the problem!



- i'm trying to find a leetcode problem that is 'greedy' via essentially asking me to code a 'furthest in future' cache
	- clrs mentions that there are ways to rephrase this problem, ie
		- [[_refs/02 algorithms/clrs.pdf#page=463&selection=184,0,241,63|clrs, page 463]]





# #iteration

## #iteration/two-pointer 
## is kmp = two pointer?

- epi:
	- lots of two pointer stuff seems to be in 'greedy', see above
	- also see [[_refs/01 competitive programming/epi.pdf#page=218&offset=0,648|epi, 13 Hash Tables]]

- actually it seems it's robin-karp
	- the specific terminology that halim and sannemo seem to use is 'rolling'
		- [[_refs/01 competitive programming/sannemo2018.pdf#page=256&selection=296,0,301,1|sannemo2018, page 256]]
		- [[_refs/01 competitive programming/halim2.pdf#page=91|halim2, 6.6.2 Rolling Hash]]
		- 
	- neither of them have 'two-pointer' sections
		- they just put these within 'string' algorithms
		- i do think this is worth generalizing though, bc there are non-string problems that use these observations
			- aka [[LeetCode/134. Gas Station|134. Gas Station]]
- cses:
	- sticks both two pointer and sliding window inside the 'amortized analysis' subsection
		- maybe bc: the first time you compute the subroutine, it is O(n)
		- but every other time is now O(1)
		- so amortized: it's O(1) amortized
		- 




- refs for kmp
	- [[_refs/02 algorithms/sedgewick.pdf#page=771|sedgewick, 5.3 Substring Search]]
	- [[_refs/02 algorithms/skiena.pdf#page=693&selection=149,0,149,37|skiena, page 693]]


- it seems that string algo theory are going to be fundamental examples of my two-pointer/iteration fundeez
	- ie rabin-karp is #iteration/for_subroutine 
		- [[_refs/02 algorithms/sedgewick.pdf#page=788&selection=42,0,52,0|sedgewick, page 788]]
		- another wording of fundy/generalization: what i mean by 'iteration for subroutine': if your search space consists of things that are like 'collections', and these collections have significant 'overlap' (importantly..'adjacent collections' essentially overlap everywhere except in like 1 or 2 spots); and if the reason you care about these collections is you use them to compute a value...then you might not need to recompute the value every time..ie can very easily compute value of one collection using value of adjacent collection. see gas station, and also one of those 'substring search' problems




find more supposed 2 pointer problems:
1. **Pair Sum Identification:** Given a sorted array, find two numbers that add up to a specific target.
2. **Remove Duplicates:** Remove duplicate elements in a sorted array.
3. **Exploring Triplets:** Find all unique triplets in an array that add up to a specific target.
4. **Maximizing Container Area:** Determine the maximum area that can be formed by two vertical lines and the x-axis in a histogram.
5. **Palindromic Strings:** Check if a given string is a palindrome.
6. **Merge Sorted Arrays:** Merge two sorted arrays in-place.
7. **Longest Subarray with Ones After Replacement:** Find the longest subarray with at most one zero by flipping at most one 0 to 1.
8. **Minimum Subarray Sums:** Find the minimum size of a contiguous subarray with a sum greater than or equal to a target value.
9. **Squared Arrays:** Given a sorted array, return a new array containing squares of each number in sorted order.
10. **Consecutive Elements Alignment:** Rearrange the elements such that all consecutive elements are in increasing order.



# #graphs


- know the main techniques
	- shortest paths
	- min spanning tree
- !! important (ie what halim is saying):
	- recognizing that a problem is a graph problem + can use a standard graph algo
	- aka need lots of problems that train this
		- ie: graph problems are another category where, lots of problems will use the same strat. but the real 'difficulty' of the problem is realizing you can use the strat
		- and so try to have as many 'patterns/examples' as possible to train this




## #graphs/topological_sort 
- refs
	- https://cp-algorithms.com/graph/topological-sort.html
		- dfs
	- https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
		- kahn
		- dfs


## #graphs/process_edge 



- [[_refs/02 algorithms/skiena.pdf#page=238|adm, 7.9 Applications of Depth-First Search]]
	- skiena's traversal template assumes that we only want to process an edge once
		- (cite the yt lectures)
		- this is why it's important to know if we've already traversed edge (x,y)
		- iirc..some algos even: there is an 'error' if you see the edge again
			- confirm whether this is what the 2 coloring discusses:
				- [[_refs/02 algorithms/skiena.pdf#page=233|adm, 7.7.2 Two-Coloring Graphs]]
	- [[_refs/02 algorithms/skiena.pdf#page=238&selection=109,32,133,1|adm, page 238]]
		- "But what if y is an ancestor of x, and thus in a discovered state..."
		- to understand this, need to understand his dfs template
			- need to understand basic C syntax; i put this somewhere...
				- ie the `->` syntax
		- note: this question isn't straightforward because of the nature of dfs
			- it's very possible to have a sequence of exploring 'new edges' that loop back to a node you've already visited
			- 


- point of 'process edge'
	- you want to do something based on the fact that there's a relationship (x,y)







## #graphs/traversal
- (idk correct jargon for this tag)
- how to handle traversal where there's lots of valid starting points
	- or don't know where to start
	- or traversals starting at diff points would give redundant/overlapping answers
		- ie probly bc connected components
	- answer: start anywhere and use a 'visited nodes' structure
		- so that we don't "initialize traversals" from alrdy visited nodes


### #graphs/traversal/dfs 
- [[_refs/02 algorithms/clrs.pdf#page=585|clrs, 20.3 Depth-first search]]






## #graphs/edge_classification 
- [[_refs/02 algorithms/clrs.pdf#page=591&selection=388,0,392,5|clrs, page 591, classification of edges]]






# #array
- imo matrix problems are such a large class, that i think maybe it should be it's own tag family
	- ie not a subtag of graphs
	- actually i'm going to rename this to 'array'
	- one of the earliest thing to point out in an early discussion/fundy:
		- think about whether your problem is really a graph problem
		- i'm going to have a few #array discussions that are essentially describing how you specifically implement graph algos on an array


- think about whether your problem is really a graph problem



### #array/traversal/storing_visited_nodes_in_place
- there is an optimization where we don't need a structure to store 'visited nodes'
	- applies to some matrix problems
		- i think more generally: problems where you're given an 'implicit graph'
			- ie not a true graph representation structure
			- but it's like obvious why we can consider it a 'graph', and what the nodes/edges are
			- tbh i think arrays are really the only applicable/useful example here
	- strat
		- after visiting/processing, modify the input matrix's entries
			- in such a way that, if you check this node again: you can see that it's been modified
				- ie to a negative number or a number that isn't 1
			- aka alrdy visited
- examples
	- [[../../LeetCode/733. Flood Fill|733. Flood Fill]]
	- [[../../LeetCode/200. Number of Islands|200. Number of Islands]]
	- [[../../LeetCode/695. Max Area of Island|695. Max Area of Island]]
	- for the above problems, consider adding code where i actually use a 'visited' structure
		- maybe also [[../../LeetCode/542. 01 Matrix|542. 01 Matrix]]

### #array/traversal/neighbors
- basically, matrix always has a very standard way of extending a traversal
- what is the jargon here...'neighbors'? 'valid neighbors'?
	- can increment left, right, up, down
	- add boundary checks




# #trees 

## #trees/traversal 

- predecessor, successor
	- [[_refs/02 algorithms/clrs.pdf#page=340&selection=207,0,211,11|clrs, page 340]]







# #python



#### #python/modules/collections/counter

https://pymotw.com/3/collections/counter.html

- [[_refs/unfiled/_markdown examples/python-counter|python-counter]]
	- [[_refs/unfiled/_markdown examples/python-counter#Counting Objects in Python|counting with dict and defaultdict]]
	- [[_refs/unfiled/_markdown examples/python-counter#Constructing Counters|feeding iterable into counter]]
	- [[_refs/unfiled/_markdown examples/python-counter#Subtracting the Elements' Multiplicity|subtracting multiplicity]]



### #python/modules/heapq

- realpython article is great
	- cite everything except the example
- https://pymotw.com/3/heapq/index.html




# assorted
- trailing pointer
	- [[_refs/02 algorithms/clrs.pdf#page=343&selection=389,0,392,6|clrs, page 343]]



- [[_refs/02 algorithms/skiena.pdf#page=51|adm, 2.2 The Big Oh Notation]]
- [[_refs/02 algorithms/skiena.pdf#page=63|adm, 2.6 Summations]]
	- through 2.8
- [[_refs/02 algorithms/skiena.pdf#page=146|adm, 4.6 Quicksort: Sorting by Randomization]]
- clrs
	- 2
		- sorting jargon (p 17-18)
		- insertion sort
		- subarray
			- a contiguous portion of the array
		- loop invariants
		- objects, atributes
		- pseudocode conventions/jargon
	- 2.2
		- complexity jargon
	- 2.3
		- algorithmic technique jargon
		- solving/analyzing recurrence relations
	- part II intro
	- 6.3 building a heap
	- 6.5 priority queues
	- 7.2-7.3 quicksort
	- 12.1 BST
		- bst property
		- pre/in/postorder tree walk
	- 16 amortized analysis
	- 20.2 bfs
	- 20.3 dfs
	- 14.1, 14.3 dp
- knuth
	- [6.2.1 searching an ordered table](_refs/02%20algorithms/taocp%203.pdf#page=427&annotation=5576R)
		- [variation](_refs/02%20algorithms/taocp%203.pdf#page=432&selection=51,0,51,23)


