# m est la matrice carrée que prend la fonction antisym et n sa dimension
def antisym(m,n):
    mtrans = []
    for i in range(n):
        for j in range(n):
            if m[i][j] != -m[j][i]:
                return 0
    return 1
    

def main():
    m = [[0, 4], [-4, 0]]
    print(antisym(m, 2))
    
main()