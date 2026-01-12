#include <stdio.h>

int n, e;
int U[100], V[100], W[100];
int parent[100];

/* Find function */
int find(int x)
{
    if (parent[x] != x)
        parent[x] = find(parent[x]);   // path compression
    return parent[x];
}

/* Union function (simple) */
void unite(int a, int b)
{
    parent[find(a)] = find(b);
}

/* Sort edges by weight using bubble sort */
void sortEdges()
{
    int t;
    for (int i = 0; i < e - 1; i++)
    {
        for (int j = 0; j < e - i - 1; j++)
        {
            if (W[j] > W[j + 1])
            {
                t = W[j]; W[j] = W[j + 1]; W[j + 1] = t;
                t = U[j]; U[j] = U[j + 1]; U[j + 1] = t;
                t = V[j]; V[j] = V[j + 1]; V[j + 1] = t;
            }
        }
    }
}

/* Kruskal's Algorithm */
void kruskal()
{
    int totalCost = 0;
    int edges = 0;

    /* Initialize parent array */
    for (int i = 0; i < n; i++)
        parent[i] = i;

    sortEdges();

    printf("MST Edges:\n");

    for (int i = 0; i < e && edges < n - 1; i++)
    {
        if (find(U[i]) != find(V[i]))
        {
            printf("%d -- %d (%d)\n", U[i], V[i], W[i]);
            totalCost += W[i];
            unite(U[i], V[i]);
            edges++;
        }
    }

    printf("Total weight of MST = %d\n", totalCost);
}

int main()
{
    printf("Enter number of vertices and edges:\n");
    scanf("%d %d", &n, &e);

    printf("Enter edges (u v w):\n");
    for (int i = 0; i < e; i++)
        scanf("%d %d %d", &U[i], &V[i], &W[i]);

    kruskal();
    return 0;
}
