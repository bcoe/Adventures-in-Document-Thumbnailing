Adventures in Document Thumbnailing
===================================

A talk by [@benjamincoe](http://twitter.com/#/benjamincoe)

The Problem
-----------

My company, [Attachments.me](http://attachments.me), makes a visual representation of the attachments inside your inbox.

Recently I've been rebuilding the part of our system that creates these thumbnails.

* I wanted to use open-source libraries to perform the thumbnailing.
* I wanted to use a Linux server for hosting the service.
* I wanted to be able to create thumbnails for the majority of documents that our system processes.
* I needed things to work on a large-scale (millions and millions of thumbnails being created).

Even though, for all intents and purposes, [we live in the future](http://www.baconnaise.com/), solving these problems was a bit of a hassle.

LibreOffice / PythonUNO
------------------------------------

Up until quite recently, we were using LibreOffice as part of our document thumbnailing process. It was used to convert various document formats into PDFs, at which point the could easily be converted into images.

**Pros**

* Supported most major document formats.
* PythonUNO provides a handy API interface to LibreOffice.

**Why We Abandoned It**

* It's not thread safe.
* It's slow and leaks memory.

The main problem we ran into with LibreOffice was its inability to handle concurrent access. We built middleware that limited document processing to one document at a time, which helped. But, this also created a huge bottleneck in our system.

80/20 Rule to the Rescue
------------------------

Taking a look at the millions of attachments that we had indexed, I noticed something: 80% of documents were either .doc, .docx, or .pdf.

This made me rethink the necessity of using LibreOffice for thumbnail creation.

PIL / ImageMagick / AbiWord
--------------------------

The approach we now use for thumbnailing uses three open-source libraries:

* _AbiWord_ converts various document formats into PDFs.
* _ImageMagick_ converts the first page of the PDF outputted by AbiWord into a JPG image.
* _python-imaging-libray_ is used to resize the images outputted by ImageMagick (this could be done entirely using ImageMagick, but I like the PIL interface).

This new approach:

* Supports 80% of the documents we observe.
* Plays nicely in a multi-process environment.
* Runs about 30% faster than the original approach.

Tomthumb
--------

I've open-sourced a library called tomthumb __(see the /tomthumb folder in this repo)__, that demonstrates the thumbnailing approach discussed above.


Dependencies
============

```bash
apt-get install python-imaging abiword imagemagick timelimit
```

Usage
=====

```bash
tomthumb -i foo.doc -o out/ --width=70 --height=120
```

__Or__

```bash
tomthumb -d in/ -o out/
```

Copyright
---------

Copyright (c) 2011 Attachments.me. See LICENSE.txt for further details.