#include <stdio.h>

extern "C" int addIntNumbers(int num1, int num2)
{
  return num1 + num2;
}

extern "C" double subtractDoubleNumbers(double num1, double num2)
{
  return num1 - num2;
}

extern "C" float divideFloatNumbers(float num1, float num2)
{
  return num1 / num2;
}

extern "C" void printSomeText(char* text)
{
  printf("%s", text);
}