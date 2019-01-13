app.controller('customer-ctrl', ['$scope', 'olaService', function ($scope, olaService) {

    function bookRide() {
        console.log('username', $scope.username);
        if (!$scope.username) {
            return;
        }

        $scope.isBooking = true;
        $scope.bookMsg = 'Booking ride...';
        olaService.bookRide($scope.username, bookedRide);
    }

    function bookedRide(success, data) {
        if (success) {
            $scope.bookMsg = `Booked a Ride <b><a href='/rides/${data.id}'>#${data.id}</a></b>`;
        } else {
            $scope.bookMsg = 'Failed to book the ride.<br/>' + data;
        }
        $scope.isBooking = false;
    }

    function refreshStats() {
        $scope.isRefreshingList = true;
        olaService.getCustomerListStats(refreshedStats);
    }

    function refreshedStats(success, data) {
        $scope.isRefreshingList = false;
        if (success) {
            $scope.customerListStats = data;
        } else {}
    }

    function submitForm(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            e.stopPropagation();

            bookRide();
        }
    }

    $scope.username = '';
    $scope.bookMsg = 'Enter a username to book a ride';
    $scope.isBooking = false;
    $scope.isBookingSuccess = true;

    $scope.customerListStats = [];
    $scope.isRefreshingList = false;
    $scope.refreshStats = refreshStats;

    $scope.submitForm = submitForm;
    $scope.bookRide = bookRide;

    $scope.refreshStats();
}]);