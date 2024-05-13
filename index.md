# assorted


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



- [[_refs/algorithms/kt.pdf#page=287|kt, 6.3 Segmented Least Squares: Multi-way Choices]]
	- multi-way choices
- [[_refs/algorithms/epi.pdf#page=314&offset=-115,647,0|epi, Dynamic programming boot camp]]
	- caching
	- recycling cache space
	- 'make choices'
	- counting problems
	- decision problems
- [[_refs/algorithms/clrs.pdf#page=385|clrs, 14.1 Rod cutting]]
	- optimal substructure
	- time-memory tradeoff
	- top-down
	- memoization
	- bottom-up
	- subproblem graph
- [[_refs/algorithms/clrs.pdf#page=404|clrs, 14.3 Elements of dynamic programming]]
	- really good explanation of optimal substructure, overlapping subproblems, 
- [[_refs/algorithms/skiena.pdf#page=354|skiena, 10.9.1 When is Dynamic Programming Correct?]]
	- principle of optimality
	- state
	- partial solution
- [[_refs/algorithms/skiena.pdf#page=321|skiena, Chapter 10 Dynamic Programming]]
	- consequences
	- caching
	- [[_refs/algorithms/skiena.pdf#page=323|skiena, 10.1.2 Fibonacci Numbers by Caching]]
		- memoization
		- caching (or tabling)
	- [[_refs/algorithms/skiena.pdf#page=329|skiena, 10.2.1 Edit Distance by Recursion]]
		- the recursion branches three ways
	- [[_refs/algorithms/skiena.pdf#page=332|skiena, 10.2.3 Reconstructing the Path]]
		- wait this is very important..aka reconstructing the solution is actually a very general procedure
			- this was mentioned by other resources as well
				- ie [[_refs/algorithms/nutshell.pdf#page=183&selection=36,0,61,62|nutshell, page 183]]
				- and there was another i swear...
	- [[_refs/algorithms/skiena.pdf#page=355|skiena, 10.9.2 When is Dynamic Programming Efficient?]]
		- size of the state space
		- combinatorial objects
- [[_refs/algorithms/dpv.pdf#page=167|dpv, 6 Dynamic programming]]
	- algorithmic paradigm
	- implicit dag
		- nodes are subproblems
		- edges are dependencies
			- if to solve subproblem B we need the answer to subproblem A, then there is a (conceptual) edge from A to B
			- ie A is a smaller subproblem than B
	- [[_refs/algorithms/dpv.pdf#page=174&selection=266,0,266,18|dpv, page 174]]
		- underlying dag structure
	- [[_refs/algorithms/dpv.pdf#page=176&selection=6,0,6,18|dpv, page 176]]
		- common subproblems
	- [[_refs/algorithms/dpv.pdf#page=180&selection=6,0,6,11|dpv, page 180]]
		- dpv say memoization is NOT dynamic programming
			- but most other authors seem to say that memoization is a type of DP
	- [[_refs/algorithms/dpv.pdf#page=186&selection=1,0,6,18|dpv, page 186]]
		- memory can be released
- [[_refs/algorithms/cses2.pdf#page=82&offset=-3,136|cses2, 6.2.4 From Permutations to Subsets]]
	- can also think of dp as turning 'permutations' into 'subsets '




- seems subproblem IS the state
	- it's just sometimes, you have to solve a different problem instead.
	- and now it maybe becomes obvious why 'subproblems' includes all 'candidates'. aka it's just 'all valid (partial) candidates for the subproblem'
- for 'candidates':
	- see what they use for backtracking
- i bet: all these problems where DP works: then backtracking would work too. but the key is: many candidates lead to the same state/consequences, which is all we care about
	- see skiena






# #graph


#graphs/process_edge 



- [[../../_refs/algorithms/skiena.pdf#page=238|adm, 7.9 Applications of Depth-First Search]]
	- skiena's traversal template assumes that we only want to process an edge once
		- (cite the yt lectures)
		- this is why it's important to know if we've already traversed edge (x,y)
		- iirc..some algos even: there is an 'error' if you see the edge again
			- confirm whether this is what the 2 coloring discusses:
				- [[../../_refs/algorithms/skiena.pdf#page=233|adm, 7.7.2 Two-Coloring Graphs]]
	- [[../../_refs/algorithms/skiena.pdf#page=238&selection=109,32,133,1|adm, page 238]]
		- "But what if y is an ancestor of x, and thus in a discovered state..."
		- to understand this, need to understand his dfs template
			- need to understand basic C syntax; i put this somewhere...
				- ie the `->` syntax
		- note: this question isn't straightforward because of the nature of dfs
			- it's very possible to have a sequence of exploring 'new edges' that loop back to a node you've already visited
			- 


- point of 'process edge'
	- you want to do something based on the fact that there's a relationship (x,y)







#graphs/traversal
- (idk correct jargon for this tag)
- how to handle traversal where there's lots of valid starting points
	- or don't know where to start
	- or traversals starting at diff points would give redundant/overlapping answers
		- ie probly bc connected components
	- answer: start anywhere and use a 'visited nodes' structure
		- so that we don't "initialize traversals" from alrdy visited nodes


#graphs/edge_classification 
- [[../../_refs/algorithms/clrs.pdf#page=591&selection=388,0,392,5|clrs, page 591, classification of edges]]


#graphs/traversal/dfs 
- [[../../_refs/algorithms/clrs.pdf#page=585|clrs, 20.3 Depth-first search]]





# #array
- imo matrix problems are such a large class, that i think maybe it should be it's own tag family
	- ie not a subtag of graphs
	- actually i'm going to rename this to 'array'
	- one of the earliest thing to point out in an early discussion/fundy:
		- think about whether your problem is really a graph problem
		- i'm going to have a few #array discussions that are essentially describing how you specifically implement graph algos on an array


#array
- think about whether your problem is really a graph problem



#array/traversal/storing_visited_nodes_in_place
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

#array/traversal/neighbors
- basically, matrix always has a very standard way of extending a traversal
- what is the jargon here...'neighbors'? 'valid neighbors'?
	- can increment left, right, up, down
	- add boundary checks




# #trees 

#trees/traversal 

- predecessor, successor
	- [[../../_refs/algorithms/clrs.pdf#page=340&selection=207,0,211,11|clrs, page 340]]







# #python

#python/modules/collections/counter

https://pymotw.com/3/collections/counter.html

- [[../../_refs/_markdown examples/python-counter|python-counter]]
	- [[../../_refs/_markdown examples/python-counter#Counting Objects in Python|counting with dict and defaultdict]]
	- [[../../_refs/_markdown examples/python-counter#Constructing Counters|feeding iterable into counter]]
	- [[../../_refs/_markdown examples/python-counter#Subtracting the Elements' Multiplicity|subtracting multiplicity]]



#python/modules/heapq

- realpython article is great
	- cite everything except the example
- https://pymotw.com/3/heapq/index.html




# assorted
- trailing pointer
	- [[_refs/algorithms/clrs.pdf#page=343&selection=389,0,392,6|clrs, page 343]]



- [[../../_refs/algorithms/skiena.pdf#page=51|adm, 2.2 The Big Oh Notation]]
- [[../../_refs/algorithms/skiena.pdf#page=63|adm, 2.6 Summations]]
	- through 2.8
- [[../../_refs/algorithms/skiena.pdf#page=146|adm, 4.6 Quicksort: Sorting by Randomization]]
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
	- [6.2.1 searching an ordered table](../../_refs/algorithms/taocp%203.pdf#page=427&annotation=5576R)
		- [variation](../../_refs/algorithms/taocp%203.pdf#page=432&selection=51,0,51,23)


