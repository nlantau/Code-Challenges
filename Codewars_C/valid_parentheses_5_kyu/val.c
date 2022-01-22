/* Valid Parentheses - 5 kyu
 * nlantau, 2021-09-04
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
	char symbol;
} StackData;

typedef struct node {
	StackData data;
	struct node *next;
} Node, *NodePtr;

typedef struct stackType {
	NodePtr top;
} StackType, *Stack;

Stack init_stack()
{
	Stack sp = (Stack)malloc(sizeof(StackType));
	sp -> top = NULL;
	return sp;
}

int empty(Stack s)
{
	return s -> top == NULL;
}

void push(Stack s, StackData d)
{
	NodePtr np = (NodePtr)malloc(sizeof(Node));
	np -> data = d;
	np -> next = s -> top;
	s -> top = np;
}

StackData pop(Stack s)
{
	if (empty(s)) {
		fprintf(stderr, "Attempt to pop empty stack\n");
		StackData err = {
			.symbol = 'x',
		};
		return err;
	}
	StackData hold = s -> top -> data;
	NodePtr temp = s -> top;
	s -> top = s -> top -> next;
	free(temp);
	return hold;
}

StackData new_stack_data(char c)
{
	StackData temp;
	temp.symbol = c;
	return temp;
}


bool validParentheses(const char *t)
{
	Stack s = init_stack();
	int balance = 0;

	for (; *t != '\0'; *t++) {
		if (*t == '(') {
			push(s, new_stack_data(*t));
			balance += 1;
		} else if (*t == ')') {
			StackData paren = pop(s);
			if (paren.symbol == 'x')
				return 0;
			if (paren.symbol == '(')
				balance -= 1;
		}
	}
	printf("Balance: %d\n", balance);
	while(!(empty(s)))
		printf("> Left in stack: %c\n", pop(s).symbol);
	return balance == 0;
}



int main(void)
{
	printf("True : %d\n", validParentheses("()"));
	printf("False: %d\n", validParentheses(")(()))"));
	printf("False: %d\n", validParentheses("("));
	printf("True : %d\n", validParentheses("(())((()())())"));

	return 0;
}













