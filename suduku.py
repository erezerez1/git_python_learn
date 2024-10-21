import numpy as np

boardin = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0], \
          [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6], \
          [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

board=np.array(boardin)

def checkn_all_unique(data):
    values, counts = np.unique(data, return_counts=True)
    if values[0]==0:
        counts = counts[1:]
    if max(counts)<2:
        return True
    else:
        return False

def all_unique_rect(s,i,j):
    flat3x3=s[i:i+3,j:j+3].flatten()
    return checkn_all_unique(flat3x3)

def all_unique_row(s,i):
    return checkn_all_unique(s[i,:])

def all_unique_col(s,j):
    return checkn_all_unique(s[:,j])

def validsol (s):
    for i in range(0,9,3):
        for j in range(0,9,3):
            if all_unique_rect(s,i,j)==False:
                return False
    for i in range(0, 9, 1):
        if all_unique_row(s,i)==False:
            return False
        if all_unique_col(s,i)==False:
            return False
    return True

def find_next_point(s):
    i=0
    while (i<9):
        oneline=s[i,:]
        onelinez=(oneline == 0)
        zeros=np.where(onelinez == True)[0]
        if len(zeros)==0:
            i=i+1
        else:
            return [True,i,zeros[0]]
    return [False,0,0]

def solve_suduku(s):
    if (np.count_nonzero(s)==81):
        if validsol(s) == True:
            print(f"Found it {s}")
            exit(0)
    [a,b,c]=find_next_point(s)
    if a== True:
        for i in range(1,10):
            snew=s.copy()
            snew[b,c]=i
            solve_suduku(snew)

wrong= [[6,1,1,1,9,5,1,1,1],[1,9,8,1,1,1,1,6,1],[8,1,1,1,6,1,1,1,3],[4,1,1,8,1,3,1,1,1],[7,1,1,1,2,1,1,1,6],[1,6,1,1,1,1,2,8,1],[1,1,1,4,1,9,1,1,5],[1,1,1,1,8,1,1,7,9]]
what=validsol(wrong)
checkn_all_unique([1,1,1,4,1,9,1,1,5])
solve_suduku(board)

    
