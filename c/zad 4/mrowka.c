#include <stdio.h>
#include <stdlib.h>
#define N 20

typedef struct Ant {
	int pi, pj;
	int direction;
} Ant;

int rnd(const int min, const int max) {
	return (rand() % (max - min)) + min;
}

void print_board(int** board, const int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
    
}

void print_ant(const Ant ant) {
    char ant_direction[] = {'N', 'E', 'S', 'W'};
    printf("%d %d %c\n", ant.pi, ant.pj, ant_direction[ant.direction]);
}

void init_board(int*** board, const int n) {
    *board = (int**)malloc(n * sizeof(int*));

    for (int i = 0; i < n; i++){
        (*board)[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++){
            (*board)[i][j] = rand() % 8 + 1;
        }
    }
}

void free_board(int** board, const int n) {
    for (int i = 0; i < n; i++){
        free(board[i]);
    }
    free(board);
}

void ant_move(int** board, const int n, Ant* ant) {
    int state = board[ant->pi][ant->pj];

    switch (state)
    {
    case 1:
        board[ant->pi][ant->pj] = 7;
        switch (ant->direction)
        {
        case 0:
            ant->pi = (ant->pi - 1 + n) % n;
            break;
        case 1:
            ant->pj = (ant->pj + 1) % n;
            break;
        case 2:
            ant->pi = (ant->pi + 1) % n;
            break;
        case 3:
            ant->pj = (ant->pj - 1 + n) % n;
            break;
        default:
            break;
        }
        break;
    case 2:
        board[ant->pi][ant->pj] = 4;
        ant->direction = (ant->direction + 1) % 4;
        break;
    case 3:
        board[ant->pi][ant->pj] = 2;
        ant->direction = (ant->direction + 3) % 4;
        break;
    case 4:
        board[ant->pi][ant->pj] = 6;
        switch (ant->direction)
        {
        case 0:
            ant->pj = (ant->pj + 1) % n;
            break;
        case 1:
            ant->pi = (ant->pi + 1) % n;
            break;
        case 2:
            ant->pj = (ant->pj - 1 + n) % n;
            break;
        case 3:
            ant->pi = (ant->pi - 1 + n) % n;
            break;
        default:
            break;
        }
        break;
    case 5:
        board[ant->pi][ant->pj] = 3;
        switch (ant->direction)
        {
        case 0:
            ant->pj = (ant->pj - 1 + n) % n;
            break;
        case 1:
            ant->pi = (ant->pi - 1 + n) % n;
            break;
        case 2:
            ant->pj = (ant->pj + 1) % n;
            break;
        case 3:
            ant->pi = (ant->pi + 1) % n;
            break;
        default:
            break;
        }
        break; 
    case 6:
        board[ant->pi][ant->pj] = 5;
        switch (ant->direction)
        {
        case 0:
            ant->pi = (ant->pi + 1) % n;
            break;
        case 1:
            ant->pj = (ant->pj - 1 + n) % n;
            break;
        case 2:
            ant->pi = (ant->pi - 1 + n) % n;
            break;
        case 3:
            ant->pj = (ant->pj + 1) % n;
            break;
        default:
            break;
        }
        break; 
    case 7:
        board[ant->pi][ant->pj] = 8;
        ant->direction = (ant->direction + 2) % 4;
        break;
    case 8:
        board[ant->pi][ant->pj] = 1;
        break; 
    default:
        break;
    }

}

void ant_simulation(int** board, const int n, Ant* ant, const int steps) {
    ant->pi = 0;
    ant->pj = 0;
    ant->direction = 1;

    for (int i = 0; i < steps; i++){
        ant_move(board, n, ant);
    }
}

int main(void) {
	int** board;
	int n, steps;
	unsigned seed;
	Ant ant;

	scanf("%d %d %d", &n, &seed, &steps);
	srand(seed);
	init_board(&board, n);
	ant_simulation(board, n, &ant, steps);
	print_board(board, n);
	print_ant(ant);

	free_board(board, n);

	return 0;
}

