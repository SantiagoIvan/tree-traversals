# Challenge de Codewars
# Si se recorre el arbol en in-order y esta ordenado, quiere decir que es un bst, binary tree search.

class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def in_order(node, res): # la raiz en el medio
    if not node:
        return res
    else:
        in_order(node.left, res)
        res.append(node.value)
        in_order(node.right, res)
    return res

def pre_order(node, res):#la raiz al principio
    if not node:
        return res
    else:
        res.append(node.value)
        pre_order(node.left, res)
        pre_order(node.right, res)
    return res
  
def post_order(node, res): # la raiz al final
    if not node:
        return res
    else:
        post_order(node.left, res)
        post_order(node.right, res)
        res.append(node.value)
    return res

  
def is_bst(node):
    res = []
    res = in_order(node, res)
    return True if res == sorted(res) or res == sorted(res, reverse=True) else False
