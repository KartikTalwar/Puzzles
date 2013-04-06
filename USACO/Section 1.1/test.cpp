/*
ID: talwar.1
PROG: test
LANG: C++
*/

/*
 * The simplest program on the training pages:
 * read in two integers from a single line and print their sum.
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    int a, b;
    fin >> a >> b;
    fout << a+b << endl;
    return 0;
}

