/**
 * Created by James on 31/07/2016.
 */
var app = angular.module('app',[]);

app.controller('resultController',function($scope,$http){
    $scope.loading = true;
    var ctx = document.getElementById("compGraph");
    // competition query and generate results graph here
    $http.get('test/query/competition').then(function success(resp){
        $scope.loading = false;
        // competition data
        var data = {
            labels: [
                "2014",
                "2013",
                "2012"
            ],
            datasets: [
                {
                    data: [resp.data['2014'][0], resp.data['2013'][0], resp.data['2012'][0]],
                    backgroundColor: [
                        "#FF6384",
                        "#36A2EB",
                        "#FFCE56"
                    ],
                    hoverBackgroundColor: [
                        "#FF6384",
                        "#36A2EB",
                        "#FFCE56"
                    ]
                }]
        };


        var myPieChart = new Chart(ctx,{
            type: 'pie',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

    });



    var scatterChart = document.getElementById("scatterChart");
    var myScatterChart = new Chart(scatterChart, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: [{
                    x: -10,
                    y: 0
                }, {
                    x: 0,
                    y: 10
                }, {
                    x: 10,
                    y: 5
                }]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    });

    var radarChart = document.getElementById("radarChart")
    var myRadarChart = new Chart(radarChart, {
        type: 'radar',
        data:  {
            labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
            datasets: [
                {
                    label: "My First dataset",
                    backgroundColor: "rgba(179,181,198,0.2)",
                    borderColor: "rgba(179,181,198,1)",
                    pointBackgroundColor: "rgba(179,181,198,1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    data: [65, 59, 90, 81, 56, 55, 40]
                },
                {
                    label: "My Second dataset",
                    backgroundColor: "rgba(255,99,132,0.2)",
                    borderColor: "rgba(255,99,132,1)",
                    pointBackgroundColor: "rgba(255,99,132,1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(255,99,132,1)",
                    data: [28, 48, 40, 19, 96, 27, 100]
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

});