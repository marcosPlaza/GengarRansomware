#include <iostream>

using namespace std;

int main()
{
	bool IsUnderVM = false;
	__asm {
		xor    eax, eax
		inc    eax
		cpuid
		bt     ecx, 0x1f
		jc     UnderVM
		NotUnderVM:
		jmp     NopInstr
		UnderVM:
		mov    IsUnderVM, 0x1
		NopInstr:
		nop
	};

	cout << IsUnderVM;
    return 0;
}