#include "testlib.h"

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

using namespace std;
vector<vector<int>> c;
vector<bool> u;

void dfs(int v)
{
    ensuref(!u[v], "forest can't contain cycles, loops and parallel edges");
    u[v] = 1;
    for (int x : c[v])
        dfs(x);
}

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int n = inf.readInt(2, 100, "n");
    inf.readSpace();
    int a = inf.readInt(1, n, "a");
    inf.readSpace();
    int b = inf.readInt(1, n, "b");
    inf.readEoln();
    ensuref(a != b, "a can't be equal to b");
    c.resize(n);
    u.resize(n, false);
    vector<int> r;

    for (int i = 0; i < n; ++i)
    {
        int x = inf.readInt(0, n, "p_i");
        if (i < n - 1)
            inf.readSpace();
        else
            inf.readEoln();
        if (x > 0)
            c[x - 1].push_back(i);
        else
            r.push_back(i);
    }
    inf.readEof();

    for (int i : r)
    {
        if (!u[i])
            dfs(i);
    }

    for (int i = 0; i < n; ++i)
        ensuref(u[i], "some vertices are not reachable from roots");

    return 0;
}
