#include "lib.h"

long int string_to_number(const char* s, char** ptr, int n) {
    return strtol(s, ptr, n);
}
