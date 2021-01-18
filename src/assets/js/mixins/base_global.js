const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const base_global = {
    data: function () {
      return {
        added_to_cart_successfully: false,
        cart_item_count: '-',
        failed_adding_to_cart: false,
        time_out_already_running: false,
      }
    },
    created: function() {
        // check if there is a saved category in the session
        self = this
        self.update_cart_item_count()

    },
    methods: {
        update_cart_item_count: function(){
            self = this
            axios.get('/cart/get_cart_items_count')
            .then(function (response){
                self.cart_item_count = response.data;
            })
        },

        add_product_to_cart: function(){
            let self= this;
            
            let form_ele = document.getElementById('cart_products_update_form');
            let cart_url = form_ele.cart.value
            let product_url = form_ele.product.value
            let quantity = form_ele.quantity.value
            let updated_by = form_ele.updated_by.value
            let created_by = form_ele.created_by.value
            axios.post('/cart/update_', {
                cart: cart_url,
                product: product_url,
                quantity: quantity,
                updated_by: updated_by,
                created_by: created_by
            })
            .then(function(response){
                self.added_to_cart_successfully = true;
                self.update_cart_item_count();
                self.pop_message_timeout();
            })
            .catch(function (error){
                self.failed_adding_to_cart = true;
                self.pop_message_timeout();
            })
            .finally(function(){
                
            })
        },
        
        delete_item_from_cart: function(cart_item_id){
            axios.delete('/api/cartitem/' + cart_item_id)
            .then(function(response){
                console.log('item deleted from cart');
                console.log(response);
                window.location.reload(true);
            })
            .catch(function (error){
            })
            .finally(function(){
            })
        },

    //   this isnt being used?????
        pop_message_timeout: function() {
            var self = this;
            if (self.time_out_already_running == true){
                // reset timeout duration and exit
                window.clearTimeout(self.cart_timeout)
                self.cart_timeout = window.setTimeout(function() {
                    self.added_to_cart_successfully = false;
                    self.failed_adding_to_cart = false;
                    self.time_out_already_running = false;
                    }, 1500)
                return
            }
            else{
                self.time_out_already_running = true;
                self.cart_timeout = window.setTimeout(function() {
                self.added_to_cart_successfully = false;
                self.failed_adding_to_cart = false;
                self.time_out_already_running = false;
                }, 1500)
            }
        },
      

    }
  }



