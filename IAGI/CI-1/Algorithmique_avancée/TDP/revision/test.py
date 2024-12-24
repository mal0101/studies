class TreeNode(object):
    def __init__(self, val = 0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right


def merge(left, right):
    result = []
    i = j = 0
    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            result.append(right[i])
            i += 1
        else:
            result.append(left[j])
            j += 1
    result += right[i:]
    result += left[j:]
    return result

def merge_sort(tab):
    if len(tab) <= 1:
        return tab
    middle = len(tab) // 2
    left = merge_sort(tab[:middle])
    right = merge_sort(tab[middle:])
    return merge(left, right)

def parcoursPrefix_Arbre(self, root):
    res = []
    if not root:
        return
    res.append(root.val)
    parcoursPrefix_Arbre(root.left)
    parcoursPrefix_Arbre(root.right)
    return res

def parcoursSuffixe_Arbre(self, root):
    res = []
    if not root:
        return
    parcoursSuffixe_Arbre(root.left)
    parcoursSuffixe_Arbre(root.right)
    res.append(root.val)
    return res

def parcoursInfixe_Arbre(self, root):
    res = []
    if not root:
        return
    parcoursInfixe_Arbre(root.left)
    res.append(root.val)
    parcoursInfixe_Arbre(root.right)
    return res

def permuter(a,b):
    temp = a
    a = b
    b = temp

def addElementheap(tab, length):
    indx_fils = length - 1
    indx_parent= (indx_fils - 1) //2
    while (tab[indx_parent] < tab[indx_fils] and indx_parent>=0):
        permuter(tab[indx_parent], tab[indx_fils])
        indx_fils = indx_parent
        indx_parent = (indx_fils - 1)//2
    
def const_heap(tab, n):
    for i in range(1, n):  # Build the heap
        addElementheap(tab, i+1)


def desc_Element(tab, i, length):
    while True:
        indx_filsg = 2 * i + 1
        indx_filsd = 2 * i + 2
        largest = i

        # Check left child
        if indx_filsg < length and tab[indx_filsg] > tab[largest]:
            largest = indx_filsg

        # Check right child
        if indx_filsd < length and tab[indx_filsd] > tab[largest]:
            largest = indx_filsd

        # If the largest is not the current node, swap and continue
        if largest != i:
            permuter(tab[i], tab[largest])
            i = largest
        else:
            break  # Exit loop if heap property is satisfied


def heapsort(tab, length):
    const_heap(tab, length)  # Build the max-heap
    for i in range(length-1, 0, -1):
        permuter(tab[0], tab[i])  # Move the largest element to the end
        desc_Element(tab, 0, i)  # Restore the heap property
    return tab
        




    
tab = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(merge_sort(tab))
print(heapsort(tab, len(tab)))