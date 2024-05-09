.. title: Installing Jupyter and More Tools
.. slug: termux-install-jupyter-and-more
.. date: 2021-02-20 12:00:00 UTC-05:00
.. status: draft
.. tags: samsung, android, termux, python
.. category: Tools
.. link: 
.. description: 
.. type: text

Let's jump right into installing git and a few other helpful
tools on our Samsung Tab 6S Lite Android Tablet.

.. code-block:: bash

    $ pkg search git

    Checking availability of current mirror: ok

    Sorting... Done
    Full Text Search... Done
    python/stable 2.33.0-1 aarch64
      Fast, scaleable, distributed revision control system
    ...

And now we can install the packages we need (I have not included all the
other package searches needed for this session).

.. code-block:: bash

    $ pkg install git build-essential

Similarly, now that we have Python installed, we can add a few
packages that we know will be needed to do useful work, like numpy
and matplotlib.

We can also install sphinx and a few other utilities. If you run
into trouble check out `Termux specific install hints for Python packages`_.

In some cases, the packages need to be built from
source on the tablet - but this takes a lot of time, so
it might be better to take advantage of the "pointless" 
install method that gives us pre-built binaries:

.. code-block:: bash

    # Subscribe to the pointless repository

    $ curl -LO https://its-pointless.github.io/setup-pointless-repo.sh
    $ bash setup-pointless-repo.sh

    # Now we can install (and search) for the Python packages using
    # pkg instead of pip

    $ pkg install numpy

    # pillow has some prerequisites

    pkg install libjpeg-turbo libpng
    pip install pillow

    # pynacl has some prerequisites

    pkg install libsodium
    pip install pynacl

    # matplotlib has some prerequisites

    pkg install freetype libjpeg-turbo libpng
    pip install matplotlib

    # lxml has some prerequisites
    pkg install libxml2 libxslt
    pip install lxml

    # sphinx has some prerequisites - but they are mostly already there
    pip install sphinx

    # nikola has some prerequisites - but they are mostly already there
    pip install webp
    pip install nikola

    # ipython has some prerequisites
    pkg install libzmq libcrypt clang
    pip install pyzmq jupyter

OK, now we have a pretty powerful piece of machinery at our fingertips. We
can start an iPython notebook like this:

.. code-block:: bash

    # Start a Jupyter notebook session
    jupyter notebook

And you can paste in a `Matplotlib sample plot`_ to make sure it's working.
I think we can call it a day and now we are ready to have some serious fun
with an Android tablet!


.. _Termux: https://termux.com/
.. _Termux from the Google Play Store: https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US
.. _Nikola: https://getnikola.com/
.. _Infiland: https://www.amazon.de/-/en/INFILAND-Case-Galaxy-Lite-Navy/dp/B0863BMT4X/ref=sr_1_10?dchild=1&keywords=tablet+h%C3%BClle+tab+s6+lite+infiland&qid=1613914719&sr=8-10
.. _Termux specific install hints for Python packages: https://wiki.termux.com/wiki/Python
.. _Matplotlib sample plot: https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html
