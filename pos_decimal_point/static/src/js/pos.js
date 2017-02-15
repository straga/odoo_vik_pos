

function pos_descimal_md(instance, module){


    /*
     * Extend Paymentline
     */
     module.DecimalPaymentline= module.Paymentline;
     module.Paymentline = module.DecimalPaymentline.extend({


         set_amount: function(value){

             //var l_dec = value.length;
             var l_dec = value.toString();


             if(l_dec.length > 0) {

                var valr = l_dec.replace(/\./g, "")

                var val_len = valr.length;
                var value1 = valr.slice(0,-2);
                var value2 = valr.slice(val_len - 2,val_len);
                value = value1 + '.' + value2;

                $('.paymentline.selected .paymentline-input').bind('keyup change', function(e) {

                    if (e.which == 8 && val_len == 1 ) {//backspace
                        value = "";
                    }

                        $('.paymentline.selected .paymentline-input').val(value);

                });

             }
             else
             {
                 value = "";
             }

             module.DecimalPaymentline.prototype.set_amount.call(this,value);


        },


    })






}

