#include <iostream>
#include "testlib.h"


using namespace std;

int main(int argc, char * argv[]) {
    setName("p2_A_03");
    registerTestlibCmd(argc, argv);


    set<string> data;
	ostringstream stream;

	for (int k = 0; k < 10; ++k)
		for (int o = 0; o < 10; ++o)
			for (int t = 0; t < 10; ++t)
				if (k * 100 + t * 10 + o +
					k * 100 + o * 10 + t ==
					t * 100 + o * 10 + k && k != o && o != t) {
						stream.str("");
						stream.clear();

						stream << k << t << o << "+" << k << o << t << "=" << t << o << k;
						data.insert(stream.str());
				}
	
	for (set<string>::iterator it = data.begin(); it != data.end(); ++ it)
		cout << *it << endl;

	
	while (!ouf.seekEof()) {
		string value = ouf.readLine();
		auto it = data.find(value);
		if (it == data.end())
			quitf(_wa, "Value %s is not allowed here!", value.c_str());
		data.erase(it);
	}

	if (data.size() == 0)
		quitf(_ok, "Everything is ok");
	else
		quitf(_wa, "Something is missing!");
	
    return 0;
}
