# encoding: utf-8

import xml.dom.minidom
import shutil
import os
from os import listdir
from os.path import isfile, join

def main():
    pathToPlaylists = "/mnt/user/appdata/binhex-jellyfin/data/data/playlists"
    for x in os.listdir(pathToPlaylists):
        doc = xml.dom.minidom.parse(pathToPlaylists + "/" +x + "/playlist.xml")

        print(doc.nodeName)

        playlistPath = u"/mnt/user/playlists/"+ doc.getElementsByTagName("LocalTitle")[0].firstChild.nodeValue + "/"
        print (playlistPath)
        path = doc.getElementsByTagName("Path")

        if os.path.exists(playlistPath):
            print("")
        else:
            os.mkdir(playlistPath) 

        onlyfiles = [f for f in listdir(playlistPath) if isfile(join(playlistPath, f))]
        
        filesToDelete = onlyfiles
        
        for p in path:
            f1,f2, s = p.firstChild.nodeValue.split("/", 2)
            completeOriginalPath = "/mnt/user/Data/" + s
            
            filename = os.path.basename(completeOriginalPath)
            exists = False
            for f in onlyfiles:
                if f == filename:
                    exists = True
                    filesToDelete.remove(f)
                    break;

            if exists:
                print("")
            else:
                print("")
                shutil.copy(completeOriginalPath, playlistPath)

        print(filesToDelete)

        for d in filesToDelete:
            os.remove(playlistPath + "/"+d)
            print (d)


if __name__ == "__main__":
    main();