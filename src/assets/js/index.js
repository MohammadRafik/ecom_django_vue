window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from 'vue';

import Demo from "./components/Demo.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo
    }
});