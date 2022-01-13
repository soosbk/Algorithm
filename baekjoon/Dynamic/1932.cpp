#include <iostream>
using namespace std;


unsigned long long num[501][501];
unsigned long long  s[501][501];
int main() {
	int n;
	unsigned long long max;
	cin>>n;
	for(int i=1;i<=n;i++){
	    for(int j=1;j<=i;j++) cin>>num[i][j];
	}
	
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            if(s[i-1][j-1]>s[i-1][j]) max=s[i-1][j-1];
            else max=s[i-1][j];
            s[i][j]=max+num[i][j];
           
            
        }
    
	}
	max=s[n][1];
	for(int i=2;i<=n;i++){
	    if(max<s[n][i]) max=s[n][i];
	}
	cout<<max<<endl;
	return 0;
}
