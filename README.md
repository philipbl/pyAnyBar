# pyAnyBar

A Python module for [AnyBar](https://github.com/tonsky/AnyBar).

## Install

```
pip install pyanybar
```

## Usage

```
from anybar import AnyBar

AnyBar().change('red')
```

A port number can also be added:

```
AnyBar(port=11111).change('red')
```

pyAnyBar always works with [Brett Terpstra's fork](https://github.com/ttscoff/AnyBar) of AnyBar that allows for text to be displayed:

```
AnyBar().change('cyan', text='hello world')

AnyBar().change('none')
```
