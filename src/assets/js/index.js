window.$ = window.jQuery = require('jquery');
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Vue from 'vue';
// importing axios needs to be done on each component or mixin seperatly
const axios = require('axios').default;


// components from github
import Dropdown from 'bp-vuejs-dropdown';
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

import { Carousel, Slide } from "vue-carousel";
import "./css/vue-carousel.css"

// my custom components
import Demo from "./components/Demo.vue";
import Navigation from "./components/navigation.vue";
import Checkout_script from "./components/checkout_script.vue";
import onload from "./components/onload.vue";


// mixins
import {base_global} from "./mixins/base_global.js"
import {vue_slides} from "./mixins/vue_slides.js"

const app = new Vue({
    el: '#app',
    data: function(){
        return {
            xd: '123',

        }
    },
    delimiters: ["[[","]]"], //changing the default because thats what django's template language uses as well
    components: {
        Demo,
        Dropdown,
        Navigation,
        Checkout_script,
        VueperSlides,
        VueperSlide,
        onload,
        Carousel,
        Slide,

    },
    mixins: [base_global, vue_slides],
    
});