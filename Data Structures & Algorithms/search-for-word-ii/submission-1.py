class Solution:

    def findWords(self, board, words):

        # Build Trie
        root = {}

        for word in words:
            node = root

            for ch in word:
                if ch not in node:
                    node[ch] = {}

                node = node[ch]

            node["#"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):

            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            # Cell already used
            if ch == "#":
                return

            # Character not present in Trie
            if ch not in node:
                return

            next_node = node[ch]

            # Word found
            if "#" in next_node:
                result.append(next_node["#"])

                # Prevent duplicate result
                del next_node["#"]

            # Mark cell as visited
            board[r][c] = "#"

            # Search in 4 directions
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # Restore cell
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result