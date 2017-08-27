/*
 * Outputs random 100-digits binary string mostly containing 0's. 
 * In average it contrains only 10% of 1's.
 *
 * To generate different values, call "bgen.exe" with different parameters.
 * 
 * It is typical behaviour of testlib generator to setup randseed by command line.
 */

#include "testlib.h"
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    registerGen(argc, argv, 1);

    string a, b;
    do
    {
        a = rnd.next("[a-h][1-8]");
        b = rnd.next("[a-h][1-8]");
    } while (a == b);

    cout << a << endl;
    cout << b << endl;

    return 0;
}
