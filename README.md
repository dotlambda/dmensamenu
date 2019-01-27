dmensamenu
==========

Print canteen menus using `dmenu`.
The menus are fetched from https://openmensa.org/.

Requirements
------------

Dmensamenu is written in Python 3 and depends on [Requests](http://python-requests.org/).
It also requires [dmenu](https://tools.suckless.org/dmenu/) to be installed.

Installation
------------

### From your package repo
[![Packaging status](https://repology.org/badge/vertical-allrepos/dmensamenu.svg)](https://repology.org/metapackage/dmensamenu)

### From source
    $ pip install --user git+https://github.com/dotlambda/dmensamenu.git

Usage
-----

    $ dmensamenu ID

where *ID* is the OpenMensa canteen ID.
If you don't know yours, just use `dmensamenu --search` and search for it.
After pressing Return, the ID will be printed to stdout.

You can even pass extra arguments to dmenu:

    $ dmensamenu --dmenu "dmenu -l \$lines -nb \#101b2a -nf \#dcdccc -sb \#dcdccc -sf \#101b2a -fn 'Fira Mono'" 281

or replace dmenu by Rofi:

    $ dmensamenu --dmenu "rofi -dmenu -i" --search --city Berlin

See `dmensamenu --help` for all available options.
