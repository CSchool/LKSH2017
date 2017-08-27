#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cstdio>

using namespace std;

pair<int, int> read()
{
    string s;
    cin >> s;
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

int main()
{
    pair<int, int> a, b;
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

    vector<pair<int, int>> o;
    while (b != a)
    {
        o.push_back(b);
        b = p[b.first][b.second];
    }
    o.push_back(a);
    for (auto it = o.rbegin(); it != o.rend(); ++it)
        write(*it);
}
