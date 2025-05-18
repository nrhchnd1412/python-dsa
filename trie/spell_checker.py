import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import re


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for a word in the trie, returns True if found"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def get_suggestions(self, word, max_suggestions=5):
        """Get spelling suggestions for a word"""
        suggestions = []
        
        # If the word is already correct, return empty list
        if self.search(word):
            return []
            
        # Try character replacements, insertions, deletions
        self._find_suggestions(word, suggestions, max_suggestions)
        return suggestions[:max_suggestions]
    
    def _find_suggestions(self, word, suggestions, max_suggestions):
        """Find suggestions based on edit distance of 1"""
        # Check words with one character different
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        # Replacements (change one letter to another)
        for i in range(len(word)):
            for c in alphabet:
                new_word = word[:i] + c + word[i+1:]
                if self.search(new_word) and new_word not in suggestions:
                    suggestions.append(new_word)
                    if len(suggestions) >= max_suggestions:
                        return
        
        # Insertions (add a letter)
        for i in range(len(word) + 1):
            for c in alphabet:
                new_word = word[:i] + c + word[i:]
                if self.search(new_word) and new_word not in suggestions:
                    suggestions.append(new_word)
                    if len(suggestions) >= max_suggestions:
                        return
        
        # Deletions (remove a letter)
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if self.search(new_word) and new_word not in suggestions:
                suggestions.append(new_word)
                if len(suggestions) >= max_suggestions:
                    return
        
        # Transpositions (swap adjacent letters)
        for i in range(len(word) - 1):
            new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            if self.search(new_word) and new_word not in suggestions:
                suggestions.append(new_word)
                if len(suggestions) >= max_suggestions:
                    return


class SpellChecker:
    def __init__(self, dictionary_file=None):
        self.trie = Trie()
        if dictionary_file:
            self.load_dictionary(dictionary_file)
        else:
            # Load a small default dictionary for testing
            default_words = [
                "hello", "world", "python", "programming", "computer", 
                "science", "algorithm", "data", "structure", "spell", 
                "checker", "implementation", "trie", "dictionary",
                "the", "be", "to", "of", "and", "a", "in", "that", "have",
                "it", "for", "not", "on", "with", "he", "as", "you", "do",
                "at", "this", "but", "his", "by", "from", "they", "we",
                "say", "her", "she", "or", "an", "will", "my", "one",
                "all", "would", "there", "their", "what", "so", "up", 
                "out", "if", "about", "who", "get", "which", "go", "me"
            ]
            for word in default_words:
                self.trie.insert(word)
    
    def load_dictionary(self, file_path):
        """Load dictionary from a file with one word per line"""
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    word = line.strip().lower()
                    if word:
                        self.trie.insert(word)
            return True
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return False
    
    def check_word(self, word):
        """Check if a word is correctly spelled"""
        return self.trie.search(word.lower())
    
    def get_suggestions(self, word, max_suggestions=5):
        """Get suggestions for misspelled word"""
        return self.trie.get_suggestions(word.lower(), max_suggestions)
    
    def check_text(self, text):
        """Check text for spelling errors and return a list of misspelled words"""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        misspelled = []
        
        for word in words:
            if not self.check_word(word):
                misspelled.append(word)
                
        return misspelled


