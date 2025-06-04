import nbformat

# Test adding a simple markdown cell
notebook_path = r"D:\Github\Relational_Life_Practice\rag_dev\notebooks\terry_real_corpus_processing.ipynb"

# Read notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

print(f"Current cells: {len(nb.cells)}")

# Add a simple test markdown cell
test_content = """## 3. Test Section Added via Command

This cell was added programmatically using nbformat!"""

new_cell = nbformat.v4.new_markdown_cell(test_content)
nb.cells.append(new_cell)

# Write back
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(f"Added cell! New total: {len(nb.cells)}")
