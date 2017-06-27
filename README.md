dmensamenu
==========

Print canteen menus using `dmenu`.
The menus is fetched from http://openmensa.org/.

Requirements
------------

Of course, this requires dmenu to be installed.
If you wish to use it with something else like Rofi, send in a pull request.

Installation
------------

    $ pip install --user git+https://github.com/dotlambda/dmensamenu.git

Usage
-----

    $ dmensamenu id

where *id* is the OpenMensa canteen ID, e.g.

* 279 for Heidelberg INF
* 280 for Heidelberg Marstall
* 281 for Heidelberg Triplex

You can even pass extra arguments to dmenu:

    $ dmensamenu --dmenu "dmenu -l \$lines -nb \#101b2a -nf \#dcdccc -sb \#dcdccc -sf \#101b2a -fn 'Fira Mono'" 280 

See

    $ dmensamenu --help

for all available options.
