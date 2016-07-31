angular.module('app',['google.places'])
    .controller('BizAppFormCtrl', function($scope, $http){
        $scope.formDisplay = true;
        $scope.businessInformation = {};
        $scope.classifications = ['Agriculture, Forestry and Fishing', 'Mining', 'Manufacturing', 'Electricity, Gas, Water and Waste Services', 'Construction', 'Wholesale Trade', 'Retail Trade', 'Accommodation and Food Services', 'Transport, Postal and Warehousing', 'Information Media and Telecommunications', 'Financial and Insurance Services', 'Rental, Hiring and Real Estate Services', 'Professional, Scientific and Technical Services', 'Administrative and Support Services', 'Public Administration and Safety', 'Education and Training', 'Health Care and Social Assistance', 'Arts and Recreation Services', 'Other Services'];
        $scope.desiredAdditionalStaffRanges = ['0', '1 - 5', '6 - 20', '> 20'];
        $scope.ages = ['0', '1 - 5', '6 - 20', '> 20'];

        $scope.submit = function() {
            $scope.businessInformation.postcode = $scope.businessInformation.bizAddress.address_components[$scope.businessInformation.bizAddress.address_components.length-1].long_name;
            $scope.businessInformation.industry = $scope.businessInformation.classification;
            var data = angular.toJson($scope.businessInformation);
            // $http({
            //     url: '/query/competition',
            //     method: "POST",
            //     data: { 'data' : data }
            // })
            //     .then(function(response) {
            //             console.log('Success');
            //             $scope.formDisplay = false;
            //             $scope.resultsDisplay = true;
            //         },
            //         function(response) {
            //             alert('Networking Error, please try again later');
            //         });


            $scope.formDisplay = false;
            $scope.loading = true;
            $scope.survLoad = true;

            processResults(data);

        };

        function processResults(formData) {

            var ctx = document.getElementById("compGraph");
            // competition query and generate results graph here
            $http.get('test/query/competition').then(function success(resp) {
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


                var myPieChart = new Chart(ctx, {
                    type: 'pie',
                    data: data,
                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });

            });


            // survivability bar graph
            $http.get('/test/query/survivability').then(function success(resp){
                var scatterChart = document.getElementById("surviveChart");

                $scope.survLoad = false;

                // create data structure for graph
                var labels = [];
                var data = [];
                var dataStruct = {'labels':[],'datasets':[]};


                var backgroundColor =[ [
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(255, 0, 0, 0.2)'
                ],[
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(0, 0, 255, 0.2)'
                ]];

                var bg = backgroundColor[0];

                for (surviveData in resp.data) {
                    for (var type in resp.data[surviveData]) {
                        labels.push(type);
                        data.push(parseInt(resp.data[surviveData][type]));
                    }
                    dataStruct['labels']=labels;
                    dataStruct['datasets'].push({'label':surviveData,'data':data,'backgroundColor':bg});

                    data = [];
                    labels = [];
                    bg = backgroundColor[1];

                }


                //var dataStruct = {'labels':labels,'datasets':[{'data':data},]};

                var myBarChart = new Chart(scatterChart, {
                    type: 'bar',
                    data: dataStruct,
                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });


             });

            var radarChart = document.getElementById("availChart")
            var myRadarChart = new Chart(radarChart, {
                type: 'radar',
                data: {
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
        }

    });