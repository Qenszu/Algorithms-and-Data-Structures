#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#define BUFFER_SIZE 1024

typedef void (*DataFp)(void*);
typedef void (*ConstDataFp)(const void*);
typedef int  (*CompareDataFp)(const void*, const void*);

typedef struct ListElement {
	struct ListElement *next;
	void *data;
} ListElement;

typedef struct {
	ListElement *head;
	ListElement *tail;
	ConstDataFp dump_data;
	DataFp free_data;
	CompareDataFp compare_data;
	DataFp modify_data;
} List;

void *safe_malloc(const size_t size) {
	void *ptr = malloc(size);
	if(ptr) return ptr;
	printf("malloc error\n");
	exit(EXIT_FAILURE);
}

void *safe_strdup(const char *string) {
	void *ptr = safe_malloc(strlen(string) + 1);
	strcpy(ptr, string);
	return ptr;
}

void init_list(List* p_list, const ConstDataFp dump_data, const DataFp free_data,
		const CompareDataFp compare_data, const DataFp modify_data) {
	p_list->head = NULL;
	p_list->tail = NULL;
	p_list->dump_data = dump_data;
	p_list->free_data = free_data;
	p_list->compare_data = compare_data;
	p_list->modify_data = modify_data;
}

void dump_list(const List* p_list) {
	ListElement *current = p_list->head;
	while (current != NULL) {
		p_list->dump_data(current->data);
		current = current->next;
		if (current != NULL) {
			printf(" ");
		}
	}
	printf("\n");
}

void dump_list_if(const List* p_list, const void *data) {
	ListElement *current = p_list->head;
	int first = 1;
	while (current != NULL) {
		if (p_list->compare_data(current->data, data) == 0) {
			if (!first) printf(" ");
			p_list->dump_data(current->data);
			first = 0;
		}
		current = current->next;
	}
	if (!first) printf("\n");
}

void free_list(List* p_list) {
	ListElement *current = p_list->head;
	while (current != NULL) {
		ListElement *next = current->next;
		if (p_list->free_data != NULL) {
			p_list->free_data(current->data);
		}
		free(current);
		current = next;
	}
	p_list->head = NULL;
	p_list->tail = NULL;
}

void push_front(List* p_list, void *data) {
	ListElement *new_element = (ListElement*)safe_malloc(sizeof(ListElement));
	new_element->data = data;
	new_element->next = p_list->head;
	
	p_list->head = new_element;
	if (p_list->tail == NULL) {
		p_list->tail = new_element;
	}
}

void push_back(List* p_list, void *data) {
	ListElement *new_element = (ListElement*)safe_malloc(sizeof(ListElement));
	new_element->data = data;
	new_element->next = NULL;
	
	if (p_list->tail == NULL) {
		p_list->head = p_list->tail = new_element;
	} else {
		p_list->tail->next = new_element;
		p_list->tail = new_element;
	}
}

void pop_front(List* p_list) {
	if (p_list->head == NULL) return;
	
	ListElement *to_remove = p_list->head;
	p_list->head = p_list->head->next;
	
	if (p_list->head == NULL) {
		p_list->tail = NULL;
	}
	
	if (p_list->free_data != NULL) {
		p_list->free_data(to_remove->data);
	}
	free(to_remove);
}

void reverse(List* p_list) {
	ListElement *prev = NULL;
	ListElement *current = p_list->head;
	ListElement *next = NULL;
	
	p_list->tail = p_list->head;
	
	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	
	p_list->head = prev;
}

ListElement* find_insertion_point(const List* p_list, const ListElement* p_element) {
	if (p_list->head == NULL || p_list->compare_data(p_element->data, p_list->head->data) < 0) {
		return NULL;
	}
	
	ListElement *current = p_list->head;
	while (current->next != NULL && p_list->compare_data(p_element->data, current->next->data) >= 0) {
		current = current->next;
	}
	
	return current;
}

void push_after(List* p_list, void* data, ListElement* previous) {
	ListElement *new_element = (ListElement*)safe_malloc(sizeof(ListElement));
	new_element->data = data;
	
	if (previous == NULL) {
		new_element->next = p_list->head;
		p_list->head = new_element;
		if (p_list->tail == NULL) {
			p_list->tail = new_element;
		}
	} else {
		new_element->next = previous->next;
		previous->next = new_element;
		if (previous == p_list->tail) {
			p_list->tail = new_element;
		}
	}
}

