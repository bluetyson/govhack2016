angular.module('app',['google.places'])
    .controller('BizAppFormCtrl', function($scope, $http){
        $scope.formDisplay = true;
        $scope.resultsDisplay = false;
        $scope.businessInformation = {};
        $scope.classifications = ['Agriculture, Forestry and Fishing', 'Mining', 'Manufacturing', 'Electricity, Gas, Water and Waste Services', 'Construction', 'Wholesale Trade', 'Retail Trade', 'Accommodation and Food Services', 'Transport, Postal and Warehousing', 'Information Media and Telecommunications', 'Financial and Insurance Services', 'Rental, Hiring and Real Estate Services', 'Professional, Scientific and Technical Services', 'Administrative and Support Services', 'Public Administration and Safety', 'Education and Training', 'Health Care and Social Assistance', 'Arts and Recreation Services', 'Other Services'];
        $scope.desiredAdditionalStaffRanges = ['0', '1 - 5', '6 - 20', '> 20'];
        $scope.ages = ['0', '1 - 5', '6 - 20', '> 20'];

        $scope.submit = function() {
            $scope.businessInformation.postcode = $scope.businessInformation.bizAddress.address_components[$scope.businessInformation.bizAddress.address_components.length-1].long_name;
            $scope.businessInformation.industry = $scope.businessInformation.classification;
            var data = angular.toJson($scope.businessInformation);
            $http({
                url: '/query/competition',
                method: "POST",
                data: { 'data' : data }
            })
            .then(function(response) {
                console.log('Success');
                $scope.formDisplay = false;
                $scope.resultsDisplay = true;
            },
            function(response) {
                alert('Networking Error, please try again later');
            });
        };
    });