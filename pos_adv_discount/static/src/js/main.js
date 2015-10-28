openerp.pos_adv_discount = function(instance){

    var module = instance.point_of_sale;


    pos_orderline_model_at(instance, module);

    pos_adv_discount_model(instance, module);

    pos_adv_discount(instance, module);




};
