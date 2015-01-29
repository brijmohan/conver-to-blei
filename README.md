# convert-to-blei
-----------------
This is a utility file which converts a text corpus to LDA-C Blei format. It takes the folder where corpus files are stored, assuming each file represents a new document.

It then generates 3 files.

    - data.txt : single document file in xml format
    - data.dat : documents vocab frequency in (M id1:f1 id2:f2 ... ) format
    - vocab.txt : vocabulary file for the text corpus


Usage
=====

`python convertBleiFormat.py <path to folder where corpus files are stored> <path to output folder>`
