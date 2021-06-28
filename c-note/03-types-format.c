Types, format codes

There are many data types we can use for our variables, which indicate to the computer what type of data they represent:
bool, a Boolean expression of either true or false
char, a single ASCII character like a or 2
double, a floating-point value with more digits than a float
float, a floating-point value, or real number with a decimal value
int, integers up to a certain size, or number of bits
long, integers with more bits, so they can count higher than an int
string, a string of characters

And the CS50 library has corresponding functions to get input of various types:
get_char
get_double
get_float
get_int
get_long
get_string

For printf, too, there are different placeholders for each type:
%c for chars
%f for floats, doubles
%i for ints
%li for longs
%s for strings
  
