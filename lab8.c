#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

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
    scanf("%d", &n);

    int pipefd[2];
    pid_t pid;

    if (pipe(pipefd) == -1)
    {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork();
    if (pid == -1)
    {
        perror("bad fork");
        exit(EXIT_FAILURE);
    }
    else if (pid == 0)
    {
        close(pipefd[0]);
        int val = sumNumbers(n);
        write(pipefd[1], &val, sizeof(val));
        close(pipefd[1]);
        exit(EXIT_SUCCESS);
    }
    else
    {
        close(pipefd[1]);
        int buffer;
        read(pipefd[0], &buffer, sizeof(buffer));
        close(pipefd[0]);
        printf("Parent received: %d\n", buffer);
    }

    return 0;
}
