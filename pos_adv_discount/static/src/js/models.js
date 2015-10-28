function pos_orderline_model_at(instance, module) {


    // module.Orderline = Backbone.Model.extend({

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

    })

}
