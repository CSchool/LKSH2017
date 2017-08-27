#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int> > x(n, vector<int>(m));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cin >> x[i][j];
        }
    }
    int q, s = 0;
    cin >> q;
    for (int i = 0; i < q; ++i)
    {
        int a, b;
        cin >> a >> b;
        s += x[a - 1][b - 1];
    }
    cout << s << endl;
    return 0;
}
