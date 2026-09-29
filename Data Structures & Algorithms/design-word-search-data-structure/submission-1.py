class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()

            node = node.children[ch]

        node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(node, index):

            if index == len(word):
                return node.isEnd

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False

                return dfs(node.children[ch], index + 1)

            # '.' can match any character
            for child in node.children.values():
                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self, 0)