var React = require('react')
var Header = require('./Header')
var Footer = require('./Footer')

// render application shell
var AppWrapper = React.createClass({

  render: function() {
    return (
      <div className="app-container">
        <Header />
        <div className="app-content">
          {this.props.children}
        </div>
        <Footer />
      </div>
    )
  }
});

module.exports = AppWrapper;