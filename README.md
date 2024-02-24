# todo
- 53
- 238,36,271,128,167,15,11,42,
- move a few more from anki into obsidian
- then delete the description and solution fields on anki cards


# why this setup
- embedded markdown files
	- very easy to edit in obsidian. in particular:
		- lists with multiple levels of nesting
		- mathjax
		- headings
		- horizontal lines
	- versus in anki, this stuff is either really annoying bc wonky shortcuts (nested lists, mathjax) or impossible without add-ons (i'm not a fan of add-ons bc they seem to break constantly bc updates, and then take awhile to get fixed...and atm no time to coding/maintain my own)
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