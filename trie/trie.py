class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        self.root_node=TrieNode()
    
    def insert(self,word):
        current=self.root_node
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.is_end_of_word=True
    
    def search(self,word):
        current=self.root_node
        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        return current.is_end_of_word

    def starts_with(self,prefix):
        current=self.root_node
        for char in prefix:
            if char not in current.children:
                return False
            current=current.children[char]
        return True
    
    def get_all_words(self,prefix):
        results=[]
        current=self.root_node
        for char in prefix:
            if char not in current.children:
                return results
            current=current.children[char]
        self._dfs(current,prefix,results)
        return results
    
    def _dfs(self,node,prefix,results):
        if node.is_end_of_word:
            results.append(prefix)
        for char,child_node in node.children.items():
            self._dfs(child_node,prefix+char,results)

    def delete_word(self,word):
        word_deleted=[False]
        if not self.search(word):
            return False
        def _delete(node,word,index=0):
            if len(word)==index:
                if node.is_end_of_word:
                    node.is_end_of_word=False
                    word_deleted[0]=True
                    return len(node.children)==0
                return False
            ch=word[index]
            if ch not in node.children:
                return False
            should_delete_child=_delete(node.children[ch],word,index+1)
            if should_delete_child:
                del node.children[ch]
                return not node.is_end_of_word and len(node.children)==0
            return False
        _delete(self.root_node,word)
        return word_deleted[0]
    
    def count_all_words(self):
        def _count(node):
            count=0
            if node.is_end_of_word:
                count+=1
            for child_nodes in node.children.values():
                count+=_count(child_nodes)
            return count
        return _count(self.root_node)

trie=Trie()
trie.insert('car')
trie.insert('carpentar')
trie.insert('camera')
trie.insert('ink')
trie.insert('inkling')

print(trie.search('ink'))
print(trie.starts_with('inklo'))
print(trie.count_all_words())
print(trie.delete_word('camera'))
print(trie.get_all_words('ca'))
