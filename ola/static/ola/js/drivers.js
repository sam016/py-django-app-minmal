app.controller('drivers-ctrl', ['$scope', 'olaService', function ($scope, olaService) {

    function createDriver() {
        console.log('username', $scope.username);
        if (!$scope.username) {
            return;
        }

        $scope.isCreating = true;
        $scope.msg = 'Creating driver...';
        olaService.createDriver($scope.username, createdDriver);
    }

    function createdDriver(success, data) {
        if (success) {
            window.location = "/drivers/" + data.id;
        } else {
            $scope.msg = 'Failed to create the driver.<br/>' + data;
        }
        $scope.isCreating = false;
    }

    function refreshDrivers() {
        $scope.isRefreshingList = true;
        olaService.getDriverListStats(refreshedStats);
    }

    function refreshedStats(success, data) {
        $scope.isRefreshingList = false;
        if (success) {
            $scope.drivers = data;
        } else {}
    }

    function submitForm(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            e.stopPropagation();

            createDriver();
        }
    }

    $scope.username = '';
    $scope.isCreating = false;

    $scope.drivers = [];
    $scope.isRefreshingList = false;
    $scope.refreshDrivers = refreshDrivers;

    $scope.submitForm = submitForm;
    $scope.createDriver = createDriver;

    $scope.refreshDrivers();
}]);