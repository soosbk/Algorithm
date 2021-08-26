#include<iostream>
#include<stack>
#include<string>
using namespace std;


bool count_fun(string a,char b,char c){
	int start=0;
	int end=0;
	for(int i=0;i<a.size();i++){
		if(a[i]==b) start+=1;
		else if(a[i]==c) end+=1;

	}
	
	if (start!=end) return true;
	else return false;
}

int main(){
	string input;
	stack<char> st;
	bool small_count;
	bool big_count;
	char tmp;
	
	while(true){
		getline(cin,input);
		if(input[0]=='.') break;
		if(input.find('(')== string::npos&&input.find(')')== string::npos&&input.find('[')== string::npos&&input.find(']')== string::npos){
			cout<<"yes"<<endl; continue;
		}

		small_count=count_fun(input,'(',')');
		big_count=count_fun(input,'[',']');

		if(small_count||big_count) {
			cout<<"no"<<endl; continue;
		}

		for(int i=0;i<input.size();i++){

			
			if(input[i]=='('||input[i]==')'||input[i]=='['||input[i]==']'){
				if(input[i]==')') tmp='(';
				else if(input[i]==']') tmp='[';
				else{
					st.push(input[i]);
					continue;
				} 
					
				if(st.empty()||st.top()!=tmp) st.push(input[i]);
				else if(st.top()==tmp) st.pop();
			}
		}

		if(st.empty()) cout<<"yes"<<endl;
		else{
			cout<<"no"<<endl;
			while(!st.empty()) st.pop();
		}


		


	}
}
