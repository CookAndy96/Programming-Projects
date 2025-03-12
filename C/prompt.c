#include <stdio.h>
#include <stdlib.h>

#include <editline.h>

/* Declare a buffer for user input of size 2048 */
static char input[2048];

int main(int argc, char** argv) {

	/* Print Version and Exit Information */
	puts("LISP V 0.0.0.0.1");
	puts("Press Ctrl+c to Exit\n");

	/* In a never ending loop. Keeps the LISP on the screen at all times. */
	while (1) {
	/* Output our prompt */
	/* fputs("lispy > ", stdout); */

		/* Output our prompt and get input */
		char* input = readline("lispy> ")

	/* Read a line of user input of maximum size 2048 */
	/*fgets(input, 2048, stdin); */

		/* Add input history */
		add_history(input);

		/* Echo input back to user */
		printf("No, you're a %s\n", input);

		/* Free retrieved input */
		free(input);
	}
	return 0;
}