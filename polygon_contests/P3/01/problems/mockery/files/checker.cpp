#include "testlib.h"
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
const double EPS = 1.5E-6;

int main(int argc, char * argv[])
{
    setName("mockery checker");
    registerTestlibCmd(argc, argv);
    int n = inf.readInt();
    vector<vector<int> > x(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            x[i][j] = inf.readInt();
        }
    }

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
                }
            }
        }
    }

    int i = ouf.readInt(1, n) - 1;
    int j = ouf.readInt(1, n) - 1;
    int k = ouf.readInt(1, n) - 1;
    if (i == j || j == k || i == k)
        quitf(_wa, "two vertices match");
    int q = x[i][j] + x[j][k] + x[k][i];
    if (q < mx)
        quitf(_fail, "participant's output is better");
    if (q > mx)
        quitf(_wa, "not good enough");
    quitf(_ok, "ok");
}
