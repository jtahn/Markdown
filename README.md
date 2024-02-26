# todo
- delete the description and solution fields on anki cards

# references
- most stuff here isn't original
- explained solutions
	- https://leetcodethehardway.com/
	- https://algo.monster/liteproblems/271
		- replace 271 with whatever number the problem is
	- leetcode forum users
		- https://leetcode.com/hiepit/
			- this guy consistently seems the best
		- https://leetcode.com/archit91/
		- https://leetcode.com/its_vishal_7575/
		- https://leetcode.com/r0gue_shinobi/
		- https://leetcode.com/MarkSPhilip31/
	- have interesting perspectives
		- https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/
		- https://leetcode.com/stefanpochmann/
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



- there's currently a bug with relative paths (as of of 2/26/2024):
	- when using relative path: if you move files around, it doesnt update the paths 
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