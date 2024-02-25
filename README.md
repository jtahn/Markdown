# todo
- 53
- 36,271,128,167,15,11,42,
- move a few more from anki into obsidian
- then delete the description and solution fields on anki cards


# references
- most stuff here isn't original
- explained solutions
	- https://leetcodethehardway.com/
	- https://algo.monster/liteproblems/271
		- replace 271 with whatever number the problem is
	- leetcode forum users
		- https://leetcode.com/archit91/
		- https://leetcode.com/its_vishal_7575/
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
	- 



# why this setup
- embedded markdown files
	- very easy to edit in obsidian. in particular:
		- lists with multiple levels of nesting
		- mathjax
		- headings
		- horizontal lines
	- versus in anki, this stuff is either really annoying bc wonky shortcuts (nested lists, mathjax) or impossible without add-ons (i'm not a fan of add-ons bc they seem to break constantly bc updates, and then take awhile to get fixed...and atm no time to coding/maintain my own)
		- to see the nested lists and indenting shortcuts, hover over the text-adjust menu; then the indenting adjustments menu will show up, and hover over that
	- can have (multiple) people polishing the files, but it doesn't affect other people's review schedule
		- polishing is fine, bc main content in the file should be pretty obvious from the beginning and will be unaffected
			- bc these are mostly all just 'reading' cards; not recall cards (which might need to be changed significantly as i realize better ways to break things up, or figure out that certain cards are unecessary)
		- in particular, the decks that use this embedded stuff will likely be continuously revised over the span of multiple years, possibly a decade...the plan is for judy/damini to use this deck too, which means i need some kind of system where it's very easy to edit the cards without affecting their reviews
- 'requiring internet' isn't that big a con, bc i'm basically always connected to internet
	- esp considering this setup will basically only be used for leetcode
- imo: only do this setup for cards where i need a combo of lots of screenies + bulleted text and/or headings
	- aka things where there's multiple different answers, possibly long
	- for my career, leetcode really seems like the only thing that fits this. i don't really think math fits here. bc thing with leetcode is that you do want multiple solutions, bc the interviews apparently like it if you discuss multiple solutions, even if there's a clear "best" one
	- stuff like textbook/webpage screenies (even when they span multiple pages), where there isn't really a need for headings + nested lists: just keep that purely in anki
- it's worth having a dedicated setup for leetcode, bc of how important it is for my career. it's arguably the most important thing.
	- it's central for my first few job hops
	- early part of career is probly the most stressful
	- early part of career might be most important? ie if i have great start, then it makes the rest of career inevitable. idk.
- why this approach better than resources already out there
	- issues with leetcode forum solutions:
		- solutions that don't have 'correct'/convincing intuition; this makes it harder to understand/'memorize'
		- don't use 'offical' jargon/terminology; this makes it harder to look stuff up in a reference if you want more info
	- issues with neetcode
		- videos are helpful for initial understanding, but not efficient for reviewing
	- for myself: this seems like by far the most convenient way to revisit and revise stuff
		- when revisiting: no need to sit at computer; can just lay back with a remote and click away
		- for revising: there's only one files to worry about per solution (i guess there's also the coding files, but this is still very low headaache)
			- as mentioned earlier, markdown is far easier to revise than the anki text entry boxes
- why reading instead of traditional recall
	- i don't even understand all the solutions yet, or have all the solutions in a convenient place; let's just get that done first
	- idk how to even make cards for this: bc leetcode requires explaining everything, so i kind of do want everything
	- i'm trusting the inductive process
	- i quit after trying traditional recall; it's just way too much effort; vs reading is so easy, i find this very funny and easy to do consistently
- basically
	- anki is best bc it will auto schedule/shuffle stuff for me, and i can control it with a remote aka i can just lounge back and click away
		- it's true that there are some pretty good sources for info (some of the posters in leetcode forums; neetcode vids); but thing is, they don't cover every problem that i want to cover, and also it'd be really annoying to have to scroll around solutions and find a good one every time; it's far more convenient to them in a file that i can revise/update very easily
			- this is where obsidian + vscode come in, and then having a way to embed github files into my anki cards
	- aka this makes both the reviewing and revising process as painless/simple/headache free as possible



