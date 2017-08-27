#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cstdio>
#include "testlib.h"

using namespace std;

pair<int, int> read()
{
    string s = inf.readString();
    return make_pair(s[0] - 'a', s[1] - '1');
}

pair<int, int> oread()
{
    string s = ouf.readToken("[a-h][1-8]");
    ouf.readEoln();
    return make_pair(s[0] - 'a', s[1] - '1');
}

void write(pair<int, int> x)
{
    printf("%c%c\n", x.first + 'a', x.second + '1');
}

bool u[8][8];
pair<int, int> p[8][8];

int dx[] = {1, 1, 2, 2, -1, -1, -2, -2};
int dy[] = {2, -2, 1, -1, 2, -2, 1, -1};
pair<int, int> a, b;

int solve()
{
    a = read();
    b = read();

    queue<pair<int, int>> q;
    u[a.first][a.second] = 1;
    q.push(a);
    while (!q.empty())
    {
        pair<int, int> v = q.front();
        q.pop();
        for (int i = 0; i < 8; ++i)
        {
            pair<int, int> w = make_pair(v.first + dx[i], v.second + dy[i]);
            if (w.first < 0) continue;
            if (w.first > 7) continue;
            if (w.second < 0) continue;
            if (w.second > 7) continue;
            if (u[w.first][w.second]) continue;
            u[w.first][w.second] = 1;
            p[w.first][w.second] = v;
            q.push(w);
        }
    }

    int ans = 1;
    auto v = b;
    while (v != a)
    {
        ans++;
        v = p[v.first][v.second];
    }
    return ans;
}

bool was[8][8];

int main(int argc, char * argv[])
{
    setName("checker for [knight]");
    registerTestlibCmd(argc, argv);
    int corr = solve();
    auto x = oread();
    if (x != a)
        quitf(_wa, "First cell of output is not first cell of input");
    int ans = 1;
    was[x.first][x.second] = 1;
    while (!ouf.eof())
    {
        auto y = oread();
        if (was[y.first][y.second])
            quitf(_wa, "repeating cells in output");
        was[y.first][y.second] = 1;
        bool ok = false;
        for (int i = 0; i < 8; ++i)
        {
            if (make_pair(x.first + dx[i], x.second + dy[i]) == y)
            {
                ok = true;
                break;
            }
        }
        if (ok)
        {
            x = y;
            ans++;
        }
        else
        {
            quitf(_wa, "Two cells are not connected by knight's move");
        }
    }
    if (x != b)
        quitf(_wa, "Last cell of output is not second cell of input");
    // if (ans > corr)
    //    quitf(_wa, "Path is too long");
    if (ans < corr)
        quitf(_fail, "Participant found shorter path");
    quitf(_ok, "%d cells", ans);
}
