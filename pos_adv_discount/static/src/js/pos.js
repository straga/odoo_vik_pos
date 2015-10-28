


function pos_adv_discount_model(instance,module) {
    var QWeb = instance.web.qweb;
    var _t = instance.web._t;

    var now =  instance.web.datetime_to_str(new Date());

    module.PosModel.prototype.models.push({
            model:  'pos.adv_discount',
            fields: ['name','code', 'amount','value_method', 'partner','product','pcategory', 'cfilter','pfilter','special_rule','product_1','pro_val_1','product_2','pro_val_2', 'start_date', 'end_date', 'journal_id', 'discount_type'],


            domain: function(self){ return [['active','=',true],['start_date','<=',now],'|',['end_date','>=',now],['end_date','=',false] ];},


/* HELP FOR DOMAIN SEARCH
To search for partners named ABC, from belgium or germany, whose language is not english:

[('name','=','ABC'),
 ('language.code','!=','en_US'),
 '|',('country_id.code','=','be'),
     ('country_id.code','=','de')]

This domain is interpreted as:

    (name is 'ABC')
AND (language is NOT english)
AND (country is Belgium OR Germany)

*/


            loaded: function(self,advdiscounts){ self.advdiscounts = advdiscounts; }
    });


}
