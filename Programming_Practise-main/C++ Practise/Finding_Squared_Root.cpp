/**
 
 Finding the roots of quadratic equation
 axsquare + bx + c = 0
 
 
 Output :
 Enter the input for a b and c 3 4 5
 Squared Roots are -2147483648-2147483648Program ended with exit code: 0
 
 */

# include <iostream>
using namespace std;

int main()
{
    // Declaring the variables
    int a,b, c, r1, r2;
    // entering the input
    cout<< "Enter the input for a b and c ";
    cin>> a>>b>>c;
    r1 = (-b +sqrt(b*b-4*a*c))/(2*a);
    r2 = (-b -sqrt(b*b-4*a*c))/(2*a);
    
    cout<<"Squared Roots are " <<r1<<r2;
    
    
    
}
