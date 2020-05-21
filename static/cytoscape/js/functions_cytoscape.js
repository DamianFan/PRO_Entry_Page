// to call functions in this file, must define following functions in a new javascript file: 
// display_options //follows pro/uni example
// color_options
// property_table_node
// property_table_edge

var windowWidth = $(window).width();
var windowHeight = $(window).height();

var removeNodeList = [];
var currentEles;
var nodeLabelFlag = []; //initilized in functions_page

$(loadCy = function(){
	options = {
		showOverlay: false,
		zoom: 1,
		minZoom: 0.1,
		maxZoom: 10,
		layout: layout_options(),
		elements: eleObj,
		style: styleObj,
		ready: function(){
			window.cy = this;
		}
	};
	$('#cy').cytoscape(options);
}); 

function update_attached_display_options(){
	color_options();
	set_mouse_event();
	node_label_switch();
	edge_label_switch();
}

function set_mouse_event(){
	var cy = $("#cy").cytoscape("get"); 
	// ---property table---
	cy.on('tap', function(e){
		if(e.cyTarget===cy){
			$("#property").hide();
			$("#contextMenu").hide();
			color_options();
		}
	});
	cy.on('cxttap', function(e){
		if(e.cyTarget===cy)
			collection_context_menu(e.originalEvent);
	});
	cy.$('node').on('tap', function(e){
		e.cyTarget.select();
		property_table_node(e.cyTarget);
	}); 
	cy.$('edge').on('tap', function(e){
		e.cyTarget.select();
		property_table_edge(e.cyTarget);
	}); 
	cy.$('node').on('cxttap',function(e){
		cy.$('node').unselect();
		e.cyTarget.select();
		node_context_menu(e.cyTarget);
	}); 
	// ---neighbor---
	cy.$('node').on('mouseover', function(e){
		var eles = e.cyTarget.closedNeighborhood();
		cy.$().css('opacity','0.2');
		eles.css('opacity','1');
	}); 
	cy.$('node').on('mouseout', function(e){
		cy.$('node').css('opacity','1');
		cy.$('edge').css('opacity','0.8');
	}); 
}

function get_ele_by_id(id){
	return cy.filter(function(i, element){
		if( element.isNode() && element.data("id")==id ){
			return true; 
		}
			return false;
	});
}

function select_node(id){
	var cy = $("#cy").cytoscape("get"); 
	cy.$().unselect();
	color_options();
	get_ele_by_id(id).select();
	get_ele_by_id(id).css({'background-color':'#f9ff00','border-color':'#e0e500','source-arrow-color':'#f9ff00','target-arrow-color':'#f9ff00'});
}

function layout_options(){
	var opt = $('#layoutMenu').val();
	$("#cy").cytoscape(function(eventObject){
		var cy = this;
		cy.layout(layoutObj[opt]);
	});
	return layoutObj[opt];
}

function layout_reset(){
	var cy = $("#cy").cytoscape("get"); 
	var hideEles = cy.$('node').not(currentEles);
	hideEles.remove();
	var opt = $('#layoutMenu').val();
	$("#cy").cytoscape(function(eventObject){
		var cy = this;
		cy.layout(layoutObj[opt]);
	});
}

function node_label_flag_all(flag){
	var eles = eleObj.nodes;
	for (var i in eles)
		nodeLabelFlag[eles[i].data.id]=flag;
}

function show_hidden_obj(){
	removeNodeList = [];
	$("#showHidden").prop('checked',true);
	$("#showHidden").prop("disabled",true);
	display_options();
	layout_reset();
}

function node_context_menu(ele){
	$('#contextMenu').empty();
	$('#contextMenu').show();
	$('#property').hide();
	$('#contextMenu').append('<table id="contextMenuTable">');
	var data = ele.data();
	$('#contextMenu').append('<tr><td colspan="2" class="context-header-1">'+data.id+'</td></tr>');
	$('#contextMenu').append('<tr><td colspan="2" class="context-header-2">'+data.Label+'</td></tr>');
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=node_context_menu_batch("'+data.id+'")>Add node to Batch Retrieval</td></tr>');
	if (requestIds.indexOf(data.id)<0)
		$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=node_context_menu_hide("'+data.id+'")>Hide node</td></tr>');
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=node_context_menu_label("'+data.id+'")>\
		<span id="contextMenuNodeLabel">Hide</span> node label</td></tr>');
	if (nodeLabelFlag[data.id]==true)
		$("#contextMenuNodeLabel").text("Hide");
	else $("#contextMenuNodeLabel").text("Show");
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=node_context_menu_first_neighbor("'+data.id+'")>Select First Neighbor</td></tr>');
	$('#contextMenu').append('</table>');
	set_div_pos(ele.renderedPosition().x,ele.renderedPosition().y,"#contextMenu",200,true);
}

