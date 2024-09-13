#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

void *childfunc(void *p)
{
    printf("child ID is---> %d\n", getpid());
    pthread_exit(0);
}

int main()
{
    pthread_t child1, child2;
    pthread_create(&child1, NULL, childfunc, NULL);
    pthread_create(&child2, NULL, childfunc, NULL);
    printf("Parent ID is ---> %d\n", getpid());
    pthread_join(child1, NULL);
    pthread_join(child2, NULL);
    printf("No more children!\n");
}