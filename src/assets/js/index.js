window.$ = window.jQuery = require('jquery');
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import Vue from 'vue';

// components from github
import Dropdown from 'bp-vuejs-dropdown';

// my custom components
import Demo from "./components/Demo.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo,
        Dropdown
    }
});