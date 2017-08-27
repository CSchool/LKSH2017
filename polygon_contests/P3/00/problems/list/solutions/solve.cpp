#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<bool> x(n + 1);
    for (int i = 0; i < m; ++i)
    {
        int t;
        cin >> t;
        x[t - 1] = 1;
    }
    int b = -1;
    bool pp = false;
    for (int i = 0; i <= n; ++i)
    {
        if (b == -1)
        {
            if (x[i])
                b = i;
        }
        else
        {
            if (!x[i])
            {
                if (pp)
                    cout << ",";
                if (i > b + 1)
                    cout << b + 1 << "-" << i;
                else
                    cout << i;
                pp = 1;
                b = -1;
            }
        }
    }
    cout << endl;
    return 0;
}
