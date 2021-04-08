#include "A/index.h"
#include "B/lib.h"

int main() {
    const char* c = "1315";
    char* ptr;
    printf("%ld\n", (string_to_number(c, &ptr, 10)));
}
