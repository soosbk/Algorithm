#include<iostream>
using namespace std;
int main()
{
    unsigned long long pre;
    unsigned long long a=0;
    unsigned long long b = 1;

    unsigned long long num;
    cin>>num;
    if (num == 0) b = 0;
    else if (num == 1) b = 1;
    else {
        for (int i = 1; i < num; i++)
        {
            pre = a;
            a = b;
            b = pre + a;
        }
    }
    cout<<b;
}
