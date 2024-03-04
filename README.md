# Meta
- this repo is for md files that i need to be publicly available. examples:
	- rough math/cs explanations for students
		- markdown > latex bc we get max convenience with all of
			- screenies, mathjax, code snippets, nested lists, headings
		- obsidian export to pdf is wonky, the md file itself looks better
	- leetcode solution writeups to embed onto anki cards[^embed]

[^embed]:  Cards need a `{{number}}` field; then paste this code into the card template: ```<script src="https://jtahn.github.io/emgithub/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fjtahn%2FMarkdown%2Fblob%2Fmain%2FLeetCode%2F{{number}}.md&style=default&type=markdown&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on"></script>```



# Calc TA stuff
- hw 2 solns (private vault)
- hw 3 solns (private vault)
- [hw 4 solutions](Calc/hw%204%20solutions.md)

# LeetCode ToC[^order][^unfinished]
[^order]: starts with neetcode150; then continues with grind169 (sorted by topic, then difficulty); then 'leetcode top interview 150'
[^unfinished]: check [todo](todo.md), some listings below are pretty rough. i try not to list it here until it's decent enough 

## Blurbs
- [Complexity of sorting](Blurbs/Complexity%20of%20sorting.md)
- [infinite loop caused by integer overflow](Bugs/infinite%20loop%20caused%20by%20integer%20overflow.md)


## Arrays & Hashing
1. [217. Contains Duplicate](LeetCode/217.%20Contains%20Duplicate.md)
2. [242. Valid Anagram](LeetCode/242.%20Valid%20Anagram.md)
3. [1. Two Sum](LeetCode/1.%20Two%20Sum.md)
4. [49. Group Anagrams](LeetCode/49.%20Group%20Anagrams.md)
5. [347. Top K Frequent Elements](LeetCode/347.%20Top%20K%20Frequent%20Elements.md)
6. [238. Product of Array Except Self](LeetCode/238.%20Product%20of%20Array%20Except%20Self.md)
7. [36. Valid Sudoku](LeetCode/36.%20Valid%20Sudoku.md)
8. [271. Encode and Decode Strings](LeetCode/271.%20Encode%20and%20Decode%20Strings.md)
9. [128. Longest Consecutive Sequence](LeetCode/128.%20Longest%20Consecutive%20Sequence.md)

## Two Pointers
10. [125. Valid Palindrome](LeetCode/125.%20Valid%20Palindrome.md)
11. [167. Two Sum II - Input Array Is Sorted](LeetCode/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.md)
12. [15. 3Sum](LeetCode/15.%203Sum.md)
13. [11. Container With Most Water](LeetCode/11.%20Container%20With%20Most%20Water.md)
14. [42. Trapping Rain Water](LeetCode/42.%20Trapping%20Rain%20Water.md)

## Sliding Window
15. [121. Best Time to Buy and Sell Stock](LeetCode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.md)
16. [3. Longest Substring Without Repeating Characters](LeetCode/3.%20Longest%20Substring%20Without%20Repeating%20Characters.md)

## Stack
21. [20. Valid Parentheses](LeetCode/20.%20Valid%20Parentheses.md)

## Binary Search
28. [704. Binary Search](LeetCode/704.%20Binary%20Search.md)

## Linked List
36. [21. Merge Two Sorted Lists](LeetCode/21.%20Merge%20Two%20Sorted%20Lists.md)
41. [141. Linked List Cycle](LeetCode/141.%20Linked%20List%20Cycle.md)

## Trees
46. [226. Invert Binary Tree](LeetCode/226.%20Invert%20Binary%20Tree.md)
49. [110. Balanced Binary Tree](LeetCode/110.%20Balanced%20Binary%20Tree.md)
52. [235. Lowest Common Ancestor of a Binary Search Tree](LeetCode/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md)

## Heap / Priority Queue
66. [973. K Closest Points to Origin](LeetCode/973.%20K%20Closest%20Points%20to%20Origin.md)

## Greedy
122. [53. Maximum Subarray](LeetCode/53.%20Maximum%20Subarray.md)

## Intervals
130. [57. Insert Interval](LeetCode/57.%20Insert%20Interval.md)

## grind169

[733. Flood Fill](LeetCode/733.%20Flood%20Fill.md)

[542. 01 Matrix](LeetCode/542.%2001%20Matrix.md)

[232. Implement Queue using Stacks](LeetCode/232.%20Implement%20Queue%20using%20Stacks.md)

