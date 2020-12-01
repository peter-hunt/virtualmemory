#include <stdio.h>

// gcc data.c -o data; ./data

int main() {
  char a = -65453;
  unsigned char b = 'P';
  char c = a + b;
  printf("%c + %c = %c\n", a, b, c);
  return 0;
}
