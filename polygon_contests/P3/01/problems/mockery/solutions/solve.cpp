#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int> > x(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> x[i][j];
        }
    }

    int mi = 0, mj = 0, mk = 0;
    int mx = -1;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            for (int k = 0; k < n; ++k)
            {
                if (i == j || j == k || i == k)
                    continue;
                int q = x[i][j] + x[j][k] + x[k][i];
                if (mx == -1 || mx > q)
                {
                    mx = q;
                    mi = i;
                    mj = j;
                    mk = k;
                }
            }
        }
    }
    cout << mi + 1 << " " << mj + 1 << " " << mk + 1 << endl;
    return 0;
}
