#include<iostream>
using namespace std;

int main()
{
    int num = 0x00;
    cin>>num;
    int c = 0x00;
    c = num / 3;
    num %= 3;
    c += num;
    if (c % 2 != 0)
        cout<<"SK"<<endl;
    else
        cout<<"CY"<<endl;


}
