#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int factorial(int num)
{
    int prod = 1;
    for (int i=1; i <= num; ++i)
        prod = prod * i;
    return prod;
}


int comb(int total, int choose)
{
    int result = factorial(total) / (factorial(choose)*factorial(total - choose));
    return result;
}

int sum_of_powers_of_2(int num)
{
    int sum = 0;
    for(int i=0; i< num; ++i)
        sum = sum + (int)pow(2, i);
    return sum;
}

int main()
{
    int max_limit = 64, num_of_ones = 3, flag = 0;
    
    int no_of_bits = log2(64);
    int no_of_selections = comb(no_of_bits, num_of_ones);
    int total_no_of_ones_selected = num_of_ones * no_of_selections;
    int no_of_times_each_bit_selected = total_no_of_ones_selected / no_of_bits;
    int sum_of_all_such_nos = no_of_times_each_bit_selected * sum_of_powers_of_2(no_of_bits);
    
    printf("The sum is %d", sum_of_all_such_nos);
    return 0;  
}