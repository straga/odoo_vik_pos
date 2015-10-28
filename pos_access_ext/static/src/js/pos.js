function pos_access_ext_widgets (instance, module) {

    /**
     * This method is the one that load & render all the PoS widgets
     * for display our new widget we need to override the original one.
     */

    var QWeb = instance.web.qweb;
    var _t = instance.web._t;


    module.PosWidget = module.PosWidget.extend({
        build_widgets: function () {
            this._super();

            // -------- Load Popups ---------
            this.access_popup = new module.AccessPopupWidget(this, {});
           // this.access_popup.appendTo($('.point-of-sale'));
            this.access_popup.appendTo(this.$el);


            // -------- Add to popup to list & hide -------

            this.screen_selector.popup_set.access = this.access_popup;
            this.screen_selector.popup_set['access'].hide();

        }
    });

}

    function pos_access_ext_include (instance, module) {

        var QWeb = instance.web.qweb;
        var _t = instance.web._t;

        module.OrderWidget.include({

         set_value: function(val) {

        	var order = this.pos.get('selectedOrder');
        	if (this.editable && order.getSelectedLine()) {
                var mode = this.numpad_state.get('mode');
                if( mode === 'quantity'){
                    order.getSelectedLine().set_quantity(val);
                }else if( mode === 'discount'){

                    this.pos_widget.screen_selector.show_popup('access');

                    $("label[name=mode]").text(mode);
                    $("input[name=password]").removeClass("error");
                    $("input[name=value], textarea").val(order.getSelectedLine().get_discountManual());
                    $("input[name=password], textarea").val("");
                    $("span[name=label_value]").show();
                    $("input[name=value]").show();
                    $('.button_ok').text('Change');
                    $("input[name=password]").focus();

                    //order.getSelectedLine().set_discount(val);

                }else if( mode === 'price'){

                    this.pos_widget.screen_selector.show_popup('access');

                    $("label[name=mode]").text(mode);
                    $("input[name=password]").removeClass("error");
                    $("input[name=password], textarea").val("");
                    $("input[name=value], textarea").val("");
                    //$("input[name=value], textarea").val(order.getSelectedLine().get_unit_price());
                    $("span[name=label_value]").show();
                    $("input[name=value]").show();
                    $('.button_ok').text('Change');
                    $("input[name=password]").focus();

                    //order.getSelectedLine().set_unit_price(val);
                }
        	}
         },


        });


        module.NumpadWidget.include({

         clickDeleteLastChar: function() {

            // return this.state.deleteLastChar();

             this.pos_widget.screen_selector.show_popup('access');

             $("label[name=mode]").text('remove');
             $("input[name=password]").removeClass("error");
             $("input[name=password], textarea").val("");
             $("input[name=value], textarea").val("");
             $("span[name=label_value]").hide();
             $("input[name=value]").hide();
             $('.button_ok').text('Remove');
             $("input[name=password]").focus();


         },

    });



}