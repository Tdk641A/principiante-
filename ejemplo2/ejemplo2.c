#include <stdio.h>
#include <string.h>

void win(){

    system("/bin/sh");
}


void vuln(){
    char buf[32];
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    //read(0,buf, 256);
    gets(buf);
}

void main(){

    printf("Comenzemos... Ahora te redigire a la funcion vulnerable, antes entragame tu input \n");
    vuln();
}