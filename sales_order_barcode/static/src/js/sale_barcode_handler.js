odoo.define('sale_order_barcode.SaleBarcodeHandler', function (require) {
    "use strict";
    var field_registry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');
    var FormController = require('web.FormController');

    FormController.include({
        _barcodeSaleAddProduct: function (barcode, activeBarcode) {
            var self = this;
            if (!activeBarcode.handle) {
                return $.Deferred().reject();
            }
            var record = this.model.get(activeBarcode.handle);
            if (record.data.state !== 'draft') {
                self.displayNotification({ title: 'Can`t add Product, state must be Draft', type: 'danger' });
                return $.Deferred().reject();
            }
            return this._barcodeAddX2MQuantity(barcode, activeBarcode);
        }
    })

    var SaleBarcodeHandler = AbstractField.extend({
        init: function () {
            this._super.apply(this, arguments);

            this.trigger_up('activeBarcode', {
                name: this.name,
                fieldName: 'order_line',
                quantity: 'product_uom_qty',
                setQuantityWithKeypress: true,
                commands: {
                    barcode: '_barcodeSaleAddProduct',
                }
            });
        },
    });
    field_registry.add('sale_barcode_handler', SaleBarcodeHandler);
    return SaleBarcodeHandler;
});