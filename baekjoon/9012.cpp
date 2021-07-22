#include<iostream>
#include<stack>
#include<cstring>
using namespace std;
int main(){
	int num=0x00;
	cin>>num;
	int out=0;
	for(int i=0;i<num;i++){
		out=1;
		stack<char>s;
		char str[51];
		cin>>str;
		for(int j=0;j<strlen(str);j++){
			if(str[j]=='(') s.push(1);
			else if((str[j]==')')&&(s.empty())) {
				out=0;
				break;}
			else if(str[j]==')') s.pop();
		}
		if(!(s.empty())) out=0;
		if(out==0) cout<<"NO"<<endl;
		else cout<<"YES"<<endl;
	}
}
