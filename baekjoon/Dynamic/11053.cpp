#include <iostream>
using namespace std;

int arr[1001];
int max_len[1001];
int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++) cin>>arr[i];
	
	int len=0;
	max_len[n-1]=1;
	for(int i=n-2;i>=0;i--){
	    int n_len=0;
	    for(int j=i+1;j<n;j++){
	        if((arr[i]<arr[j])&&(n_len<max_len[j])) n_len= max_len[j];
	    }
	    max_len[i]=n_len+1;
	
	}
	
	int real_max=max_len[0];
	for(int i=1;i<n;i++){
	    if(max_len[i]>real_max) real_max=max_len[i];
	}
	
    printf("%d\n",real_max);
}
