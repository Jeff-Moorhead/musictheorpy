============
Contributing
============

Musictheorpy is under active development and will grow to include new features in the future. If you are interested in
contributing to the project, all you need to do is fork the Github repository, download the source code, and begin
working. Continue to the complete guide below for more details. Even if you don't want to contribute directly,
I am always open to hearing people's ideas, so if you have a thought on how the project can improve, please
feel free to send me an email at jeff.moorhead1@gmail.com with your name, thoughts on improving the library, and
how I can best contact you to continue the discussion. I only ask that you be patient, as between work, graduate school,
and life, it may take me a few days to respond.

Setting Up Your Environment
---------------------------
The first step to contributing code to Musictheorpy is to fork the repository on Github and download a copy to your computer
so you can make your changes. See `git-scm <https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project>`_ for more information
on contributing to projects on Github.

You can run the unit tests using either Python's built in :file:`unittest` module, or by installing :file:`Nose`, and running ``nosetests`` from the project root::

   # from the project root directory
   >>> python -m unittest discover
   
   # or, using Nose...
   >>> nosetests

If you do not have Nose, you can create a virtual environment and install Nose with ``pip install nose``. See the `Python docs <https://docs.python.org/3/library/venv.html>`_ for more information about virtual environments.

All changes are required to have accompanying unit tests. Untested changes will be rejected. Further, any new classes, methods,
or functions are required to contain a docstring describing the new functionality and any parameters present in the signature.

Once you have finished your changes and have a passing test suite, please submit a pull request to have your changes merged.
More information on pull requests can be found `here <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_.
