var app = angular.module('app',[]);

app.controller('formController',function($scope,$http){

    $http.post('/query/competition').then(function success(resp){
        $scope.data1 = resp.data;
        console.log(resp);
    });




});