function pos_categories_at(instance, module){

//Method for inherit exist model in POS JSscript for example we have pos.category in PosModel

    var PosModelSuper = module.PosModel
    module.PosModel = module.PosModel.extend({
        load_server_data: function(){
            var self = this;
            var loaded = PosModelSuper.prototype.load_server_data.call(this);

            loaded = loaded.then(function(){
                return self.fetch(
                    'pos.category',
                    ['counted_cat'],
                    {}
                );

            }).then(function(categories){
                $.each(categories, function(){
                    $.extend(self.db.get_category_by_id(this.id) || {}, this)
                })
                return $.when()
            })
            return loaded;
        },

    })
}

