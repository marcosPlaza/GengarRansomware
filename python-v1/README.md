# Ransomware developement

Very simple ransomware. Works with plain text files, with a symmetric encription. Academic purpose only.

## (Currently deprecated) Getting Started

Different options to work with:
* (-h) Help menu.
* (-p) Path to the directory files you want to encrypt/decrypt.
* (-a) Action you want to do. Only two possible values: 'encrypt' or 'decrypt'.

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
pyhton3 main.py -p ~/dir1/dir2/target -a decrypt
```
