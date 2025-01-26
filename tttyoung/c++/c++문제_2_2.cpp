#include <iostream>
using namespace std;

int main()
{
	const int num = 12;
	const int* ptr = &num; //포인터 변수를 만들어 num의 주솟값을 ptr에 저장
	const int* (&ref) = ptr; //포인터변수 ptr 를 참조하는 참조자 ref를 만듦(포인터 변수에 대한 참조자 선언)
	cout << num << endl;
	cout << ptr << endl;
	cout << ref << endl;
	cout << "result: " << *ref << endl;

	return 0;
}