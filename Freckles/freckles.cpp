#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef pair<double,ii> dii;
typedef pair<double,int> di;
typedef pair<double,double> ddi;
typedef vector<ddi> vddi;
typedef vector<di> vdi;
typedef vector<vdi> vvdi;

double distance(double x1, double x2, double y1, double y2){
    double xVal = x2 - x1;
    double yVal = y2 - y1;
    double x = pow(xVal,2);
    double y = pow(yVal,2);


    return sqrt(x+y);
}


struct union_find {
    vi p; 
    union_find(int n) : p(n, -1) { }
    int find(int x) {
        return p[x] < 0 ? x : p[x] = find(p[x]); }
    bool united(int x, int y) {
        return find(x) == find(y); }
    void unite(int x, int y) {
        int xp = find(x), yp = find(y);
        if (xp == yp) return;
        if (p[xp] > p[yp]) swap(xp,yp);
        p[xp] += p[yp], p[yp] = xp;
        return; 
        }
    int size(int x) { return -p[find(x)]; 
    
    } 

};

double kruskal(vvdi& g) {
    priority_queue<dii> s;
    union_find uf(g.size());
    double res = 0;
    for(int i = 0; i < g.size(); ++i)
    for(auto x : g[i]) s.push(dii(-x.first, ii(x.second, i)));
    while(uf.size(0) < g.size()) {
        auto x = s.top(); s.pop();
        if(uf.united(x.second.first, x.second.second)) continue;
        res -= x.first; uf.unite(x.second.first, x.second.second);
    }
    return res; 
    
    }


int main() {
    int cases, tests;
    cin >> cases;

    for(int i = 0; i<cases; ++i){
        cin >> tests;
        vddi values(tests);

        for(int j = 0; j<tests; j++){
            double x,y;
            cin >> x >> y;
            values[j] = ddi(x,y);
        }


        vvdi g(tests, vdi());
        for(int j = 0; j < tests; j++) {
            for(int k = j+1; k<tests; k++){

                double x1 = values[j].first;
                double y1 = values[j].second;
                double x2 = values[k].first;
                double y2 = values[k].second;
                double weight = sqrt(pow(x2-x1, 2) + pow(y2-y1,2));
                g[j].push_back(di(weight, k));
                g[k].push_back(di(weight, j));
                
            }
        }
        double returner = kruskal(g);

        cout << fixed << setprecision(2) << returner << "\n";
                
            }
        }
    

