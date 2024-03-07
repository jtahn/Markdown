


- overflow
	- not an issue in python
		- (cite articles)
	- an issue for some other languages, i.e. java or cpp

	
# examples
- any kind of binary search technique
	- `left+right` might be above the int max
	- so to avoid it:
		- `mid = left + (right-left) // 2` instead of `mid = (left + right) // 2`
	- otherwise, can get stuck in an infinite loop, see [infinite loop caused by integer overflow](../Bugs/infinite%20loop%20caused%20by%20integer%20overflow.md)
- multiplying integers
	- [150. Evaluate Reverse Polish Notation](../LeetCode/150.%20Evaluate%20Reverse%20Polish%20Notation.md)
		- ![](../!assets/attachments/Pasted%20image%2020240307132226.png)
			- ![](../!assets/attachments/Pasted%20image%2020240307132236.png)
			- ![](../!assets/attachments/Pasted%20image%2020240307132257.png)
			- ![](../!assets/attachments/Pasted%20image%2020240307132350.png)
			- ![](../!assets/attachments/Pasted%20image%2020240307132400.png)






## [python - Integer overflow in Python3 - Stack Overflow](https://stackoverflow.com/questions/52151647/integer-overflow-in-python3)

![](../!assets/attachments/Pasted%20image%2020240304185849.png)

![](../!assets/attachments/Pasted%20image%2020240304185920.png)