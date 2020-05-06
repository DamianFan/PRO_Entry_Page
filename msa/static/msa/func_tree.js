$(function () {
    var selKeys = [];
    $("#tree").dynatree({
        children: treeData,
        checkbox: true,
        minExpandLevel: 2,
        persist: false,
        selectMode: 2,
        onSelect: function (select, node) {
            selKeys = $.map(node.tree.getSelectedNodes(), function (node) {
                return node.data.key;
            });
        },
        onClick: function (node, event) {
            if (node.getEventTargetType(event) == "title")
                node.toggleSelect();
        },
        onKeydown: function (node, event) {
            if (event.which == 32) {
                node.toggleSelect();
                return false;
            }
        },
    });
    selKeys = $.map($("#tree").dynatree("getSelectedNodes"), function (node) {
        return node.data.key;
    });
    $("#tree").dynatree("getRoot").visit(function (node) {
        node.expand(true);
    });
    $("li[name='treeActionsLi']").click(function () {
        var opt = $(this).attr("value");
        console.log(opt);
        if (opt == "btnExpandAll") {
            $("#tree").dynatree("getRoot").visit(function (node) {
                node.expand(true);
            });
            exc();
        }
        if (opt == "btnCollapseAll") {
            $("#tree").dynatree("getRoot").visit(function (node) {
                node.expand(false);
            });
            exc();
        }
        if (opt == "btnToggleSelect") {
            $("#tree").dynatree("getRoot").visit(function (node) {
                node.toggleSelect();
            });
            exc();
        }
        if (opt == "btnDeselectAll") {
            $("#tree").dynatree("getRoot").visit(function (node) {
                node.select(false);
            });
            exc();
        }
        if (opt == "btnSelectAll") {
            $("#tree").dynatree("getRoot").visit(function (node) {
                node.select(true);
            });
            exc();
        }
    });
    $("#btnGet").click(function (e) {
        e.preventDefault();
        refresh(selKeys);
        return false;
    });
    // first load
    $("#msaResult").html('<object  width="100%" height="800px" data="'+msaFullUrl+'" type="text/html">');
});

function refresh(selKeys) {
    var request = selKeys.join(",").replace(/\s/g, ''); //first id is always the query one
    var url = msaUrl+'view/full-selected/'+request;
    console.log(url);
    var height = $("#td-1").height()+20;
    $("#msaResult").html('<object  width="100%" height="'+height+'" data="'+url+'" type="text/html">');
}

function exc() {
    $('#treeActions option[value="default"]').attr('selected', 'selected');
}