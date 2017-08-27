#include<cstdio>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
  //freopen("sort.in", "r", stdin);
  //freopen("sort.out", "w", stdout);
  int n;
  cin >> n;
  vector<int> a(n), p(n + 1);
  for(int i = 0; i < n; i++)
    cin >> a[i], p[a[i]] = i;
  vector<pair<int, int> > ans;
  /*for(int j = 0; j < n; j++)
    cout << a[j] << ' ';
  cout << endl; */
  for(int i = 0; i < n; i++)
    while(a[i] != i + 1)
    {
      int t = p[a[i] - 1];
      swap(p[a[i]], p[a[i] - 1]);
      swap(a[i], a[t]);
      ans.push_back(make_pair(i + 1, t + 1));
      /*for(int j = 0; j < n; j++)
        cout << a[j] << ' ';
      cout << endl;*/
    } 
  cout << ans.size() << endl;
  for(int i = 0; i < (int)ans.size(); i++)
    cout << ans[i].first << ' ' << ans[i].second << endl;
  return 0;
}

