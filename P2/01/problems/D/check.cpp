#include <iostream>
#include "testlib.h"


using namespace std;

int main(int argc, char * argv[]) {
    setName("p2_A_05");
    registerTestlibCmd(argc, argv);

    // счастливые билеты

    set<string> data;
	ostringstream stream;
	
	for (int a = 0; a < 10; ++a)
		for (int b = 0; b < 10; ++b)
			for (int c = 0; c < 10; ++c)
				for (int d = 0; d < 10; ++d)
					for (int e = 0; e < 10; ++e)
						for (int f = 0; f < 10; ++f)
							if (a + b + c == d + e + f) {
								stream.str("");
								stream.clear();

								stream << a << b << c << d << e << f;
								data.insert(stream.str());
							}
	
	/*
	for (set<string>::iterator it = data.begin(); it != data.end(); ++ it)
		cout << *it << endl;

	cout << data.size();
	*/

	
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
