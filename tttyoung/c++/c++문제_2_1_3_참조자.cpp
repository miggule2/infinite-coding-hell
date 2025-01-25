#include <iostream>
using namespace std;

void swappointer(int* n1, int* n2)
{
	int temp = *n1;
	*n1 = *n2;
	*n2 = temp;
}

void swappointer2(int* (&ref1), int* (&ref2)) // ptr1, ptr2라는 포인터 변수를 참조자로 선언하여 매개변수에 참조자를 넣어주고 그 참조자의 원본?은 포인터 변수이기 때문에 앞에 *를 붙인다.
{
	int* temp = ref1;
	ref1 = ref2;
	ref2 = temp;
}

int main()
{
	int num1 = 5;
	int* ptr1 = &num1;
	int num2 = 10;
	int* ptr2 = &num2;

	swappointer(ptr1, ptr2);
	cout << *ptr1 << " and " << *ptr2 << endl;
	swappointer2(ptr1, ptr2);
	cout << *ptr1 << " and " << *ptr2 << endl;
	return 0;
}