.. _con-TS:

Constrained-TS Method
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

`Constrained-TS (Con-TS) <https://pubs.acs.org/doi/10.1021/ja801648h>`_ is a much faster method to locate the transition state (TS), which searches for TSs from a guessed TS-like structure by fixing only one degree of freedom, e.g., the distance of the dissociating chemical bond.

:program:`GVasp` support to generate the inputs of Con-TS, just run the command below:

.. code-block:: bash

    gvasp submit con-TS

specify potential
-------------------

If you want to specify potential, just run the command:

.. code-block:: bash

    gvasp submit con-TS -p/--potential POTENTIAL

.. note::
    More information of potential setting can be seen in :ref:`optimization <potential>` task.