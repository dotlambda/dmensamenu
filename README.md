dmensamenu
==========

Print canteen menus using `dmenu`.
The menus are fetched from http://openmensa.org/.

Requirements
------------

Of course, this requires dmenu to be installed.
If you wish to use it with something else like Rofi, send in a pull request.

Installation
------------

### From your package repo
[![Packaging status](https://repology.org/badge/vertical-allrepos/dmensamenu.svg)](https://repology.org/metapackage/dmensamenu)

### From source
    $ pip install --user git+https://github.com/dotlambda/dmensamenu.git

Usage
-----

    $ dmensamenu id

where *id* is the OpenMensa canteen ID.
If you don't know yours, just use `dmensamenu --search` and search for it.
After pressing Return, the ID will be printed to stdout.

You can even pass extra arguments to dmenu:

    $ dmensamenu --dmenu "dmenu -l \$lines -nb \#101b2a -nf \#dcdccc -sb \#dcdccc -sf \#101b2a -fn 'Fira Mono'" 280 

See `dmensamenu --help` for all available options.
