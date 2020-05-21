function form_setup() {
    Object.keys(ROOT).forEach(function(i){
        create_title(ROOT[i], 1); // root node, level of display
    });
    draw_forms(ROOT);

    $('a.term-cat-num').click(function () {
        var selectedCat = $(this).attr('pro-category');
        $('#selected').text(selectedCat);
        action_filter_forms(selectedCat);
    });

    $('#filter_category_dropdown').click(function (e) {
        e.stopPropagation();
        e.preventDefault();
        $('#filter_category_dropdown_button').dropdown('toggle');
    });

    $('#filter_category_dropdown a').click(function (e) {
        var selectedCat = $(this).text();
        $('#selected').text(selectedCat);
        if (selectedCat == 'All'){
            $('#filter_category_dropdown_button')
                .removeClass('btn-danger')
                .addClass('btn-default');
            redraw_forms(ROOT);
        }
        else
            action_filter_forms(selectedCat);
    });
}

function action_filter_forms(selectedCat) {
    filter_forms(selectedCat);
    $('#filter_category_dropdown_button')
        .removeClass('btn-default')
        .addClass('btn-danger');
}

function draw_forms(data_source) {
    // Only used to initial the form table. Later use redraw_forms().
    $('#tree').fancytree({
        extensions: ['table', 'gridnav'],
        checkbox: false,
        icons: false,
        //titlesTabbable: true,        // Add all node titles to TAB chain
        source: data_source,
        table: {
            checkboxColumnIdx: null, // render the checkboxes into the this column index (default: nodeColumnIdx)
            customStatus: false,     // true: generate renderColumns events for status nodes
            indentation: 10,         // indent every node level by 16px
            nodeColumnIdx: 0         // render node expander, icon, and title to this column (default: #0)
        },
        gridnav: {
            autofocusInput: false, // Focus first embedded input if node gets activated
            handleCursorKeys: true   // Allow UP/DOWN in inputs to move to prev/next node
        },

        renderColumns: function (event, data) {
            var node = data.node,
                $tdList = $(node.tr).find('>td');

            // remove category=... in the data.comment.
            var comment = node.data.comment.split('.').filter(function (ele) {
                if (ele.indexOf('Category') < 0 && ele.length > 0) return true;
            }).join('.');

            $tdList.eq(1).html(node.data.name);
            $tdList.eq(2).html(node.data.short_label);
            $tdList.eq(3).html('<span class="add-link">' + node.data.def_text + '</span><br/>' +
                '<span class="add-link">' + comment + '</span>');
        }
    });
    highlight_item();
}

function redraw_forms(data) {
    var tree = $('#tree').fancytree('getTree');
    tree.reload(data);
    highlight_item();
}

function create_title(obj, level) {
    var labels = forms_bootstarp_label(obj);
    obj.title = href_(proEntryUrl + obj.id, '', obj.id) + labels + '<br/>' + obj.category;
    if (level > 0) {
        obj.expanded = true;
    }
    for (var i in obj.children) {
        create_title(obj.children[i], (level - 1));
    }
}

function filter_forms(category) {
    function form_shallow_copy(obj) {
        var copy = {};
        for (var k in obj) {
            copy[k] = k != 'children' ? obj[k] : [];
        }
        return copy;
    }

    function dfs(node, result) {
        if (node.category == category) {
            result.push(form_shallow_copy(node));
        }
        for (var idx in node.children) {
            dfs(node.children[idx], result);
        }
    }

    var filtered_forms = [];
    for (var i in ROOT) {
        dfs(ROOT[i], filtered_forms);
    }
    redraw_forms(filtered_forms);
}


function highlight_item() {
    // Highligh clicked tr
    $('a.form-tag').click(function (e) {
        var id = $(this).attr("href");
        // Jquery need escape colon in selector.
        var cls = $(this).attr("href").replace(':', '\\:').replace('#', '.');

        // Anchor the page
        if (id.startsWith('#paf')) {
            var tab = $('.tab-pane.active').attr('id');
            var row = $('#'+tab+' '+cls).first();

            $('html, body').animate({
                scrollTop: row.offset().top
            }, 100);
        }

        // Add highlight.
        if (id.startsWith('#paf')) {
            $('#functional-annotation tr.highlight').removeClass('highlight');
        }
        else if (id.startsWith('#complex')) {
            $('#complex tr.highlight').removeClass('highlight');
        }
        else if (id.startsWith('#subunit')) {
            $('#complex-subunits tr.highlight').removeClass('highlight');
        }
        $(cls).addClass('highlight');
        // setTimeout(function () {
        //     $('tr.highlight').removeClass('highlight');
        // }, 3000);
    });
}