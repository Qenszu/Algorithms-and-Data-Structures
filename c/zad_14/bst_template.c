#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_SIZE 32

typedef struct node {
	int number;
	char name[MAX_NAME_SIZE];
	struct node* left;
	struct node* right;
	struct node* parent;
} node;

node* create_node(const int number, const char* name) {
	node* new_node = (node*)malloc(sizeof(node));
	if (new_node == NULL) {
		return NULL;
	}
	
	new_node->number = number;
	strcpy(new_node->name, name);
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->parent = NULL;
	
	return new_node;
}

void delete_tree(node* root) {
	if (root == NULL) {
		return;
	}
	
	delete_tree(root->left);
	delete_tree(root->right);
	
	free(root);
}

node* insert(node* root, node* to_insert) {
	if (to_insert == NULL) {
		return root;
	}
	
	if (root == NULL) {
		return to_insert;
	}
	
	if (to_insert->number < root->number) {
		root->left = insert(root->left, to_insert);
		if (root->left != NULL) {
			root->left->parent = root;
		}
	} else if (to_insert->number > root->number) {
		root->right = insert(root->right, to_insert);
		if (root->right != NULL) {
			root->right->parent = root;
		}
	} else {
		free(to_insert);
	}
	
	return root;
}

node* find(node* root, const int number) {
	if (root == NULL) {
		return NULL;
	}
	
	if (number == root->number) {
		return root;
	} else if (number < root->number) {
		return find(root->left, number);
	} else {
		return find(root->right, number);
	}
}

node* find_min(node* root) {
	while (root != NULL && root->left != NULL) {
		root = root->left;
	}
	return root;
}

node* delete(node* root, const int number) {
	if (root == NULL) {
		return NULL;
	}
	
	if (number < root->number) {
		root->left = delete(root->left, number);
		if (root->left != NULL) {
			root->left->parent = root;
		}
	} else if (number > root->number) {
		root->right = delete(root->right, number);
		if (root->right != NULL) {
			root->right->parent = root;
		}
	} else {
		if (root->left == NULL && root->right == NULL) {
			free(root);
			return NULL;
		} else if (root->left == NULL) {
			node* temp = root->right;
			if (temp != NULL) {
				temp->parent = root->parent;
			}
			free(root);
			return temp;
		} else if (root->right == NULL) {
			node* temp = root->left;
			if (temp != NULL) {
				temp->parent = root->parent;
			}
			free(root);
			return temp;
		} else {
			node* successor = find_min(root->right);
			
			root->number = successor->number;
			strcpy(root->name, successor->name);
			
			root->right = delete(root->right, successor->number);
			if (root->right != NULL) {
				root->right->parent = root;
			}
		}
	}
	
	return root;
}

int main() {
	int a, r, f;
	scanf("%d %d %d", &a, &r, &f);

	node* root = NULL;
	int number;
	char name[MAX_NAME_SIZE];

	while (a-- > 0) {
		scanf("%d", &number);
		scanf("%s", name);
		root = insert(root, create_node(number, name));
	}

	while (r-- > 0) {
		scanf("%d", &number);
		root = delete(root, number);
	}

	while (f-- > 0) {
		scanf("%d", &number);
		node* student = find(root, number);
		printf("%s\n", student == NULL ? "NO" : student->name);
	}

	delete_tree(root);
}