void insert_in_order(List* p_list, void* p_data) {
	ListElement temp_element;
	temp_element.data = p_data;
	temp_element.next = NULL;
	
	ListElement *current = p_list->head;
	while (current != NULL) {
		if (p_list->compare_data(current->data, p_data) == 0) {
			if (p_list->modify_data != NULL) {
				p_list->modify_data(current->data);
			}
			if (p_list->free_data != NULL) {
				p_list->free_data(p_data);
			}
			return;
		}
		current = current->next;
	}
	
	ListElement *insertion_point = find_insertion_point(p_list, &temp_element);
	push_after(p_list, p_data, insertion_point);
}

void dump_int(const void* d) {
	printf("%d", *(const int*)d);
}

void free_int(void* d) {
	free(d);
}

int cmp_int(const void* a, const void* b) {
	int val_a = *(const int*)a;
	int val_b = *(const int*)b;
	if (val_a < val_b) return -1;
	if (val_a > val_b) return 1;
	return 0;
}

int* create_data_int(const int v) {
	int *ptr = (int*)safe_malloc(sizeof(int));
	*ptr = v;
	return ptr;
}

typedef struct DataWord {
	char* word;
	int counter;
} DataWord;

void dump_word(const void* d) {
	const DataWord *word_data = (const DataWord*)d;
	printf("%s", word_data->word);
}

void dump_word_lowercase(const void* d) {
	const DataWord *word_data = (const DataWord*)d;
	char *word = word_data->word;
	for (int i = 0; word[i]; i++) {
		printf("%c", tolower(word[i]));
	}
}

void free_word(void* d) {
	DataWord *word_data = (DataWord*)d;
	free(word_data->word);
	free(word_data);
}

int cmp_word_alphabet(const void* a, const void* b) {
	const DataWord *word_a = (const DataWord*)a;
	const DataWord *word_b = (const DataWord*)b;
	return strcasecmp(word_a->word, word_b->word);
}

int cmp_word_counter(const void* a, const void* b) {
	const DataWord *word_a = (const DataWord*)a;
	const DataWord *word_b = (const DataWord*)b;
	if (word_a->counter < word_b->counter) return -1;
	if (word_a->counter > word_b->counter) return 1;
	return 0;
}

void modify_word(void* p) {
	DataWord *word_data = (DataWord*)p;
	word_data->counter++;
}

void* create_data_word(const char* string, const int counter) {
	DataWord *word_data = (DataWord*)safe_malloc(sizeof(DataWord));
	word_data->word = (char*)safe_strdup(string);
	word_data->counter = counter;
	return word_data;
}

void stream_to_list(List* p_list, FILE* stream) {
	const char delimits[] = " \r\t\n.,?!:;-";
	char buffer[BUFFER_SIZE];
	
	while (fgets(buffer, BUFFER_SIZE, stream)) {
		char *token = strtok(buffer, delimits);
		while (token != NULL) {
			if (strlen(token) > 0) {
				void *word_data = create_data_word(token, 1);
				if (p_list->compare_data != NULL) {
					insert_in_order(p_list, word_data);
				} else {
					push_back(p_list, word_data);
				}
			}
			token = strtok(NULL, delimits);
		}
	}
}

void list_test(List* p_list, const int n) {
	char op;
	int v;
	for (int i = 0; i < n; ++i) {
		scanf(" %c", &op);
		switch (op) {
			case 'f':
				scanf("%d", &v);
				push_front(p_list, create_data_int(v));
				break;
			case 'b':
				scanf("%d", &v);
				push_back(p_list, create_data_int(v));
				break;
			case 'd':
				pop_front(p_list);
				break;
			case 'r':
				reverse(p_list);
				break;
			case 'i':
				scanf("%d", &v);
				insert_in_order(p_list, create_data_int(v));
				break;
			default:
				printf("No such operation: %c\n", op);
				break;
		}
	}
}

int main(void) {
	int to_do, n;
	List list;

	scanf ("%d", &to_do);
	switch (to_do) {
		case 1:
			scanf("%d",&n);
			init_list(&list, dump_int, free_int, cmp_int, NULL);
			list_test(&list, n);
			dump_list(&list);
			free_list(&list);
			break;
		case 2:
			init_list(&list, dump_word, free_word, NULL, NULL);
			stream_to_list(&list, stdin);
			dump_list(&list);
			free_list(&list);
			break;
		case 3:
			scanf("%d",&n);
			init_list(&list, dump_word_lowercase, free_word, cmp_word_alphabet, modify_word);
			stream_to_list(&list, stdin);
			list.compare_data = cmp_word_counter;
			const DataWord data = { NULL, n };
			dump_list_if(&list, &data);
			free_list(&list);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}