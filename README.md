# ToC[^1]
[^1]: starts with neetcode150; then continues with grind169 (sorted by topic, then difficulty)

## Arrays & Hashing
1. [217](LeetCode/217.md)
2. [242](LeetCode/242.md)
3. [1](LeetCode/1.md)
4. [49](LeetCode/49.md)
5. [347](LeetCode/347.md)
6. [238](LeetCode/238.md)
7. [36](LeetCode/36.md)
8. [271](LeetCode/271.md)
9. [128](LeetCode/128.md)

## Two Pointers
10. [125](LeetCode/125.md)
11. [167](LeetCode/167.md)
12. [15](LeetCode/15.md)
13. [11](LeetCode/11.md)
14. [42](LeetCode/42.md)

## Sliding Window
15. [121](LeetCode/121.md)
16. [3](LeetCode/3.md)

## Stack
21. [20](LeetCode/20.md)


## Binary Search
28. [704](LeetCode/704.md)

## Linked List
36. [21](LeetCode/21.md)
41. [141](LeetCode/141.md)

## Trees
46. [226](LeetCode/226.md)
49. [110](LeetCode/110.md)
52. [235](LeetCode/235.md)

## Heap / Priority Queue
66. [973](LeetCode/973.md)

## Greedy
122. [53](LeetCode/53.md)

## Intervals
130. [57](LeetCode/57.md)


## grind169
[733](LeetCode/733.md)
[542](LeetCode/542.md)
[232](LeetCode/232.md)
[278](LeetCode/278.md)
[383](LeetCode/383.md)




# Todo
- urgent
	- i don't understand the main solutions; aka either the 'simple inefficient' ones and/or the 'important efficient' ones
		- z
	- revision ideas after review (check voice memos/notebook for edits)
		- z
	- whatever is next on neetcode 150 (https://neetcode.io/practice); understand main solutions, then create card in anki
		- [424](LeetCode/424.md)
		- [567](LeetCode/567.md)
		- [76](LeetCode/76.md)
		- [239](LeetCode/239.md)
		- [155](LeetCode/155.md)
		- [150](LeetCode/150.md)
		- [[LeetCode/22]]
		- [[LeetCode/739]]
		- [[LeetCode/853]]
		- [[LeetCode/84]]
		- [[LeetCode/74]]
		- [[LeetCode/875]]
		- [[LeetCode/153]]
		- [[LeetCode/33]]
		- [[LeetCode/981]]
		- [[LeetCode/4]]
		- [[LeetCode/206]]
		- [[LeetCode/143]]
		- [[LeetCode/19]]
		- [[LeetCode/138]]
		- [[LeetCode/2]]
		- [[LeetCode/287]]
		- [[LeetCode/146]]
		- [[LeetCode/23]]
		- [[LeetCode/25]]
		- [[LeetCode/104]]
		- [[LeetCode/543]]
		- [[LeetCode/100]]
		- [[LeetCode/572]]
		- [[LeetCode/102]]
		- [[LeetCode/199]]
		- [[LeetCode/1448]]
		- [[LeetCode/98]]
		- [[LeetCode/230]]
		- [[LeetCode/105]]
		- [[LeetCode/124]]
		- [[LeetCode/297]]
		- [[LeetCode/208]]
		- [[LeetCode/211]]
		- [[LeetCode/212]]
		- [[LeetCode/703]]
		- [[LeetCode/1046]]
		- [[LeetCode/215]]
		- [[LeetCode/621]]
		- [[LeetCode/355]]
		- [[LeetCode/295]]
- not as urgent
	- don't understand a qualitatively different technique (but probly not urgent bc it's not strictly better)
		- [53](LeetCode/53.md) divide and conquer
		- [36](LeetCode/36.md) logn space (claimed)
	- extremely rough (but i understand it)
		- [42](LeetCode/42.md) stacks
		- [973](LeetCode/973.md) heaps
		- [733](LeetCode/733.md) dfs
		- [704](LeetCode/704.md) binary
		- [128](LeetCode/128.md) hashing
# meta
- solving similar looking problems seems INCREDIBLY important if they actually have qualitatively different 'optimal' techniques
	- examples
		- 42 trapping rain water: monotone stack is not optimal (use two pointers), but is apparently optimal in other similar problem, ie "Largest Rectangle in Histogram"
		- '973 k closest points to origin' problem, we dont have the bucket sort technique; but we have that for '347 top k frequent elements'
			- bc bounded and discrete range of buckets
	- i should understand what is different about these problems
		- ie what prevents certain solutions
- there are sometimes qualitatively different solutions that are objectively worse bc its worse intuition.
	- usually means its not actually qualitatively different...it's actually similar to a 'better' solution, but they introduce an observation/intuition that makes things more confusing..no need to save these

# references
- most stuff here isn't original
- explained solutions
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