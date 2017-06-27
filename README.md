dmensamenu
==========

Print Heidelberg canteen menus using `dmenu`.
The menu is fetched from http://stw.uni-heidelberg.de/de/speiseplan.

Requirements
------------

Of course, this requires dmenu to be installed.
If you wish to use it with something else like Rofi, send in a pull request.

Installation
------------

    $ git clone https://github.com/dotlambda/dmensamenu.git
    $ cd dmensamenu
    $ pip install --user .

Usage
-----

    $ dmensamenu canteen-name

where *canteen-name* is one of

* INF
* Marstall
* Triplex

You can even pass extra arguments to dmenu:

    $ dmensamenu Marstall -nb \#101b2a -nf \#dcdccc -sb \#dcdccc -sf \#101b2a -fn "Fira Mono"
