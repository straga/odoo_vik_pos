
function snap_product_wd(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    var round_di = instance.web.round_decimals;
    var round_pr = instance.web.round_precision


module.PaymentScreenWidget.include({

    update_payment_summary: function() {

        this._super();


        //SNAP journal code

         var order  = this.pos.get('selectedOrder');
         var selected_paymentline = order.selected_paymentline;

         var currentOrder = this.pos.get('selectedOrder');

        if (selected_paymentline)
        {
            var journal_code = selected_paymentline.cashregister.journal.code;
            var amount = selected_paymentline.amount;
        }


        if (journal_code == 'WIC' || journal_code =='EBT') {

            var paidTotal = currentOrder.getEWPaidTotal();
            var dueTotal = currentOrder.getEWTotalTaxIncluded();

            paidTotal = round_di(parseFloat(paidTotal) || 0, this.pos.currency.decimals);
            dueTotal = round_di(parseFloat(dueTotal) || 0, this.pos.currency.decimals);




            if (dueTotal >= paidTotal) {


                if (journal_code == 'WIC' ){

                    var ebt_to  = currentOrder.getEWTotalTaxIncluded();
                    var ebt_get = currentOrder.getEBTPaidTotal();
                    var wic_to = currentOrder.getWICTotalTaxIncluded();


                    var ebt_total = ebt_to - ebt_get;
                    var wic_left;

                    if (ebt_total < (ebt_to-wic_to)) {

                        wic_left = wic_to - ebt_total;
                    }

                    else {

                        wic_left = 0;
                    }

                    dueTotal = wic_to - wic_left;
                    paidTotal = currentOrder.getWICPaidTotal();

                }


                var remaining = dueTotal > paidTotal ? dueTotal - paidTotal : 0;
                var change = paidTotal > dueTotal ? paidTotal - dueTotal : 0;

                this.$('.payment-due-total').html(this.format_currency(dueTotal));
                this.$('.payment-paid-total').html(this.format_currency(paidTotal));
                this.$('.payment-remaining').html(this.format_currency(remaining));
                this.$('.payment-change').html(this.format_currency(change));

            }

            else {

                paidTotal = 0;
                dueTotal = 0;
                remaining = 0;
                change =  0;

                this.$('.payment-due-total').html(this.format_currency(dueTotal));
                this.$('.payment-paid-total').html(this.format_currency(paidTotal));
                this.$('.payment-remaining').html(this.format_currency(remaining));
                this.$('.payment-change').html(this.format_currency(change));

                if (this.pos_widget.action_bar) {
                    this.pos_widget.action_bar.set_button_disabled('validation', true);
                    this.pos_widget.action_bar.set_button_disabled('invoice', true);
                }

            }

        }


        if (currentOrder.getEWPaidTotal() > currentOrder.getEWTotalTaxIncluded()) {

            if (this.pos_widget.action_bar) {
                    this.pos_widget.action_bar.set_button_disabled('validation', true);
                    this.pos_widget.action_bar.set_button_disabled('invoice', true);
            }

        }


    }


});


    module.WicProductOrder = module.Order;
    module.Order = module.WicProductOrder.extend({


// TotalTaxIncluded

        getWICTotalTaxIncluded: function() {

           var wic_val =  this.get('orderLines').reduce((function(sum, orderLine)
            {

                 if(orderLine.get_product().wic_ok) {
                    return sum + orderLine.get_price_with_tax();
                }
                else {
                    return sum;}

            }), 0);

            return wic_val;


        },

        getEBTTotalTaxIncluded: function() {


            var ebt_val = this.get('orderLines').reduce((function(sum, orderLine)
            {

                if(orderLine.get_product().ebt_ok  && !orderLine.get_product().wic_ok ) {
                //if(orderLine.get_product().ebt_ok) {
                    return sum + orderLine.get_price_with_tax();
                }
                else {
                    return sum;}

            }), 0);

            return ebt_val;
        },


        getEWTotalTaxIncluded: function() {


            var ew_val = this.getWICTotalTaxIncluded() + this.getEBTTotalTaxIncluded();

            return ew_val;
        },



// PaidTotal

        getWICPaidTotal : function()

        {

            return (this.get('paymentLines')).reduce((function(sum, paymentLine)
                {

                    var journal_Code = paymentLine.cashregister.journal.code;

                    if (journal_Code == 'WIC')
                    {
                        return sum + paymentLine.get_amount();
                    }
                    else
                    {
                        return sum
                    }

                }), 0);
        },


        getEBTPaidTotal : function()

        {

            return (this.get('paymentLines')).reduce((function(sum, paymentLine)
                {

                    var journal_Code = paymentLine.cashregister.journal.code;

                    if (journal_Code == 'EBT')
                    {
                        return sum + paymentLine.get_amount();
                    }
                    else
                    {
                        return sum
                    }

                }), 0);
        },


        getEWPaidTotal: function() {


           var val = this.getEBTPaidTotal() + this.getWICPaidTotal();

           return val;

        },


// DueLeft

        getWICDueLeft: function() {

           var val = this.getWICTotalTaxIncluded() - this.getWICPaidTotal();
           return val;

        },

        getEBTDueLeft: function() {

            var val = this.getEBTTotalTaxIncluded() - this.getEBTPaidTotal();
            return val;


        },


        getEWDueLeft: function() {


            var val = this.getWICDueLeft() + this.getEBTDueLeft();
            return val;

        },


        getWICLDueLeft: function() {


            var val;

            var ebt_to  = this.getEWTotalTaxIncluded();
            var ebt_get = this.getEBTPaidTotal();
            var wic_to = this.getWICTotalTaxIncluded();


                    var ebt_total = ebt_to - ebt_get;
                    var wic_left;

                    if (ebt_total < (ebt_to-wic_to)) {

                        wic_left = wic_to - ebt_total;
                    }

                    else {

                        wic_left = 0;
                    }

                    val = wic_to - wic_left;


            return val;


        },

//Add Payment Line

         addPaymentline: function(cashregister) {
            var self = this;
            var journal = cashregister.journal
            if (journal.debt && ! this.get_client()){
                setTimeout(function(){
                    var ss = self.pos.pos_widget.screen_selector;
                    ss.set_current_screen('clientlist');
                }, 30);
                return;
            }

            var paymentLines = this.get('paymentLines');

            var newPaymentline = new module.Paymentline({},{cashregister:cashregister, pos:this.pos});



            if(journal.type !== 'cash'){
                var val;
                if (journal.debt)
                    val = -this.getChange() || 0;
                else
                    if (journal.code == 'WIC'){
                       
                       val = this.getWICLDueLeft();
                    }

                    else if (journal.code == 'EBT'){

                        val = this.getEWDueLeft();
                    }

                    else{
                        val = this.getDueLeft();
                    }


                newPaymentline.set_amount( val );
            }
            paymentLines.add(newPaymentline);
            this.selectPaymentline(newPaymentline);
        }

    });


}
