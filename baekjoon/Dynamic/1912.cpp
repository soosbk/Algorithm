#include<iostream>
#include<vector>
using namespace std;


vector<int> num;

int main(){


    long long max_sum;

    int siz,n;
    cin>>siz;


    for(int i=0;i<siz;i++){
        cin>>n;
        num.push_back(n);
    }



    max_sum=num[siz-1];
    long long last_sum=num[siz-1];

   for(int i=siz-2;i>=0;i--){

        if(num[i]<last_sum+num[i]) last_sum=last_sum+num[i];

        else last_sum=num[i];



        if(max_sum<last_sum) max_sum=last_sum;

    }
    cout<<max_sum;

}
