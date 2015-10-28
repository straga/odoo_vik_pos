
function pos_subtotal_wd(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;



//Ihherit exit Update_sammary - it after

    module.OrderWidget.include({

        update_summary: function() {
            this._super();

            var order = this.pos.get('selectedOrder');

            var subtotal = order ? order.getSubtotal() : 0 ;
            var total_discount = order ? order.getDiscountTotal() : 0 ;
            var subtotal_total_discount = subtotal + total_discount;
            var total = order ? order.getTotalTaxIncluded() : 0;
            var taxes = order ? total - order.getTotalTaxExcluded() : 0;

            var subtotal_n = ""+this.format_currency(subtotal_total_discount)+"";
            var discount_n = "-"+this.format_currency(total_discount)+"";
            var taxes_n = ""+this.format_currency(taxes)+"";
            var total_n = ""+this.format_currency(total)+"";

            this.el.querySelector('.summary .show_disc .subtotal_n > .value_s').textContent = subtotal_n;
            this.el.querySelector('.summary .show_disc .discount_n > .value_s').textContent = discount_n;
            this.el.querySelector('.summary .show_disc .taxes_n > .value_s').textContent = taxes_n;
            this.el.querySelector('.summary .show_disc .total_n > .value_s').textContent = total_n;


        },


    });

}
