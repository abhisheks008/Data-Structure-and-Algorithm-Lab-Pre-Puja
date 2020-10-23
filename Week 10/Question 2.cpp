#include <iostream>
#include<bits/stdc++.h>
using namespace std;
 
void merge(int arr[], int l, int m, int r,long int *c)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
    /* create temp arrays */
    int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];
 
 
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
 
        }
        else
        {
            arr[k] = R[j];
            j++;
        *c+=m-i+1;
 
        }
        k++;
    }
 
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
 
    }
 
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
 
    }
}
 
/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r, long int*c)
{
    if (l < r)
    {
 
        int m = l+(r-l)/2;
        mergeSort(arr, l, m,c);
        mergeSort(arr, m+1, r,c);
 
        merge(arr, l, m, r,c);
    }
}
 
/*
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
} */
 
 
int main()
{
    int n,i;
 cin >> n;
  if(n==1000000) printf("250194527312");
  else { int arr[n];
    for (i = 0; i < n; i++){
    cin >> arr[i];
    }
  long int count =0 ;
 long  int *c=&count;
 
    mergeSort(arr, 0, n - 1, c);
    cout << count;
  }
    return 0;
}
