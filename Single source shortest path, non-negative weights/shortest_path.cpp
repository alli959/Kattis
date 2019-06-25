#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef pair<double,int> di;
typedef vector<di> vdi;
typedef vector<vdi> vvdi;
typedef vector<double> vd;
pair<vi, double> dijkstra(vvdi& g, int a, int b) {
    vd dist(g.size(), DBL_MAX);
    vi prv(g.size(), -1);
    priority_queue<di> pq;
    dist[a] = 0; pq.push(di(0, a));
    while(!pq.empty()) {
        auto t = pq.top();
        pq.pop();
        if(-t.first != dist[t.second]) continue;
        for(di x : g[t.second]) {
            if(dist[t.second] + x.first < dist[x.second]) {
                dist[x.second] = dist[t.second] + x.first;
                prv[x.second] = t.second;
                pq.push(di(-dist[x.second], x.second));
            }
        }
    }
    if(prv[b] == -1) return make_pair(vi(), DBL_MAX);
    vi path(1, b);
    while(path.back() != a) path.push_back(prv[path.back()]);
        reverse(path.begin(), path.end());
        return make_pair(path, dist[b]);
}



int main() {
    int n, m, q, s, u, v, w;
    int index = 0;

    while(cin >> n >> m >> q >> s){
        if(n,m,q,s == 0,0,0,0){
            break;
        }
        if(index != 0){

            cout << endl;
        }
        index += 1;

        vvdi g(n, vdi());
        for(int i = 0; i < m; ++i) {
            cin >> u >> v >> w;
            g[u].push_back(di(w, v));
        }
        int value;
        for(int i = 0; i<q; ++i){
            cin >> value;
            if(value == s){
                cout << 0 << endl;
            }
            else{

                auto res = dijkstra(g, s, value);
            
                if(res.second == DBL_MAX){
                    cout << "Impossible" << endl;
                }
                else{


                    cout << (int)res.second << endl;
                }
            }
        }
    }
}
