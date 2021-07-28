#include<iostream>
using namespace std;
int main()
{
    unsigned long long pre;
    unsigned long long a=1;
    unsigned long long b = 1;
    unsigned long long c=1;

    unsigned long long num;
    cin>>num;
    if(num<=3) c=1;
    else {
        for (int i = 1; i < num-2; i++)
        {
            pre = b;
            b = c;
            c +=a;

            a=pre;
        }
    }
    cout<<c;
}
