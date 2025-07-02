#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define BUFFER_SIZE 128

// Stack structure for operators
typedef struct {
    char data[BUFFER_SIZE];
    int top;
} OperatorStack;

// Stack structure for integers
typedef struct {
    int data[BUFFER_SIZE];
    int top;
} IntStack;

// Stack operations for operators
void init_op_stack(OperatorStack* s) {
    s->top = -1;
}

int is_op_empty(OperatorStack* s) {
    return s->top == -1;
}

void push_op(OperatorStack* s, char c) {
    s->data[++s->top] = c;
}

char pop_op(OperatorStack* s) {
    if (is_op_empty(s)) return '\0';
    return s->data[s->top--];
}

char peek_op(OperatorStack* s) {
    if (is_op_empty(s)) return '\0';
    return s->data[s->top];
}

// Stack operations for integers
void init_int_stack(IntStack* s) {
    s->top = -1;
}

int is_int_empty(IntStack* s) {
    return s->top == -1;
}

void push_int(IntStack* s, int val) {
    s->data[++s->top] = val;
}

int pop_int(IntStack* s) {
    if (is_int_empty(s)) return 0;
    return s->data[s->top--];
}

// Get operator precedence
int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

// Check if character is an operator
int is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

void to_onp(char* expression, char* onp) {
    OperatorStack stack;
    init_op_stack(&stack);
    
    int onp_pos = 0;
    int i = 0;
    
    while (expression[i] != '\0' && expression[i] != '\n') {
        // Skip whitespace
        if (isspace(expression[i])) {
            i++;
            continue;
        }
        
        // If it's a digit, read the entire number
        if (isdigit(expression[i])) {
            // Add space if not first element
            if (onp_pos > 0) {
                onp[onp_pos++] = ' ';
            }
            
            // Copy the entire number
            while (isdigit(expression[i])) {
                onp[onp_pos++] = expression[i++];
            }
        }
        // If it's an opening parenthesis
        else if (expression[i] == '(') {
            push_op(&stack, expression[i]);
            i++;
        }
        // If it's a closing parenthesis
        else if (expression[i] == ')') {
            while (!is_op_empty(&stack) && peek_op(&stack) != '(') {
                if (onp_pos > 0) {
                    onp[onp_pos++] = ' ';
                }
                onp[onp_pos++] = pop_op(&stack);
            }
            pop_op(&stack); // Remove the '('
            i++;
        }
        // If it's an operator
        else if (is_operator(expression[i])) {
            while (!is_op_empty(&stack) && 
                   peek_op(&stack) != '(' && 
                   precedence(peek_op(&stack)) >= precedence(expression[i])) {
                if (onp_pos > 0) {
                    onp[onp_pos++] = ' ';
                }
                onp[onp_pos++] = pop_op(&stack);
            }
            push_op(&stack, expression[i]);
            i++;
        }
        else {
            i++;
        }
    }
    
    // Pop remaining operators
    while (!is_op_empty(&stack)) {
        if (onp_pos > 0) {
            onp[onp_pos++] = ' ';
        }
        onp[onp_pos++] = pop_op(&stack);
    }
    
    onp[onp_pos] = '\0';
}

int evaluate_onp(char* onp) {
    IntStack stack;
    init_int_stack(&stack);
    
    int i = 0;
    while (onp[i] != '\0') {
        // Skip whitespace
        if (isspace(onp[i])) {
            i++;
            continue;
        }
        
        // If it's a digit, parse the number
        if (isdigit(onp[i])) {
            int num = 0;
            while (isdigit(onp[i])) {
                num = num * 10 + (onp[i] - '0');
                i++;
            }
            push_int(&stack, num);
        }
        // If it's an operator
        else if (is_operator(onp[i])) {
            int b = pop_int(&stack);
            int a = pop_int(&stack);
            int result;
            
            switch (onp[i]) {
                case '+':
                    result = a + b;
                    break;
                case '-':
                    result = a - b;
                    break;
                case '*':
                    result = a * b;
                    break;
                case '/':
                    result = a / b;
                    break;
            }
            
            push_int(&stack, result);
            i++;
        }
        else {
            i++;
        }
    }
    
    return pop_int(&stack);
}

int main() {
	char buffer[BUFFER_SIZE];
	char onp[BUFFER_SIZE] = { '\0' };
	fgets(buffer, BUFFER_SIZE, stdin);
	to_onp(buffer, onp);
	printf("%s\n", onp);
	printf("%d\n", evaluate_onp(onp));
}