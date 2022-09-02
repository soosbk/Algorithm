#include<iostream>
using namespace std;




unsigned long long arr[1000001]={0,1,2,};



int main(){

    unsigned long long n;

    cin>>n;





    for(unsigned long long i=3;i<=n;i++){

        arr[i]=(arr[i-2]+arr[i-1])%15746;

    }

    cout<<arr[n];

}
