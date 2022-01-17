#include <stdio.h>
#include <string.h>

void do_rofi_init(char *envp[]);
void do_rofi_process(const char *value, char *envp[]);
void do_rofi_other(int state, char *envp[]);

int main(int argc, char **argv, char *envp[]){
    const char *rofi_ret_val = "ROFI_RETV";
    
    int state = 0;

    for (int i = 0; envp[i]; i++) {
        char *loc = strchr(envp[i], '=');

        if (memcmp(rofi_ret_val, envp[i], loc - envp[i])) continue;

        char *value = loc + 1;
        sscanf(value, "%i", &state);

        break;
    }

    if (state == 0) do_rofi_init(envp);
    else if (state == 1) do_rofi_process(argv[1], envp);
    else do_rofi_other(state, envp);
}