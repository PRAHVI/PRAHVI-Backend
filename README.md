## Dependencies
```
sudo apt-get install python-pip python-dev nginx virtualenv
```

### Recommended
* virtualenvwrapper

## Set up

Get the dependency library binaries and the tessdata from Abe. 

Make a virtual env:
```
mkvirtualenv prahvi_backend
```
```
workon prahvi_backend
```

Run:
```
tar -zxvf dependencies.tar.gz -C .
```
```
tar -zxvf tessdata.tar.gz -C .
```
```
rm dependencies.tar.gz tessdata.tar.gz
```
```
chmod 755 bootstrap.sh
```
```
./bootstrap.sh
```
