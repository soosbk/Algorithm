#include<iostream>

using namespace std;

int count[1001]={0, 1,3,};

int main(){
    int num;

    cin>>num;

    if(num<3) cout<<count[num];

   else {
        for(int i=3;i<=num;i++){
            count[i]=(count[i-1]+count[i-2]*2)%10007;
            

    
        }


        cout<<count[num];
    
    }
    



}
