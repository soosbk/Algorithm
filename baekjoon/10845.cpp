#include<iostream>
using namespace std;

int main(){
    int n=0x00;
    cin>>n;
    int arr[10000];
    int front=0x00;
    int rear=0x00;
    char input[6]={0x00,};
    int num=0x00;
    for(int i=0;i<n;i++){
        cin>>input;
        if(input[0]=='p'&&input[1]=='u'){
            cin>>num;
            arr[rear]=num;
            rear++;
        }
        else if(input[0]=='p'&&input[1]=='o'){
            if(rear==front) cout<<-1<<endl;
            else{
                cout<<arr[front]<<endl;
                front++;
            }
        }
        else if(input[0]=='f'){
            if(rear==front) cout<<-1<<endl;
            else cout<<arr[front]<<endl;
                
            
        }
        else if(input[0]=='b'){
            if(rear==front) cout<<-1<<endl;
            else cout<<arr[rear-1]<<endl;
                
        }
        else if(input[0]=='s'){
            cout<<rear-front<<endl;
        }
        else if(input[0]=='e'){
            if(rear==front) cout<<1<<endl;
            else cout<<0<<endl;
        }
    }
}