function node_context_menu_batch(id){
	$('#contextMenu').hide();
	batch_addEle(get_ele_by_id(id));
	$("#batch").dialog("open");
	batch_alert();
}

function node_context_menu_hide(id){
	$('#contextMenu').hide();
	removeNodeList.push(id);
	get_ele_by_id(id).remove();
	$("#showHidden").prop('checked',false);
	$("#showHidden").prop("disabled",false);
}

function node_context_menu_label(id){
	$('#contextMenu').hide();
	var ele = get_ele_by_id(id);
	if (nodeLabelFlag[id]==true){
		ele.css({'content':'\t',});
		nodeLabelFlag[id]=false;
	}
	else{
		ele.css({'content':'data(Label)'});
		nodeLabelFlag[id]=true;
	}
}

function node_context_menu_first_neighbor(id){
	$('#contextMenu').hide();
	var eles = get_ele_by_id(id).closedNeighborhood();
	eles.select();
}

function collection_context_menu(e){
	$('#contextMenu').empty();
	$('#contextMenu').show();
	$('#property').hide();
	$('#contextMenu').append('<table id="contextMenuTable">');
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=collection_context_menu_batch()>Add selected nodes to Batch Retrieval</td></tr>');
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=collection_context_menu_hide()>Hide selected node</td></tr>');
	var flag = false;
	cy.$('node:selected').each(function(i, ele){
		flag = flag || nodeLabelFlag[ele.id()];
	});
	if (flag == true)
		 $('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=collection_context_menu_label(true)>Hide selected nodes Label</td></tr>');
	else $('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=collection_context_menu_label(false)>Show selected nodes label</td></tr>');
	$('#contextMenu').append('<tr class="context-row"><td class="context-table-left"></td><td class="context-table" onclick=collection_context_menu_first_neighbor()>Select First Neighbor</td></tr>');
	$('#contextMenu').append('</table>');
	set_div_pos(e.offsetX,e.offsetY,"#contextMenu",200,false);
}

function collection_context_menu_batch(){
	$('#contextMenu').hide();
	$("#batch").dialog("open");
	cy.$('node:selected').each(function(i, ele){
		batch_addEle(ele);
	});
	batch_alert();
}

function collection_context_menu_hide(){
	$('#contextMenu').hide();
	cy.$('node:selected').each(function(i, ele){
		if (requestIds.indexOf(ele.id())>-1) return 
		removeNodeList.push(ele.id());
		ele.remove();
	});
	$("#showHidden").prop('checked',false);
	$("#showHidden").prop("disabled",false);
}

function collection_context_menu_label(flag){
	$('#contextMenu').hide();
	if (flag==true){
		cy.$('node:selected').each(function(i, ele){
			ele.css({'content':'\t',});
			nodeLabelFlag[ele.id()]=false;
		});
	}
	else{
		cy.$('node:selected').each(function(i, ele){
			ele.css({'content':'data(Label)'});
			nodeLabelFlag[ele.id()]=true;
		});
	}
}

function collection_context_menu_first_neighbor(){
	$('#contextMenu').hide();
	cy.$('node:selected').each(function(i, ele){
		node_context_menu_first_neighbor(ele.data().id);
	});
}

function node_label_switch(){
	var cy = $("#cy").cytoscape("get"); 
	if($("#nodeLabel").prop('checked')){
		cy.$('node').css({'content':'data(Label)'});
		node_label_flag_all(true);
	}
	else{
		cy.$('node').css({'content':'\t',});
		node_label_flag_all(false);
	}
}

function edge_label_switch(){
	var cy = $("#cy").cytoscape("get"); 
	if($("#edgeLabel").prop('checked'))
		cy.$('edge').removeCss();
	else cy.$('edge').css({'content':'\t',});
}

function create_property_table(x,y){
	$('#property').empty();
	$('#property').show();
	$('#contextMenu').hide();
	$('#property').append('<table id="propertyTable"></table>');
	set_div_pos(x,y,"#propertyTable",400,true);
}

function alink(url,id,name){
	return '<a class="tlink" href="'+url+id+'" target="_blank">'+name+'</a>,'
}

function set_div_pos(x,y,divid,w,shift){ 
	if (shift==true) {
		var xs=30; 
		var ys=15;
	}
	else{
		var xs=0;
		var ys=0;
	}
	if (x+w>windowWidth) x = x-w-xs;
	else x = x+xs;
	y = y+131;
	var h = $(divid).height();
	if (y+h>windowHeight) y = y-h-ys;
	else y = y+ys;
	y = Math.max(y,131);
	$(divid).offset({ top: y, left: x});
}

function save_options(){
	var saveOpt = $('input[name="networkFormat"]').val();
	var cy = $("#cy").cytoscape("get");
	if (saveOpt=='networkPng') 
		cy.png();
}
