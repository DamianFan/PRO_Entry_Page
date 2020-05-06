$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();

    $("#msaResult").html('<object  width="100%" height="400" data="' + msaEntryUrl + '" type="text/html">');

    add_links();

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

function add_links() {
    // add links for def text part. The function will break down the text into pieces (and remember the separator), then exam each piece and decide if there is a link for it.
    $('.add-link').each(function (idx, ele) {
        var debris = $(ele).text().split(/([\s,;.|])/g);
        $.each(debris, function (i, e) {
            if (e.indexOf(':') > -1) {
                d = e.split(':');
                if (d[0] in link['fullid']){
                    var id = (d[0] == 'MOD' || d[0] == 'PSI-MOD') ? e.replace(':', '_') : e;
                    debris[i] = href_(link['fullid'][d[0]] + id, '', e);
                }
                else if (d[0] in link['noprefix'] && d[1].length > 3) {
                    var linkstr = link['noprefix'][d[0]] + d[1];
                    if (d[0] == "SGD") linkstr += "/overview"; //special case
                    debris[i] = href_(linkstr, '', e);
                }
            }
        });
        $(ele).html(debris.join(''));
    });
}

function href_(link, title, text) {
    return '<a href="' + link + '" target="_blank" title="' + title + '">' + text + '</a>'
}
