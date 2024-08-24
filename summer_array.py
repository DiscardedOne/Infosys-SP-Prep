n = int(input('Enter the number of elements: '))
a=[]
cost=0

for i in range(n):
    a.append(int(input(f"Element {i+1}: ")))

# First we need to understand which side is odd and which is even
# To do so we list all indexes of even elements and find the median index
# If the median index is on the left half of the list then even is left sided
# Doing this will grant us a smaller swap cost as we know which side the even cluster is heavy

def summerArray(n,a,cost):
    ind=[]
    for i in range(n):
        if a[i]%2==0:
            ind.append(i+1)

    summ=0
    for i in ind:
        summ+=i
    if len(ind)>0: median=summ//len(ind)
    else: return cost

    swap=False
    if median<=n//2: 
        # even is at the left side
        if a[-1]%2==0:
            for i in range(n-2,-1,-1):
                if not a[i]%2==0:
                    a[-1],a[i]=a[i],a[-1]
                    cost+=1
        while swap==False:
            for i in range(n-1):
                if not a[i]%2==0 and a[i+1]%2==0:
                    a[i],a[i+1]=a[i+1],a[i]
                    cost+=1
                    swap=True
            if swap==True: swap=False
            elif swap==False: break
    
    elif median>n//2:
        # even is at the right side
        # this block is same as above but with odd at the left side
        if not a[-1]%2==0:
            for i in range(n-2,-1,-1):
                if a[i]%2==0:
                    a[-1],a[i]=a[i],a[-1]
                    cost+=1
        while swap==False:
            for i in range(n-1):
                if a[i]%2==0 and not a[i+1]%2==0:
                    a[i],a[i+1]=a[i+1],a[i]
                    cost+=1
                    swap=True
            if swap==True: swap=False
            elif swap==False: break
    return cost

cost = summerArray(n,a,cost)        
print('The cost is: ',cost)










'''
You are given an array of size N.

An array A is considered a summer array if all the even values in A are on one side and odd values are on the other side.

You are allowed to swap two adjacent elements in A in one operation. Find the minimum swap operations required to change A into a summer array.

Input Format

The first line contains an integer N, denoting the number of elements in A. Each line i of the N subsequent lines (where 0 <= i <= N) contains an integer describing A[i].

Constraints

1<= N <= 10^5

1 <= A[i] <= 10^5

Sample Input 1

3

1

2

2

Sample Output 1

0

Explanation:

Here N=3 A= [1,2,2]. 0 swaps are required here as the odd number is already on the left and all the even number are already on the right

 

Sample Input 2

3

1

2

1

Sample Output 2

1

Explanation:

Here N =3 A=[1,2,1]. We can swap 2 at 1st index with 1 at  0th index after which A becomes [2,1,1] satisfying the condition.

 

Sample Input 3

6

1

2

3

4

5

6

Sample Output 3

3

Explanation:

Here N =6 A= [1,2,3,4,5,6] We have to swap 4 one time to right and 2 two times to right making A = [1,3,5,2,4,6]

 

C Solution
#include <stdio.h>

int main()

{

    int N,swap=0,i;

    scanf("%d",&N);

    int a[N];

    for(int i=0;i<N;i++)

    {

        scanf("%d",&a[i]);

    }

    for(i=0;i<N;i++)

    {

        for(int j=i;j<N-1;j++)

        {

            if (((a[j])%2==0) && (a[j+1]%2==1))

            {

                int temp = a[j];

                a[j] = a[j+1];

                a[j+1] = temp;

                swap++;

                break;

            }

        }

    }

    printf("%d",swap);

    return 0;

}

 

C++ Solution
#include <iostream>

using namespace std;

int main()

{

    int N,swap=0,i;

    cin>>N;

    int a[N];

    for(int i=0;i<N;i++)

    {

        cin>>a[i];

    }

    for(i=0;i<N;i++)

    {

        for(int j=i;j<N-1;j++)

        {

            if (((a[j])%2==0) && (a[j+1]%2==1))

            {

                int temp = a[j];

                a[j] = a[j+1];

                a[j+1] = temp;

                swap++;

                break;

            }

        }

    }

    cout<<swap;

    return 0;

}

 

Java
import java.util.Scanner;

public class Main

{

                public static void main(String[] args) {

                                Scanner sc = new Scanner(System.in);

                                int i,swap=0;

                                int N = sc.nextInt();

                                int a[] = new int[N];

        for(i=0;i<N;i++)

        {

            a[i]=sc.nextInt();

        }

        for(i=0;i<N;i++)

        {

            for(int j=i;j<N-1;j++)

            {

                if (((a[j])%2==0) && (a[j+1]%2==1))

                {

                int temp = a[j];

                a[j] = a[j+1];

                a[j+1] = temp;

                swap++;

                break;

                }

            }

        }

        System.out.println(swap);

 

                }

}

 

Python
N=int(input())

swap=0

a=[]

for i in range(0,N):

    a.append(int(input()))

for i in range(0,N):

    for j in range(i,N-1):

        if ((a[j]%2==0) and (a[j+1]%2==1)):

            temp=a[j]

            a[j] = a[j+1]

            a[j+1] = temp

            swap=swap+1

            break

print(swap)
'''