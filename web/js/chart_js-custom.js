$(function () {

    var lineData = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
                        {
                            label: "Example dataset",
                            fillColor: "rgba(231, 123, 85, 0.5)",
                            strokeColor: "rgba(231, 123, 85, 1)",
                            pointColor: "rgba(231, 123, 85, 1)",
                            pointStrokeColor: "#e77b55",
                            pointHighlightFill: "#e77b55",
                            pointHighlightStroke: "rgba(0, 0, 0,1)",
                            data: [65, 59, 80, 81, 56, 55, 40]
                        },
                        {
                            label: "Example dataset",
                            fillColor: "rgba(175, 53, 42, 0.5)",
                            strokeColor: "rgba(175, 53, 42, 1)",
                            pointColor: "rgba(175, 53, 42, 1)",
                            pointStrokeColor: "#e77b55",
                            pointHighlightFill: "#e77b55",
                            pointHighlightStroke: "rgba(0, 0, 0,1)",
                            data: [28, 48, 40, 19, 86, 27, 90]
                        }
        ]
    };

    var lineOptions = {
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(255,255,255,.05)",
        scaleGridLineWidth: 1,
        bezierCurve: true,
        bezierCurveTension: 0.4,
        pointDot: true,
        pointDotRadius: 4,
        pointDotStrokeWidth: 1,
        pointHitDetectionRadius: 20,
        datasetStroke: true,
        datasetStrokeWidth: 2,
        datasetFill: true,
        responsive: true,
        scaleFontColor:'#949ba2'
    };


    var ctx = document.getElementById("lineChart").getContext("2d");
    var myNewChart = new Chart(ctx).Line(lineData, lineOptions);

    var barData = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "My First dataset",
                fillColor: "rgba(231, 123, 85,0.5)",
                strokeColor: "rgba(231, 123, 85,0.8)",
                highlightFill: "rgba(231, 123, 85,0.75)",
                highlightStroke: "rgba(231, 123, 85,1)",
                data: [65, 59, 80, 81, 56, 55, 40]
            },
            {
                label: "My Second dataset",
                fillColor: "rgba(175, 53, 42,0.5)",
                strokeColor: "rgba(175, 53, 42,0.8)",
                highlightFill: "rgba(175, 53, 42,0.75)",
                highlightStroke: "rgba(175, 53, 42,1)",
                data: [28, 48, 40, 19, 86, 27, 90]
            }
        ]
    };

    var barOptions = {
        scaleBeginAtZero: true,
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(255,255,255,.05)",
        scaleGridLineWidth: 1,
        barShowStroke: true,
        barStrokeWidth: 2,
        barValueSpacing: 5,
        barDatasetSpacing: 1,
        responsive: true,
        scaleFontColor:'#949ba2'
    };


    var ctx = document.getElementById("barChart").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(barData, barOptions);

    var polarData = [
        {
            value: 300,
            color: "#e77b55",
            highlight: "#db7d59",
            label: "App"
        },
        {
            value: 140,
            color: "#af352a",
            highlight: "#db7d59",
            label: "Software"
        },
        {
            value: 200,
            color: "#360e11",
            highlight: "#db7d59",
            label: "Laptop"
        }
    ];

    var polarOptions = {
        scaleShowLabelBackdrop: true,
        scaleBackdropColor: "rgba(255,255,255,0.75)",
        scaleBeginAtZero: true,
        scaleBackdropPaddingY: 1,
        scaleBackdropPaddingX: 1,
        scaleShowLine: true,
        segmentShowStroke: true,
        segmentStrokeColor: "#fff",
        segmentStrokeWidth: 2,
        animationSteps: 100,
        animationEasing: "easeOutBounce",
        animateRotate: true,
        animateScale: false,
        responsive: true

    };

    var ctx = document.getElementById("polarChart").getContext("2d");
    var myNewChart = new Chart(ctx).PolarArea(polarData, polarOptions);

    var doughnutData = [
        {
            value: 300,
            color: "#e77b55",
            highlight: "#e77b55",
            label: "App"
        },
        {
            value: 50,
            color: "#af352a",
            highlight: "#af352a",
            label: "Software"
        },
        {
            value: 100,
            color: "#360e11",
            highlight: "#360e11",
            label: "Laptop"
        }
    ];

    var doughnutOptions = {
        segmentShowStroke: true,
        segmentStrokeColor: "#fff",
        segmentStrokeWidth: 2,
        percentageInnerCutout: 45, // This is 0 for Pie charts
        animationSteps: 100,
        animationEasing: "easeOutBounce",
        animateRotate: true,
        animateScale: false,
        responsive: true
    };


    var ctx = document.getElementById("doughnutChart").getContext("2d");
    var myNewChart = new Chart(ctx).Doughnut(doughnutData, doughnutOptions);


});


