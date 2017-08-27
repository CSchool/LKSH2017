#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n, m;
    cin >> n >> m;
    std::vector<int> x(n);
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        x[a - 1]++;
        x[b - 1]++;
    }
    for (int i = 0; i < n; ++i)
        cout << x[i] << " ";
    cout << endl;
}
