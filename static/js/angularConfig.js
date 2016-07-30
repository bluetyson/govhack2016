angular.module('BizHackFormApp',['google.places'])
    .controller('BizAppFormCtrl', ['$scope', function($scope){
        $scope.classifications = ['Agriculture, Forestry and Fishing', 'Mining', 'Manufacturing', 'Electricity, Gas, Water and Waste Services', 'Construction', 'Wholesale Trade', 'Retail Trade', 'Accommodation and Food Services', 'Transport, Postal and Warehousing', 'Information Media and Telecommunications', 'Financial and Insurance Services', 'Rental, Hiring and Real Estate Services', 'Professional, Scientific and Technical Services', 'Administrative and Support Services', 'Public Administration and Safety', 'Education and Training', 'Health Care and Social Assistance', 'Arts and Recreation Services', 'Other Services'];
        $scope.desiredAdditionalStaffRanges = ['0', '1 - 5', '6 - 20', '> 20'];
        $scope.ages = ['0', '1 - 5', '6 - 20', '> 20'];

        $scope.submit = function() {
            $scope.businessInformation = {};
            $scope.businessInformation.bizName = $scope.bizName;
            $scope.businessInformation.bizClassification = $scope.bizClassification;
            $scope.businessInformation.bizAddress = $scope.bizAddress;
            $scope.businessInformation.postcode = $scope.bizAddress.address_components[$scope.bizAddress.address_components.length-1].long_name;
            $scope.businessInformation.bizABN = $scope.bizABN;
            $scope.businessInformation.bizNumberOfEmployees = $scope.bizNumberOfEmployees;
            $scope.businessInformation.bizAnnualRevenue = $scope.bizAnnualRevenue;
            $scope.businessInformation.bizDesiredAdditionalStaffRange = $scope.bizDesiredAdditionalStaffRange;
            $scope.businessInformation.bizAge = $scope.bizAge;
        };
    }]);
