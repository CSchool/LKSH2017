#include <iostream>
#include "testlib.h"


using namespace std;

int main(int argc, char * argv[]) {
    setName("p2_A_01");
    registerTestlibCmd(argc, argv);

    // 100 .. 1000 делится на 5, вторая цифра - 3

    set<int> data;

    for (int i = 100; i < 1001; ++i) {
        if (i % 5 == 0 && ((i / 10) % 10 == 3))
            data.insert(i);
    }

	for (set<int>::iterator it = data.begin(); it != data.end(); ++it)
		cout << *it << endl;

	
	while (!ouf.seekEof()) {
		int value = ouf.readInt(100, 1000);
		auto it = data.find(value); 
		if (data.find(value) == data.end())
			quitf(_wa, "Value %d is not allowed here!", value);
		data.erase(it);
	}

	if (data.size() == 0)
		quitf(_ok, "Everything is ok");
	else
		quitf(_wa, "Some values is not mentioned here");
	return 0;
}
