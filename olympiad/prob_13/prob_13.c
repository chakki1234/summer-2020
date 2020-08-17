#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int find(int temp[], int a, int len)
{
    int flag = 0;

    for(int i = 0; i < len; ++i)
    {
        if(a == temp[i])
        {
            flag = 1;
            break;
        }
    }

    return flag;
}


int main()
{
    int multiple_of = 15, no_of_elem_in_set = 1000, temp[no_of_elem_in_set], len = 0;
    
    for(int i = 1; i < multiple_of; ++i)
        {
            if(find(temp, i, len) == 0)
            {
                temp[len] = i;
                temp[len+1] = multiple_of - i;
                len+=2;
            } 
        }
        printf("The number of unique elements is %d", len / 2 + 1);
     
    return 0;  
}