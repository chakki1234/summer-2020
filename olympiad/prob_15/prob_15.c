#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int main()
{
    int num = 2013, sum, len, start, flag = 0;
    
    for(int a = 1; a < num; ++a)
    {
        for(int k = 1; k < num; ++k)
        {
            sum = k*((2*a) + k -1)/2;

            if(sum == num && flag == 0)
            {
                len = k;
                start = a;
                flag = 1;
            }
        }
    }
    printf("The length of consecutive integers is %d and start value is %d", len, start);
    return 0;  
}