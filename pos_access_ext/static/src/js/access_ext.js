    
function pos_access_ext_screens (instance, module){

    // Extend PopupWidget to show our own message
    module.AccessPopupWidget = module.PopUpWidget.extend({
        template:'AccessPopupWidget',

        order_ex: function(pass, value, type) {
            var self = this;
            var secret = this.pos.config.secret_access;

            if (pass == secret && pass.length > 0 && secret.length > 0 )
                {
                    var order = this.pos.get('selectedOrder');

                    if ( type == 'discount')
                        {
                            order.getSelectedLine().set_discountManual(value);
                        }
                    else if( type == 'price')
                        {
                            order.getSelectedLine().set_unit_price(value);
                        }

                    return true;
                }
            return false;
        },


        show: function(){
            this._super();
            var self = this;

            this.$el.find('.button_ok').off('click').click(function()
                {
                    var password_ae = $("input[name=password]").val();
                    var value_ae = $("input[name=value]").val();
                    var type_ae =  $("label[name=mode]").text();
                    var result = self.order_ex(password_ae,value_ae, type_ae);

                    if (result && type_ae== 'remove' ) //Numpad backspace
                        {
                            self.pos_widget.screen_selector.close_popup();
                            return self.pos_widget.numpad.state.deleteLastChar();
                        }
                    else
                        {
                            $("input[name=password]").addClass("error");
                        }

                    if (result && (type_ae == 'price' || type_ae == 'discount')) //Numpad mode
                        {
                            self.pos_widget.screen_selector.close_popup();
                        }
                    else
                        {
                            $("input[name=password]").addClass("error");
                        }
                });

            this.$el.find('.button_close').off('click').click(function()
                {
                    self.pos_widget.screen_selector.close_popup();
                });


           $("input[name=value]").bind('keyup change', function(e)
            {

               var type_ae = $("label[name=mode]").text();

               if (type_ae == 'price')
                {
                    var value = $("input[name=value]").val();
                    var l_dec = value.length;

                    if (l_dec > 0)
                     {
                        var valr = value.replace(/\./g, "")
                        var val_len = valr.length;
                        var value1 = valr.slice(0, -2);
                        var value2 = valr.slice(val_len - 2, val_len);
                        value = value1 + '.' + value2;

                        if (e.which == 8 && val_len == 1) {//backspace
                            value = "";
                        }

                        $("input[name=value]").val(value);

                    }
                }

            });

        }
    });


  }