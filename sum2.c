#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define NUM_THREADS 5

void *print_thread_id(void *arg)
{
    printf("Thread ID: %ld\n", (long)pthread_self());
    return NULL;
}
int main()
{
    pthread_t thread_ids[NUM_THREADS];
    int i;
    for (i = 0; i < NUM_THREADS; i++)
        pthread_create(&thread_ids[i], NULL, &print_thread_id, NULL);
    for (i = 0; i < NUM_THREADS; i++)
        pthread_join(thread_ids[i], NULL);
    return 0;
}