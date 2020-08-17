#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

float cal_func(float num) 
{ 
    int is_int = 0;

    float ans = (8 * num)/(9999 - num); 
    if((int)ans == ans)
        is_int = 1;
        
    return is_int;
} 


int main()
{
    float start_value = (float)1, end_value = (float)2014;
    int int_num = 0;

    for(int i=start_value; i<=end_value; ++i)
        if(cal_func(i) == 1)
            int_num+=1;

    printf("The value is %d", int_num);
    return 0;  
}

