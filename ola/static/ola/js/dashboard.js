app.controller('dashboard-ctrl', ['$scope', 'olaService', function ($scope, olaService) {
    var STATUSES = {
        0: 'Pending',
        1: 'Ongoing',
        2: 'Finished',
    }

    function refreshRides() {
        $scope.isRefreshingList = true;
        olaService.getRideListStats(1, 0, refreshedRides);
    }

    function refreshedRides(success, data) {
        if (success) {
            for (var row of data) {
                row['status'] = STATUSES[row['status']];
            }
            $scope.rideStats = data;
        } else {}

        $scope.isRefreshingList = false;
    }

    $scope.rideStats = [];
    $scope.isRefreshingList = false;
    $scope.refreshRides = refreshRides;

    $scope.refreshRides();
}]);