/**
 * Validates that the input contains the only token token.
 * This token can contain only lowercase latin letters a-z. The length should be between 1 and 100, inclusive.
 * Also validates that file ends with EOLN and EOF.
 */

#include "testlib.h"

using namespace std;

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);
    
    string a = inf.readToken("[a-h][1-8]", "a");
    inf.readEoln();
    string b = inf.readToken("[a-h][1-8]", "b");
    inf.readEoln();
    ensuref(a != b, "first cell cannot be equal to last cell");
    inf.readEof();

    return 0;
}
