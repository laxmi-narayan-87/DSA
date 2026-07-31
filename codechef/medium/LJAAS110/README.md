# LJAAS110

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Print factorial

Write a program that uses a do-while loop to find the factorial of a given input number.

### Sample 1:
Input
Output

```
5
```

```
120
```

### Explanation:

1 x 2 x 3 x 4 x 5 = 120

### Sample 2:
Input
Output

```
6
```

```
720
```

### Explanation:

1 x 2 x 3 x 4 x 5 x 6 = 720

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T10:52:39.711Z  

```java
import java.util.Scanner;

class Codechef
{
	public static void main (String[] args)
	{
		// your code goes here
		Scanner sc =new Scanner(System.in);
		int n=sc.nextInt();
		int fact=1;
		do{
		    fact=fact*n;
		    n-=1;
		}while(n>0);
		System.out.println(fact);

	}
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LJAAS110)