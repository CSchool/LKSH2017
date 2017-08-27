#include <iostream>

using namespace std;

int x[10];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= m; ++j)
        {
            int q = i * j;
            while (q)
            {
                x[q % 10]++;
                q /= 10;
            }
        }
    }
    for (int i = 0; i < 10; ++i)
    {
        cout << x[i] << endl;
    }
    return 0;
}
