$(document).ready(function () {
    // $('[data-toggle="tooltip"]').tooltip();

    // $("#msaResult").html('<object  width="100%" height="400" data="' + msaEntryUrl + '" type="text/html">');

    // add_links();

    // Intitial
    $("table.table-pro-toggle").each(function () {
        // Add title to thead.
        $(this).find('thead').find('tr').first().attr("title", "Click to show/hide the table.");
        // Hide all tbody
        // $(this).find('tbody').hide();
    });

    // Set toggle
    $("table.table-pro-toggle").on('click', 'thead:first', function () {
        var tbody = $(this).closest('table').find('tbody');
        var logo = $(this).closest('table').find('thead').find('div.table-pro-toggle-icon');

        tbody.toggle();
        if (!tbody.is(':visible')) { // hide
            $(logo).html('<span class="glyphicon glyphicon-collapse-up"></span>');
        }
        else {
            $(logo).html('<span class="glyphicon glyphicon-collapse-down"></span>');
        }
        //$(this).closest('table').find('tfoot').toggle();
    });

    // stop propagation
    $("#paf-switch-div ul li a").click(function(e){
        e.stopPropagation();
        e.preventDefault();
        $(this).tab('show');
    });
});


