Bankline Direct Parser
======================

Python module for parsing Natwest/RBS Bankline Direct Data Services files.


Requirements
------------

Only python 3.4+ supported.


Installation
------------

.. code-block:: bash

    pip install git+https://github.com/ministryofjustice/bankline-direct-parser.git


Usage
-----

.. code-block:: python

    from bankline_parser.data_services import parse

    # from file
    with open(filename) as f:
        parsed = parse(f)
        if parsed.is_valid():
            print(parsed.account.records[0].transaction_code)
        else:
            print(parsed.errors)

    # from list of rows
    parsed = parse(lines)


Model Layout
------------

.. code-block::

    DataServicesFile
        VolumeHeaderLabel
        [Account]
            FileHeaderLabel
            UserHeaderLabel
            [DataRecord|BalanceRecord]
            UserTrailerLabel
