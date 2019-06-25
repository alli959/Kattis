#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;



ll invnum(vi &v) {
    ll res = 0;
    vi cnt(v.size() + 1), w(v);
    sort(w.begin(), w.end());
    map<int,int> rnk;
    for(int i = 0; i < v.size(); ++i)
    rnk[w[i]] = i + 1;
    for(int i = v.size() - 1; i >= 0; --i) {
        int j = rnk[v[i]] - 1;
        while(j) res += cnt[j], j -= j & -j;
        j = rnk[v[i]];
        while(j <= v.size()) cnt[j]++, j += j & -j;
    }
    return res;
}


int main(){
    int length;
    cin >> length;
    vi vec(length);
    for(int i = 0; i<length; i++){
        int value;
        cin >> value;
        vec.push_back(value);
    }

    cout << invnum(vec) << endl;
}
