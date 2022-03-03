from nbconvert.exporters.html import HTMLExporter
import shutil as sh
import os
import zipfile as zf
import nbformat

from pathlib import Path


exporter, pth = HTMLExporter(), os.path


def main():
    Root = Path(pth.dirname(pth.abspath(__file__)))
    html = Root / "html"

    outdir = html.joinpath("notebooks")
    outdir.mkdir(exist_ok=True)

    if 1:
        for notebook in Root.joinpath("notebooks", "hu").glob("*.ipynb"):
            contents = notebook.read_bytes()
            contents = nbformat.reads(contents, as_version=4)

            body, _ = exporter.from_notebook_node(contents)

            out = "%s.html" % notebook.name.split(".")[0]

            with outdir.joinpath(out).open("w") as f:
                f.write("".join(body))

    if 1:
        cwd = os.getcwd()
        try:
            os.chdir(html)
            sh.make_archive(
                str(Root.joinpath("releases", "jegyzet")),
                "zip",
            )
        finally:
            os.chdir(cwd)


if __name__ == "__main__":
    main()
