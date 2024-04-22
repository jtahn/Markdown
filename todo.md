# anki cards
- (to blurb on 'workflow')
- add anki cards once i make the template
- once i make a template: then add the anki card
	- so all the 'new cards' will be things where i've only 'made template'
	- only graduate to learning phase once i 'understand optimized'
	- (so maybe: edit the settings for 'reading/revising cards' so that there's only 1 learning step)
- each time a card shows up for a review:
	- minimum review actions:
		- fully understand what's already there
		- do any edits that feel 'easy'
	- if i have the energy:
		- try to reach the next 'stage' of completeness
		- ie if i'm at 'understand optimized'; then try to complete 'fill with comprehensive'






# markdown structure: possible changes
- can i add code lines to code snippets?
- best way to add diagrams?
	- you can drag and drop local gif files into obsidian (check if i can drag straight from browser; probly not though); they automatically will get moved to attachments folder + linked there; then they show up on github markdown viewer, and also in the anki card embedding! 
	- making gifs:
		- * [Make an animated GIF from a slide show - Microsoft Support](https://support.microsoft.com/en-us/office/make-an-animated-gif-from-a-slide-show-a598753e-92de-4f1b-8393-714db4d334b4)
		- seems google slides doesn't have this functionality...so you could create in gslides, then open in ppt
			- https://www.howtogeek.com/832437/how-to-convert-google-slides-to-video-or-gif/
	- alternative (that seems worse, but maybe could be useful to be aware of)
		- you can share a link to a google slides prez that auto plays/loops it 
		- ie https://docs.google.com/presentation/d/e/2PACX-1vQ-Oy-oQ0i4CvWbo8gf9-v42gVOb5gS76sJvhG7jqIntQV7R1dDG3tS7YUhRiPqYXBCjqCcVsJUeZjG/pub?start=true&loop=false&delayms=1500&slide=id.gbc95359713_0_384
		- * [Make Google Docs, Sheets, Slides & Forms public - Computer - Google Docs Editors Help](https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop#)
			- can get an embed link

# anki card changes
- the js embedding needs to also replace the 'directory' field; and then i add leetcode directory to all my leetcode cards

# general card structure/content reminders
- it's fine to leave a todo list for later
	- get stuff down in a state where, it won't be a headache to resume where i stopped
	- if revising is difficult (ie idk how to word things properly; or i can't really figure out the 'big idea'): just means i don't have the background/connections to make yet
		- it's just inefficient to spend an hour trying to figure it out: the explanation will eventually appear somewhere else (ie clrs; stackexchange; solution to another problem)
			- i have too much stuff to cover atm, i need to prepare for swe and quant interviews
	- so just come back later, when i've done more reviews; eventually, i'll have the bg/cnxns
- add the function prototype to every card, right under the link
- add descriptors 
- discussions of 'fundamental techniques'
	- remove from cards where this is just 1 step of the approach
		- ie [347. Top K Frequent Elements](LeetCode/347.%20Top%20K%20Frequent%20Elements.md)
	- add reference to cards where the 'fundamental technique' is the entire approach; ie exactly solved by these fundamental techniques
	- examples
		- [703. Kth Largest Element in a Stream](LeetCode/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md)
			- heaps
		- [704. Binary Search](LeetCode/704.%20Binary%20Search.md)
			- 2 vs 3 cases
			- while loop condition allowing equality or not
		- [242. Valid Anagram](LeetCode/242.%20Valid%20Anagram.md) will contain discussions on:
			- counting
			- (a lot of this covered by realpython article on Counter class)
			- choice of what python structure to use for counting
				- dict (and the 2 typical ways ppl handle absent keys)
				- default dict
				- Counter
			- how to compare hash structures
				- cover the built-in ops/commands
					- ie `&` operator for Counter
				- optimizations:
					- construct structure as you pass through 1 item; then decrement counts as you pass through another
					- using a variable to store total counts, so you dont have to iterate through entire hashmap every time to compare 
						- 2 ways here too:
							- store how many 'letters of alphabet have the correct count'
							- store total letters we are correct with (and so we have success when total letter matches length of whatever we're trying to find/match)




# resources
- ![](!assets/attachments/Pasted%20image%2020240412021212.png)
	* [10 CS 106B Lecture Recursion 2 recursive data - YouTube](https://www.youtube.com/watch?v=iiF7rFx32Fw&list=PL-h0BZdG_K4kAmsfvAik-Za826pNbQd0d&index=10)
	* [14 CS 106B Lecture Backtracking printBinary, printDecimal - YouTube](https://www.youtube.com/watch?v=zL4mjpYpRmc&list=PL-h0BZdG_K4kAmsfvAik-Za826pNbQd0d&index=14)




#  comprehensive (1-41)
- 1-41
46. [226. Invert Binary Tree](226.%20Invert%20Binary%20Tree.md)
49. [110. Balanced Binary Tree](110.%20Balanced%20Binary%20Tree.md)
52. [235. Lowest Common Ancestor of a Binary Search Tree](235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md)
66. [973. K Closest Points to Origin](973.%20K%20Closest%20Points%20to%20Origin.md)
122. [53. Maximum Subarray](LeetCode/53.%20Maximum%20Subarray.md)
130. [57. Insert Interval](LeetCode/57.%20Insert%20Interval.md) 
- and anything i've done in blind75
	- [232. Implement Queue using Stacks](LeetCode/232.%20Implement%20Queue%20using%20Stacks.md)
	- [278. First Bad Version](LeetCode/278.%20First%20Bad%20Version.md)
	- [733. Flood Fill](LeetCode/733.%20Flood%20Fill.md)
	- [542. 01 Matrix](LeetCode/542.%2001%20Matrix.md)
	- [383. Ransom Note](LeetCode/383.%20Ransom%20Note.md)

revise in passes; can combine passes
1. make template
1. understand optimal
2. determine optimal fundies
3. make comprehensive
4. determine comprehensive fundies
5. make structured
6. make concise


## not comprehensive
21. (maybe) [20. Valid Parentheses](LeetCode/20.%20Valid%20Parentheses.md)

34. [[LeetCode/4. Median of Two Sorted Arrays]]

## not structured
20. [239. Sliding Window Maximum](LeetCode/239.%20Sliding%20Window%20Maximum.md)
23. [150. Evaluate Reverse Polish Notation](LeetCode/150.%20Evaluate%20Reverse%20Polish%20Notation.md)
24. [22. Generate Parentheses](LeetCode/22.%20Generate%20Parentheses.md)
36. [21. Merge Two Sorted Lists](LeetCode/21.%20Merge%20Two%20Sorted%20Lists.md)

## not concise
(all listed above; next time i review, work on concise)






# optimal only (42+)
(do comprehensive later; ie once i fully finish 'optimal' pass of neetcode and grind75)
(and after i go through EPI/CTCI/skiena)


- quicklinks
	- https://www.youtube.com/playlist?list=PLPe9IkX86X3y5m_MvtNu2ughxsvkqUNKr
	- https://algo.monster/liteproblems/1
	- https://leetcodethehardway.com/solutions/category/3000---3099

## created template


89. [261. Graph Valid Tree](LeetCode/261.%20Graph%20Valid%20Tree.md)
90. [323. Number of Connected Components in an Undirected Graph](LeetCode/323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph.md)
91. [684. Redundant Connection](LeetCode/684.%20Redundant%20Connection.md)
92. [127. Word Ladder](LeetCode/127.%20Word%20Ladder.md)

93. [332. Reconstruct Itinerary](LeetCode/332.%20Reconstruct%20Itinerary.md)









# reminder of order

- meta: workflow for comprehensive
	- reliable github repos
		- https://github.com/lzl124631x/LeetCode/tree/master/leetcode
	- possibly reliable github repos
		- https://github.com/knockcat/Leetcode
	- possibly reliable leetcoders if i see them in leetcode solutions; otherwise open a bunch of solutions in tabs
		- https://leetcode.com/lee215/
		- https://leetcode.com/linfq/
	- draft a skeleton + dump screenies/etc for the solutions
		- high level summary of the optimal solution:  https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0
		- watch the vid https://neetcode.io/practice
		- look it up on reliable sources for the 'best solution'
			- https://leetcodethehardway.com/
			- https://algo.monster/liteproblems/424
		- reliable leetcoders
			- hiepit https://leetcode.com/hiepit/
			- chaudhary1337 https://leetcode.com/chaudhary1337/
			- DBabichev https://leetcode.com/DBabichev/
		- reliable youtubers
			- https://www.youtube.com/@chaudharycodes/videos
		- then check leetcode forum solutions for other possible methods and clean explanations
	- clean it up a bit
	- once it's clean enough
		- unsuspend card in anki
		- add to toc in the readme

- more interesting/useful/related (these might've already been covered)
	- monotonic queues/stacks
		- https://leetcode.com/problems/jump-game-iv/description/
		- https://leetcode.com/problems/constrained-subsequence-sum/description/
		- https://leetcode.com/problems/132-pattern/description/
		- https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
		- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
		- https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
	- binary search
		- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
		- https://leetcode.com/problems/divide-chocolate/description/
			- https://leetcode.com/discuss/interview-question/350800/Google-or-Onsite-or-Chocolate-Sweetness
		- 1539. [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC++Python-O(logN))
		- 1482. [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/javacpython-binary-search/578488)
		- 1283. [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/javacpython-bianry-search/401806)
		- 1231. [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/discuss/408503/Python-Binary-Search)
		- 1011. [Capacity To Ship Packages In N Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/javacpython-binary-search/351188?page=3)
		- 774. [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/113633/Easy-and-Concise-Solution-using-Binary-Search-C++JavaPython)
	- design
		1. Design Tic-Tac-Toe
		2. Design TinyURL
		3. Encode and Decode TinyURL
		4. Moving Average from Data Stream
		5. Zigzag Iterator
		6. Insert Delete GetRandom O(1) - Duplicates allowed
		7. All O`one Data Structure
		8. Flatten Nested List Iterator
		9. Design Search Autocomplete System
		10. Two Sum III - Data structure design
		11. Design Circular Queue
		12. Find Median from Data Stream

- find/focus/figure out topics that the top companies seem to love
	- binary search (ie google)
	- "Hudson river is asking combinatronics + geom algo"
	- primeagen said: focus on arrays (and javascript) (and asyncio in js?)
	- google
		- https://javascript.plainenglish.io/leetcode-1293-shortest-path-in-a-grid-with-obstacles-elimination-b60f229579f7
		- https://javascript.plainenglish.io/leetcode-1091-shortest-path-in-binary-matrix-e9119754ceb1
		- 




- fill in problems for fundies that i think should exist, but neetcode/grind/etc dont provide 'fundy enough' problem for it
	- backtracking algo with multiple obvious extension paths at each node
		- ie 'find all paths from source to target vertex in graph'
		- there are some problems that are kinda like this, but they're both a bit more complicated imo
			- [17. Letter Combinations of a Phone Number](LeetCode/17.%20Letter%20Combinations%20of%20a%20Phone%20Number.md) 
			- [46. Permutations](LeetCode/46.%20Permutations.md)
	- https://leetcode.com/problems/next-greater-element-i/description/
		- seems like one of the best fundies for monotonic stack?
		- this one is related to [739. Daily Temperatures](LeetCode/739.%20Daily%20Temperatures.md)
		- this problem: it shouldnt matter which way you iterate, wrt complexity
			- which is why: it's valuable bc it highlights why [739. Daily Temperatures](LeetCode/739.%20Daily%20Temperatures.md) has 2 optimal solutions instead of just 1...it's bc the possible temps are a finite set




- other references to make problem writeups for
	- directly applicable to swe interview
		- aziz (EPI)
			- maybe buy the most recent python version at some point
			- https://elementsofprogramminginterviews.com/2017/11/27/2017-11-27-buying-epi/
		- skiena
		- maybe cormen
	- directly applicable to quant interview
		- brain teasers
		- combinatorics
		- mathcounts / AMC / IMO
		- art of problem solving
- return to leetcode
	- all problems covered by 'reliable' sources
		- neetcode
		- algomonster
		- hard way
- problems that are tangentially related
	- other programming problem sites
		- https://checkio.org
	- competitive programming
		- https://en.wikipedia.org/wiki/Competitive_programming#Online_platforms
			- project euler
			- codeforces
		- other lists
			- peking icpc
				- http://poj.org/problemlist
- other references idk if i'm making problem writeups yet; bc seems like i should just make zotero reading cards out of references
	- swe performance
		- clean code, etc
		- most popular posts on swe-related stack exchange communities
		- reputable informal sources
			- realpython
			- hitchhikers
			- pmotw
		- reputable formal sources
			- ramalho's fluent python
	- swe interview at places like hrt
		- cpp
		- low level and systems concepts
	- stuff i alrdy know but i want to make cards on, for completeness, and is so fundamental, even tho mebe wont apply to job
		- linalg
		- prob
		- stats
		- signal processing
- 



# meta
- always keep the list in order of urgency
- examples of todo items
	- calc explanation
	- anki
		- backlog for reviews
		- revision ideas after review (check voice memos/notebook for edits)
		- blurbs that i think would be helpful for swe/leetcode interviews
		- leetcode
			- "i don't understand the main solutions; aka either the 'simple inefficient' ones and/or the 'important efficient' ones"
			- "don't understand a qualitatively different technique (but probly not urgent bc it's not strictly better)"
		- extremely rough cards that i understand the material, and have all the prose there; but are written very sloppily
		- future cards that i (just) have a skeleton for





---


# specific companies

## ttzztt

scroll the left sidebar down, it will show categories
https://ttzztt.gitbooks.io/lc/content/longest-increasing-subsequence.html


Twitter
Identifying Triangle
Last and Second-Last
300. Longest increasing subsequence
Twin String
647. Number of palindromic substring
Wildcard Matching
Akuna
C++ Intern
V1
V2
Cut the Sticks
Quant Dev
Postfix_to_infix
Drone Delivery
phone
LintCode Contest
Ask For Cooling Time
SQL
176. Second Highest Salary
597. Friend Requests I: Overall Acceptance Rate
FB 19
Convert Binary Search Tree (BST) to Sorted Doubly-Linked List
3Sum
Minimum Window Substring
Count number of occurrences (or frequency) in a sorted array
Count NO2
Valid Palindrome
Merge k Sorted Lists
Kth Largest Element in an Array
Move Zeros
Remove Invalid Parenthesis
friends
Integer to English
Islands
Valid Palindrome
sec
Longest Increasing Path in a Matrix
Product of Array Except Self
Binary Tree Vertical Order Traversal
Add Binary
Valid Parentheses
sup
128. Longest Consecutive Sequence
Combination Sum II
Add and Search Word - Data structure design
feb
Google 20
410. Split Array Largest Sum

