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

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int n = inf.readInt(1, 100, "n");
    inf.readSpace();
    int m = inf.readInt(0, n * (n - 1) / 2, "m");
    inf.readEoln();

    set<pair<int,int> > edges;

    forn(i, m)
    {
        int a = inf.readInt(1, n, "a_i");
        inf.readSpace();
        int b = inf.readInt(1, n, "b_i");
        inf.readEoln();

        ensuref(a != b, "Graph can't contain loops");
        ensuref(edges.count(make_pair(a, b)) == 0, "Graph can't contain multiple edges between a pair of vertices");

        edges.insert(make_pair(a, b));
        edges.insert(make_pair(b, a));
    }

    forn(i, n)
    {
	int c = inf.readInt(1, 3, "k_i");
	if (i < n - 1)
		inf.readSpace();
	else
		inf.readEoln();
    }

    inf.readEof();
    return 0;
}
