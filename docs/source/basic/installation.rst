.. _installation:

============
Installation
============

Grammers-Python is a Python library, which means you need to download and install
Python from https://www.python.org/downloads/ if you haven't already. Once
you have Python installed, `upgrade pip <https://pythonspeed.com/articles/upgrade-pip/>`_ and run:

.. code-block:: sh

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade grammers

…to install or upgrade the library to the latest version.

Installing Development Versions
===============================

If you want the *latest* unreleased changes,
you can run the following command instead:

.. code-block:: sh

    python3 -m pip install --upgrade https://github.com/HBcao233/grammers-python/

.. note::

    The development version may have bugs and is not recommended for production
    use. However, when you are `reporting a library bug <https://github.com/HBcao233/grammers-python/issues/>`_, you should try if the
    bug still occurs in this version.


Verification
============

To verify that the library is installed correctly, run the following command:

.. code-block:: sh

    python3 -c "import grammers; print(grammers.__version__)"

The version number of the library should show in the output.
