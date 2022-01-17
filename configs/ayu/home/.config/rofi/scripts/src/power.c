#include "custom-rofi.h"
#include <stdlib.h>

const char *strings[] = {
    "shutdown",
    "reboot",
    "quit",
    NULL
};

void do_rofi_init(char *envp[]) {
    for (int i = 0; strings[i]; i++) {
        printf("%s\n", strings[i]);
    }
}

void do_rofi_process(const char *value, char *envp[]) {
    if (!strcmp(value, strings[0])) {
        system("shutdown now");
    } else if (!strcmp(value, strings[1])) {
        system("reboot");
    }
}

void do_rofi_other(int state, char *envp[]) {
    
}