[278. First Bad Version](LeetCode/278.%20First%20Bad%20Version.md)

[383. Ransom Note](LeetCode/383.%20Ransom%20Note.md)



# Style
- code
	- make it easy to not just READ, but UNDERSTAND what it is doing
		- i'll probably remember it better if i understand the code too
	- it's fine to have 'longer code' for these problems: the solutions are so short, that a 'long solution' isn't even that long
	- this generally means, avoid:
		- oneliners
		- code that doesn't match up with the intuition/explanation


# References
- most stuff here isn't original
- Leetcode
	- youtube
		- neetcode
			- he doesnt give all 'good to know solutions', but he always explains the 'best' solution very well. so imo, these are probably the best starting point for completely understanding the problem and solutions
			- this is reason why i'm starting with neetcode150 list instead of grind169; ie if i cant understand it, then i know i can fall back here; or if i'm too tired that i dont even want to read, then i can at minimum watch the youtube solution 
		- https://www.youtube.com/@cheatcodeninja/videos
	- https://leetcodethehardway.com/
	- https://algo.monster/liteproblems/271
		- replace 271 with whatever number the problem is
		- these sometimes/often don't actually have the best solution
	- leetcode forum users
		- https://leetcode.com/hiepit/
			- this guy consistently seems the best. covers all the necessary approaches, extremely concise, gives the key idea with proper terminology. some of the other guys below are more comprehensive but too rambly, and/or provide extra approaches that don't seem 'necessary' to know/cover
		- https://leetcode.com/archit91/
		- https://leetcode.com/its_vishal_7575/
		- https://leetcode.com/r0gue_shinobi/
		- https://leetcode.com/MarkSPhilip31/
	- might have interesting perspectives
		- https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/
		- https://leetcode.com/stefanpochmann/
			- this guy seems famous, but actually i'm generally not a fan, he's addicted to writing unreadable code bc he just slaps way too many operators, language specific things/tricks into it in order to cut down the number of lines, that don't seem to actually make the code any more efficient
			- basically he's inadvertently singlehandedly convincing me that oneliners are terrible, and i shouldnt use too many esoteric functions or going inception style and nesting dozens of generators/comprehensions
				- just stick to popular functions; when the solutions are already this short, there's nothing wrong with loops and multiline conditional statements, bc everyone knows what you're doing and it's way easier to read, even if you're familiar with oneliner if/else assignments
				- even if you're aware of how increment operators behave (ie ocurring before or after assignment); it's just completely unecessary brainpower to use when you're trying to read a solution; or keeping track of all the generators that are nested inside each other; its just far easier to read when it's just indented
			- ie completely missing the point...point of leetcode is to understand the patterns and major techniques of how to work with structures...not to write oneliners lol
	- chinese
		- https://github.com/topics/leetcode-solutions
		- https://github.com/grandyang/leetcode
		- 1point3acres leetcode (need a mandarin translator)
- code
	- neetcode github
	- https://walkccc.me/LeetCode/
- general interview tips
	- https://interviewguide.dev/
	- https://www.techinterviewhandbook.org/
- to look up premium leetcode problem descriptions
	- https://www.lintcode.com/problem
	- https://leetcode.ca/search/
- more lists of problems
	- when i go thorugh grind169..tbh i should order it by topic and difficulty (like neetcode does); not by the og ordering
		- the og ordering (where they mix it up) is more meant if i'm practicing leetcode their way, ie actually going through and solving them without looking up solutions..completely different from what i'm doing, which is just reading and understanding solutions
		- https://www.techinterviewhandbook.org/grind75?weeks=26&hours=40&mode=all&grouping=topics&order=difficulty
	- https://projecteuler.net/archives
	- teamblind
		- https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
		- https://www.teamblind.com/post/Looking-for-a-good-follow-up-to-Blind-Curated-List-of-Top-75-Leetcode-Questions-nbV7TTvS
- 'theory'
	- CLRS
	- skiena
	- https://medium.com/leetcode-patterns




# Obsidian settings that I changed for this vault
- recording them here in case i need to set this up again

## editor
![](!assets/attachments/Pasted%20image%2020240226102400.png)
- the first option is because code snippets are sometimes harder to read bc the default width is so small, so they get moved to diff lines..i might change this tho, seems reducing font size seems to solve this for most code (since most code, if line too long, then i just manually put stuff on another line)
	- actually i turned it back on; i think reducing font solves this issue; turning this off is kinda annoying
