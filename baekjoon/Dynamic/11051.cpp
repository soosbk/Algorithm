
#include<iostream>
using namespace std;

unsigned long long dp[1001][1001];


int main(){
	int n,k;
	cin>>n>>k;

	for(int i=1;i<=n;i++) {
		dp[i][i]=1;
		dp[i][0]=1;
	}


	if(n>=2){
		for(int i=2;i<=n;i++){
			for(int j=1;j<i;j++) dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007;
	
		}
	}	


	
	cout<<dp[n][k]<<endl;
	
}
