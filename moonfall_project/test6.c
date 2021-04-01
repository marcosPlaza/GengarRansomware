#include <stdio.h>

void test6(void)
{
    unsigned int a = 0;

    __try
    {
        __asm {

            // save register values on the stack
            push eax
            push ebx
            push ecx
            push edx

                            // perform fingerprint
            mov eax, 'VMXh' // VMware magic value (0x564D5868)
            mov ecx, 0x14 //14h // get memory size command (0x14)
            mov dx, 'VX' // special VMware I/O port (0x5658)
 
            in eax, dx // special I/O cmd
 
            mov a, eax // data

                // restore register values from the stack
            pop edx
            pop ecx
            pop ebx
            pop eax
        }
    }
    __except (EXCEPTION_EXECUTE_HANDLER)
    {
    }

    printf("\n[+] Test 6: VMware \"get memory size\" command\n");

    if (a > 0)
        printf("Result  : VMware detected\n\n");
    else
        printf("Result  : Native OS\n\n");
}

int main(){
    return 0;
}