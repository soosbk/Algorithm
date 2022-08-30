#include<iostream>
#include<vector>


using namespace std;


vector<unsigned long long>v;
unsigned long long tmp;



int main(){
	int num;
	int largest_num=3;
	int n;
	cin>>num;
	v.push_back(0);
	v.push_back(1);
	v.push_back(2);
	v.push_back(4);

	for(int i=4;i<11;i++){
		tmp=v[i-1]+v[i-2]+v[i-3];
		v.push_back(tmp);
	}

	for(int i=0;i<num;i++){
		cin>>n;
		cout<<v[n]<<endl;
	}
}
