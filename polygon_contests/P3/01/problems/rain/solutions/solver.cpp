#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;
	vector<vector<int>> adj(n);
	for (int i = 0; i < m; ++i)
	{
		int a, b;
		cin >> a >> b;
		adj[a - 1].push_back(b - 1);
	}
	vector<int> c(n);
	for (int &x : c)
		cin >> x;
	int ans = 0;
	for (int i = 0; i < n; ++i)
		for (int j : adj[i])
			if (c[i] != c[j])
				ans++;
	cout << ans;
	return 0;
}
