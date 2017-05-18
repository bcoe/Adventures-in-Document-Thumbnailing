import os
import optparse
from thumbnail import Thumbnail

def main():
    parser = optparse.OptionParser()
    
    parser.add_option(
        "-i",
        "--in-file",
        action="store",
        dest="in_file",
        default=None,
        help="Document to thumbnail."
    )

    parser.add_option(
        "-d",
        "--in-directory",
        action="store",
        dest="in_dir",
        default=None,
        help="Directory of documents to thumbnail."
    )

    parser.add_option(
        "-w",
        "--width",
        action="store",
        dest="width",
        default='490',
        help="Width of thumbnail."
    )

    parser.add_option(
        "-t",
        "--height",
        action="store",
        dest="height",
        default='700',
        help="Height of thumbnail."
    )
    
    parser.add_option(
        "-o",
        "--out-dir",
        action="store",
        dest="out_dir",
        default='./',
        help="Directory to output thumbnail to."
    )
    
    (options, args) = parser.parse_args()
    
    if options.in_file:
        try:
            Thumbnail(
                in_file=options.in_file,
                out_dir=options.out_dir,
                width=int( options.width ),
                height=int( options.height )
            )
        except Exception, e:
            print '%s. Make sure all the dependencies for tomthumb are installed:\n\n\tapt-get install python-imaging abiword imagemagick timelimit' % (e)
    elif options.in_dir:
        for f in os.listdir( options.in_dir ):
            in_file = '%s/%s' % (options.in_dir, f)
            if os.path.isfile( in_file ):
                try:
                    Thumbnail(
                        in_file=in_file,
                        out_dir=options.out_dir,
                        width=int( options.width ),
                        height=int( options.height )
                    )
                except Exception, e:
                    print e
    else:
        print "type 'tomthumb -h' for usage information."
                
if __name__ == "__main__":
    main()