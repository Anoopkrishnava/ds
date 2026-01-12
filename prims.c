#include<stdio.h>
#include<limits.h>// used for INT_MAX
#define MAX 100
int main()
{
    int n,u,v;
    printf("Enter the numberof vertices :");
    scanf("%d",&n);

    int V[MAX]={0}; //set all vertices initially unvisited
    int A[n][n];
    printf("\nEnter the adjacency matrix :\n");
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        {
            scanf("%d",&A[i][j]);

            //replace 0(no edge) with INT_MAX except diagonal
            if(i!=j && A[i][j]==0){
                A[i][j]=INT_MAX;
            }
        }
    }

    printf("\nMinimum cost spanning tree\n");
    int e=0; //no of edges added into MST
    int cost=0;   //

    V[0]=1;  //starting from node 0

    while(e<n-1){
        int min=INT_MAX;
        int u=-1,v=-1;

        for(int i=0;i<n;i++){
            if(V[i]){           //if node i is in mst
                for(int j=0;j<n;j++){
                    if(!V[j] && A[i][j] <min){
                        min=A[i][j];
                        u=i;
                        v=j;
                    }
                }
            }
        }
        //adding edge to mst
        V[v]=1;
        printf("{%d , %d} = %d",u,v,min);
        cost+=min;
        e++;
    }
    printf("Minimum cost : %d",cost);

    return 0;
}