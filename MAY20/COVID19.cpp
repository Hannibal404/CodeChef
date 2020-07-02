#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int x[n];
        cin >> x[n];
        int min = n;
        int max = 1;
        int i = 0, c = 1;
        while (i < n - 1){
            if (x[i + 1] - x[i] <= 2){
                c++;
            }
            else{
                if (c > max){
                    max = c;
                }
                if (c < min){
                    min = c;
                }
                c = 1;
            }
            i++;
        }
        if (c > max){
            max = c;
        }
        if (c < min){
            min = c;
        }
        cout << min <<" " + t << max <<" "<< x <<endl;
    }
}