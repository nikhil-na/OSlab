/* Program to create two children, one output integers from 1 to 50, the other from 51 to 100*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    int pid1, pid2;
    pid1 = fork();
    if (pid1 == -1)
    {
        perror("bad fork");
        exit(1);
    }
    if (pid1 == 0)
    {
        for (int i = 1; i < 51; ++i)
        {
            printf("%d ", i);
        }
        return 0;
    }
    pid2 = fork();
    if (pid2 == -1)
    {
        perror("bad fork");
        exit(1);
    }
    if (pid2 == 0)
    {
        for (int i = 51; i < 101; ++i)
        {
            printf("%d ", i);
        }
        return 0;
    }
    return 0;
}