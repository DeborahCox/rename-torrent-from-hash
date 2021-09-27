import os
import sys
from torrentool.api import Torrent

torrents_path = "\n".join(sys.argv[1:]) 

for subdir, dirs, files in os.walk(torrents_path):
    for filename in files:
        filepath = subdir + os.sep + filename
        # Only rename files ended with .torrent extension
        if filepath.endswith(".torrent"):
            torrent = Torrent.from_file(filepath)
            torrent_name = torrent.name
            print (subdir + torrent_name)
            if not os.path.isfile(torrents_path + torrent_name + ".torrent"):
                os.rename(filepath, torrents_path + torrent_name + ".torrent")
            else:  # In case duplicate torrent file name
                # If ABC.torrent exists, rename to ABC 1.torrent, ABC 2.torrent, etc.
                counter = 1
                while os.path.isfile(torrents_path + torrent_name + " " + str(counter) + ".torrent"):
                    counter += 1
                os.rename(filepath, subdir + torrent_name + " " + str(counter) + ".torrent")

print("Rename complete")
