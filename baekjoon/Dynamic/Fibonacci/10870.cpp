#include<iostream>
using namespace std;
int main()
{
    int pre;
    int a=0;
    int b = 1;

    int num;
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
