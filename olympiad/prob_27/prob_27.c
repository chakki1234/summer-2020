#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int sum_of_even_digits(int digits[], int len)
{
    int sum = 0;

    for(int i=0; i<len; ++i)
        if(digits[i]%2 == 0)
            sum = sum + digits[i];

    return sum;
}


int printDigit(int N) 
{ 
    int temp[100], len = 0, remain; 
  
    while (N != 0) 
    { 
        remain = N % 10; 
        temp[len] = remain; 
        len++; 
        N = N / 10; 
    } 

    return sum_of_even_digits(temp, len);
} 


int main()
{
    int first_num = 1, last_term = 100, sum = 0;

    for(int i=first_num; i<=last_term; ++i)
        sum = sum + printDigit(i);

    printf("The value is %d", sum);
    return 0;  
}

