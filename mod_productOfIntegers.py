n = int(input('Enter the number of elements: '))

prod=1
count=0

for i in range(2,n):
    prod*=i
    if prod%n==1:
        count=i
if count==0:
    count=1
print('The length is: ',count)




'''
You are given an integer N.

You have to choose a set of integers S from the range [1, N-1] such that the product of integers in S is 1 modulo N. This means that if N=5, we can choose set S = [1,2,3] as the product is 6 and 6 modulo 5 is 1.

Find the length of the biggest set S you can choose.

Input Format

The first line contains an integer N, denoting the given integer.

Constraints

1<=N<= 5 * 10^5

Sample Input 1

7

Sample Output 1

5

Explanation:

We can choose set (1,2,3,4,5). Here product = 120 which mod 7 is 1

Sample Input 2

5

Sample Output 2

3

Explanation:

Here we can choose set (1,2,3) where product is 6 and 6 mod 5 =1

Sample Input 3

4

Sample Output 3

1

Explanation

Here we choose only (1)

 

C Solution

#include <stdio.h>

int fact(int num)

{

    if(num>0)

    return num * fact(num-1);

    else

    return 1;

}

int main()

{

    int N,i;

    scanf("%d",&N);

    int a[N-1];

    for(i=0;i<N;i++ )

    {

        a[i]=i+1;

    }

    for(int x =N-1;x>=1;x--)

    {

        int y = fact(x);

        if (y%N == 1)

        {

            printf("%d",x);

            break;

        }

    }

    return 0;

}

 

 

C++ Solution

#include <iostream>

using namespace std;

int fact(int num)

{

    if(num>0)

    return num * fact(num-1);

    else

    return 1;

}

int main()

{

    int N,i;

    cin>>N;

    int a[N-1];

    for(i=0;i<N;i++ )

    {

        a[i]=i+1;

    }

    for(int x =N-1;x>=1;x--)

    {

        int y = fact(x);

        if (y%N == 1)

        {

            cout<<x;

            break;

        }

    }

    return 0;

}

 

Java

import java.util.Scanner;

public class Main

{

    public static int fact(int num)

    {

        if(num>0)

        return num * fact(num-1);

        else

        return 1;

    }

 

public static void main(String[] args)

{

Scanner sc = new Scanner(System.in);

int N,i;

N = sc.nextInt();

int a[] = new int[N];

for(i=0;i<N;i++)

   {

     a[i]=i+1;

   }

for(int x =N-1;x>=1;x--)

        {

            int y = fact(x);

            if (y%N == 1)

            {

                System.out.print(x);

                break;

            }

        }                            

   }

}

 

Python

N=int(input())

a=[]

 

def fact(num):

    if num>0:

        return num * fact(num-1)

    else:

        return 1

 

for i in range (0,N-1):

    a.append(i+1)

for x in range (N-1,0,-1):

    y=fact(x)

    if(y%N)==1:

        print(x)

        break
'''