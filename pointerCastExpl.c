#include <stdio.h>
#include <stdlib.h>


void main() {
    int myInt;
    float myFloat;

    int* intPtr = &myInt;
    float* floatPtr = &myFloat;

    int szint = sizeof(myInt);
    int szflt = sizeof(myFloat);

    // Assume intPtr has the value 0x3000
    //  and floatPtr == 0x4000
    //  and szint = 4, szflt = 8 (bytes)
    
    int intsize = sizeof(myInt);
    int floatsize = sizeof(myFloat);
    
    printf("Size of int is %d bytes. Size of float is %d bytes.\n",intsize,floatsize);

    printf("intPtr   = %d\n", (int)intPtr);
    printf("intPtr+1 = %d\n", (int)intPtr+1);
    printf("intPtr+1 = %d\n", (int)(intPtr+1));  // check precedence!
    printf("fltPtr   = %d\n", (int)floatPtr);
    printf("fltPtr++ = %d\n", (int)(floatPtr+1) );
    printf("fltPtr++ = %d\n", (int)floatPtr+1 );
    
    printf("\n now lets cast to unsigned ints\n");
    printf("intPtr   = %u\n", (unsigned int)intPtr);
    printf("intPtr+1 = %u\n", (unsigned int)intPtr+1);
    printf("intPtr+1 = %u\n", (unsigned int)(intPtr+1));
    printf("fltPtr   = %u\n", (unsigned int)floatPtr);
    printf("fltPtr++ = %u\n", (unsigned int)floatPtr+1 );
    printf("fltPtr++ = %u\n", (unsigned int)(floatPtr+1) );

}
