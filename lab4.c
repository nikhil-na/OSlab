#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
void main(void){
    int pid;
    int status;
    printf("Hello World!\n");
    pid = fork();
    if (pid == -1){
        perror("bad fork");
        exit(1);
    }
    if(pid == 0){
        printf("I am the child process\n");
    } else{
        wait(NULL); /* Parent waits for child to finish*/
        printf("I am the parent process\n");
    }
}