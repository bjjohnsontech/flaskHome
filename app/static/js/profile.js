(function() {
    'use strict';
    angular.module('profileApp', ['ngAnimate', 'ui.bootstrap'])
    .controller('taskAppController', ['$scope',
        function($scope) {
            $scope.oneAtATime = true;
        }           
    ]);
}());