import os
import sys
import getopt
import time
from ffmpy import FFmpeg


if __name__ == "__main__":
    flacfile = sys.argv[1]
    originalflac = flacfile
    flacfolder = sys.argv[2]
    mp3 = sys.argv[3]
    print("start converting file: " + flacfile)

    flacfile = flacfile.removeprefix(flacfolder)
    flacfile, file_extension = os.path.splitext(flacfile)
    mp3folder = os.path.dirname(flacfile)
    mp3folder = os.path.join(mp3, mp3folder)
    print(mp3folder)
    print(flacfile)
    if not os.path.exists(mp3folder):
        os.mkdir(mp3folder)

    mp3fileandfolder = os.path.join(mp3, flacfile + ".mp3")

    if os.path.exists(mp3fileandfolder):
        os.remove(mp3fileandfolder)

    ff = FFmpeg(
        inputs={originalflac: None},
        outputs={mp3fileandfolder: "-c:a libmp3lame -b:a 320k"}
    )

    ff.run()
