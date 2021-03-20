import React from 'react';
import ReactDOM from 'react-dom';
import * as d3 from "d3";

class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
    this.drawChart();

  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }

  drawChart() {
    
    const data = [12, 5, 6, 6, 9, 10];
      
    const svg = d3.select("body").append("svg").attr("width", 700).attr("height", 300);
    
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);

