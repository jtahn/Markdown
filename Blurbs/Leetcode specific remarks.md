# Purpose
- highlight things that will not work in the real world, but pass leetcode tests





---


# auto-imported modules
- technically on leetcode, you can just do `ceil()` instead of `math.ceil()`, bc the modules are auto-imported in leetcode..ie imagine leetcode has this line at the top of every solution: `from math import *`
- imo i should make it a habit to not only explicitly import modules, but also use their name
	- well maybe dont have to explicitly import; but definitely use the name
	- ie always do math.ceil() instead of just ceil()







# bad solutions that only work because of 'newly created memory address space'
- https://leetcode.com/problems/reorder-list/solutions/1007965/Most-Elegant-Recursive-C++-solution-(no-stack)-in-O(n)/
	- ![](../!assets/attachments/Pasted%20image%2020240311174721.png)
	- ![](../!assets/attachments/Pasted%20image%2020240311174658.png)


