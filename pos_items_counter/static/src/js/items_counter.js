
function sum(numbers) {
           return _.reduce(numbers, function(result, current) {
        return result + parseFloat(current);
        }, 0);
}

function openerp_posline_showline(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

//Ihherit exit Update_sammary - it after

    module.OrderWidget.include({

        update_summary: function() {
            this._super();

            var order  = this.pos.get('selectedOrder');
            var orderlines = order.get('orderLines').models;


            var stringcat = new Array();

            for(var i = 0, len = orderlines.length; i < len; i++){

                var orderline = orderlines[i];
                var poscateg =  orderline.get_product().pos_categ_id;
                var orderline_quant = orderline.get_quantity();

                if(poscateg !== false) {

                    var poscateg_id = poscateg[0];
                    var poscateg_full = this.pos.db.get_category_by_id(poscateg_id);

                    var poscateg_counted_cat = poscateg_full.counted_cat;
                    var poscateg_name = poscateg_full.name;

                    if (poscateg_counted_cat == true) {

                        stringcat[i] =  {catid: poscateg_id, catname: poscateg_name, quant: orderline_quant};
                    };

                };

            }


           var TotaGrouplItems = _.chain(stringcat)
               .groupBy("catname")
               .map(function(value, key)
               {
                   return {


                       Item: key,
                       Total: sum(_.pluck(value, "quant"))
                   }
               })
           .value();

           var totalcatstr = "";

           for(var i = 0, len = TotaGrouplItems.length; i < len; i++) {

               totalcatstr += "(Item: "+TotaGrouplItems[i].Item+" = "+TotaGrouplItems[i].Total+"), ";
           }

           this.el.querySelector('.order .polines .category .total').textContent = totalcatstr

        },


    });


}
