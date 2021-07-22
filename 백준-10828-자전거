#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
    int n=0x00;
    cin>>n;
    int *arr=new int[n];
    char input[6]={0x00,};
    int num=0x00;
    int top=0x00;
    for(int i=0;i<n;i++){
        cin>>input;
        if(input[0]=='p'&&input[1]=='u'){
            cin>>num;
            arr[top]=num;
            top++;
        } 
        
        else if(input[0]=='t'){
            if(top==0) cout<<-1<<endl;
            else cout<<arr[top-1]<<endl;
        }
        
        else if(input[0]=='p'&&input[1]=='o'){
            if(top==0) cout<<-1<<endl;
            else {
                cout<<arr[top-1]<<endl;
                top--;
            }
        }
        
        else if(input[0]=='s') cout<<top<<endl;
        else if(input[0]=='e'){
            if(top==0) cout<<1<<endl;
            else cout<<0<<endl;
        }
        
    }
}
