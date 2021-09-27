# Rename torrent from hash

If your torrent client renamed your torrent's filename to its hash and you want to rename it back to torrent's name, this Python 3 script will help you do that.

## Dependency

* [torrentool](https://github.com/idlesign/torrentool)

To install, run this command:
```
pip install --upgrade -r torrentool
```

## Usage

Run the script with this command:

```
python rename-from-hash.py /path/to/torrentfiles
```

It will automatically rename all the torrent files to their corresponding name.

Note: If torrent name already exist, it will add a number before the ``.torrent`` extension.
