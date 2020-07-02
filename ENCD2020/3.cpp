#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        long long n;
        cin>>n;
        int i = 1;
        while (n > i + 1){
            n -= i + 1;
            i++;
        }
        cout<< n-1<<endl;
    }
}