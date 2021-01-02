Tree or List Search Date By Range
=================================
This module extends the functionality of the odoo putaway strategy.
It defines a new type of putaway strategy where users can set a specific
stock location per product.

On the product form, add spesific product Location

A putaway strategy can be used to ensure that incoming products will be
stored in the location set on the product form.

A recommended set-up is to create a separate putaway strategy for each
warehouse. This will ensure that the same product will be placed in the
appropriate location in each warehouse it is received.

Configuration
=============

To configure this module, you need to:

* Go to Inventory > Configuration > Settings
* Enable "Manage several locations per warehouse" on Location & Warehouse >
   Multi Locations
* Enable "Advanced routing of products using rules" on Location & Warehouse >
   Routes
* Go to Inventory > Configuration > Warehouse Management > Locations
* On the main inventory location of your warehouse,
   set a new putaway strategy.
* For the new putaway strategy, select 'Fixed per product location'
   as method

Usage
=====

* Install the module Tree or List Search With Range

Credits
=======

Contributors
------------

* Lucky Kurniawan <kurniawanluckyy@gmail.com>
