odoo.define('purchase_order_barcode.PurchaseBarcodeHandler', function (require) {
    "use strict";
    var field_registry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');
    var FormController = require('web.FormController');

    FormController.include({
        _barcodePurchaseAddProduct: function (barcode, activeBarcode) {
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

    var PurchaseBarcodeHandler = AbstractField.extend({
        init: function () {
            this._super.apply(this, arguments);

            this.trigger_up('activeBarcode', {
                name: this.name,
                fieldName: 'order_line',
                quantity: 'product_qty',
                setQuantityWithKeypress: true,
                commands: {
                    barcode: '_barcodePurchaseAddProduct',
                }
            });
        },
    });
    field_registry.add('purchase_barcode_handler', PurchaseBarcodeHandler);
    return PurchaseBarcodeHandler;
});