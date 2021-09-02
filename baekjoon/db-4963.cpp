#include<iostream>
#include<stack>
#include<vector>
using namespace std;
struct cor{
	int x;
	int y;

	void init(int x, int y)
    {
    	this->x = x;
        this->y = y;
    }
};

int land[50][50];

int main(){
	int w,h;
	cor dir[8]={{1,0},{1,1},{1,-1},{-1,0},{-1,1},{-1,-1},{0,1},{0,-1}};
	//cor dir[3]={{1,0},{1,1},{0,1}};
	stack<cor> s;
	cor tmp,tmp2; 
	int count;
	vector<int>v;
	while(true){

		cin>>w>>h;
		if(w==0 && h==0) break;
		count=0;
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++) cin>>land[i][j];
		}


		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++) {
				if(land[i][j]==0) continue;
				tmp.x=i; tmp.y=j;
				s.push(tmp);
				land[i][j]=0;
				count+=1;
				while(!s.empty()){
					tmp=s.top();
					s.pop();
					for (int k = 0; k < 8; k++)
					{
						int dx=tmp.x+dir[k].x;
						int dy=tmp.y+dir[k].y;

						if(dx<0||dy<0||dx>=h||dy>=w||land[dx][dy]==0) continue;
						tmp2.x=dx; tmp2.y=dy;
						s.push(tmp2);
						land[dx][dy]=0;
						
					}
				}

			}
		}
			

		cout<<count<<endl;



	}	



	


}
