#include <stdio.h>

int add_together(int x, int y) {
	int result = x + y;
	return result;
}

int world(int n) {
	while (n > 0) {
		puts("Hello world!");
	}
	return 0;
}

int main(int argc, char** argv) {
	int i = 5;
	while (i > 0){
		puts("Hello, world! <- this is getting boring.");
		i--;
	}

	for (int i = 0; i < 5; i++){
		puts("Hello, world! <- this is getting boring.");
	}

	return 0;
}