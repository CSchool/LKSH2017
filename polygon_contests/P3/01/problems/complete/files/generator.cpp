
#include "testlib.h"
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    registerGen(argc, argv, 1);

    int n = rnd.next(1, atoi(argv[1]));
    int p = atoi(argv[2]);
    vector<pair<int, int>> g;

    if (n > 1)
    {
        int q = 200 / (n - 1);

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j <= i; ++j)
            {
                int ii = 0;
                while (rnd.next(0, 100) < p && ii < q)
                {
                    int a = i + 1;
                    int b = j + 1;
                    if (rnd.next(0, 1) == 0)
                        swap(a, b);
                    g.push_back(make_pair(a, b));
                    ii++;
                }
            }
        }
    }
    shuffle(g.begin(), g.end());

    cout << n << " " << g.size() << endl;
    for (auto x : g)
    {
        cout << x.first << " " << x.second << endl;
    }

    return 0;
}
