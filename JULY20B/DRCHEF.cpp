#include <iostream>
#include <bits/stdc++.h>
#include <array>
using namespace std;

int main(){
    int t;
    cin>>t;
    int n,x;
    while (t--) {
        cin>>n>>x;
        int a[n];
        for (int i = 0; i < n; i++){
            cin>>a[i];
        }
        sort(a,a+n);
        int d = 0;
        int i = 0;
        int cured = 0;
        int m = a[n-1];
        if (x > m){
            cout<<n<<endl;
            continue;
        } 
        while (i<n){
            while (i < (n-1) && a[i] < x/2){
            i++;
            }
            while (x < a[i]){
                x *= 2;
                d ++;
            }
            cured ++;
            x = 2 * a[i];
            d++;
            i++;
        }
        d += (n - cured);
        cout<<d<<endl;
    }
    return 0;
}