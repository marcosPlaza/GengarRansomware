#include <stdio.h>

void test5(void)
{
    unsigned int a, b;

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
            mov ecx, 0x0a //0Ah // special version cmd (0x0a)
            mov dx, 'VX' // special VMware I/O port (0x5658)
 
            in eax, dx // special I/O cmd
 
            mov a, ebx // data 
            mov b, ecx // data (eax gets also modified
                // but will not be evaluated)

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

#if DEBUG == 1
    printf("\n [ a=%x ; b=%d ]\n\n", a, b);
#endif

    printf("\n[+] Test 5: VMware \"get version\" command\n");

    if (a == 'VMXh')
    { // is the value equal to the VMware magic value?
        printf("Result  : VMware detected\nVersion : ");
        if (b == 1)
            printf("Express\n\n");
        else if (b == 2)
            printf("ESX\n\n");
        else if (b == 3)
            printf("GSX\n\n");
        else if (b == 4)
            printf("Workstation\n\n");
        else
            printf("unknown version\n\n");
    }
    else
        printf("Result  : Native OS\n\n");
}

int main()
{
    printf("Executing test 5");
    test5();
    printf("END");
    return 0;
}