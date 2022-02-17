Amvision API example
====================

Example data and code for use with the `AM-Vision API tutorial <https://docs.am-flow.com/amvision/api/tutorial.html>`_.

Installation
------------

To run the sample code, you will need to use python 3 (tested on 3.8), and you'll need some pip packages installed::

    pip install -r requirements.txt

Usage
-----

Please see the API tutorial for more explanation of what each script does.

You can run the `One-time configuration` example code using::

    python configuration.py [API_URL] [API_TOKEN]

You can run the `Sorting to next step` example code using::

    python sorting_to_next_step.py [API_URL] [API_TOKEN]

You can run the `Sorting to order` example code using::

    python sorting_to_order.py [API_URL] [API_TOKEN]


:API_URL: is the full url to the api of your AM-Vision machine or sandbox, e.g. https://192.1.2.3/api/
:API_TOKEN: is the authorization token for your machine that you should have received from AM-Flow
