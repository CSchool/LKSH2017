#include <iostream>
#include "testlib.h"


using namespace std;

int main(int argc, char * argv[]) {
    setName("p2_A_02");
    registerTestlibCmd(argc, argv);

    // 1000 ... 9999, оканчивается на 5, 2 цифра + 3 цифра = 7

    set<int> data;

    for (int i = 1000; i < 9999; ++i) {
        if (i % 10 == 5) {
			int second = (i / 10) % 10;
			int third = (i / 100) % 10;
			if (second + third == 7)
				data.insert(i);
		}
    }

	while (!ouf.seekEof()) {
		int value = ouf.readInt(1000, 9999);
		auto it = data.find(value);
		if (it == data.end())
			quitf(_wa, "Value %d is not allowed here!", value);
		data.erase(it);
	}

	if (data.size() == 0)
		quitf(_ok, "Everything is ok");
	else
	quitf(_wa, "Something is not mentioned here!");
    return 0;
}
