#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
typedef long long ll;

ll arr[10000];

ll ferey(ll number){
    if(arr[number]){
        return arr[number];
    }
    double mult = (double) (number+3.0)/2;
    ll length = (ll)number*mult;
    ll q = 0;
    for(ll i = 2; i<=number; i=q ){
        q = number/(number/i) +1;
        ll diff = ferey(number/i) * (q-i);

        length -= diff;
    }

    arr[number] = length;
    return length; 
}

int main(){

    ll p, k, n;
    cin >> p;
    for(int i = 0; i<p; i++){
        cin >> k >> n;
        ll length = ferey(n);
        cout << k << " " << length << endl;
    }

    return 0;
}