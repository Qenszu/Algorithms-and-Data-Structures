#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#define TAB_SIZE  1000
#define BUF_SIZE  1000

// 1
////////////////////////////////////////////////////////////

int get(int cols, int row, int col, const int* A) {
	return *(A + row * cols + col);
}

void set(int cols, int row, int col, int* A, int value) {
	*(A + row * cols + col) = value;
}

int count_val(int* A, int* B, int rowsA, int colsA, int colsB, int i, int j){
	int val = 0;
	for(int a = 0; a < colsA; ++a){
		val += get(colsA, i, a, A) * get(colsB, a, j, B);
	}
	return val;
}

void prod_mat(int rowsA, int colsA, int colsB, int* A, int* B, int* AB) {
	int val;
	for(int i = 0; i < rowsA; i++){
		for(int j = 0; j < colsB; j++){
			set(colsB, i, j, AB, count_val(A, B, rowsA, colsA, colsB, i, j));
		}
	}
}

void read_mat(int rows, int cols, int* t) {
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < cols; j++){
			scanf("%d", t + i * cols + j);
		}
	}
}

void print_mat(int rows, int cols, int* t) {
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < cols; j++){
			printf("%d ", get(cols, i, j, t));
		}
		printf("\n");
	}
}

// 2
/////////////////////////////////////////////////////////////

int read_int_lines_cont(int* ptr_array[]) {
    char buffer[1024];
    int line_count = 0;
    int total_numbers = 0;
    
    // Pierwsze przejście - zliczanie linii i liczb
    while (fgets(buffer, sizeof(buffer), stdin)) {
        if (buffer[0] == '\n') continue;
        line_count++;
        char* token = strtok(buffer, " \n");
        while (token != NULL) {
            total_numbers++;
            token = strtok(NULL, " \n");
        }
    }
    
    // Alokacja pamięci
    int* data_block = malloc(total_numbers * sizeof(int));
    rewind(stdin);  // Przewijamy stdin do początku
    
    // Drugie przejście - wczytywanie danych
    int data_index = 0;
    for (int i = 0; i < line_count; i++) {
        fgets(buffer, sizeof(buffer), stdin);
        if (buffer[0] == '\n') {
            i--;
            continue;
        }
        
        ptr_array[i] = &data_block[data_index];
        char* token = strtok(buffer, " \n");
        while (token != NULL) {
            data_block[data_index++] = atoi(token);
            token = strtok(NULL, " \n");
        }
    }
    
    return line_count;
}

void write_int_line_cont(int* ptr_array[], int n) {
    int* line = ptr_array[n-1];  // n jest liczone od 1
    // Zakładamy, że wiersz kończy się na 0 (można dodać dodatkowy parametr z długością)
    int i = 0;
    while (line[i] != 0) {  // Tymczasowe rozwiązanie
        printf("%d ", line[i]);
        i++;
    }
    printf("\n");
}
// 3
///////////////////////////////////////////////////////////

int read_char_lines(char *array[]) {
    int line_count = 0;
    char buffer[1024]; // Tymczasowy bufor na wiersz
    
    // Wczytaj liczbę wierszy do wypisania (ignorujemy w tej funkcji)
    int lines_to_print;
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        sscanf(buffer, "%d", &lines_to_print);
    }
    
    // Wczytuj linie aż do końca danych (EOF)
    while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        // Pomijaj puste linie
        if (buffer[0] == '\n') continue;
        
        // Usuń znak nowej linii jeśli istnieje
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len-1] == '\n') {
            buffer[len-1] = '\0';
        }
        
        // Alokuj pamięć dla wiersza
        array[line_count] = malloc(len + 1); // +1 dla '\0'
        if (array[line_count] == NULL) {
            perror("Błąd alokacji pamięci");
            exit(EXIT_FAILURE);
        }
        
        // Skopiuj zawartość bufora
        strcpy(array[line_count], buffer);
        line_count++;
    }
    
    return line_count;
}

void write_char_line(char *array[], int n) {
    // Indeksy liczone od 1, więc zmniejszamy o 1
    int index = n - 1;
    if (array[index] != NULL) {
        printf("%s\n", array[index]);
    }
}

void delete_lines(char *array[]) {
    for (int i = 0; array[i] != NULL; i++) {
        free(array[i]);
        array[i] = NULL;
    }
}
// auxiliary
////////////////////////////////////////////////////////////

int read_int(void) {
	char c_buf[BUF_SIZE];
	fgets(c_buf, BUF_SIZE, stdin);
	return (int)strtol(c_buf, NULL, 10);
}

int main(void) {
	const int to_do = read_int();

	int A[TAB_SIZE], B[TAB_SIZE], AB[TAB_SIZE];
	int n, rowsA, colsA, rowsB, colsB;
	char* char_lines_array[TAB_SIZE] = { NULL };
	int continuous_array[TAB_SIZE];
	int* ptr_array[TAB_SIZE];

	switch (to_do) {
		case 1:
			scanf("%d %d", &rowsA, &colsA);
			read_mat(rowsA, colsA, A);
			scanf("%d %d", &rowsB, &colsB);
			read_mat(rowsB, colsB, B);
			prod_mat(rowsA, colsA, colsB, A, B, AB);
			print_mat(rowsA, colsB, AB);
			break;
		case 2:
			n = read_int() - 1; // we count from 0 :)
			ptr_array[0] = continuous_array;
			read_int_lines_cont(ptr_array);
			write_int_line_cont(ptr_array, n);
			break;
		case 3:
			n = read_int() - 1;
			read_char_lines(char_lines_array);
			write_char_line(char_lines_array, n);
			delete_lines(char_lines_array);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

