#include<iostream>
#include<deque>
using namespace std;


deque<int>d;

void recur(unsigned long long num){
    if(num==1) {
        d.push_front(num);
        return;}

    else{
        d.push_front(num%2);
        recur(num/2);
    }
}

int main()
{
    unsigned long long num;
    cin>>num;
    recur(num);

    for(int i=0;i<d.size();i++){
        cout<<d[i];
    }
    cout<<endl;

}
