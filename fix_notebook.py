import nbformat

notebooks = [
    "1_DA_Basics/1_DA1.ipynb",
    "1_DA_Basics/2_DataCleanup.ipynb",
    "1_DA_Basics/4_matplotlib_labelling.ipynb",
]

for path in notebooks:
    nb = nbformat.read(path, as_version=4)

    # Remove notebook-level widget metadata
    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]

    # Remove cell metadata related to widgets if present
    for cell in nb.cells:
        if "widgets" in cell.get("metadata", {}):
            del cell["metadata"]["widgets"]

    nbformat.write(nb, path)
    print(f"Fixed: {path}")