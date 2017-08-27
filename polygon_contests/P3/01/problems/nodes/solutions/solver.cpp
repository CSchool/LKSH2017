#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> x(n);
    for (int i = 0; i < m; ++i)
    {
        int u, v;
        cin >> u >> v;
        x[u - 1]++;
        x[v - 1]++;
    }
    int k;
    cin >> k;
    vector<int> ans;
    for (int i = 0; i < n; ++i)
    {
        if (x[i] >= k)
            ans.push_back(i + 1);
    }
    cout << ans.size() << endl;
    for (int x : ans)
        cout << x << " ";
    cout << endl;
    return 0;
}
