#include<iostream>
#include<stack>
#include<string>
using namespace std;



int main(){
	stack<char> st;
	string input;
	int count=0;
	cin>>input;
	for(int i=0;i<input.size();i++){
		if(st.empty()||!((input[i]==')'&&st.top()=='('))) st.push(input[i]);
		else st.pop();
		
		
	}

	
	while(!st.empty()) {
		count+=1;
		st.pop();
	}

	cout<<count<<endl;
	
	
}
