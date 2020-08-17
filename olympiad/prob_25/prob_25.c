#include <stdio.h>
#include <math.h> 
#include <stdlib.h>

int main()
{
    float time_to_walk_and_ride = 3 + 3.0/4.0, time_to_ride_both_ways = 2 + 1.0/2.0;
    
    float time_to_ride_single_way = time_to_ride_both_ways/2;
    float time_to_walk_single_way = time_to_walk_and_ride - time_to_ride_single_way;
    float time_to_walk_both_ways = time_to_walk_single_way * 2;

    printf("The value is %f", time_to_walk_both_ways);
    return 0;  
}
