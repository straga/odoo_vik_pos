function pos_orderline_model_at(instance, module) {


    module.OrderLineAt = module.Orderline;
    module.Orderline = module.OrderLineAt.extend({


        initialize: function (attr,options) {

            module.OrderLineAt.prototype.initialize.apply(this, arguments);

            this.discountManual = 0;

        },

        get_discountManual: function () {
            return this.discountManual;
        },

        set_discountManual: function (discountManual) {
            this.discountManual = discountManual;
            this.trigger('change',this);
        }

    });

    module.OrderWidgetAt = module.OrderWidget;
    module.OrderWidget = module.OrderWidgetAt.extend({

        set_value: function(val) {
        	var order = this.pos.get('selectedOrder');
        	if (this.editable && order.getSelectedLine()) {
                var mode = this.numpad_state.get('mode');
                if( mode === 'quantity'){
                    order.getSelectedLine().set_quantity(val);
                }else if( mode === 'discount'){
                    order.getSelectedLine().set_discountManual(val);
                }else if( mode === 'price'){
                    order.getSelectedLine().set_unit_price(val);
                }
        	}
        }

    });


}
