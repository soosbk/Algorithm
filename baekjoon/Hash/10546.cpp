#include<iostream>
#include<map>
#include<string>
using namespace std;
bool cmp(const pair<string,int>& a, const pair<string,int>& b) {
	if (a.second == b.second) return a.first < b.first;
	return a.second < b.second;
}

int main(){
	int num;
	string input;
	cin>>num;
	map<string,int> m;

	for(int i=0;i<num;i++){
		cin>>input;
		if (m.find(input)!=m.end()) m[input]+=1;
		else m.insert(pair<string,int>(input,1));

	}


	for(int i=0;i<num-1;i++){
		cin>>input;
		if (m[input]==1) m.erase(input);
		else m[input]-=1;
	}

	auto iter=m.begin();
	cout<<iter->first<<endl;

}
