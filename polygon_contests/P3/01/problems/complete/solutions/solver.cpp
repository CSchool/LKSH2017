#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> x(n, vector<bool>(n, false));
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        x[a - 1][b - 1] = 1;
        x[b - 1][a - 1] = 1;
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (i == j) continue;
            if (!x[i][j])
            {
                cout << "NO\n";
                return 0;
            }
        }
    }
    cout << "YES\n";
}
