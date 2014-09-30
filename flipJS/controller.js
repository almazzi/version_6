angular.module('app.controllers', [

    ]).controller('NavigationCtrl', function ($scope, $window, authService, alertService) {
        $scope.isLoggedIn = function () {
            return authService.isAuthenticated();
        };
        $scope.logout = function () {
            authService.logout();
            $window.location.href = '/';
        };

        $scope.login = function () {
            $window.location.href = '/login';
        };
    }).controller('ClickCtrl', function ($scope, $state, popupService, $window, flipFactory) {
        $scope.peers;
        getPeers();

        function setBidInfo() {
            flipFactory.setBidInfo.success(function (peers) {
                $scope.peers = peers;
            }).error(function (error) {
                    $scope.status = 'Could not load partials';
                });
        }

        $scope.deletePeer = function (peer) {
            peerFactory.deletePeer(peer.id).success(function () {
                $window.location.reload();
            }).error(function (error) {
                    $scope.status = "Could not delete";
                });
        }
    };