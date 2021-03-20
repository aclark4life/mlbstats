import React, { useEffect } from "react";
import * as d3 from "d3";

export default function App() {
  useEffect(() => {
    d3.select(".target").style("stroke-width", 5);
  }, []);
  return (
    <div className="App">
      <svg>
        <circle
          class="target"
          style={{ fill: "green" }}
          stroke="black"
          cx={50}
          cy={50}
          r={40}
        ></circle>
      </svg>
    </div>
  );
}
