#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
struct node *head=NULL;
void begin_insert();
void last_insert();
void randominsert();
void begin_delete();
void last_delete();
void randomdelete();
void display();
int main(){
    int ch=0;
    while(ch!=3){
        printf("\n1.Insert at beginning\n2.Display\n3.Exit\n4.Insert at last\n5.Insert at any random position\n6.Delete from beginning\n7.Delete from end\n8.Delete from any random position\nEnter your choice :");
        scanf("%d",&ch);
    
    switch(ch)
    {
        case 1:begin_insert();
            break;
        case 2:display();
            break;
        case 3:printf("\nprogram terminated \n");
            exit(0);
            break;
        case 4:last_insert();
            break;
        case 5:randominsert();
            break;
        case 6:begin_delete();
            break;
        case 7:last_delete();
            break;
        case 8:randomdelete();
            break;

        default :printf("\nInvalid choice\n");
    }
}
return 0;
}
void begin_insert(){
    int item;
    struct node *ptr;
    ptr=(struct node*)malloc(sizeof(struct node));
    printf("\nEnter the value :");
    scanf("%d",&item);
        ptr->data=item;
        ptr->next=head;
        head=ptr;

}
void display(){
    if(head==NULL){
        printf("\nEmpty list !!! nothing to print \n");
    }
    else{
        for(struct node *i=head;i!=NULL;i=i->next)
        {
            printf("%d\t",i->data);
        }
    }
}
void last_insert()
{
    int item;
    struct node *ptr,*temp;
    ptr=(struct node *)malloc(sizeof(struct node));
    printf("\nEnter the element :");
    scanf("%d",&item);
    if(head==NULL){
        ptr->data=item;
        ptr->next=NULL;
        head=ptr;
        printf("\nOnly node insered\n");
    }
    else{
        temp=head;
        ptr->data=item;
        while(temp->next!=NULL)
        {
            
            temp=temp->next;

        }
        temp->next=ptr;
        ptr->next=NULL;
        printf("\nNode inserted\n");


    }
}
void randominsert()
{
    int item,pos;
    struct node *ptr,*temp;
    ptr=(struct node*)malloc(sizeof(struct node));
    printf("\nEnter the value :");
    scanf("%d",&item);
    printf("\nEnter the position you want to insert :");
    scanf("%d",&pos);
    ptr->data=item;
    if(head==NULL){
        ptr->next=NULL;
        head=ptr;
        printf("\nOnly node inserted \n");
    }
    else{
        temp=head;
       for(int i=1;i<pos-1;i++){
        temp=temp->next;
       }
       
       ptr->next=temp->next;
       temp->next=ptr;
       printf("\nNode inserted at  %d",pos);

        

    }
}
void begin_delete()
{
    struct node *ptr;
    if(head==NULL){
        printf("\nempty list\n");
    }
    else{
        ptr=head;
        head=ptr->next;
        free(ptr);
        printf("\nNode deleted\n");
    }


}
void last_delete()
{
    struct node *ptr,*temp;
    if(head!=NULL)
    {
        temp=head;
        while(temp->next!=NULL)
        {
            ptr=temp;
            temp=temp->next;
        }
        ptr->next=NULL;
        free(temp);
        printf("\nNode deleted from end\n");

    }
}
void randomdelete()
{
    struct node *ptr,*temp=head;
    int item;
    printf("Enter the value to delete :");
    scanf("%d",&item);
    if(head==NULL){
        printf("\nList is empty\n");
    }
    
    while(temp->next!=NULL){
        if(temp->data==item){
            break;
        }
        ptr=temp;
        temp=temp->next;
    }
    if(head->data==item){
        head=head->next;
        free(temp);
        printf("node deleted\n");
        return;
    }
    else{
    printf("%d deleted\n",temp->data);
    ptr->next=temp->next;
    free(temp);
    }
}