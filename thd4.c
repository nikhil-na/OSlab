#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int max_val;
int min_val;
int array[10];
void *generate_array(void *arg)
{
    srand(0);
    for (int i = 0; i < 10; ++i)
    {
        array[i] = rand() % 1000;
    }
    pthread_exit(0);
}

void *max_value(void *arg)
{
    max_val = array[0];
    for (int i = 1; i < 10; ++i)
    {
        if (array[i] > max_val)
        {
            max_val = array[i];
        }
    }
}

void *min_value(void *arg)
{
    min_val = array[0];
    for (int i = 0; i < 10; ++i)
    {
        if (array[i] < min_val)
        {
            min_val = array[i];
        }
    }
}

int main()
{
    pthread_t t1, t2, t3;
    pthread_create(&t1, NULL, &generate_array, NULL);
    pthread_create(&t1, NULL, &max_value, &generate_array);
    pthread_create(&t1, NULL, &min_value, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    printf("Maximum value: %d\n", max_val);
    printf("Minimum value: %d", min_val);
}