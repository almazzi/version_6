var app = angular.module("app", [
    'ui.router',
    'ngResource',
    'ngRoute',
    'ngCookies',
    'ui.bootstrap',
    'app.controllers',
    'app.services'
]);
app.config(['$routeProvider', '$stateProvider',
    function ($routeProvider, $stateProvider) {
        $stateProvider.state('click', {
            url: '/click',
            controller: 'ClickCtrl'
        })
    }
]);

app.run(['$location', '$rootScope', '$log', '$cookies', 'authService',
    function ($location, $rootScope, $log, $cookies, authService) {

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {
            if (toState.authenticate && !authService.isAuthenticated()) {
                event.preventDefault();
                window.location = '/login';
            }

            if (toState.role && !authService.hasRole(toState.role)) {
                event.preventDefault();
                window.location = '/access_denied';
            }
        });
    }]);