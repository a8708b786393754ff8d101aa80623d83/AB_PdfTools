# AB_pdfTools
## python scripts which encrypts, decrypts is can raw force the encryption of a pdf file

## Install 

```sh
git clone https://github.com/a6888b/AB_pdfTools
pip install -r requirements.txt
``` 

## Using
Encrypt file pdf:
```sh
python main.py --encrypt -f <file_to_encrypt> -p <password>
```

decrypter pdf file
```sh
python main.py --decrypt -p <password> -f <file_to_decrypt>
```

brute force pdf
```sh
python main.py --decrypt -w <wordlists> -f <file_to_brute_force>
```