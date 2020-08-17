#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int sum_of_cubes_of_digits(int digits[], int len)
{
    int sum = 0;

    for(int i=0; i<len; ++i)
        sum = sum + (int)pow(digits[i], 3);

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

    return sum_of_cubes_of_digits(temp, len);
} 


int main()
{
    int first_term = 2014, term_req = 2014, temp = first_term;

    for(int i=1; i<term_req; ++i)
        temp = printDigit(temp);

    printf("The value is %d", temp);
    return 0;  
}

