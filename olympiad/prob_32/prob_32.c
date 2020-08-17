#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int main()
{
    int no_of_men = 9, no_of_woman_each_man_danced = 4, no_of_man_each_woman_danced = 3;

    int total_no_of_dances = no_of_men*no_of_woman_each_man_danced;
    int no_of_women = total_no_of_dances/no_of_man_each_woman_danced;

    printf("The value is %d", no_of_women);
    return 0;  
}

