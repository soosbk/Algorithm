#include<iostream>


using namespace std;


int main(){
	int a_count=1;
	int b_count=0;
	int tmp;

	int time;

	cin>>time;


	for(int i=0;i<time;i++){
		tmp=b_count;
		b_count=a_count+b_count;
		a_count=tmp;
	}

	cout<<a_count<<" "<<b_count<<endl;
}
