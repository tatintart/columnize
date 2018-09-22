# Columnize

> List things in columns

`columnize` is a small python module and command to format a list of words in columns.

## Install

The project is using [setuptools](https://setuptools.readthedocs.io/).
To install it, run `python3 setup.py install`.

## Usage

Pipe the output of a command to `columnize`. For instance:

```
echo $PATH | sed 's/:/ /g' | columnize
```
