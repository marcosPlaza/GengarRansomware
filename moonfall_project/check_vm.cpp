#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
	bool IsUnderVM = false;
	
	__asm__ ("xor %%eax, %%eax;");
	__asm__ ("inc %%eax;");
	__asm__ ("cpuid;");
	__asm__ ("bt %%ecx, 0x1f;");
	__asm__ ("NotUnderVM: jmp NopInstr;");
	__asm__ ("UnderVM: mov 0x1;" : "=a" (IsUnderVM));
	__asm__ ("NopInstr: nop;");

	cout << IsUnderVM;
    return 0;
}