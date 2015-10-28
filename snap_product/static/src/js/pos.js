function snap_product_at(instance, module) {


    module.PosWIC = module.PosModel;
    module.PosModel = module.PosWIC.extend({
        load_server_data: function(){
            var self = this;
            var loaded = module.PosWIC.prototype.load_server_data.call(this);

            loaded = loaded.then(function(){
                return self.fetch(
                    'product.product',
                    ['wic_ok','ebt_ok'],
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







}
