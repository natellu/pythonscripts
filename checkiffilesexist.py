import os

def main():
    pathtomp3s = r"C:\Users\natellu\Music\mp3"
    pathtoflacs = r"C:\Users\natellu\Music\flacs"
    
    mp3subfolders, mp3sfiles = run_fast_scandir(pathtomp3s, [".mp3"])
    flacsubfolders, flacfiles = run_fast_scandir(pathtoflacs, [".flac"])
    
    for f in mp3sfiles:
        root_ext = os.path.splitext(f)
        print(root_ext[0])
        
def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files




if __name__ == "__main__":
    main();