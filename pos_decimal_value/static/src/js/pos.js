
    function pos_decimal_value_include (instance, module) {

        var QWeb = instance.web.qweb;
        var _t = instance.web._t;

        module.OrderWidget.include({

        set_value: function(val) {
        	var order = this.pos.get('selectedOrder');

            var value = val;
                    var l_dec = value.length;

                    if (l_dec > 0) {
                        var valr = value.replace(/\./g, "")
                        var val_len = valr.length;
                        var value1 = valr.slice(0, -2);
                        var value2 = valr.slice(val_len - 2, val_len);
                        value = value1 + '.' + value2;

                    }


        	if (this.editable && order.getSelectedLine()) {
                var mode = this.numpad_state.get('mode');
                if( mode === 'quantity'){
                    order.getSelectedLine().set_quantity(val);
                }else if( mode === 'discount'){
                    order.getSelectedLine().set_discountManual(value);
                }else if( mode === 'price'){
                    order.getSelectedLine().set_unit_price(value);
                }
        	}
    },

        });





}