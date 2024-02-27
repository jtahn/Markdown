# todo
- urgent
	- i don't understand the main solutions; aka either the 'simple inefficient' ones and/or the 'important efficient' ones
		- z
	- revision ideas after review (check voice memos/notebook for edits)
		- z
	- whatever is next on neetcode 150 (https://neetcode.io/practice); understand main solutions, then create card in anki
		- [424](424.md)
		- [567](567.md)
		- [76](76.md)
		- [239](239.md)
		- [155](155.md)
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

# purpose
- i guess randos can browse the solutions if they want
- this is mainly for me/judy/damini/(anyone else who wants my anki deck), bc imo you need to repeatedly reread these solutions, and it's easiest to set this up via anki
- anki:
	- why
		- to schedule readings of these solutions (and for myself, to schedule revisions as i inductively/indirectly learn/memorize this and make connections)
		- see below, but i can set up a reviewing/revising system via anki that makes both processes soo easy/lazy
	- the anki cards use https://jtahn.github.io/emgithub/ (fork of emgithub) to embed the md file onto the back of the anki card
	- briefly, this setup means that:
		- reading is incredibly easy bc it's scheduled for me
		- can connect a bluetooth gaming controller and assigns keys for scroll a little/lot up/down, again/hard/good, undo
			- so i can just sit back and click away as i read my cards (on an ultrawide monitor, aligned vertically)
		- very easy to revise cards: use obsidian to quickly edit markdown
			- markdown significantly more convenient to work with than the anki editor, particularly:
				- code snippet environments (and basic highlighting) using ticks
				- mathjax support using typical usd delimiters (instead of janky cmd+m, m)
				- nested lists
				- headings
			- also i'm just paranoid of ankiweb losing my notes
- why 'reading' cards instead of 'recall'
	- simply, atm i have no clue how to make good/effective recall cards out of this stuff
	- even if i just understand something and dont intentionally try to commit it to memory, i personally seem to have pretty decent recall...probly exactly bc i understand it? i'm sure there's some studying theory here, but i'm too busy to look that up rn..more importantly, i dont think that theory matters because of the next point
	- i enjoy reading cards bc they're easy and i'm lazy, so i actually consistently do this
		- also, revising a reading card is easy; revising recall cards is a nightmare atm (bc they're all broken up and stuff, and you need to phrase things in terms of questions...etc etc)
		- aka this is the only workflow i actually consistently do atm, and i can't really see how any 'recall' method wouldn't share similar problems as my 'recall' attempt i made in the past (and couldn't stick to)
	- my plan is just...at some point a few years from now, maybe i'll master the material enough to the point where i realize how to make recall cards out of this. but for now, reading seems to work good, so lets just do that
- btw, why vertical ultrawide monitor:
	- i extend reading cards to pages from clrs/skiena, and screenies of webpages (wikipedia,realpython,stackexchange)
- i need to repeatedly reread this stuff, bc the interview time constraints essentially makes it seem like i need to essentially memorize these (patterns)
	- point is, i don't actually know how to make/revise proper recall cards, or even stick to a study plan involving those cards
	- so i'm just gambling on the reading cards being enough, provided i reread them constantly
- more accurately, i need to know/memorize these patterns so well that when it comes to answer questions, it's almost like i'm "reacting" on instinct/intuition. i mean it's basically just like how i solve all other problems in math, it's just that in these interviews, i don't have the luxury of time
	- so just do the equivalent of what i did studying for math gre, just do literally every odd problem in the textbook; and then do them again
		- i never tried to memorize every problem...i just repeatedly did them. same thing probly applies here to some degree
	- aka (attempt) do every leetcode problem bc there are solutions; and then repeatedly do them
- anecdote/aesthetic/motivation
	- think of 'anki re-reading' like nfl players 'film study'...these guys need to know and process stuff so fast that's it's essentially memory + reacting on intuition/instinct too
	- there's absolutely zero reason why i (mental career) (if i want to be 'elite') should ever spend less time doing 'after hours' 'film study' compared to brady/reed/kuechly/kelce/kupp/etc (ie even tho elite in physical career; it should motivate me to work harder if they're spending more time doing academic/mental work than i am)
		- [Tom Vs Time Episode 2 - The Mental Game](https://www.youtube.com/watch?v=qkFZybpxNtk&t=332s)
		- [Secondary Squad Dinner & Watching Film - Best of Ed Reed | Baltimore Ravens](https://www.youtube.com/watch?v=ORnFvZNQ5kE)
		- [Celebrating Luke Kuechly, Smartest Linebacker to Play the Game | NFL Films Presents](https://www.youtube.com/watch?v=cbsRZDxlYEQ&t=197s)
		- [why don’t teams double cover Travis Kelce?](https://www.youtube.com/watch?v=3w704PjSYt8&t=940s)
		- [Baldy's Breakdowns: The Film Behind Cooper Kupp's Viral Touchdown Analysis](https://www.youtube.com/watch?v=7LXG0h5Txis)
- i need a system/process that i'm happy to do for hours, even after i'm tired from research/work/etc; this is that process:
	- reading cards for sure
	- revising cards, almost for sure
	- drilling/muscle memory cards: i think i can squeeze in there
	- recall: has not worked in the past. might work in the future once i 'master' all this stuff




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
	- https://leetcodethehardway.com/
	- https://algo.monster/liteproblems/271
		- replace 271 with whatever number the problem is
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
			- this guy seems famous, but actually i'm generally not a fan, he's addicted to writing unreadable code bc he just slaps way too many language specific things/tricks into it in order to cut down the number of lines, that don't seem to actually make the code any more efficient
			- basically he's inadvertently convincing me that oneliners are terrible, and i shouldnt use too many esoteric functions or going inception style and nesting dozens of generators/comprehensions
				- just stick to popular functions; when the solutions are already this short, there's nothing wrong with loops and multiline conditional statements, bc everyone knows what you're doing and it's way easier to read, even if you're familiar with oneliner if/else assignments
				- even if you're aware of how increment operators behave (ie ocurring before or after assignment); it's just completely unecessary brainpower to use when you're trying to read a solution; or keeping track of all the generators that are nested inside each other; its just far easier to read when it's just indented
	- youtube
		- neetcode
		- https://www.youtube.com/@cheatcodeninja/videos
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
	- when using relative path: if you move files around, it doesnt update the paths 
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