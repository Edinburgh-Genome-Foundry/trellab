.. .. raw:: html

..     <p align="center">
..     <img alt="trellab Logo" title="trellab Logo" src="https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/trellab/master/docs/title.png" width="600">
..     <br /><br />
..     </p>

.. .. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/trellab.svg?branch=master
..    :target: https://travis-ci.org/Edinburgh-Genome-Foundry/trellab
..    :alt: Travis CI build status

.. .. image:: https://coveralls.io/repos/github/Edinburgh-Genome-Foundry/trellab/badge.svg?branch=master
..    :target: https://coveralls.io/github/Edinburgh-Genome-Foundry/trellab?branch=master

Trellab
=======

Trellab is a thin layer on top of py-trello that makes it easier to navigate
through the projects of a given organization.

Assume that you have an organization on trello with id ``myorganization`` and
you want to add a card "Task 1" to the list "DONE TASKS" of board "PROJECT 1".

First create a file ``secrets.yaml`` with the credentials obtained on the
Trello app-key page (https://trello.com/app-key):

.. code:: yaml

    api_key: b3bdcf43ad6e96993ab894be2784dad3
    api_secret: 7f35610c2707d32072c712911f8f24cd9ba3b1f730a5b8e6a5
    token: 0b61529eace7f7e46c228e59af73120b554cc904ae5d0cea6d0cd0c
    organization_id: myorganization

Then run the following Python code:

.. code:: python

    from trellab import TrellabOrganizationClient
    client = TrellabOrganizationClient.from_yaml('secrets.yaml')
    boards = client.boards_dict()
    project_1_board = boards.PROJECT_1
    project_1_lists = board.lists_dict()
    project_1_lists.DONE_TASKS.add_card(name="task 1")

Installation
-------------

You can install trellab through PIP

.. code::

    sudo pip install trellab

Alternatively, you can unzip the sources in a folder and type

.. code::

    sudo python setup.py install

License = MIT
--------------

Trellab is an open-source software originally written at the
`Edinburgh Genome Foundry <http://genomefoundry.org>`_ by
`Zulko <https://github.com/Zulko>`_ and
`released on Github <https://github.com/Edinburgh-Genome-Foundry/trellab>`_
under the MIT licence (¢ Edinburg Genome Foundry).

Everyone is welcome to contribute !

More biology software
---------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
  :target: https://edinburgh-genome-foundry.github.io/

Trellab is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_ synthetic biology software suite for DNA design, manufacturing and validation.
