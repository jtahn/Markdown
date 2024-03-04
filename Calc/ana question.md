
![](../!assets/attachments/Pasted%20image%2020240304154132.png)


> we are just supposed to look for continuity between [a,b] and differentiability in (a, b) ( (through the f(b)-f(a) / (b-a) = f '(c) equation)

perfect exactly

> I was wondering how we are supposed to confirm continuity. Are we just supposed to see if the original equation has a denominator or anything that will make it undefined? 


- checking for undefined (ie valid denominators) is definitely part of it
	- though you’ll notice some of these are piecewise functions that have been defined so that the denominator skips the 'trouble points' (ie #12)
	- (you will need to do more for piecewise: see below)
- for piecewise:
	- the general strategy for checking continuity:
		1. check that each ‘function piece is continuous”
			- this part, you can skip if the pieces are “obviously" continuous; ie if they’re polynomials or trig, etc
		2. check for continuity at the points where the pieces meet
			- (this is the important part)
			- so for #12, this is at x=0.
				- aka you need to check for continuity at x=0: which means:
					1. the limit exists (the left and right limits exists and are equal): $$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x)$$
					2. the limit equals the point: $$\lim_{x \to 0} f(x) = f(0)$$
			- might be worth reviewing/skimming:
				- 2.4: one sided limits
				- 2.5: continuity
	- to check differentiability:
		- check each function piece is differentiable
		- check for differentiability where the pieces meet
			- (use limit definition of derivative (pg 125))
			- you will need to use one-sided limits here as well
			- see pg128 (3.2 example 4) for how this works for piecewise



This was pretty long…lmk if you still have questions/or is confusing..if entire thing is confusing lmk too, i can try to find a different way/resource/video to explain it 
