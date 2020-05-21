$(function(){
	// Legend
    $("#legend").dialog({
		autoOpen: false,
		closeOnEscapeType: true,
		hide: {	effect: "blind", duration: 100 },
		show: {	effect: "blind", duration: 100 },
		title: "Legend",
		position: { my: "left top", at: "left+2 top+33", of:"#legendMenuText"},
		width:340
    });
    $("#legendMenuText").click(function() {
		if ($("#legend").dialog("isOpen"))
			$("#legend").dialog("close");
		else {
			$("#legend").dialog("open");
			$("#displayOptions").dialog("close");
		}
    });
	// Display Options
	$("#displayOptions").dialog({
		autoOpen: false,
		closeOnEscapeType: true,
		hide: {	effect: "blind", duration: 100 },
		show: {	effect: "blind", duration: 100 },
		title: "Display Options",
		position: { my: "left top", at: "left+2 top+33", of:"#legendMenuText"},
		width: 320
    });
    $("#displayOptionsMenuText").click(function() {
		if ($("#displayOptions").dialog("isOpen"))
			$("#displayOptions").dialog("close");
		else{
			$("#displayOptions").dialog("open");
			$("#legend").dialog("close");
		}
    });
	// Batch Retrieval
	$("#batch").dialog({
		autoOpen: false,
		closeOnEscapeType: true,
		hide: {	effect: "blind", duration: 100 },
		show: {	effect: "blind", duration: 100 },
		title: "Batch Retrieval",
		position: { my: "right top", at: "right-5 top+33", of:"#docMenuText"},
    });
    $("#batchMenuText").click(function() {
		if ($("#batch").dialog("isOpen")) 
			$("#batch").dialog("close");
		else {
			$("#batch").dialog("open");
			$("#save").dialog("close");
		}
    });
	// Save
	$("#save").dialog({
		autoOpen: false,
		closeOnEscapeType: true,
		hide: {	effect: "blind", duration: 100 },
		show: {	effect: "blind", duration: 100 },
		title: "Save",
		position: { my: "right top", at: "right-5 top+33", of:"#docMenuText"},
    });
    $("#saveMenuText").click(function() {
		if ($("#save").dialog("isOpen"))
			$("#save").dialog("close");
		else {
			$("#save").dialog("open");
			$("#batch").dialog("close");
		}
    });
	// Doc
	$("#doc").dialog({
		autoOpen: false,
		closeOnEscapeType: true,
		hide: {	effect: "blind", duration: 100 },
		show: {	effect: "blind", duration: 100 },
		title: "Documentation",
		position: { my: "right top", at: "right-5 top+33", of:"#docMenuText"},
		width: 370
    });
    $("#docMenuText").click(function() {
		if ($("#doc").dialog("isOpen")){
			$("#doc").dialog("close");
		}
		else $("#doc").dialog("open");
	});
});

function remove(list,ele){
	list.splice(list.indexOf(ele),1);
	return list
}

function set_autocomplete(){
	var availableTags = [];
	currentEles.each(function(i, ele){
		availableTags.push(ele.data().id+" "+ele.data().Label);
	});
    $("#searchInput" ).autocomplete({
		source: availableTags,
		select: function(event,ui){
			var ele = get_ele_by_id(ui.item.value.split(' ')[0]);
			cy.$('node').unselect();
			ele.select();
			property_table_node(ele);
		}
    });
	$("#batchInput" ).autocomplete({
		source: availableTags,
		select: function(event,ui){
			var ele = get_ele_by_id(ui.item.value.split(' ')[0]);
			cy.$('node').unselect();
			ele.select();
			batch_addEle(ele);
			batch_alert();
			ui.item.value="";
		},
    });
}

$(window).ready(function(){
	// // // function_page
	// $(document).tooltip();
	$("#searchInput").on("click", function(){$(this).val("")});
	// $("#batchInput").on("click", function(){$(this).val("")});
	// // // legend
	$('#legendDialog').html(legendTable);
	// // // function_cytoscape
	$("#property").hide();
	$("#contextMenu").hide();
	// if (eleObj.nodes.length>100){
		// alert(errorExcessNodes1+eleObj.nodes.length+errorExcessNodes2);
		// $("#nodeLabel").prop("checked",false);
		// $("#edgeLabel").prop("checked",false);
		// $("#displayOptions").dialog("open");
	// }
	display_options(); 			// contain all attached function
	// layout_reset();
	// // // function_batch
	batch_count();
	$("#cy").cytoscapePanzoom();
});

window.oncontextmenu = function(event) {
    event.preventDefault();
    event.stopPropagation();
    return false;
};