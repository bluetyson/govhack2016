angular.module('app',['google.places'])
    .controller('BizAppFormCtrl', function($scope, $http){
        $scope.formDisplay = true;
        $scope.businessInformation = {};
        $scope.classifications = ['Agriculture, Forestry and Fishing', 'Mining', 'Manufacturing', 'Electricity, Gas, Water and Waste Services', 'Construction', 'Wholesale Trade', 'Retail Trade', 'Accommodation and Food Services', 'Transport, Postal and Warehousing', 'Information Media and Telecommunications', 'Financial and Insurance Services', 'Rental, Hiring and Real Estate Services', 'Professional, Scientific and Technical Services', 'Administrative and Support Services', 'Public Administration and Safety', 'Education and Training', 'Health Care and Social Assistance', 'Arts and Recreation Services', 'Other Services'];
        $scope.desiredAdditionalStaffRanges = ['0', '1 - 5', '6 - 20', '> 20'];
        $scope.ages = ['0', '1 - 5', '6 - 20', '> 20'];

        $scope.submit = function() {

            var obj =  $scope.businessInformation.bizAddress.address_components;
            var postCode = '2601';
            for (var idx in obj){
                if (obj[idx].hasOwnProperty('types') && obj[idx].types[0] == 'postal_code'){
                    postCode = obj[idx].short_name;
                }
            }


            $scope.businessInformation.postcode = $scope.businessInformation.bizAddress
                .address_components[$scope.businessInformation.bizAddress.address_components.length-1].long_name;
            $scope.businessInformation.state = $scope.businessInformation.bizAddress
                .address_components[$scope.businessInformation.bizAddress.address_components.length-3].short_name;

            console.log();

            $scope.data = {}
            $scope.data['industry'] = $scope.businessInformation.industry;
            $scope.data['postcode'] = postCode;
            $scope.data['state'] = $scope.businessInformation.state;
            $scope.data['employees'] = $scope.businessInformation.employees;
            $scope.data['revenue'] = $scope.businessInformation.revenue;




            $scope.businessInformation.industry = $scope.businessInformation.industry;
            var data = angular.toJson($scope.businessInformation);



            $scope.formDisplay = false;
            $scope.loading = true;
            $scope.survLoad = true;
            $scope.avgLoad = true;
            $scope.availLoad = true;


            $scope.noData = false;

            processResults($scope.data);

        };

        function processResults(formData) {

            var ctx = document.getElementById("compGraph");
            // competition query and generate results graph here
            $http({
                method:'POST',
                url:'query/competition',
                data:formData

            }).then(function success(resp) {

                $scope.loading = false;

                if (resp.data == null || resp.data == undefined || resp.data == 'null'){
                    $scope.noData= true;
                    return;
                }


                // competition data
                var data = {
                    labels: [
                        "2014",
                        "2013",
                        "2012"
                    ],
                    datasets: [
                        {
                            data: [resp.data['2014'][0]/1000, resp.data['2013'][0]/1000, resp.data['2012'][0]/1000],
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
            $http({
                method:'POST',
                url:'query/survivability',
                data: formData

            }).then(function success(resp){
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



            $http({
                url:'query/avgperson',
                method:'POST',
                data:formData
            }).then(function success(resp){
                $scope.avgLoad = false;
                $scope.age = resp.data["Median Age"];
                $scope.income = resp.data["Median Income"];
                $scope.kids = resp.data["dependent_children"];
                $scope.educ = resp.data["education"];
                $scope.marry = resp.data["marital_status"];
                $scope.rent = resp.data["rent"].join('-');
                $scope.cars  = resp.data["cars"];
                $scope.net = resp.data["internet"];

            });




            $http({
                url:'query/labouravail',
                method:'POST',
                data:formData
            }).then(function success(resp){

                $scope.availLoad = false;

                var radarChart = document.getElementById("availChart");
                //TTEEGDGDGDG
                // create data structure for graph
                var labels = [];
                var data = [];
                var dataStruct = {'labels':[],'datasets':[]};


                var backgroundColor =[
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(0, 0, 255, 0.2)'
                ];

                for (type in resp.data) {

                    labels.push(type);
                    data.push(parseInt(resp.data[type]));



                }
                dataStruct.labels = labels;
                dataStruct['datasets'].push({'label':"Job Availability",'data':data,'backgroundColor':backgroundColor});


                var myBarChart = new Chart(radarChart, {
                    type: 'bar',
                    data: dataStruct,
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            yAxes: [{
                                display: true,
                                ticks: {
                                    suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                                    // OR //
                                    beginAtZero: true   // minimum value will be 0.
                                }
                            }]
                        }
                    }
                });


            });

        }

    });