(function () {
    var app = angular.module('msaApp', []);
    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{+');
        $interpolateProvider.endSymbol('+}');
    });
    app.controller('msaController', function ($scope) {
        $.ajax({
            url: dataUrl,
            dataType: 'json',
            success: function(js){
                data = eval('(' + js.result + ')');
                $scope.msa = data;
                $scope.$apply();
                if (data.ov.numOfSeq == 0) {
                    console.log('no sequence');
                    $('#loadingMsg').html('Sorry, the server is not able to return the alignment.');
                }
                else {
                    stat = data.stat;
                    init();
                    $('#msa').show();
                    $('#loadingMsg').hide();
                }
            },
            error: function() {
                $('#loadingMsg').html('Sorry, the server is not able to return the alignment.');
            }
        });
    });
    app.controller('msaProSwitchController', function($scope){
        $scope.toggle = true;
        $scope.$watch('toggle', function(){
            $scope.toggleText = $scope.toggle ? 'Show' : 'Hide';
            msa_pro_switch($scope.toggle);
        })
    });
    app.filter('unsafe', function($sce) {
        return function(val) {
            return $sce.trustAsHtml(val);
        };
    });
})();

