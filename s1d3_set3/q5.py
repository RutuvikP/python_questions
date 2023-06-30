def selectionSort(arr):
    n=len(arr)

    for i in range(0,n-1):
        minInd=i
        for j in range(i+1,n):
            if arr[j]<arr[minInd]:
                minInd=j
        arr[i], arr[minInd] = arr[minInd], arr[i]

    print(arr)

selectionSort([64, 25, 12, 22, 11])