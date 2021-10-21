import heapq

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
    heapq.heapify(nodes)
    for key,val in freqs.items():
        heapq.heappush(nodes, (val, Node(val, letter=key)))

    while len(nodes) > 1:
        a = heapq.heappop(nodes)
        b = heapq.heappop(nodes)
        composite = Node(a[0]+b[0], a[1], b[1])
        heapq.heappush(nodes, (composite.getVal(), composite))
    return heapq.heappop(nodes)[1]

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

    tree = buildTree(freqs)
    code_map = letter_to_code(tree)
    encoded_string = encode(text_to_encode, code_map)
    print(encoded_string)

    decoded_string = decode(encoded_string, tree)
    print(decoded_string)
    assert decoded_string == text_to_encode

driver()
