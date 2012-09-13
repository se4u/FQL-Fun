FQL-Fun app, query your fb network in a natural language
====================================

This is app is meant to provide a platform through which one can test
the understanding of nlp and apply them to my network of friends. for
example i could query show me all my friends and the backend would
parse the request into fql and show me a table of all my friends.

it is currently running at `FQL-Fun` and an alias location is on my
site ``fbfqlfun.pushpendre.in``

Run locally
-----------

Set up a Virtualenv and install dependencies::

    virtualenv --no-site-packages env/
    source env/bin/activate
    pip install -r requirements.txt

`Create an app on Facebook`_ and set the Website URL to
``http://localhost:5001/``.

Copy the App ID and Secret from the Facebook app settings page into
your ``.env``::

    echo FACEBOOK_APP_ID=12345 >> .env
    echo FACEBOOK_SECRET=abcde >> .env

and launch the app by entering on your command line the contents of
Procfile and hitting enter.

.. _FQL-Fun: apps.facebook.com/fql-fun
.. _Create an app on Facebook: https://developers.facebook.com/apps
