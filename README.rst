Amvision API example
====================

Example data and code for use with the `AM-Vision API tutorial <https://docs.am-flow.com/amvision/api/tutorial.html>`_.

Installation
------------

To run the sample code, you will need to use python 3 (tested on 3.8), and you'll need some pip packages installed::

    pip install -r requirements.txt

Usage
-----

Upload prints using::

    python -m upload_prints [-u URL] token

The url is the target URL and token is the authentication token you have been given to access your AM-Vision machine or sandbox.

Example
-----
```
python -m upload_prints -u http://localhost/api/ 12a34bc5d6e6b9fgh78ijkl901mno234f567890
```