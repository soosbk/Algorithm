#include<iostream>
#include<cstdlib>
using namespace std;

int n;
void print_underbar(int num){
	for(int i=0;i<num;i++) cout<<"____";
	
}

void p5(int num){
	print_underbar(num);
	cout<<"라고 답변하였지."<<endl;
	if(num>0){
		p5(num-1);
	}
	else return;
	
}


void p1(int num){
	
	if(num<n) {
		print_underbar(num);
		cout<<"\"재귀함수가 뭔가요?\""<<endl;
		print_underbar(num);
		cout<<"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."<<endl;
		print_underbar(num);
		cout<<"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."<<endl;
		print_underbar(num);
		cout<<"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""<<endl;
		
		p1(num+1);
	}
	else {
		print_underbar(num);
		cout<<"\"재귀함수가 뭔가요?\""<<endl;
		print_underbar(num);
		cout<<"\"재귀함수는 자기 자신을 호출하는 함수라네\""<<endl;
		p5(num);

	}
}
int main(){
	cin>>n;
	cout<<"어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."<<endl;
	p1(0);
}


