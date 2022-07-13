import sys
sys.setrecursionlimit(10**6)

def preorder(X, Y, answer):
    node = X[0]
    idx = Y.index(node)
    arr1 = []
    arr2 = []

    for i in range(1, len(X)):
        if node[0] > X[i][0]:
            arr1.append(X[i])
        else:
            arr2.append(X[i])

    answer.append(node[2])

    if len(arr1) > 0:
        preorder(arr1, Y[:idx], answer)
    if len(arr2) > 0:
        preorder(arr2, Y[idx + 1:], answer)


def postorder(X, Y, answer):
    node = X[0]
    idx = Y.index(node)
    arr1 = []
    arr2 = []

    for i in range(1, len(X)):
        if node[0] > X[i][0]:
            arr1.append(X[i])
        else:
            arr2.append(X[i])

    if len(arr1) > 0:
        postorder(arr1, Y[:idx], answer)
    if len(arr2) > 0:
        postorder(arr2, Y[idx + 1:], answer)

    answer.append(node[2])

def solution(nodeinfo):
    preanswer = []
    postanswer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    X = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    Y = sorted(nodeinfo)


    preorder(X, Y, preanswer)
    postorder(X, Y, postanswer)

    return [preanswer, postanswer]
