![](!assets/attachments/clappingbear.gif)   

# shortcuts
- index of leetcode writeups: [README](LeetCode/README.md)








---

# Meta
- [todo, macro](_private/Drafts/todo,%20macro.md)
- why markdown (instead of vscode latex or anki editor)
	- max convenience with all of:
		- mathjax, code snippets, nested lists (multiple indents), headings, quotes
			- for short informal stuff, all this stuff is helpful
				- quick to skim
				- easy to revise
				- (and no real cons exactly bc it's for short informal stuff)
		- gifs (helpful for diagrams/visualizations)..see the top
- why obsidian
	- immediately insert screenies
		- (note you can do this in vscode as well, with Paste Image extension)
	- turns wikilinks into relative paths, and this is actually p helpful for github viewing/embedding
	- even my pdfs have backlinks...this seems like an incredibly useful feature in the future
		- ie if i want to remind myself of specific leetcode problems that are examples of a concept in CLRS/skiena
- this repo is for md files that i need to be publicly available. examples:
	- [Calc TA stuff](_private/Calc/README.md)
		- rough math/cs explanations for students
		- obsidian export to pdf is wonky, the md file itself looks better
	- [LeetCode](LeetCode/README.md)
		- solution writeups to embed onto anki cards[^embed]


[^embed]:  Cards need a `{{number}}` field; then paste this code into the card template: ```<script src="https://jtahn.github.io/emgithub/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fjtahn%2FMarkdown%2Fblob%2Fmain%2FLeetCode%2F{{number}}.md&style=default&type=markdown&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on"></script>```






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


- actually i'm now going to switch to switch to wikilink
	- i will convert most images into mermaid, so embedding images isn't usually necessary
	- the ones that are too complicated to convert: i'll keep as "markdown links with relative paths"



---

![[!assets/attachments/Pasted image 20240427223421.png]]


---


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




## plugin settings

![[!assets/attachments/Pasted image 20240508035229.png]]




# Device settings
- bc i do a lot of technical writing, ie variables:
	- means i should turn off auto-capitalization on my DEVICE
		- obsidian's spellcheck (in editor settings) doesn't auto-capitalize
	- ie otherwise, when i type `i+1` it will autocorrect to `I+1`
	- so on chromebook:
		- settings > device > keyboard > change input settings > English > physical keyboard > turn off autocorrection



# markdown/obsidian 
- https://docs.github.com/en/get-started/writing-on-github
	- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- just use double space for line break
	- https://www.markdownguide.org/basic-syntax/#line-break-best-practices
	- https://stackoverflow.com/questions/36583502/how-to-force-a-linebreak
		- Just one thing: don't do a global trim on trailing spaces, as is often habit for source code, otherwise you'll lose important formatting.
- code snippets
	- https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Code+blocks
		- https://prismjs.com/#supported-languages
- linking to headings
	- https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link+to+a+heading+in+a+note
	- on creation: works for markdown links, not just wikilinks
		- don't use obsidian automplete suggestions for the file name
		- seems you need to type in the full filename, then type a hashtag symbol; then obsidian will show suggestions to autocomplete the heading (which you can use)
- https://www.tablesgenerator.com/markdown_tables#
- quotes
	- [Basic formatting syntax - Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Quotes)
	- [Basic writing and formatting syntax - GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#quoting-text)
	- callouts/alerts
		- use `[!note]` bc its compatible with both obsidian and github
		- [Callouts - Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Callouts)
		- [Basic writing and formatting syntax - GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)


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
	- [CJ Stroud Breaks Down His OWN Game Film](https://www.youtube.com/watch?v=D2t1B2Ev4nY&t=66s)
	- [LeBron's Photographic Memory](https://www.youtube.com/watch?v=HG6M2xQZvj0)
	- [Sean McVay Literally Remembers Every Play of His Coaching Career 🤯| Simms & Lefkoe: The Show](https://www.youtube.com/watch?v=IjlfQBQk_kg)




![](!assets/attachments/HUHrabbit.gif)