from nbconvert.exporters.html import HTMLExporter
import shutil as sh
import os
import zipfile as zf
import nbformat

import utils

exporter = HTMLExporter()

Root = utils.Path(__file__).abspath().dirname()
html = Root.join("html")
outdir = html.join("notebooks").mkdir()

def main():
    if 1:
        for notebook in Root.join("notebooks", "hu", "*.ipynb").iglob():
            contents = notebook.read_all()
            contents = nbformat.reads(contents, as_version=4)
    
            body, _ = exporter.from_notebook_node(contents)
            
            out = notebook.basename().replace_ext("html")
            
            with outdir.join(out).open("w") as f:
                f.write("".join(body))
    
    if 1:
        with utils.cd(html):
            sh.make_archive(
                Root.join("releases", "jegyzet").get_path(),
                "zip",
            )    
    
if __name__ == "__main__":
    main()
