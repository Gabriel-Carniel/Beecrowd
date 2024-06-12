#include <stdio.h>
#include <stdlib.h>

typedef struct arvore {
    struct arvore* dir;
    struct arvore* esq;
    int val;
} ar;

ar* insert (ar* start, int n){
    if (start == NULL){
        start = calloc(1 , sizeof(ar));
        start->val = n;
        start->dir = NULL;
        start->esq = NULL;
        return start;
    }
    else {
        if (n < start->val){
            start->esq = insert(start->esq, n);
            return start;
        }
        else if (n > start->val){
            start->dir = insert(start->dir, n);
            return start;
        }
        else {
            return start;
        }
    }
}

void imprime_ordem (ar* root){
    ar* x = root;
    if (root == NULL){
        int a;
    }
    else {
        if (x->esq != NULL){
            imprime_ordem(x->esq);
        }
        printf(" %d", x->val);
        if (x->dir != NULL){
            imprime_ordem(x->dir);
        }
    }
}

void imprime_pre_ordem (ar* root){
    ar* x = root;
    if (root == NULL){
        int a;
    }
    else {
        printf(" %d", x->val);
        if (x->esq != NULL){
            imprime_pre_ordem(x->esq);
        }
        if (x->dir != NULL){
            imprime_pre_ordem(x->dir);
        }
    }
}

void imprime_pos_ordem (ar* root){
    ar* x = root;
    if (root == NULL){
        int a;
    }
    else {
        if (x->esq != NULL){
            imprime_pos_ordem(x->esq);
        }
        if (x->dir != NULL){
            imprime_pos_ordem(x->dir);
        }
        printf(" %d", x->val);
    }
}

int main()
{
    ar* start = NULL;
    int option;
    int num;
    int caso;
    int n;
    int x;
    int a;
    scanf("%d", &caso);
    for (int i = 0; i < caso; i++){
        start = NULL;
        scanf("%d", &n);
        for (int j = 0; j < n; j++){
            scanf("%d", &x);
            start = insert (start, x);
        }
        printf("Case %d:", i+1);
        printf("\n");
        printf("Pre.:");
        imprime_pre_ordem(start);
        printf("\n");
        printf("In..:");
        imprime_ordem(start);
        printf("\n");
        printf("Post:");
        imprime_pos_ordem(start);
        printf("\n");
        printf("\n");
    }
    return 0;
}
