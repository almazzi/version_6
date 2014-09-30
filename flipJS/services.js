angular.module('app.services', [])
    .factory('flipFactory', ['$http'], function ($http) {
        var peersURLBase = '/peers';
        var flipFactory = {};

        flipFactory.getPeers = function () {
            return $http.get(peersURLBase);
        };

        flipFactory.addPeer = function (peer) {
            return $http.post(peersURLBase, peer);
        };

        flipFactory.getPeer = function (id) {
            return $http.get(peersURLBase + '/' + id);
        };

        flipFactory.deletePeer = function (id) {
            return $http.delete(peersURLBase + '/' + id);
        };

        flipFactory.updatePeer = function (peerId, peerToken, peerName, peerIsBlocked, peerIp) {
            return $http({
                method: 'PUT',
                url: updatePeerURL + '/' + peerId,
                data: $.param({id: peerId, token: peerToken, name: peerName, blocked: peerIsBlocked, ipAddress: peerIp}),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            })
        };


        )
        

