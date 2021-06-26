var width = window.innerWidth;
var height = (window.innerHeight/3)*2;
var svg = d3.select(".root").append('svg')
  .attr('width', width)
  .attr('height', height);
var color = d3.scaleOrdinal(d3.schemeCategory20);
var div = d3.select("body").append('div')
  .attr('class', 'tooltip')
  .style('opacity', 0);
var simulation = d3.forceSimulation()
  .force("link", d3.forceLink().id(function (d) {
      return d.id;
    })
    .distance(function (d) {
      return 2 * d.value;
    }).strength(0.2))
  .force("charge", d3.forceManyBody())
  .force("center", d3.forceCenter(width / 2, height / 2));
d3.json("./cg/data.json", function (error, graph) {
  if (error) throw error;
  var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .attr("stroke", "#999")
    .attr("stroke-opacity", 0.8)
    .attr("stroke-width", function (d) {
      return d.value / 100;
    });
  var tool_tip = d3.tip()
    .attr("class", "d3-tip")
    .offset([-8, 0])
    .html(function (d) {
      if (d.data != undefined) {
        return d.data;
      } else {
        return d.id;
      }

    });
  svg.call(tool_tip);
  var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("r", function (d) {
      return d.size;
    })
    .attr("stroke", "#fff")
    .attr("stroke-width", "1.5px")
    .attr("fill", function (d) {return "#" + d.color;})
    
    .on('mouseover', tool_tip.show)
    .on('mouseout', tool_tip.show)
    .call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));
      
  simulation
    .nodes(graph.nodes)
    .on("tick", ticked);
  simulation.force("link")
    .links(graph.links);


  function ticked() {
    link
      .attr("x1", function (d) {
        return d.source.x;
      })
      .attr("y1", function (d) {
        return d.source.y;
      })
      .attr("x2", function (d) {
        return d.target.x;
      })
      .attr("y2", function (d) {
        return d.target.y;
      });
    node
      .attr("cx", function (d) {
        return d.x;
      })
      .attr("cy", function (d) {
        return d.y;
      });
  }
});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}