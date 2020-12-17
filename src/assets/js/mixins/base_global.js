const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const base_global = {
    data: function () {
      return {
        added_to_cart_successfully: false,
        cart_item_count: 0,
        failed_adding_to_cart: false,
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
            })
            .catch(function (error){
                self.failed_adding_to_cart = true;
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
                console.log('error with delete request')
                console.log(error)
            })
            .finally(function(){
                
            })
        },

      
        enter: function(el, done) {
    
            var self = this;
            setTimeout(function() {
                self.added_to_cart_successfully = false
            }, 1500); // hide the message after 1.5 seconds
        },
      

    }
  }



