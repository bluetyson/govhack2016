var app = angular.module('app',[]);

app.controller('frontPageController', ['$scope', function($scope){

    $scope.title = 'BizHack';
    $scope.submit = 'Grow your business today!';
    $scope.submitDescription = 'Enter details for your current business, or perhaps your desired future ' +
        'business and start today!';
    $scope.submitButton = 'Start now';

}]);