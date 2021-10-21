
class Node:
    def __init__(self, val, left=None, right=None, letter=None):
        self.val = val
        self.left = left
        self.right = right
        self.letter=letter
    def getVal(self):
        return self.val

def buildTree(freqs):
    nodes = []
    for key,val in freqs.items():
        nodes.append(Node(val, letter=key))

    while len(nodes) > 1:
        nodes = sorted(nodes, key= lambda x: x.getVal(), reverse=True)
        a = nodes.pop()
        b = nodes.pop()
        composite = Node(a.getVal()+b.getVal(), a, b)
        nodes.append(composite)
    return nodes

def letter_to_code(tree):
    mp = {}
    def traverse_tree(root, s):
        if not root:
            return

        if root.letter != None:
            mp[root.letter] = s

        traverse_tree(root.left, s + "0")
        traverse_tree(root.right, s + "1")

    traverse_tree(tree, "")
    return mp

def encode(text, mp):
    res = ""
    for ch in text:
        res += mp[ch]
    return res

def decode(text, tree):
    root = tree
    res = ""
    for t in text:
        if t == "0":
            root = root.left
        else:
            root = root.right
        if root.letter != None:
            res += root.letter
            root = tree
    return res

def get_freqs(s):
    freqs = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 1) + 1
    return freqs

def driver():
    text_to_encode = "etanainateinaitainetainnnaaaa"
    freqs = get_freqs(text_to_encode)

    tree = buildTree(freqs)[0]
    code_map = letter_to_code(tree)
    encoded_string = encode(text_to_encode, code_map)
    print(encoded_string)

    decoded_string = decode(encoded_string, tree)
    print(decoded_string)
    assert decoded_string == text_to_encode

driver()
