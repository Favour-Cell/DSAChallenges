def hour_glass(arr):
    sums = []
    j = 0

    while j < 4:
        i = 0
        while i < 4:
            z = arr[j][i] + arr[j][i+1] + arr[j][i+2] 
            y = arr[j+1][i+1]
            x = arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]

            Z = z+y+x
            sums.append(Z)
            i+=1
        j+=1
    return max(sums)     

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
arr2 = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]

print(hour_glass(arr2))
