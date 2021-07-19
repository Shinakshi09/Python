/*

Enum Data types = User defined data types
Output : 0
*/

#include <iostream>

using namespace std;

enum day
{
    mon,
    tue,
    wed,
    thu,
    fri,
    sat,
    sun
};

int main()

{
    day d;
    d = mon; // note : We can only assign these values which we have mentioned

    cout << d << endl;
}
