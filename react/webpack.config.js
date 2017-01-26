var path = require('path')
var webpack = require('webpack')
var merge = require('webpack-merge')
var CompressionPlugin = require('compression-webpack-plugin')

var TARGET = process.env.npm_lifecycle_event;

var PATHS = {
  app: path.join(__dirname, 'app'),
  build: path.join(__dirname, 'build'),
  node_modules: path.join(__dirname, 'node_modules')
};

// Specify babel configuration
process.env.BABEL_ENV = TARGET;

// Define configuration options common to 
// development and production environments
var common = {

  entry: {
    app: PATHS.app
  },

  // Use the history api fallback so React routes
  // are obeyed
  devServer: {
    historyApiFallback: true
  },

  // Specify which assets webpack should load
  // '' allows files without an extension
  // to be loaded
  resolve: {
    extensions: ['', '.js', '.jsx']
  },

  // Specify where compiled assets will be bundled
  output: {
    path: PATHS.build,
    filename: 'bundle.js'
  },

  // Include loaders for styles and jsx
  // the include param specifies the location
  // of files to be loaded (a subdomain of PATHS)
  module: {
    loaders: [
      {
        test: /\.css$/,
        loaders: ['style', 'css'],
        include: [PATHS.app, PATHS.node_modules]
      },
      {
        test: /\.jsx?$/,
        // Leverage caching for better performance
        loaders: ['babel?cacheDirectory'],
        include: PATHS.app
      }
    ]
  }
}

// Development configuration
if(TARGET === 'start' || !TARGET) {
  module.exports = merge(common, {
    
    // Enable sourcemaps for debugging
    devtool: 'eval-source-map',

    // Configure server
    devServer: {
      contentBase: PATHS.build,

      // Enable history API fallback to facilitate
      // API-based routing. 
      historyAPIFallback: true,
      hot: true,
      inline: true,
      progress: true,

      // Display only errors amd minimize output:
      stats: 'errors-only',

      // When using Vagrant or other VM, set:
      // host: process.env.HOST || '0.0.0.0';
      //
      // 0.0.0.0 is available to all network devices
      // unlike default
      host: process.env.HOST,
      port: process.env.PORT || 8081
    },
    plugins: [

      // Use hot module replacement
      new webpack.HotModuleReplacementPlugin()
    ]
  });
}

// Bundled development configuration
if(TARGET === 'build' || !TARGET) {
  module.exports = merge(common, {
    plugins: [
      new webpack.optimize.OccurrenceOrderPlugin()
    ]
  });
}

// Production configuration
if(TARGET === 'compress' || !TARGET) {
  module.exports = merge(common, {
    plugins: [
      // Optimize React library for production
      new webpack.DefinePlugin({
        'process.env.NODE_ENV': '"production"'
      }),

      // Squash uglify warnings like 'Condition always true'
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false
        }
      }),

      new webpack.optimize.OccurrenceOrderPlugin()
    ]
  });
}