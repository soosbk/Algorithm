
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool compare(pair<unsigned int,unsigned int> a,pair<unsigned int,unsigned int> b){
	if(a.second==b.second) return a.first<b.first;
	else return a.second<b.second;
}

vector<pair<unsigned int,unsigned int>>t;

int main(){
	unsigned int n;
	int cnt=1;
	cin>>n;
	int t1,t2;

	for(int i=0;i<n;i++){
		cin>>t1>>t2;
		t.push_back(pair<unsigned int,unsigned int>(t1,t2));
	}
	sort(t.begin(),t.end(),compare);
	int end_t=t[0].second;

	for(int i=1;i<n;i++){
		if(end_t>t[i].first) continue;
		cnt+=1;
		end_t=t[i].second;
	}

	printf("%d\n",cnt);
	
}
