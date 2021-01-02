const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    context: __dirname,
    entry: './src/assets/js/index',
    output: {
        path: path.resolve('./src/assets/bundles/'),
        filename: 'app.js'
    },

    plugins: [
        new BundleTracker({filename: './src/webpack-stats.json'}),
        new VueLoaderPlugin(),
    ],

    module: {
        rules:  [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
        ],
    },
    resolve: {
        alias: {vue: 'vue/dist/vue.min.js'}
    },

    mode: 'production',

};
