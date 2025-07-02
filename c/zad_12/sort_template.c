#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
	int day;
	int month;
	int year;
} Date;

#define NAME_MAX  20   
#define FOOD_MAX  30   
#define RECORD_MAX 64  

typedef struct {
	char name[NAME_MAX];
	float price;
	int amount;
	Date exp_date;
} Food;

typedef int (*CompareFp)(const void *, const void *);

int cmp_date(const void *d1, const void *d2) {
	const Date *date1 = (const Date *)d1;
	const Date *date2 = (const Date *)d2;
	
	if (date1->year != date2->year)
		return date1->year - date2->year;
	if (date1->month != date2->month)
		return date1->month - date2->month;
	return date1->day - date2->day;
}

int cmp(const void *a, const void *b) {
	const Food *food1 = (const Food *)a;
	const Food *food2 = (const Food *)b;
	
	int name_cmp = strcmp(food1->name, food2->name);
	if (name_cmp != 0)
		return name_cmp;
	
	if (food1->price < food2->price)
		return -1;
	if (food1->price > food2->price)
		return 1;
	
	return cmp_date(&food1->exp_date, &food2->exp_date);
}

void* bsearch2 (const void *key, const void *base, const size_t n_items,
		const size_t size, const CompareFp compare, char *result) {
	if (n_items == 0) {
		*result = 0;
		return (void *)base;
	}
	
	const char *arr = (const char *)base;
	size_t left = 0, right = n_items;
	
	while (left < right) {
		size_t mid = left + (right - left) / 2;
		const void *mid_ptr = arr + mid * size;
		int cmp_result = compare(key, mid_ptr);
		
		if (cmp_result == 0) {
			*result = 1;
			return (void *)mid_ptr;
		} else if (cmp_result < 0) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	
	*result = 0;
	return (void *)(arr + left * size);
}

Food* add_record(Food *tab, int *np, const CompareFp compare, const Food *new) {
	char result;
	Food *pos = (Food *)bsearch2(new, tab, *np, sizeof(Food), compare, &result);
	
	if (result) {
		pos->amount += new->amount;
		return pos;
	}
	
	int insert_idx = pos - tab;
	for (int i = *np; i > insert_idx; i--) {
		tab[i] = tab[i-1];
	}
	
	tab[insert_idx] = *new;
	(*np)++;
	
	return &tab[insert_idx];
}

int read_goods(Food *tab, FILE *stream, const int sorted) {
	int n = 0;
	int num_lines;
	fscanf(stream, "%d", &num_lines);
	
	for (int i = 0; i < num_lines; i++) {
		Food new_food;
		fscanf(stream, "%s %f %d %d.%d.%d", 
			   new_food.name, &new_food.price, &new_food.amount,
			   &new_food.exp_date.day, &new_food.exp_date.month, &new_food.exp_date.year);
		
		if (sorted) {
			add_record(tab, &n, cmp, &new_food);
		} else {
			tab[n] = new_food;
			n++;
		}
	}
	
	return n;
}

void print_art(Food *food_tab, const int n, const char *name) {
	for (int i = 0; i < n; i++) {
		if (strcmp(food_tab[i].name, name) == 0) {
			printf("%.2f %d %02d.%02d.%d\n", 
				   food_tab[i].price, food_tab[i].amount,
				   food_tab[i].exp_date.day, food_tab[i].exp_date.month, food_tab[i].exp_date.year);
		}
	}
}

float value(Food *food_tab, const size_t n, const Date curr_date, const int days) {
	qsort(food_tab, n, sizeof(Food), (int(*)(const void*, const void*))cmp_date);
	
	struct tm tm_curr = {0};
	tm_curr.tm_mday = curr_date.day;
	tm_curr.tm_mon = curr_date.month - 1;
	tm_curr.tm_year = curr_date.year - 1900;
	
	time_t time_curr = mktime(&tm_curr);
	time_curr += days * 24 * 60 * 60;
	
	struct tm *tm_target = localtime(&time_curr);
	Date target_date;
	target_date.day = tm_target->tm_mday;
	target_date.month = tm_target->tm_mon + 1;
	target_date.year = tm_target->tm_year + 1900;
	
	float total_value = 0.0f;
	
	for (size_t i = 0; i < n; i++) {
		if (cmp_date(&food_tab[i].exp_date, &target_date) == 0) {
			total_value += food_tab[i].price * food_tab[i].amount;
		}
	}
	
	return total_value;
}

int read_int() {
	char buff[RECORD_MAX];
	int value;
	fgets(buff, RECORD_MAX, stdin);
	sscanf(buff, "%d", &value);
	return value;
}

int main(void) {

	int n;
	Food food_tab[FOOD_MAX];
	char buff[RECORD_MAX];
	const int to_do = read_int();

	switch (to_do) {
		case 1:  
			n = read_goods(food_tab, stdin, 1);
			scanf("%s", buff);
			print_art(food_tab, n, buff);
			break;
		case 2: 
			n = read_goods(food_tab, stdin, 0);
			Date curr_date;
			int days;
			scanf("%d %d %d", &curr_date.day, &curr_date.month, &curr_date.year);
			scanf("%d", &days);
			printf("%.2f\n", value(food_tab, (size_t)n, curr_date, days));
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
	}
	return 0;
}