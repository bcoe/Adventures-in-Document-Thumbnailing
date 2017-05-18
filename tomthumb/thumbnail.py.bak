import os
import re
import tempfile
from PIL import Image
from subprocess import call

class Thumbnail(object):
    
    SUPPORTED_EXTENSIONS = ['doc', 'docx', 'odt', 'rtf', 'txt', 'ods', 'pdf']
    
    def __init__(self, in_file=None, out_dir='./', width=490, height=770):
        
        self.delete_tmp_pdf = False # Important otherwise we delete the original PDFs.
        
        self.in_file = in_file
        self.in_file_prefix, self.in_file_ext = self._get_filename_and_extension()
        if not self.in_file_ext in Thumbnail.SUPPORTED_EXTENSIONS:
            raise Exception('%s was not a supported extension' % self.in_file_ext)
        
        print 'Creating thumbnail %s.jpg in %s' % (self.in_file_prefix, out_dir)
        
        self.width = width
        self.height = height
        self.out_dir = out_dir
        self._create_temporary_pdf()
        self._convert_pdf_to_temporary_image()
        self._create_thumbnail()
        
        if self.delete_tmp_pdf:
            self._remove_file(self.tmp_pdf_path)
        
        self._remove_file(self.tmp_image_path)
        
    def _get_filename_and_extension(self):
        match = re.search(r'(?P<prefix>[^/.]*)\.(?P<ext>.*)$', self.in_file)
        return match.group('prefix'), match.group('ext')
        
    def _create_temporary_pdf(self):
        
        # If we're converting a PDF we can just use the file directly.
        if self.in_file_ext == 'pdf':
            self.tmp_pdf_path = self.in_file
            return
            
        self.delete_tmp_pdf = True
        
        self.tmp_pdf_path = tempfile.mktemp(suffix='.pdf')
        if call("timelimit -t 30 -- abiword --to=pdf '%s' -o '%s'" % (self.in_file, self.tmp_pdf_path), shell=True) != 0:
            raise Exception('Could not create temporary PDF file')
    
    def _convert_pdf_to_temporary_image(self):
        self.tmp_image_path = tempfile.mktemp(suffix='.jpg')
        if call("timelimit -t 30 -- convert '%s[0]' '%s'" % (self.tmp_pdf_path, self.tmp_image_path), shell=True) != 0:
            raise Exception('Could not convert PDF to image')
    
    def _create_thumbnail(self):
        img = Image.open(self.tmp_image_path)
        img = img.resize(
            (self.width, self.height),
            Image.ANTIALIAS
        )
        img.save('%s/%s.jpg' % (self.out_dir, self.in_file_prefix), 'JPEG', quality=80)
            
    def _remove_file(self, path):
        os.remove(path)