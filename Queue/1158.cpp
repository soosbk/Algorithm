#include<iostream>
#include<queue>


using namespace std;

int main(){
	int n,k;
	cin>>n>>k;


	queue<int>q;
	cout<<"<";
	int i=0	;
	for(int i=0;i<n;i++) q.push(i+1);
	while(q.size()>1){

		i+=1;
		if(i%k) q.push(q.front());
		
		else cout<<q.front()<<", ";
		q.pop();
		i%=k;
	}


	cout<<q.front()<<">";
}
