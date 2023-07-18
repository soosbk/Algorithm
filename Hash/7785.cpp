#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#define pp pair<string,bool>
using namespace std;

bool cmp(const pp& a, const pp& b) {
	return a.first > b.first;
}

int main(){

	int num;
	cin>>num;
	map<string,bool>m;
	string s1,s2;
	for(int i=0;i<num;i++){
		cin>>s1>>s2;
		if(s2[0]=='e') m.insert(pp(s1,true));
		else m.erase(s1);
	}

	vector <pp> vec( m.begin(), m.end() );
	sort(vec.begin(),vec.end(),cmp);
	auto i=vec.begin();
	for(;i!=vec.end();i++) printf("%s\n",i->first.c_str());
	

}


