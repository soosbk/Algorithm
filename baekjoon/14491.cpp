#include<iostream>
using namespace std;

int n;

void print(int n){
	if(n<9){
		cout<<n;
		return;
	}
	print(n/9);
	cout<<n%9;
}
int main(){
	cin>>n;
	print(n);
}
