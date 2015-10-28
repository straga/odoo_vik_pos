function pos_sort_bt(instance, module){



    var QWeb = instance.web.qweb;

    module.PosWidget.include({
        build_widgets: function(){
            var self = this;
            this._super();
            

            var sort_code = $(QWeb.render('SortCodeButton'));


            sort_code.click(function(){

                var bystate =  self.pos.get_bystate();

                if(bystate == 2)
                    {
                        self.pos.set_bystate(0);
                        $('.js_sortcode').removeClass('confirm');
                    }

                if(bystate == 0)
                    {
                        self.pos.set_bystate(2);
                        $('.js_sortcode').addClass('confirm');
                    }

            });

            sort_code.appendTo(this.$('.pos-rightheader'));

        }
    });

};