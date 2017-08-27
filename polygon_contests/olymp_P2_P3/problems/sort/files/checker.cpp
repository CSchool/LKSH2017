#include "testlib.h"

using namespace std;

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);
    int n = inf.readInt();
    int a[n];
    for (int i = 0; i < n; i++) {
        a[i] = inf.readInt();
    }
    int k = ouf.readInt();
    if (k < 0 || k >= 50000)
         quitf(_wa, "Wrong number of operations");
    for(int i = 0; i < k; i++) {
      int ind1 = ouf.readInt(), ind2 = ouf.readInt();
      if(ind1 < 1 || ind1 > n || ind2 < 1 || ind2 > n)
         quitf(_wa, "Incorrect index");
      ind1--;
      ind2--;
      if(a[ind1] - a[ind2] != 1 && a[ind1] - a[ind2] != -1)
         quitf(_wa, "Wrong operation");
      int tmp = a[ind1];
      a[ind1] = a[ind2];
      a[ind2] = tmp;
    }

    for(int i = 0; i < n - 1; i++)
      if(a[i] > a[i + 1])
        quitf(_wa, "Wrong order");

    quitf(_ok, "ok");

    return 0;
}
