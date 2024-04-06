- complexity wrt constraints: technically correct vs “spirit of the problem”
	- problem constraints often involve some finite bounds, that result in certain techniques technically having smaller space complexity than ‘intended’
		- ie that bound should really be considered ‘unbounded’; but it is probably a finite number so that ppl using other languages don’t have to clutter their code with error handling routines (ie for overflow errors), and can instead just focus on the ‘meat’ of the problem
- brownie points during interview
	- point out when these constraints technically have an important effect on complexity of a technique
- but in actual writeups: define complexity in terms of spirit of the problem


- examples where this comes up:
	- 167: two pointer vs hashing
		- one of these solutions is technically O(1) because of the constraints (finite set of numbers), but it doesn’t seem to be the spirit of the problem
	- daily temps: i do think it is intended that we should use the fact that temp range is bounded/finite
		- because i think spirit of the problem IS to realize that direction of iteration matters


