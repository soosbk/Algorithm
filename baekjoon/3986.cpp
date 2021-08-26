#include<iostream>
#include<stack>
#include<string>
#include<algorithm>
using namespace std;

int count_fun(string a,char b){
	int count=0;
	for(int i=0;i<a.size();i++){
		if(a[i]==b) count+=1;
	}
	
	return count;
}

int main(){
	int num;
	int count=0;
	stack<char>st;
	string inp;
	cin>>num;

	for(int i=0;i<num;i++){

		cin>>inp;
		int a_count=count_fun(inp,'A')%2;
		int b_count=count_fun(inp,'B')%2;
		
		
		if(a_count==1 ||b_count==1) continue;
		

		//st.push(inp[0]);
		for(int j=0;j<inp.size();j++){
			if(st.empty()||st.top()!=inp[j]) st.push(inp[j]);
			else st.pop();
		}
		if(st.empty()) count+=1;
		else{
			while(!st.empty()) st.pop();
		}
		
	}
	cout<<count<<endl;

}
