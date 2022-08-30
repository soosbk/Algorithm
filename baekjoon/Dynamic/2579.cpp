#include<iostream>
#include<vector>
#include<utility>


using namespace std;

typedef pair<unsigned long long,unsigned long long> p;

vector<p> v;
vector<int> number;


int max(p v){
	if(v.first>v.second) return v.first;
	else return v.second;
}

int main(){
	int num;
	int tmp;
	cin>>num;


	for(int i=0;i<num;i++){
		cin>>tmp;
		number.push_back(tmp);
	}

	v.push_back(make_pair(number[0],0));
	v.push_back(make_pair(number[1],number[0]+number[1]));

	if (num>1){
		for(int i=2;i<=num;i++){
			unsigned long long left=max(v[i-2])+number[i];
			unsigned long long right=v[i-1].first+number[i];

			v.push_back(make_pair(left, right));
		}
	}

	

	cout<<max(v[num-1]);
}
