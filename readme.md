Git Extensions Manual
=====================
This repository contains the new Git extensions Manual. Feel free to help us improve this manual by sending pull requests
or by opening issues.

View Online
-----------
The current documentation can be viewed here: https://gitextensions.readthedocs.org/en/latest/

PDF and others format can be downloaded here: https://readthedocs.org/projects/gitextensions/downloads/

**Note:** Only the HTML is "supported" (i.e: on the display point of view). Other format might have layout issue
but the content remains the same for all format, wether or not you build it locally (provided your local clone is 
up to date).

Build
-----

### HTML
Simply run `make-html.cmd`. You can also use `make-singlehtml.cmd` to generate a single HTML
file. The `make_and_start_Browser.cmd` is an alias of `make-html.cmd` that will open in your
default browser the documentation main index.

### HTML Help Files
**Warning:** This format is not completly supported (i.e: you can generate it but we don't 
guarantee an as good display quality as for HTML).

Download HTML Help Workshop (http://www.microsoft.com/en-us/download/details.aspx?id=21138).

To build the file, use `makeHTMLHelp.cmd`

### PDF
**Warning:** This format is not completly supported (i.e: you can generate it but we don't 
guarantee an as good display quality as for HTML).

To use the PDF builder, you'll need to install:

* rst2pdf `easy_install rst2pdf`
* pil `easy_install pil`

Also add `,'rst2pdf.pdfbuilder'` to the source/conf.py file at the line 28. Then run `make.cmd pdf`.
