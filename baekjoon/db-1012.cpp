#include<iostream>
#include<stack>

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

int land[1000][1000];

int main(){
	int m,n,k;
	cor dir[4]={{1,0},{-1,0},{0,1},{0,-1}};
	int x,y;
	int case_num;
	stack<cor> s;

	cor tmp,tmp2; 
	int count;
	
	cin>>case_num;
	for(int i=0;i<case_num;i++)
	{
		cin>>m>>n>>k;
		count=0;
		for(int i=0;i<k;i++){
			cin>>x>>y;
			land[x][y]=1;
		}


		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++) {
				if(land[i][j]==0) continue;
				tmp.x=i; tmp.y=j;
				s.push(tmp);
				land[i][j]=0;
				count+=1;
				while(!s.empty()){
					tmp=s.top();
					s.pop();
					land[tmp.x][tmp.y]=0;
					for (int k = 0; k < 4; k++)
					{
						int dx=tmp.x+dir[k].x;
						int dy=tmp.y+dir[k].y;

						if(dx<0||dy<0||dx>=m||dy>=n||land[dx][dy]==0) continue;
						tmp2.x=dx; tmp2.y=dy;
						s.push(tmp2);
						
						
					}

					
				}

			}
		}
			

		cout<<count<<endl;


	}
	




	


}
