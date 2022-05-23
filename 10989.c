#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 0;
    scanf("%d", &n);
    int arr[10001] = {
        0,
    };
    for (int i = 0; i < n; i++)
    {
        int a;
        scanf("%d", &a);
        arr[a]++;
    }
    for (int i = 1; i < 10001; i++)
    {
        for (int j = 0; j < arr[i]; j++)
        {
            printf("%d\n", i);
        }
    }
}