#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

void *threadOne(void *arg)
{
    for (int i = 0; i <= 100; i += 2)
    {
        printf("%d\t", i);
    }
    pthread_exit(0);
}

void *threadTwo()
{
    for (int i = 1; i < 100; i += 2)
    {
        printf("%d\t", i);
    }
    pthread_exit(0);
}

int main()
{
    pthread_t t1, t2;
    pthread_create(&t1, NULL, &threadOne, NULL);
    pthread_create(&t1, NULL, &threadTwo, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
}