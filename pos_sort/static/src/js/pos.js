

  // An internal function to generate lookup iterators.
  var lookupIterator = function(value) {
    if (value == null) return _.identity;
    if (_.isFunction(value)) return value;
    return _.property(value);
  };

  var mysortBy = function(obj, iterator, context) {
    iterator = lookupIterator(iterator);
    return _.pluck(_.map(obj, function(value, index, list) {
      return {
        value: value,
        index: index,
        criteria: iterator.call(context, value, index, list)
      };
    }).sort(function(left, right) {


      var a = left.criteria;
      var b = right.criteria;

        if (a===null) a='';
        if (b===null) b='';
        if (a===false) a='';
        if (b===false) b='';

      if (a !== b) {
        if (a > b || a === void 0) return -1;
        if (a < b || b === void 0) return 1;
      }
      return left.index - right.index;
    }), 'value');
  };



function pos_sort_at(instance, module){


    module.PosSort = module.PosModel;
    module.PosModel = module.PosSort.extend({


        initialize: function (session, attributes) {

            module.PosSort.prototype.initialize.apply(this, arguments);

            this.bystate = 0;

  },

        get_bystate: function(){
            return this.bystate;
        },

        set_bystate: function(bystate){
                this.bystate = bystate;
        }

    })


    module.PosDB  =  module.PosDB.extend({

        get_product_by_category: function (category_id) {
              var product_ids = this.product_by_category_id[category_id];
              var list = [];
              if (product_ids) {
                  for (var i = 0, len = Math.min(product_ids.length, this.limit); i < len; i++) {
                      list.push(this.product_by_id[product_ids[i]]);
                  }
              }

            var by_state = self.posmodel.get_bystate();

             if(by_state == 2)

             {
                 list = mysortBy(list, "default_code");

             }
            else
             {
                 list = _.sortBy(list, "display_name");

             }


        return list;

          }

      })

















}

