.. title: Samsung Tab S6 Lite First Impressions
.. slug: samsung-tab-s6-lite-first-impressions
.. date: 2021-02-20 12:00:00 UTC-05:00
.. status: draft
.. tags: samsung, android, termux
.. category: Tools
.. link: 
.. description: 
.. type: text

.. image:: /images/products/samsung-tab-s6-lite-with-name.webp
    :align: right
    :width: 240px

I have been resisting getting a tablet (Android or iOS) for years now, in
part because it's yet another piece of tech that might not be as useful
as I imagined it to be. The good news is that the Samsung Tab S6 Lite
is actually good enough to do useful work on, it's not too expensive, and
it comes with an S-Pen.

In terms of first impressions, I am super happy with this tablet in
combination with an inexpensive case from `Infiland`_. It has great
battery life, loads web pages quickly, and is not so precious that
I don't mind taking it everywhere.

To be relevant in my daily life, a tablet must be able to do the following
things besides the normally expected tasks:

 #. Edit text files
 #. Run Python programs
 #. Log in to ssh sessions on remote computers
 #. Allow sketching of ideas using a stylus

With the addition of `Termux`_ an Android tablet can be a surprisingly
powerful computer, giving you access to almost anything you can expect
of a Linux machine.

To make the setup as easy as possible, I set used the free installer
for `Termux from F-Droid`_.

In subsequent articles I'll add git, Python, matplotlib, and a few other
packages. In fact, this website is generated on the Galaxy Tab S6 Lite
using `Nikola`_ , a static website generator.

Note that the point of this exercise is not to make a really great
portable programming system - that's what your laptop is for. What
we are trying to accomplish here is to see if an inexpensive Android
tablet can be used to maintain a lightweight static website and
occasionally so some programming.

With that in mind, the next section covers installing and configuring
a couple of packages that let you access the Termux shell from your
"real" computer. 

Remote Access Your Tablet with `sshd`
-------------------------------------

The first thing we'll do is install `sshd` and transfer our public ssh key
to the tablet so that we can log in over a secure connection. If you don't
have an `ssh` keypair yet go ahead and generate one on your regular computer
now. You probably already have one if you use `git`.

On the tablet do the following:

.. code-block:: bash

    $ pkg install termux-auth
    $ passwd
    New password:
    Retype new password:
    New password was successfully set.
    
    $ ip a show wlan0
    2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
        inet 192.168.0.102/24 brd 192.168.0.255 scope global wlan0
           valid_lft forever preferred_lft forever
        inet6 fe80::14a9:aabb:ccdd:eeff/64 scope link 
           valid_lft forever preferred_lft forever

    $ pkg upgrade
    $ pkg install openssh

    $ sshd


At this point you have `sshd` running on the tablet, but of course you need
to send your public key so that you can log on securely in the future. Note
the IP_ADDRESS that your tablet is using and do the following on your
computer:

.. code-block:: bash

    ssh-copy-id -p 8022 -i path/to/id_rsa.pub IP_ADDRESS

    # Test out the ssh access

    ssh -p 8022 IP_ADDRESS


For complete details refer to `Termux Wiki - Remote Access`_.

Grant Storage Permissions to Termux
-------------------------------------

By default and in compliance with Android's SELinux policies, Termux keeps
its file separate from other apps, and has limited access to your tablet's
files. This will limit your ability to access Termux files over `ssh` and
make it harder to make useful scripts that access data outside of Termux.

For a detailed description of how Termux handles storage, how to set it up,
and how to trigger the Android file picker to get any file it has access
to, refer to `Termux Wiki - Internal and External Storage`_.

Enabling acccess to the shared files is as easy as:

.. code-block:: bash

    termux-setup-storage

That's it for now - next step is getting a few useful Termux packages installed.


.. _Termux: https://termux.com/
.. _Termux from F-Droid: https://f-droid.org/en/packages/com.termux/
.. _Nikola: https://getnikola.com/
.. _Infiland: https://www.amazon.de/-/en/INFILAND-Case-Galaxy-Lite-Navy/dp/B0863BMT4X/ref=sr_1_10?dchild=1&keywords=tablet+h%C3%BClle+tab+s6+lite+infiland&qid=1613914719&sr=8-10
.. _Termux Wiki - Remote Access: https://wiki.termux.com/wiki/Remote_Access
.. _Termux Wiki - Setup Storage Permissions: https://wiki.termux.com/wiki/Termux-setup-storage
.. _Termux Wiki - Internal and External Storage: https://wiki.termux.com/wiki/Internal_and_external_storage
