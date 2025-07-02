#include <stdio.h>

//funkcja 1
void linspace(double v[], double start, double stop, int n);
double abss(double x);

//funkcja 2
void add(double v1[], const double v2[], int n);

//funkcja 3
double dot_product(const double v1[], const double v2[], int n);

//funkcja 4
void multiply_by_scalar(double v[], int n, double s);

//funkcja 5
void range(double v[], int n, double start, double step);

//funkcja dodatkowa
void read_vector(double v[], int n);

int main(void){

    int task_num; 
    scanf("%d", &task_num);

    if(task_num == 1){
        int n;
        double val_1;
        double val_2;
        
        scanf("%d %lf %lf", &n, &val_1, &val_2);
        double v[n];
        linspace(v, val_1, val_2, n);
    }
    else if(task_num == 2){        
        int n;
        scanf("%d", &n);
        double v1[n];
        double v2[n];
        
        for(int i = 0; i < n; ++i){
            scanf("%lf", &v1[i]);
        }

        for(int j = 0; j < n; ++j){
            scanf("%lf", &v2[j]);
        }

        add(v1, v2, n);
    }
    else if(task_num == 3){
        int n;
        scanf("%d", &n);
        double v1[n];
        double v2[n];
        
        for(int i = 0; i < n; ++i){
            scanf("%lf", &v1[i]);
        }

        for(int j = 0; j < n; ++j){
            scanf("%lf", &v2[j]);
        }

        printf("%.2lf", dot_product(v1, v2, n));
    }
    else if(task_num == 4){
        int n;
        double s;
        scanf("%d %lf", &n, &s);

        double v[n];
        for(int i = 0; i < n; ++i){
            scanf("%lf", &v[i]);
        }

        multiply_by_scalar(v, n, s);
    }
    else if(task_num == 5){
        int n;
        double start, step;
        scanf("%d %lf %lf", &n, &start, &step);
        double v[n];

        range(v, n, start, step);

    }

    return 0;    
}

void read_vector(double v[], int n){
    for(int i = 0; i < n; i++){
        printf("%.2lf", v[i]);
        printf("   ");
    }
}

void range(double v[], int n, double start, double step){
    for(int i = 0; i < n; ++i){
        v[i] = start;
        start += step;
        printf("%.2lf", v[i]);
        printf("   ");
    }
}

void multiply_by_scalar(double v[], int n, double s){
    for(int i = 0; i < n; ++i){
        double tmp = v[i] * s;
        printf("%.2lf", tmp);
        printf("   ");
    }

}

double dot_product(const double v1[], const double v2[], int n){
    double result = 0;
    for(int i = 0; i < n; i++){
        result += v1[i]*v2[i];
    }

    return result;
}

void add(double v1[], const double v2[], int n){
    for(int i = 0; i < n; i++){
        double result = v1[i]+v2[i];
        printf("%.2lf", result);
        printf("   ");
    }
}

double abss(double x){

    if (x < 0){
        return x * -1;
    }

    return x;
}

void linspace(double v[], double start, double stop, int n){

    if(n == 0){
        return;
    }


    double jump;
    if(start * stop < 0){
        jump = (abss(start) + abss(stop))/(n-1);
    }
    else{
        jump = (abss(abss(start) - abss(stop)))/(n-1);
    }


    double multi = 0;
    if(start < stop){
        for(int i = 0; i < n; i++){
            v[i] = start + multi;
            multi += jump;
        }
    }
    else{
        for(int i = 0; i < n; i++){
            v[i] = start - multi;
            multi += jump;
        }
    }

    for(int i = 0; i < n; i++){
        printf("%.2f", v[i]);
        printf("   ");
    }
}