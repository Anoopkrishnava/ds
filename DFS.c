#include<stdio.h>
#include<stdlib.h>
#define MAX 10
int adj[MAX][MAX];
int v[MAX];
int n;
void dfs(int start)
{
    int i;
    v[start]=1;
    printf("%d",start);
    for(i=0;i<n;i++)
    {
        if(adj[start][i]==1&&v[i]==0){
            dfs(i);
        }
    }
}
int main()
{
    int start,i,j;
    printf("Enter number of vertices :");
    scanf("%d",&n);
    printf("\nEnter adjacency matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++){
            scanf("%d",&adj[i][j]);
        }
    }
    printf("\nEnter the starting vertex\n");
    scanf("%d",&start);
    for(i=0;i<n;i++)
    {
        v[i]=0;
    }
    printf("\ndepth firs search of graph is\n");
    dfs(start);
    return 0;
}


