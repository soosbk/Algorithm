
#include<iostream>
#include<cstring>
using namespace std;

char first[1001];
char second[1001];
int common_len[1001][1001];
int main(){
	cin>>first;
	cin>>second;
	int first_len=strlen(first);
	int second_len=strlen(second);

	for(int i=1;i<=first_len;i++){
		for(int j=1;j<=second_len;j++){
			if(first[i-1]==second[j-1]) 
				common_len[i][j]=common_len[i-1][j-1]+1;
			else{
				if(common_len[i-1][j]>common_len[i][j-1]) common_len[i][j]=common_len[i-1][j];
				else common_len[i][j]=common_len[i][j-1];
			}
		}
	}

	printf("%d\n",common_len[first_len][second_len]);
}
