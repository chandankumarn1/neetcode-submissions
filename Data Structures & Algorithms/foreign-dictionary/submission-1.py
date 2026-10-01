from collections import deque

class Solution:
    def foreignDictionary(self, words):
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        # Build graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))
            found = False

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1

                    found = True
                    break

            # Invalid prefix case
            if not found and len(word1) > len(word2):
                return ""

        # Topological Sort
        queue = deque()

        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)

        result = []

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbor in graph[c]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detected
        if len(result) != len(indegree):
            return ""

        return "".join(result)