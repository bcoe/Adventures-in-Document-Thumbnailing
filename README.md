Adventures in Document Thumbnailing
===================================

Talk By, [@benjamincoe](http://twitter.com/#/benjamincoe)

The Problem
-----------

My company, [Attachments.me](http://attachments.me), makes a visual representation of the attachments inside your inbox.

Recently I've been rebuilding the part of our system that creates these thumbnails.

* I wanted to use open-source libraries to perform the thumbnailing.
* I wanted to use a Linux server for hosting the service.
* I wanted to be able to create thumbnails for the majority of documents our system processes.
* I needed things to work on a large-scale (millions and millions of thumbnails being created).

Even though, for all intents and purposes, we live in the future, solving these problems was a bit of a hassle.

OpenOffice (LibreOffice) / PythonUNO
------------------------------------

Up until quite recently we were using OpenOffice as part of our document thumbnailing process. OpenOffice is used to convert a document format to a PDF, at which point it can be easily converted into an image.

**Pros**

* Supported most major document formats.
* PythonUNO provides a handy API interface to OpenOffice.

**Why We Abandoned It**

* It's not thread safe.
* It's slow and leaks memory.

One of the bigger problems we ran into with OpenOffice was its inability to handle concurrent access. We built middleware that limited document processing to one document at a time, which helped. But, OO would frequently hang during conversions, and this made for a huge bottleneck in the system.

80/20 Rule to the Rescue
------------------------

Taking a look at the millions of attachments that we had indexed, I noticed something: 80% of documents were either .doc, .docx, or .pdf.

This made me rethink the necessity of using OpenOffice for thumbnail creation.

PIL / ImageMagick / AbiWord
--------------------------

The approach we now use for thumbnailing uses three open-source libraries:

* _AbiWord_ converts various document formats into PDFs.
* _ImageMagick_ converts the first page of the PDF into a JPG image.
* _python-imaging-libray_ is used to resize the images outputted by ImageMagick (this could be done entirely using ImageMagick, but I like the PIL interface).

This new approach:

* Supports 80% of the documents we observe.
* Deals better with multiple-processes.
* Runs about 30% faster than the original approach.

Tomthumb
--------

I've open-sourced a library called tomthumb (see /tomthumb). This demonstrates the thumbnailing approach discussed above.

Usage
=====

```bash
tomthumb -o outputdir/ --width=70 --height=120

OR

tomthumb -d inputdir/ -o outputdir/
```

Copyright
---------

Copyright (c) 2011 Attachments.me. See LICENSE.txt for further details.