



function screen_hd(instance, module){



    module.PosScreen = module.PosModel;
    module.PosModel = module.PosScreen.extend({
        load_server_data: function(){
            var self = this;
            var loaded = module.PosScreen.prototype.load_server_data.call(this);

            loaded = loaded.then(function(){
                return self.fetch(
                    'product.product',
                    ['pos_screen'],
                    [['sale_ok','=',true],['available_in_pos','=',true]],
                    {}
                );

            }).then(function(products){
                $.each(products, function(){
                    $.extend(self.db.get_product_by_id(this.id) || {}, this)
                });
                return $.when()
            })
            return loaded;
        }
    });









module.PosDB  =  module.PosDB.extend({


        get_product_by_category: function(category_id) {

            var list = this._super(category_id);

            if (category_id == 0)
            {
                var product_ids  = this.product_by_category_id[category_id];
                var list2 = [];
                if (product_ids) {
                    for (var i = 0, len = Math.min(product_ids.length, product_ids.length); i < len; i++)
                    {
                        list2.push(this.product_by_id[product_ids[i]]);
                    }
             }
                
               list = _.where(list2, {pos_screen: true});


            }


        return list;

  }


    })



}