# resources
- https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax
- https://help.obsidian.md/Editing+and+formatting/Embed+web+pages
- https://obsidian.md/account
	- dang why didn't i lock in early bird discount for Publish




# Obsidian settings that I changed for this vault
- recording them here in case i need to set this up again
- these are necessary so that images show up when viewing markdown files on github.com; so them emgithub sees them too when it embeds them into anki cards
	- ![](!assets/attachments/Pasted%20image%2020240224004117.png)
	- ![](!assets/attachments/Pasted%20image%2020240224004445.png)

- these are just so the github folder/file structure is cleaner; mimics my personal obsidian
	- ![](!assets/attachments/Pasted%20image%2020240224004123.png)
- settings i accidentally stumbled on, but probly have toggles in the settings
	- when i moved an attachment file, it asked me if i wanted the app to always update the links, and i said yes
	- when i tried to delete a file, i checked dont remind
		- ![](!assets/attachments/Pasted%20image%2020240224005640.png)



# why python
- https://www.techinterviewhandbook.org/programming-languages-for-coding-interviews/
	- Most companies let you code in any language you want - the only exception I know being Google, where they only allow candidates to pick from Java, C++, JavaScript or Python for their algorithmic coding interviews.
- there's no point putting in stuff for cpp/java in these solutions; you can pick whatever language you want, python is most efficient and has best readability and is fastest to type. aka it will be the fastest language for reading cards and also for drilling cards. and probly recall cards as well. cpp seems cool bc competitive programming, but there's no point studying this (same with project euler i'm guessing?) the interviews are in leetcode, there's thousands of leetcode questions...just do leetcode questions. no need to add cards for competitive programming or project euler. 
	- large beauty of python is that there's basically no need to have pseudocde; bc python seems barely more lines
- again, the whole point of this is to pass interviews. most urgent. after leetcode, seems the next thing to study is systems and c/cpp (NOT competitive programming), to get those lower level programming jobs at elite finance firms (hrt, jane street, etc).  possibly also 'in depth python' as well, iirc HRT has a job for that. 
- by prepping for interview, i'm probly alrdy going to be good enough at my job as long as i work hard and listen and friendly. so even tho 'being good at my job' isn't urgent, i'm not saying it's unimportant. i'm just saying it's not urgent to directly prep this. what's most important is having high TC, bc my family is most important; not the company i work for. i doubt they care about individual job performance past a certain threshold; and also, me being 'better' at topics will very likely barely translate into tangible performance improvements, bc i'll alrdy be so good. obviously this is something i'm still gonna do bc i find learning fun, but the point is it's not urgent
- aka remember goals, in order of urgency (which thus inform urgent topics, in order of urgency)
	- pass swe interview at faang
		- leetcode
		- necessary python
		- necessary clrs/skiena
	- pass swe interview at hrt/jane/etc
		- all of the above
		- systems/os/etc
		- cpp
	- pass quant interview at hrt/jane/etc
		- all of the above
		- brain teasers
		- combinatorics
		- necessary linalg
	- pass senior/staff swe interviews
		- all of the above
		- tbh i'm not sure at this point...
		- system design
		- networks
	- job performance (or kinda helpful/tangentially related to interview prep)
		- clean code
		- thorough clrs/skiena/etc
		- competitive programming, project euler
		- thorough linalg
		- thorough grad numerical analysis, in the spirit of trefethen
			- stuff like golub textbook
			- awareness of common tools in numerical analysis (like fft, wavelets, etc)
		- tools in swe
			- awareness of everything
			- thorogouh of the important stuff
			- this is very vague, but i mean stuff like: adding wiki articles of jpeg algo. tho actually, i bet this type of stuff shows up in algo textbooks
	- thus topics that are not urgent whatsoever to put into cards
		- all other grad math

