#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int main()
{
    int m = 0, n = 0, flag_m = 0, flag_n = 0, i = 1, sum;
    

    while(flag_m == 0 || flag_n == 0)
    {
        sum = i * (i + 1) / 2;
        if(sqrt(sum) == (int)sqrt(sum))
        {
            if(i%2 == 1 && flag_m == 0)
            {
                m = i;
                flag_m = 1;
            }

            if(i%2 == 0 && flag_n == 0)
            {
                n = i;
                flag_n = 1;
            }
        }
        i+=1;
    }

    printf("The sum is %d", m + n);
    return 0;  
}