#include<iostream>
using namespace std;

unsigned long long col[1000001];



int main(){
	unsigned long long n;
	unsigned long long min_v;
	cin>>n;
	for(int i=1;i<=n;i++){
		if(i==1) col[i]=0;
		else if(i<4) col[i]=1;
		else
		{	
			min_v=col[i-1];
			if((i%3==0)&&(min_v>col[(unsigned long long)i/3])) min_v=col[(unsigned long long)i/3];
			if((i%2==0)&&(min_v>col[(unsigned long long)i/2])) min_v=col[(unsigned long long)i/2];
			col[i]=min_v+1;
		}

	}

	cout<<col[n]<<endl;
}
