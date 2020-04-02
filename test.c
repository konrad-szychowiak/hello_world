#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int main(int argc, char const *argv[]) {

  float foo = 0.0, bar = 1.0, i = 0.0;

  for (int i = 0; i < INT_MAX; i++)
  {
    foo += pow(double(-1), double(i)) / (1+2*i);
    printf("%.50f\n", foo);
  }

  printf("%.50f\n", foo);

}
