# Columnize

> List things in columns

`columnize` is a small python module and command to format a list of words in columns.

## Install

The project is using [setuptools](https://setuptools.readthedocs.io/).
To install it, run `python3 setup.py install`.

## Usage

In its simplest form, pipe the output of a command to `columnize`. For instance:

```
» echo $PATH | sed 's/:/ /g' | columnize
```

You can also columnize the content of files:

```
» columnize test/countries.txt LICENSE README.md
```

And control the output:


```
» columnize -w 40 test/countries.txt
Afghanistan  Greenland      Nepal
Akrotiri     Grenada        Netherlands
Albania      Guadeloupe     Nicaragua
Algeria      Guam           Niger
Andorra      Guatemala      Nigeria
Angola       Guernsey       Niue
Anguilla     Guinea         Norway
Antarctica   Guinea-Bissau  Oman
Argentina    Guyana         Pakistan
Armenia      Haiti          Palau
[...]

» columnize -w 80 -s 10 test/countries.txt
Afghanistan          Dominica               Laos                   Poland
Akrotiri             Ecuador                Latvia                 Portugal
Albania              Egypt                  Lebanon                Qatar
Algeria              Eritrea                Lesotho                Reunion
Andorra              Estonia                Liberia                Romania
Angola               Ethiopia               Libya                  Russia
Anguilla             Fiji                   Liechtenstein          Rwanda
Antarctica           Finland                Lithuania              Samoa
Argentina            France                 Luxembourg             Senegal
Armenia              Gabon                  Macau                  Seychelles
[...]
```
