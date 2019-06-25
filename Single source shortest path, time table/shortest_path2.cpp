#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef vector<int> vi;
typedef pair<double,int> di;
typedef pair<di,di> ddi;
typedef vector<ddi> vddi;
typedef vector<vddi> vvddi;
typedef vector<double> vd;

#define INF 20000000



double timer(int t, int P, int currtime){
	if (P == 0){
		if (t >= currtime) {
            return t-currtime;
        }
		else{ 
            return INF;
            }
	}
	if (t >= currtime){
        return t-currtime;
    }
	int value = (currtime-t+P-1)/P;
	return t + value*P -currtime;
}

double dijkstra(vvddi& g, int a, int b) {
    vd dist(g.size() + 1, INF);
    vi prv(g.size(), -1);
    priority_queue<di> pq;
    dist[a] = 0; pq.push(di(0, a));
    while(!pq.empty()) {
        auto t = pq.top();
        pq.pop();
        if(-t.first != dist[t.second]) continue;
        for(ddi x : g[t.second]) {
            if(dist[t.second] + x.first.first < dist[x.first.second]) {
                int value = timer(x.second.first, x.second.second, dist[t.second]);
                if(dist[t.second] + x.first.first + value < dist[x.first.second]) {
                    dist[x.first.second] = dist[t.second] + x.first.first + value;
                    prv[x.first.second] = t.second;
                    pq.push(di(-dist[x.first.second], x.first.second));
                    
                }

            }
        }
    }
    if(prv[b] == -1) return INF;;
        return dist[b];
}



int main() {
    int n, m, q, s, u, v, t, P, d;

    while(cin >> n >> m >> q >> s){
        if(n,m,q,s == 0,0,0,0){
            break;
        }

        vvddi g(n, vddi());
        for(int i = 0; i < m; ++i) {
            cin >> u >> v >> t >> P >> d;
            di first(d,v);
            di second(t,P);
            g[u].push_back(ddi(first, second));
        }
        int value;
        for(int i = 0; i<q; ++i){
            cin >> value;
            if(value == s){
                cout << 0 << endl;
            }
            else{

                double res = dijkstra(g, s, value);
            
                if(res == INF){
                    cout << "Impossible" << endl;
                }
                else{
                    cout << (int)res << endl;
                }
            }
        }
        cout << '\n';
    }
}



