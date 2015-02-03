#include <stdio.h>
#include <string.h>

void reverse(char s[], int len);

int main() {
    char s[] = "Reverse me!";
    reverse(s, strlen(s));
    printf("%s\n", s);
}

void reverse(char s[]) {
    int i, j;
    char tmp;
    int len = strlen(s);
    for (i = 0, j = len - 1; i < len / 2; i++, j--) {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}
