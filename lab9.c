#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int long factorial(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    else
    {
        return n * factorial(n - 1);
    }
}

int sumNumbers(int n)
{
    int ans = 0;
    for (int i = 1; i <= n; ++i)
    {
        ans += i;
    }
    return ans;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf(" %d", &n);
    int pipefd1[2], pipefd2[2];
    pid_t pid1, pid2;
    if (pipe(pipefd1) == -1)
    {
        perror("pipe1");
        exit(EXIT_FAILURE);
    }
    if (pipe(pipefd2) == -1)
    {
        perror("pipe2");
        exit(EXIT_FAILURE);
    }

    pid1 = fork();
    if (pid1 == -1)
    {
        perror("fork");
        exit(EXIT_FAILURE);
    }
    if (pid1 == 0)
    {
        close(pipefd1[0]);
        int fact = factorial(n);
        write(pipefd1[1], &fact, sizeof(fact));
        close(pipefd1[1]);
        exit(EXIT_SUCCESS);
    }
    pid2 = fork();
    if (pid2 == -1)
    {
        perror("fork");
        exit(EXIT_FAILURE);
    }
    if (pid2 == 0)
    {
        close(pipefd2[0]);
        int sum = sumNumbers(n);
        write(pipefd2[1], &sum, sizeof(sum));
        close(pipefd2[1]);
        exit(EXIT_SUCCESS);
    }

    // Parent process
    close(pipefd1[1]);
    close(pipefd2[1]);

    int fac, sumv;
    read(pipefd1[0], &fac, sizeof(fac));
    read(pipefd2[0], &sumv, sizeof(sumv));

    close(pipefd1[0]);
    close(pipefd2[0]);

    printf("Parent received factorial: %d sum: %d", fac, sumv);

    return 0;
}