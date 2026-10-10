# JPRACMCQ10 - Rating 238

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T10:57:56.138Z  

```java
import java.util.*;
import java.lang.*;
import java.io.*;


class Codechef
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
    		int x = sc.nextInt();
    		int y = sc.nextInt();
    		// write your code here
    		int sum = x+y;
    		if (sum>6){
    		    System.out.println("YES");
    		}
    		else{
    		    System.out.println("NO");
    		}
		}
		
	}
}

```

---

[View on CodeChef](https://www.codechef.com/problems/JPRACMCQ10)