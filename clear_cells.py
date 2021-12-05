import nbformat as nbf
ntbk = nbf.read("Test.ipynb", nbf.NO_CONVERT)
new_ntbk = ntbk
new_ntbk.cells = [cell if cell.cell_type == "markdown" else nbf.v4.new_code_cell() for cell in ntbk.cells ]
nbf.write(new_ntbk, "Test2.ipynb", version=nbf.NO_CONVERT)