class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Checker")
        self.root.geometry("800x600")
        
        # Create the spell checker
        self.spell_checker = SpellChecker()
        
        # Create menu
        self.create_menu()
        
        # Create the text area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12))
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Bind events
        self.text_area.bind("<space>", self.check_on_space)
        self.text_area.bind("<Return>", self.check_on_return)
        self.text_area.bind("<KeyRelease>", self.delayed_check)
        
        # Bind right-click (Button-2 for Mac, Button-3 for other platforms)
        if self.root.tk.call('tk', 'windowingsystem') == 'aqua':  # macOS
            self.text_area.bind("<Button-2>", self.show_context_menu)
            # Also bind Control-click as it's common on Mac
            self.text_area.bind("<Control-Button-1>", self.show_context_menu)
        else:  # Windows/Linux
            self.text_area.bind("<Button-3>", self.show_context_menu)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configure tags for marking misspelled words
        self.text_area.tag_configure("misspelled", foreground="red", underline=True)
        
        # Dictionary to store misspelled words and their positions
        self.misspelled_words = {}
        
        # After ID for delayed checking
        self.after_id = None
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Dictionary menu
        dict_menu = tk.Menu(menubar, tearoff=0)
        dict_menu.add_command(label="Load Dictionary", command=self.load_dictionary)
        menubar.add_cascade(label="Dictionary", menu=dict_menu)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Check Spelling", command=self.check_spelling)
        tools_menu.add_command(label="Clear All Marks", command=self.clear_marks)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        
        self.root.config(menu=menubar)
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.clear_marks()
        self.status_var.set("New file created")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.check_spelling()
                self.status_var.set(f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, 'w') as file:
                    file.write(content)
                self.status_var.set(f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
    
    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
    
    def load_dictionary(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Dictionary files", "*.dict"), ("All files", "*.*")]
        )
        if file_path:
            success = self.spell_checker.load_dictionary(file_path)
            if success:
                self.status_var.set(f"Dictionary loaded: {file_path}")
                # Re-check spelling with new dictionary
                self.check_spelling()
            else:
                messagebox.showerror("Error", "Failed to load dictionary")
    
    def check_spelling(self):
        """Check spelling of all text"""
        # Clear previous marks
        self.clear_marks()
        
        # Get all text
        text = self.text_area.get(1.0, tk.END)
        
        # Find misspelled words
        words = re.finditer(r'\b[a-zA-Z]+\b', text)
        
        for match in words:
            word = match.group(0)
            start_pos = match.start()
            end_pos = match.end()
            
            # Convert position to tkinter format (line.char)
            start_line_char = self.text_area.index(f"1.0 + {start_pos} chars")
            end_line_char = self.text_area.index(f"1.0 + {end_pos} chars")
            
            # Check if word is misspelled
            if not self.spell_checker.check_word(word):
                self.text_area.tag_add("misspelled", start_line_char, end_line_char)
                self.misspelled_words[(start_line_char, end_line_char)] = word
        
        self.status_var.set(f"Spell check complete. Found {len(self.misspelled_words)} misspelled words.")
    
    def clear_marks(self):
        """Clear all misspelled marks"""
        self.text_area.tag_remove("misspelled", "1.0", tk.END)
        self.misspelled_words = {}
    
    def check_on_space(self, event):
        """Check spelling when space is pressed"""
        self.check_current_word()
        return
    
    def check_on_return(self, event):
        """Check spelling when return is pressed"""
        self.check_current_word()
        return
    
    def delayed_check(self, event):
        """Set up delayed spell check"""
        if self.after_id:
            self.root.after_cancel(self.after_id)
        self.after_id = self.root.after(1000, self.check_current_word)
    
    def check_current_word(self):
        """Check spelling of the current word"""
        # Get current cursor position
        current_pos = self.text_area.index(tk.INSERT)
        
        # Get line and column
        line, col = map(int, current_pos.split('.'))
        
        # Get the current line text
        line_text = self.text_area.get(f"{line}.0", f"{line}.end")
        
        # Find words in the current line
        words = list(re.finditer(r'\b[a-zA-Z]+\b', line_text))
        
        # Remove previous misspelled marks on this line
        self.text_area.tag_remove("misspelled", f"{line}.0", f"{line}.end")
        
        # Update misspelled_words to remove entries from this line
        to_remove = []
        for pos in self.misspelled_words:
            start_pos = pos[0]
            start_line = int(start_pos.split('.')[0])
            if start_line == line:
                to_remove.append(pos)
        
        for pos in to_remove:
            del self.misspelled_words[pos]
        
        # Check each word in the line
        for match in words:
            word = match.group(0)
            start_col = match.start()
            end_col = match.end()
            
            # Check if word is misspelled
            if not self.spell_checker.check_word(word):
                start_pos = f"{line}.{start_col}"
                end_pos = f"{line}.{end_col}"
                
                self.text_area.tag_add("misspelled", start_pos, end_pos)
                self.misspelled_words[(start_pos, end_pos)] = word
    
    def show_context_menu(self, event):
        """Show context menu with spelling suggestions"""
        # Get click position
        click_pos = f"@{event.x},{event.y}"
        
        # Check if click is on a misspelled word
        for (start_pos, end_pos), word in self.misspelled_words.items():
            if self.text_area.compare(start_pos, "<=", click_pos) and self.text_area.compare(click_pos, "<=", end_pos):
                # Get suggestions
                suggestions = self.spell_checker.get_suggestions(word)
                
                # Create context menu
                context_menu = tk.Menu(self.root, tearoff=0)
                
                # Add suggestions
                for suggestion in suggestions:
                    context_menu.add_command(
                        label=suggestion,
                        command=lambda s=suggestion, start=start_pos, end=end_pos: self.replace_word(s, start, end)
                    )
                
                if not suggestions:
                    context_menu.add_command(label="No suggestions", state=tk.DISABLED)
                
                context_menu.add_separator()
                context_menu.add_command(
                    label="Add to dictionary",
                    command=lambda w=word, start=start_pos, end=end_pos: self.add_to_dictionary(w, start, end)
                )
                
                # Display context menu
                try:
                    context_menu.tk_popup(event.x_root, event.y_root)
                finally:
                    context_menu.grab_release()
                
                return "break"  # Prevent default context menu
    
    def replace_word(self, suggestion, start_pos, end_pos):
        """Replace misspelled word with suggestion"""
        self.text_area.delete(start_pos, end_pos)
        self.text_area.insert(start_pos, suggestion)
        
        # Remove misspelled tag
        if (start_pos, end_pos) in self.misspelled_words:
            del self.misspelled_words[(start_pos, end_pos)]
        
        # Re-check current line
        self.check_current_word()
    
    def add_to_dictionary(self, word, start_pos, end_pos):
        """Add word to dictionary"""
        self.spell_checker.trie.insert(word.lower())
        
        # Remove misspelled tag
        self.text_area.tag_remove("misspelled", start_pos, end_pos)
        
        # Remove from misspelled words
        if (start_pos, end_pos) in self.misspelled_words:
            del self.misspelled_words[(start_pos, end_pos)]
        
        self.status_var.set(f"Added '{word}' to dictionary")


if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    
    # Create the app
    app = SpellCheckerApp(root)
    
    # Start the main loop
    root.mainloop()