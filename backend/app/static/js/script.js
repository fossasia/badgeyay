/*jshint esversion: 6 */
$(document).on('ready', function () {
    'use strict';
    $('.glyphicon-th').click(function () {
        $('.custom-menu-content').toggleClass('hidden');
    });

    var apiUrl = 'https://api.github.com/repos/fossasia/badgeyay/git/refs/heads/development';
    $.ajax({
        url: apiUrl,
        async: true,
        success(result) {
            if (typeof result.object !== 'undefined' && typeof result.object.sha !== 'undefined') {
                var version = result.object.sha;
                var versionLink = 'https://github.com/fossasia/badgeyay/tree/' + version;
                var deployLink = $('.version').attr('href', versionLink).html(version);
            } else {
                $('.version').html('Failed to access version');
            }
        },
        error(error) {
            $('.version').html('Failed to access version');
        }
    });
});
