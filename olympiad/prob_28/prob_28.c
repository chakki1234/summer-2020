#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int check_perfect_square(int num)
{
    int flag = 0;

    if(sqrt(num) == (int)sqrt(num))
        flag = 1;
    
    return flag;
}

int reverse_num(int num)
{    
    int remainder, rev_num = 0; 

    while (num != 0) 
    {
        remainder = num % 10;
        rev_num = rev_num * 10 + remainder;
        num /= 10;
    }
    return rev_num;
}

int main()
{
    int first_num = 10, last_term = 99, count = 0;

    for(int i=first_num; i<=last_term; ++i)
        if( check_perfect_square(reverse_num(i) + i) == 1)
            count+=1;
      
    printf("The value is %d", count);
    return 0;  
}

