#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TEXTS 20

int is_over(char *text) {
    while (*text != '\0') {
        if (*text == '_') {
            return 0;
        }
        text++;
    }
    return 1;
}

int guess_a_letter(char* text, const char* original_text) {
    char letter = 'A' + rand() % ('Z' - 'A' + 1);

    const char *tmp_org = original_text;
    char *tmp_text = text;
    int found = 0;

    while (*tmp_org != '\0') {
        if (*tmp_org == letter && *tmp_text == '_') {
            *tmp_text = letter;
            found = 1;
        }
        tmp_org++;
        tmp_text++;
    }

    return found;
}

char* play(const char* original_text, const int number_of_players, const int turns, int* p_player) {
    int length = strlen(original_text);

    char *text = (char*)malloc((length + 1) * sizeof(char));
    if (!text) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    for (int i = 0; i < length; i++) {
        text[i] = (original_text[i] == ' ') ? ' ' : '_';
    }
    text[length] = '\0';

    int current_player = 0;
    int rounds_played = 0;
    *p_player = current_player;

    while (rounds_played < turns) {
        if (is_over(text)) {
            break;
        }

        int result = guess_a_letter(text, original_text);

        if (result == 0) {
            current_player = (current_player + 1) % number_of_players;
            *p_player = current_player;
            rounds_played++;
        }
    }

    return text;
}

int main() {

    const char* texts[MAX_TEXTS] = {
        "PAN TADEUSZ",
        "HENRYK SIENKIEWICZ",
        "MORZE KASPIJSKIE",
        "POGODA DLA BOGACZY",
        "CZERWONE GITARY",
        "KAZANIE PIOTRA SKARGI",
        "QUO VADIS",
        "ADAM MICKIEWICZ",
        "ALBERT EINSTEIN",
        "DENNIS RITCHIE",
        "FIZYKA KWANTOWA",
        "PROGRAMOWANIE IMPERATYWNE",
        "ALGORYTMY I STRUKTURY DANYCH",
        "BRIAN KERNIGHAN",
        "CZERWONY KAPTUREK",
        "MARIA KONOPNICKA",
        "WILLIAM SHAKESPEARE",
        "ZBIGNIEW ZAPASIEWICZ",
        "MAGDALENA SAMOZWANIEC",
        "JEZIORO ONTARIO"
    };

    int number_of_players, turns, player;
    unsigned seed;

    scanf("%d %u %d", &number_of_players, &seed, &turns);
    srand(seed);
    const int number = rand() % MAX_TEXTS;
    char* text = play(texts[number], number_of_players, turns, &player);
    printf("%s\n", text);
    printf("%d\n", player);
    free(text);

    return 0;
}