var app = angular.module('app',[]);

app.controller('frontPageController', function($scope){

    $scope.title = 'BizHack';
    $scope.submit = 'Grow your business today!';
    $scope.submitDescription = 'BizHack uses real world data to predict market trends and business demographics to ' +
        'provide .... nevermind';
    $scope.submitButton = 'Start now';

});