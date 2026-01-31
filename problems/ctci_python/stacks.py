"""
How would you convert recursion which is overflowing to explict?
"""

def process_tree(root):    
    if root is None:
        return
    
    stack = [root]

    while stack:
        node = stack.pop()
        process(node.data)

        for child in node.children:
            stack.append(child)
    
