
var app = angular.module("flip", ['timer']);
app.controller("flipCtrl", function($scope, $http){
    $http.get('http://localhost:8000/click/products/?format=json')
        .success(function(data){
            $scope.products = data;
         }).error(function(){alert("Something went wrong")});
    $scope.bidTask=function(){
            var data = { Name: $scope.products.owner}
            $http.post('http://localhost:8000/click/bid',data).success(data, status, headers)
        }
    });



$interpolateProvider.startSymbol('{[').endSymbol(']}');