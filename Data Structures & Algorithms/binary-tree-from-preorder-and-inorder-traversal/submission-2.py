class Solution:
    def buildTree(self, preorder, inorder):
        pos = {value: i for i, value in enumerate(inorder)}
        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootValue = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootValue)

            mid = pos[rootValue]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)