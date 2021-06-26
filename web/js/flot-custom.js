//Flot Bar Chart
$(function () {
    var barOptions = {
        series: {
            bars: {
                show: true,
                barWidth: 0.3,
                fill: true,
                fillColor: {
                    colors: [{
                            opacity: 0.8
                        }, {
                            opacity: 0.8
                        }]
                }
            }
        },
        yaxis: {
         tickColor : '#transparent',
				tickLength: 0,
            font: {
                color: '#949ba2'
            }
        },
        xaxis: {
        tickColor : '#transparent',
				tickLength: 0,
            font: {
                color: '#949ba2'
            }
        },
        colors: ["#e77b55"],
        grid: {
            color: "#999999",
            hoverable: true,
            clickable: true,
            tickColor: " #949ba2",
            borderWidth: 0
        },
        legend: {
            show: false

        },
        tooltip: true,
        tooltipOpts: {
            content: "x: %x, y: %y"
        }
    };
    var barData = {
        label: "bar",
        data: [
            [1, 34],
            [2, 25],
            [3, 19],
            [4, 34],
            [5, 32],
            [6, 44]
        ]
    };
    
    $.plot($("#flot-bar-chart"), [barData], barOptions);

});

$(function () {
    var barOptions = {
        series: {
            lines: {
                show: true,
                lineWidth: 2,
                fill: true,
                fillColor: {
                    colors: [{
                            opacity: 0.0
                        }, {
                            opacity: 0.0
                        }]
                }
            }
        },
        colors: ["#e77b55"],
        grid: {
            color: "#999999",
            hoverable: true,
            clickable: true,
            tickColor: "#949ba2",
            borderWidth: 0
        },
        legend: {
            show: false
        },
          yaxis: {
         tickColor : '#transparent',
				tickLength: 0,
            font: {
                color: '#949ba2'
            }
        },
        xaxis: {
        tickColor : '#transparent',
				tickLength: 0,
            font: {
                color: '#949ba2'
            }
        },
        tooltip: true,
        tooltipOpts: {
            content: "x: %x, y: %y"
        }
    };
    var barData = {
        label: "bar",
        data: [
            [1, 34],
            [2, 25],
            [3, 19],
            [4, 34],
            [5, 32],
            [6, 44]
        ]
    };
    $.plot($("#flot-line-chart"), [barData], barOptions);

});
//Flot Pie Chart
$(function () {

    var data = [{
            label: "Sales 1",
            data: 21,
            color: "#e77b55"
        }, {
            label: "Sales 2",
            data: 3,
            color: "#af352a"
        }, {
            label: "Sales 3",
            data: 15,
            color: "#360e11"
        }, {
            label: "Sales 4",
            data: 52,
            color: "#db7d59"
        }];

    var plotObj = $.plot($("#flot-pie-chart"), data, {
        series: {
            pie: {
                show: true
            }
        },
        grid: {
            hoverable: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
            shifts: {
                x: 20,
                y: 0
            },
            defaultTheme: false
        }
    });

});

$(function () {

    var container = $("#flot-line-chart-moving");

    // Determine how many data points to keep based on the placeholder's initial size;
    // this gives us a nice high-res plot while avoiding more than one point per pixel.

    var maximum = container.outerWidth() / 2 || 300;

    //

    var data = [];

    function getRandomData() {

        if (data.length) {
            data = data.slice(1);
        }

        while (data.length < maximum) {
            var previous = data.length ? data[data.length - 1] : 50;
            var y = previous + Math.random() * 10 - 5;
            data.push(y < 0 ? 0 : y > 100 ? 100 : y);
        }

        // zip the generated y values with the x values

        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]]);
        }

        return res;
    }

    series = [{
            data: getRandomData(),
            lines: {
                fill: true
            }
        }];


    var plot = $.plot(container, series, {
        grid: {
            color: "#999999",
            tickColor: "#ddd",
            borderWidth: 0,
            minBorderMargin: 20,
            labelMargin: 10,
            backgroundColor: {
                colors: ["#fff", "#fff"]
            },
            margin: {
                top: 8,
                bottom: 20,
                left: 20
            },
       
            markings: function (axes) {
                var markings = [];
                var xaxis = axes.xaxis;
                for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
                    markings.push({
                        xaxis: {
                            from: x,
                            to: x + xaxis.tickSize
                        },
                        color: "#fff"
                    });
                }
                return markings;
            }
        },
        colors: ["#e77b55"],
        xaxis: {
             font: {
                color: '#949ba2'
            },
            tickFormatter: function () {
                return "";
                
            }
        },
        yaxis: {
             font: {
                color: '#949ba2'
            },
            min: 0,
            max: 110
        },
        legend: {
            show: true
        }
    });

    // Update the random dataset at 25FPS for a smoothly-animating chart

    setInterval(function updateRandom() {
        series[0].data = getRandomData();
        plot.setData(series);
        plot.draw();
    }, 40);

});




