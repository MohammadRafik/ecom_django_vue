window.$ = window.jQuery = require('jquery');
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Vue from 'vue';
// importing axios needs to be done on each component or mixin seperatly
const axios = require('axios').default;


// components
import Dropdown from 'bp-vuejs-dropdown';

// my custom components
import Demo from "./components/Demo.vue";
import Navigation from "./components/navigation.vue";
import Checkout_script from "./components/checkout_script.vue";


// mixins
import {base_global} from "./mixins/base_global.js"

const app = new Vue({
    el: '#app',
    data: function(){
        return {
            xd: '123',

        }
    },
    delimiters: ["[[","]]"],
    components: {
        Demo,
        Dropdown,
        Navigation,
        Checkout_script
    },
    mixins: [base_global],
    
});


