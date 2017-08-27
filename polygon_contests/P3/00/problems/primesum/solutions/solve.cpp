#include <iostream>

using namespace std;

int main()
{
    long long a, b, c;
    long long p;
    cin >> a >> b >> c;
    p = a + b + c;
    for (long long i = 2; i * i <= p; ++i)
    {
        if (p % i == 0)
        {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}
