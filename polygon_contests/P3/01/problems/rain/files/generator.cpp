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

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (rnd.next(0, 99) < p)
            {
                int a = i + 1;
                int b = j + 1;
                if (rnd.next(0, 1) == 0)
                    swap(a, b);
                g.push_back(make_pair(a, b));
            }
        }
    }

    cout << n << " " << g.size() << endl;
    for (auto x : g)
    {
        cout << x.first << " " << x.second << endl;
    }

    for (int i = 0; i < n; ++i)
    {
	cout << rnd.next(1, 3) << ((i == n - 1) ? "\n" : " ");
    }

    return 0;
}
