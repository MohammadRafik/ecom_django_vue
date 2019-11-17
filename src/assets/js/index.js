window.$ = window.jQuery = require('jquery');
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Vue from 'vue';
// importing axios needs to be done on each component seperatly
const axios = require('axios').default;


// components
import Dropdown from 'bp-vuejs-dropdown';

// my custom components
import Demo from "./components/Demo.vue";
import Navigation from "./components/navigation.vue"

const app = new Vue({
    el: '#app',
    // data: data,
    delimiters: ["[[","]]"],
    components: {
        Demo,
        Dropdown,
        Navigation
    }
});