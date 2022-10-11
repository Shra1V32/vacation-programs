#include<stdio.h>
void main() {  
   int a = 10, b = 20, c;  
   
   asm("   movl    %2,%d;"
    "   addl    %1,%0;"
    : "=&r" (c)
    : "r" (a), "r" (b)
   );
   
   printf("c= %d",c);
} 