- the second i think will solve issue of where: in obsidian, stuff on subsequent lines, gets instead put on same line when i view in github
	- nah it doesnt; what it means tho is that if i look at the file in reading mode, it looks more accurate to what i'd see on github 

![](!assets/attachments/Pasted%20image%2020240228151535.png)



## appearance
![](!assets/attachments/Pasted%20image%2020240226102207.png)


## files and links
- these are necessary so that images show up when viewing markdown files on github.com; so them emgithub sees them too when it embeds them into anki cards
	- ![](!assets/attachments/Pasted%20image%2020240224004117.png)
	- ![](!assets/attachments/Pasted%20image%2020240224004445.png)


- moving forward:
	- if i want to move files/folders around (maybe even rename folders as well), i need to use a script to do this
		- ie script goes into each markdown file and edits relative links, based on how i moved/renamed folders
		- bc obsidian currently is bugged with this
- there's currently a bug with relative paths (as of of 2/26/2024):
	- when using relative path: if you move/rename files, it doesnt update the relative paths inside those files
		- but it DOES rename places where this file is linked...ie seems if i move the attachments folder, that actually might not break anything (but idk why i would even do that rn, there's no point)
	- yea see here
		- https://forum.obsidian.md/t/broken-links-in-relative-path-mode-on-move-rename/4386
- cannot use absolute paths
	- absolute links don't work; bc obsidian doesnt know to put 'github.com/jtahn/Anki/LeetCode' etc before the '!assets/attachments/etc'
		- aka obsidan 'absolute' links are different 'definition' compared to github 'absolute'
	- github seems to only support relative links
		- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes#relative-links-and-image-paths-in-readme-files
		- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links
	- github absolute links without needing to use the website? see examples at the bottom of this subsection
		- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images
			- ![](!assets/attachments/Pasted%20image%2020240226104913.png)



- these are just so the github folder/file structure is cleaner; mimics my personal obsidian
	- ![](!assets/attachments/Pasted%20image%2020240224004123.png)
- settings i accidentally stumbled on, but probly have toggles in the settings
	- when i moved an attachment file, it asked me if i wanted the app to always update the links, and i said yes
	- when i tried to delete a file, i checked dont remind
		- ![](!assets/attachments/Pasted%20image%2020240224005640.png)



# markdown/obsidian 
- https://docs.github.com/en/get-started/writing-on-github
	- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- just use double space for line break
	- https://www.markdownguide.org/basic-syntax/#line-break-best-practices
	- https://stackoverflow.com/questions/36583502/how-to-force-a-linebreak
		- Just one thing: don't do a global trim on trailing spaces, as is often habit for source code, otherwise you'll lose important formatting.



# obsidian decisions discussion
- absolute paths
	- https://stackoverflow.com/questions/7653483/github-relative-link-in-markdown-file
		- maybe combine obsidian templates with this

# anki decisions discussion
- image resizing
	- essentially i want my images to fill out the full horizontal width of card, unless this magnifies the image by more than 2x (aka stop once it hits 2x magnification)
		- aka `width=100%` doesnt work for me, bc it causes rly small images to get fully magnified until they hit the width, so it's way too big
	- seems `zoom` is supported by every browser except firefox, so nbd using this for now; bc zoom immediately work, `scale(2)` didn't immediately work lol. so let's just use zoom. switch to scale if it becomes a problem in the future
		- https://stackoverflow.com/questions/10217639/how-to-double-an-image-size-in-html-using-only-css
		- https://developer.mozilla.org/en-US/docs/Web/CSS/zoom#browser_compatibility
		- the important thing is whether the anki renderer supports it (which it does)


# fun
- youtube vids that make me want to study again
	- [Tom Vs Time Episode 2 - The Mental Game](https://www.youtube.com/watch?v=qkFZybpxNtk&t=332s)
	- [Celebrating Luke Kuechly, Smartest Linebacker to Play the Game | NFL Films Presents](https://www.youtube.com/watch?v=cbsRZDxlYEQ&t=197s)
	- [Baldy's Breakdowns: The Film Behind Cooper Kupp's Viral Touchdown Analysis](https://www.youtube.com/watch?v=7LXG0h5Txis)
	- [LeBron's Photographic Memory](https://www.youtube.com/watch?v=HG6M2xQZvj0)
	- [Sean McVay Literally Remembers Every Play of His Coaching Career 🤯| Simms & Lefkoe: The Show](https://www.youtube.com/watch?v=IjlfQBQk_kg)
