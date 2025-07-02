#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>

double sum_var (int number, ...) {
	va_list args;
	double suma = 0;

	va_start(args, number);

	for(int i = 0; i < number; i++){
		suma += va_arg(args, double);
	}

	va_end(args);

	return suma;
}

double average_var (int number, ...) {
	va_list args;
	double suma = 0;

	va_start(args, number);

	for(int i = 0; i < number; i++){
		suma += va_arg(args, double);
	}

	va_end(args);

	return suma / number;
}

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

double median_var (int number, ...) {
	va_list args;
	va_start(args, number);
	double *tab = malloc(number * sizeof(double));

	for(int i = 0; i < number; i++){
		tab[i] = va_arg(args, double);
	}

	va_end(args);

	for (int i = 0; i < number - 1; i++) {
        for (int j = 0; j < number - i - 1; j++) {
            if (tab[j] > tab[j + 1]) {
                double temp = tab[j];
                tab[j] = tab[j + 1];
                tab[j + 1] = temp;
            }
        }
    }
	
	double result;
    int ind = number / 2;
    
    if (number % 2) { 
        result = tab[ind];
    }
    else { 
        result = (tab[ind - 1] + tab[ind]) / 2.00;
    }

    free(tab); 
    return result;
}

double min_var (int number, ...) {
	va_list args;
	double result = 0;
	double arg;

	va_start(args, number);

	for(int i = 0; i < number; i++){
		arg = va_arg(args, double);
		if (i == 0){
			result = arg;
		}
		if (result > arg){
			result = arg;
		}
	}

	va_end(args);

	return result;
}

double max_var (int number, ...) {
	va_list args;
	double result = 0;
	double arg;

	va_start(args, number);

	for(int i = 0; i < number; i++){
		arg = va_arg(args, double);
		if (i == 0){
			result = arg;
		}
		if (result < arg){
			result = arg;
		}
	}

	va_end(args);

	return result;
}

#define MAX_LINE 256
#define MAX_NUMBER 64
#define MAX_TEXTS 64

double sum(const int number, const double* values) {
    double result = 0.0;
    for (int i = 0; i < number; i++) {
        result += values[i];
    }
    return result;
}

double average(const int number, const double* values) {
    if (number <= 0) return 0.0;
    return sum(number, values) / number;
}

int compare_doubles(const void* a, const void* b) {
    double diff = *(const double*)a - *(const double*)b;
    if (diff < 0) return -1;
    if (diff > 0) return 1;
    return 0;
}

double median(const int number, double* values) {
    if (number <= 0) return 0.0;
    
    qsort(values, number, sizeof(double), compare_doubles);
    
    if (number % 2 == 0) {
        return (values[number/2 - 1] + values[number/2]) / 2;
    } else {
        return values[number/2];
    }
}

double min(const int number, const double* values) {
    if (number <= 0) return 0.0;
    
    double min_val = values[0];
    for (int i = 1; i < number; i++) {
        if (values[i] < min_val) {
            min_val = values[i];
        }
    }
    return min_val;
}

double max(const int number, const double* values) {
    if (number <= 0) return 0.0;
    
    double max_val = values[0];
    for (int i = 1; i < number; i++) {
        if (values[i] > max_val) {
            max_val = values[i];
        }
    }
    return max_val;
}

int read_from_line(char* c_buf, double *values, char** texts, int* text_counter) {
    int value_counter = 0;
    *text_counter = 0;

    char* token = strtok(c_buf, " ");
    
    while (token != NULL) {
        char* endptr;
        double value = strtod(token, &endptr);

        if (*endptr == '\0') {
            values[value_counter++] = value;
        } 
        else if (endptr != token) {
            char number_part[256] = {0};
            int i;
            
            for (i = 0; i < (endptr - token); i++) {
                number_part[i] = token[i];
            }
            number_part[i] = '\0';
            
            value = strtod(number_part, NULL);
            values[value_counter++] = value;
            
            texts[*text_counter] = (char*)malloc(strlen(endptr) + 1);
            strcpy(texts[*text_counter], endptr);
            (*text_counter)++;
        } 
        else {
            texts[*text_counter] = (char*)malloc(strlen(token) + 1);
            strcpy(texts[*text_counter], token);
            (*text_counter)++;
        }
        
        token = strtok(NULL, " ");
    }
    
    return value_counter;
}

int read_int(void) {
	char c_buf[MAX_LINE];
	fgets(c_buf, MAX_LINE, stdin);
	return (int)strtol(c_buf, NULL, 10);
}

int main(void) {
	int number;
	double v1, v2, v3, v4, v5;

	char c_buf[MAX_LINE];
	double values[MAX_NUMBER];
	char* texts[MAX_TEXTS];
	int text_counter;

	const int to_do = read_int();

	switch (to_do) {
		case 1:
			number = 3;
			scanf("%lf%lf%lf", &v1, &v2, &v3);
			printf("%.2f %.2f %.2f %.2f %.2f\n",
					sum_var(number, v1, v2, v3),
					average_var(number, v1, v2, v3),
					median_var(number, v1, v2, v3),
					min_var(number, v1, v2, v3),
					max_var(number, v1, v2, v3));

			number = 5;
			scanf("%lf%lf%lf%lf%lf", &v1, &v2, &v3, &v4, &v5);
			printf("%.2f %.2f %.2f %.2f %.2f\n",
					sum_var(number, v1, v2, v3, v4, v5),
					average_var(number, v1, v2, v3, v4, v5),
					median_var(number, v1, v2, v3, v4, v5),
					min_var(number, v1, v2, v3, v4, v5),
					max_var(number, v1, v2, v3, v4, v5));
			break;
		case 2:
			fgets(c_buf, MAX_LINE, stdin);
			number = read_from_line(c_buf, values, texts, &text_counter);
			printf("%.2f %.2f %.2f %.2f %.2f\n",
					sum(number, values),
					average(number, values),
					median(number, values),
					min(number, values),
					max(number, values));

			for (int k = 0; k < text_counter; k++) {
				printf("%s\n", texts[k]);
			}
			break;
		default:
			printf("Nothing to do for n = %d\n", to_do);
			break;
	}

	return EXIT_SUCCESS;
}

