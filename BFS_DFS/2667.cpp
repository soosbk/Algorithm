#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;


int main(){
	stack<int> s1;  //x좌표 저장
	stack<int> s2; //y좌표 저장
	stack<int> dir; //dir 저장
	int num[314]={0x00,};
	int row;
	cin>>row;
	char **arr;
	int n=0x00;

	int direction[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
	int d=0x00;
	int inx=0x00;
	int iny=0x00;
	int x,y;
	arr=new char*[row];
	for(int i=0;i<row;i++) arr[i]=new char[row+1];
	for(int i=0;i<row;i++){
		for(int j=0;j<row;j++) cin>>arr[i][j];}

	for(int i=0;i<row;i++){
		for(int j=0;j<row;j++){
			if(arr[i][j]!='1') continue;
			arr[i][j]='x';
			num[n]++;
			s1.push(i);
			s2.push(j);
			dir.push(0);
			while(!(s1.empty())){
				x=s1.top();
				y=s2.top();
				d=dir.top();
				s1.pop();
				s2.pop();
				for(int d=0;d<4;d++){
					if((d==0)&&(y==row-1)) continue;
					else if((d==1)&&(y==0)) continue;
					else if((d==2)&&(x==row-1)) continue;
					else if((d==3)&&(x==0)) continue;
					inx=x+direction[d][0];
					iny=y+direction[d][1];
					if(arr[inx][iny]=='1'){
						num[n]++;
						arr[inx][iny]='x'; //이미 방이 포함되었다는 걸 x로
						s1.push(inx);
						s2.push(iny);
						
					}
				}
				
			
			}
			n++;
			
		}
	}
	sort(num, num+n);
	cout<<n<<endl;
	for(int i=0;i<n;i++) cout<<num[i]<<endl;
	for(int i=0;i<row;i++) delete[] arr[i];
	delete[] arr;
	
	return 0;
}


