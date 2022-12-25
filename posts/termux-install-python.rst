.. title: Installing Python on Termux
.. slug: installing-python-on-termux
.. date: 2021-02-20 12:00:00 UTC-05:00
.. status: draft
.. tags: samsung, android, termux, python
.. category: Tools
.. link: 
.. description: 
.. type: text

As mentioned in a previous post, I'm really liking my Samsung Galaxy
Tab S6 Lite. Now it's time to turn it into a device capable of
lightweight programming - and the pleasant surprise is that it might
be good enough for even more.

Let's get started with installing Python 3.x from the Termux package
repository. To find packages matching Python in the name:

.. code-block:: bash

    $ pkg search python

    Checking availability of current mirror: ok

    Sorting... Done
    Full Text Search... Done
    python/stable 3.9.7 aarch64
      Python 3 programming language intended to enable clear programs
    ...

That's good enough - we get Python 3.9.7 which is quite up to date. Note
that Termux uses a rolling release model - that means you get the most
up to date packages, but you can't mix and match or downgrade to older
versions without a LOT of work.

.. code-block:: bash

    $ pkg install python

This will take a few minutes, so be patient. Once that's done you can
fire up Python and test out the console. Next we'll install iPython
and some useful packages like numpy and matplotlib - maybe we can do
a little more than lightweight work on this tablet!

in subsequent articles I'll add git, Python, matplotlib, and a few other
packages. In fact, this website is generated on the Galaxy Tab S6 Lite
using `Nikola`_ , a static website generator.

.. _Termux: https://termux.com/
.. _Termux from the Google Play Store: https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US
.. _Nikola: https://getnikola.com/
.. _Infiland: https://www.amazon.de/-/en/INFILAND-Case-Galaxy-Lite-Navy/dp/B0863BMT4X/ref=sr_1_10?dchild=1&keywords=tablet+h%C3%BClle+tab+s6+lite+infiland&qid=1613914719&sr=8-10
