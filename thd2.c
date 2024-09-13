#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int glob_data = 5;
void *childfunc(void *p)
{
    printf("child here. Global data was %d.\n", glob_data);
    glob_data = 15;
    printf("child Again. Global data was now %d.\n", glob_data);
}
main()
{
    pthread_t child1;
    pthread_create(&child1, NULL, childfunc, NULL);
    printf("Parent here. Global data = %d\n", glob_data);
    glob_data = 10;
    pthread_join(child1, NULL);
    printf("End of program. Global data = %d\n", glob_data);
}