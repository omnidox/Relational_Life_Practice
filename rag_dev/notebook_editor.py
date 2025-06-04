#!/usr/bin/env python3
"""
Jupyter Notebook Cell Adder
Add cells to existing Jupyter notebooks programmatically
"""
import nbformat
import sys
from pathlib import Path

def add_markdown_cell(notebook_path, content, position=None):
    """Add a markdown cell to the notebook"""
    # Read existing notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create new markdown cell
    new_cell = nbformat.v4.new_markdown_cell(content)
    
    # Add to notebook
    if position is None:
        nb.cells.append(new_cell)
    else:
        nb.cells.insert(position, new_cell)
    
    # Write back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"Added markdown cell to {notebook_path}")

def add_code_cell(notebook_path, code, position=None):
    """Add a code cell to the notebook"""
    # Read existing notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create new code cell
    new_cell = nbformat.v4.new_code_cell(code)
    
    # Add to notebook
    if position is None:
        nb.cells.append(new_cell)
    else:
        nb.cells.insert(position, new_cell)
    
    # Write back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"Added code cell to {notebook_path}")

def list_cells(notebook_path):
    """List all cells in the notebook"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    print(f"Notebook has {len(nb.cells)} cells:")
    for i, cell in enumerate(nb.cells):
        cell_type = cell.cell_type
        if cell_type == 'markdown':
            preview = cell.source[:50].replace('\n', ' ')
        else:
            preview = cell.source[:50].replace('\n', ' ')
        print(f"   {i}: {cell_type} - {preview}...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python notebook_editor.py <command> <notebook_path> [content]")
        print("Commands: list, add-md, add-code")
        sys.exit(1)
    
    command = sys.argv[1]
    notebook_path = sys.argv[2]
    
    if command == "list":
        list_cells(notebook_path)
    elif command == "add-md" and len(sys.argv) > 3:
        content = sys.argv[3]
        add_markdown_cell(notebook_path, content)
    elif command == "add-code" and len(sys.argv) > 3:
        code = sys.argv[3]
        add_code_cell(notebook_path, code)
    else:
        print("Invalid command or missing content")
