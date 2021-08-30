#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<vector>

#define pp pair<string,int>
using namespace std;




bool cmp(pp& a, pp& b) {
	if (a.second==b.second) return a.first<b.first;
    return a.second> b.second;
}


int main(){
	map<string,int> s;
	string str;


	int num;
	cin>>num;
	for(int i=0;i<num;i++){
		cin>>str;
		if((s.find(str)!=s.end())) s[str]+=1;
		else s.insert(pair<string,int>(str,1));


	}

	vector<pp> v(s.begin(),s.end());
	sort(v.begin(),v.end(),cmp);

	auto iter=v.begin();

	cout<<iter->first<<endl;
}
