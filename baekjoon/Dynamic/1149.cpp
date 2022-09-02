#include<iostream>
#include<vector>

using namespace std;


unsigned long long cost[1001][4];
unsigned long long dp[1001][4];

unsigned long long min(unsigned long long a, unsigned long long b){
    if(a<b) return a;
    else return b;
    
}


int main(){
    int num, n;
    cin>> num;
    for(int i=1;i<=num;i++){
        for(int j=1;j<=3;j++){
            cin>>cost[i][j];
            
        }
        
    } 
    dp[1][1]=cost[1][1];
    dp[1][2]=cost[1][2];
    dp[1][3]=cost[1][3]; //기본항

    for(int i=2;i<=num;i++){
        dp[i][1]=min(dp[i-1][2],dp[i-1][3])+cost[i][1];
        dp[i][2]=min(dp[i-1][1],dp[i-1][3])+cost[i][2];
        dp[i][3]=min(dp[i-1][2],dp[i-1][1])+cost[i][3];
    }


    cout<<min(min(dp[num][1],dp[num][2]),dp[num][3]);
    

    
}
