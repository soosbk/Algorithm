#include <iostream>
using namespace std;

unsigned long long num[91]={0,1,1,};
int main() {
	int n;
	cin>>n;
	if(n>2) {
	    for(int i=3;i<=n;i++){
	        num[i]=num[i-1]+num[i-2];
	    }
	}
	
	cout<<num[n];
	return 0;
}
