#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void to_lower(char * buffer, int length){
	for (int i=0; i<length; i++){
		buffer[i] = tolower(buffer[i]);
	}
	printf("RESULT: ");
	printf(buffer);
}

void input()
{
	char buffer[64];

	fgets(buffer, 96, stdin);
	to_lower(buffer, 24);
}

int main()
{
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);

	printf("Input Text:\n");
	input();

	int i = 1;
	if(i == 0){
		__asm__("jmp %rsi;");
	}

	return 0;
}
