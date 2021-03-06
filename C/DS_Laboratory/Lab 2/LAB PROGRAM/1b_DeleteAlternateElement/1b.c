#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
 int info;
 struct node* link;
}NODE;

typedef struct head_node
{
	NODE* head;
}H;

void delete(H* h,int n);

int main()
{

        H h;int k,l;
        printf("Enter Number of elements: ");
        int n;
        scanf("%d",&n);
        if(n>0)
        {
                h.head = NULL;
                printf("Enter data %d: ",1);
                h.head = (NODE*)malloc(sizeof(NODE));
                scanf("%d",&(h.head->info));
                NODE* pres = h.head;
                for(int i=0 ;i<n-1;i++)
                {
                        pres->link = (NODE*)malloc(sizeof(NODE));
                        printf("Enter data %d: ",i+2);
                        scanf("%d",&(pres->link->info));
                        pres = pres->link;
                }
                pres->link= NULL;
                delete(&h,n);
				pres = h.head;
                while(pres!=NULL)
                {
					printf("%d\n",(pres->info));
					pres = pres->link;
                }
        }
}


void delete(H* h,int n)
{

     NODE* pres = h->head,*prev = NULL;
        for(int i=0;i<n && pres;i++)
        {
                if(i%2==0)
                {
                        if(prev==NULL)
                        {
                                h->head = h->head->link;
                                free(pres);
                                pres = h->head;
                        }
                        else
                        {
                        
                                prev->link = pres->link;
                                free(pres);
                                pres = prev->link;
                        }
                        
                }
                else
                {
                        prev = pres;
                        pres = pres->link;
                
                }
        }
}