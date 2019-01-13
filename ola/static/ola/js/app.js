var app = angular.module('app', ['ngSanitize'])

    .config(function ($locationProvider, $interpolateProvider) {
        $locationProvider.html5Mode({
            enabled: true
        });
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })
    .filter('toDate', function () {
        return function (items) {
            if (items && !items.endsWith('Z')) {
                items = items + ' UTC';
            }
            return items && new Date(items);
        };
    })
    .service('olaService', ['$http', function ($http) {

        function get(url, queryParams, cb) {
            if (queryParams) {
                var strParams = '';
                for (var key in queryParams) {
                    strParams = '&' + key + '=' + encodeURIComponent(queryParams[key]);
                }
                url = url + '?' + strParams;
            }
            $http.get(url)
                .then(function (response) {
                    if (response.status >= 200 && response.status <= 299) {
                        cb(true, response.data);
                    } else {
                        cb(false, response.data);
                    }
                });
        }

        function post(url, requestBody, cb) {
            $http.post(url, requestBody)
                .then(function (response) {
                    if (response.status >= 200 && response.status <= 299) {
                        cb(true, response.data);
                    } else {
                        cb(false, response.data);
                    }
                });
        }

        function put(url, requestBody, cb) {
            $http.put(url, requestBody)
                .then(function (response) {
                    if (response.status >= 200 && response.status <= 299) {
                        cb(true, response.data);
                    } else {
                        cb(false, response.data);
                    }
                });
        }

        this.bookRide = function (username, cb) {
            var requestBody = {
                'customer': username
            };
            post('/api/rides/book/', requestBody, cb);
        };

        this.acceptRide = function (rideId, driverId, cb) {
            var requestBody = {
                'driver': driverId
            };
            put(`/api/rides/${rideId}/accept/`, requestBody, cb);
        };

        this.finishRide = function (rideId, driverId, cb) {
            put(`/api/rides/${rideId}/finish/`, {}, cb);
        };

        this.getCustomerStats = function (cb) {};

        this.getCustomerListStats = function (cb) {
            get('/api/customers/ride-stats/', {}, cb)
        };

        this.getRideListStats = function (page, ts, cb) {
            var queryParams = {
                'ts': (ts || 0),
                'page': (page || 1),
                'limit': 10,
                "ordering": '-requested_at',
            };

            get('/api/rides/', queryParams, cb);
        };

        this.getDriverStats = function (driverId, cb) {};

        this.getDriverListStats = function (cb) {
            var ts = 0;
            var page = 1;
            var queryParams = {
                'ts': (ts || 0),
                'page': (page || 1),
                'limit': 10,
                "ordering": '-updated_at',
            };

            get('/api/drivers/', queryParams, cb);
        };
    }]);