# Ransomware developement

Very simple ransomware. Works with plain text files, with a symmetric encription. Academic purpose only.

## Getting Started

Different options to work with:
* (-h) Help menu.
* (-p) Path to the directory files you want to encrypt/decrypt.
* (-a) Action you want to do. Only two possible values: 'encrypt' or 'decrypt'.
* (-k) If action is 'decrypt', intro the key located in key.key in order to decrypt.

## Usage examples

### Help menu

```
python3 main.py -h
```

### Encrypt

```
pyhton3 main.py -p ~/dir1/dir2/target -a encrypt
```

### Decrypt

```
pyhton3 main.py -p ~/dir1/dir2/target -a decrypt -k 8qbyg_-jUVt6q5rly7G3a23t71rOogBz5M0Tk3SWCFs=
```
