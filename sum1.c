#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int sum;                         /* this data is shared by the thread(s) */
void *threadRunner(void *param); /* the thread */
int main()
{
    pthread_t tid1; /* the thread identifier */
    long p;         // long integer
    printf("enter your number\n");
    scanf("%ld", &p);
    /* Create Thread1*/
    pthread_create(&tid1, NULL, threadRunner, (void *)p);
    /* Wait for thread1 to exit */
    pthread_join(tid1, NULL);
    printf("total sum = %d\n", sum);
}
/* Thread1 will begin control in this function */
void *threadRunner(void *param)
{
    int i;
    sum = 0;
    for (i = 1; i <= (long)param; i++)
    {
        sum += i;
        printf("in thread , i= %d\n", i);
    }
    printf("\n");
    pthread_exit(0);
}
