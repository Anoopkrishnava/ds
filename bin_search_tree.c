#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};
struct node *root=NULL;

void insert()
{
    int value;
    printf("\nEnter the value :");
    scanf("%d",&value);
    struct node *newnode, *temp, *parent;

    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->left = NULL;
    newnode->right = NULL;

    if (root == NULL) {
        root = newnode;
        return;
    }

    temp = root;
    parent = NULL;

    while (temp != NULL) {
        parent = temp;
        if (value < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    if (value < parent->data)
        parent->left = newnode;
    else
        parent->right = newnode;
}
//INORDER TRAVERSAL
void inorder(struct node* root)
{
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

/* PREORDER TRAVERSAL */
void preorder(struct node* root)
{
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

/* POSTORDER TRAVERSAL */
void postorder(struct node* root)
{
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

/* SEARCH */
void search()
{
    int key;
    printf("\nEnter the key :");
    scanf("%d",&key);
    struct node *temp = root;

    while (temp != NULL) {
        if (temp->data == key) {
            printf("Element found\n");
            return;
        }
        else if (key < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    printf("Element not found\n");
}

/* DELETE NODE */
void deleteNode()
{
    int key;
    printf("\nEnter the value to delete :");
    scanf("%d",&key);
    struct node *temp = root, *parent = NULL;

    while (temp != NULL && temp->data != key) {
        parent = temp;
        if (key < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    if (temp == NULL) {
        printf("Element not found\n");
        return;
    }

    /* CASE 1: LEAF NODE */
    if (temp->left == NULL && temp->right == NULL) {
        if (temp == root)
            root = NULL;
        else if (parent->left == temp)
            parent->left = NULL;
        else
            parent->right = NULL;
        free(temp);
    }

    /* CASE 2: ONE CHILD */
    else if (temp->left == NULL || temp->right == NULL) {
        struct node *child;
        if (temp->left != NULL)
            child = temp->left;
        else
            child = temp->right;

        if (temp == root)
            root = child;
        else if (parent->left == temp)
            parent->left = child;
        else
            parent->right = child;

        free(temp);
    }

    /* CASE 3: TWO CHILDREN */
    else {
        struct node *successor = temp->right;
        struct node *succParent = temp;

        while (successor->left != NULL) {
            succParent = successor;
            successor = successor->left;
        }

        temp->data = successor->data;

        if (succParent->left == successor)
            succParent->left = successor->right;
        else
            succParent->right = successor->right;

        free(successor);
    }

    printf("Node deleted\n");
}

//main function
int main()
{
    int choice;

    while (1) {
        printf("\n\n1.Insert\n2.Search\n3.Inorder\n4.Preorder\n5.Postorder\n6.Delete\n7.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
           
            insert();
            break;

        case 2:
            
            search();
            break;

        case 3:
            inorder(root);
            break;

        case 4:
            preorder(root);
            break;

        case 5:
            postorder(root);
            break;

        case 6:
            
            deleteNode();
            break;

        case 7:
            exit(0);

        default:
            printf("Invalid choice\n");
        }
    }
    return 0;
}
