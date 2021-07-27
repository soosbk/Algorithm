#include<iostream>
using namespace std;

int main()
{
    int a = 0;
    int b = 1;
    int ke = 0;

    int num;
    cin>>num;
    if (num == 0) b = 0;
    else if (num == 1) b = 1;
    else //b: n->n-1 a: n-2
    {
        for (int i = 0; i < (num-1); i++)
        {
            ke = b% 1000000007;
            b = (a + ke)% 1000000007;
            a = ke;
        }

    }
    cout<<b<<endl;;

}
