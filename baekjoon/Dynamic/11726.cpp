#include <iostream>
using namespace std;


unsigned long long cnt[1001];
int main() {
	cnt[1]=1;cnt[2]=2;
	int n;
	scanf("%d",&n);
	for(int i=3;i<=n;i++) cnt[i]=(cnt[i-1]+cnt[i-2])%10007;
    cout<<cnt[n]<<endl;
	return 0;
}
