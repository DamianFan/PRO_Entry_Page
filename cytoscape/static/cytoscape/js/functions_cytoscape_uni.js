function children_selection(){
	option = '<select id="childrenMenu" onchange="display_options()">';
	if (childrenMenu.length==0) 
		option += '<option value="15" selected>all</option>';
	else{
		for( var i in childrenMenu)
			option += '<option value="'+childrenMenu[i]+'">'+L2C[childrenMenu[i]]+'</option>';
	}
	option += '</select>';
	$("#childrenLevel").html(option);
	$("#childrenMenu option").each(function(){
		if ($(this).val()%2 == 0) 
			$(this).addClass("organism");
	});
}

function display_options(){
	var cy = $("#cy").cytoscape("get"); 
	cy.load(eleObj);
	var groupHidden = [];
	// // // ---groupName options---
	if (siblingSwitch==0) { 
		$("#sibling").prop("checked",false); 
		$("#sibling").prop("disabled",true); $("#siblingText").css("color","#d1d1d1"); 
	}
	else { 
		$("#sibling").prop("disabled",false); $("#siblingText").css("color","black"); 
	}
	if (!$("#parent").prop("checked")){ 
		groupHidden.push("parent","sibling"); 
		$("#sibling").prop("disabled",true); $("#siblingText").css("color","#d1d1d1");
	}
	if (!$("#sibling").prop("checked")) 
		groupHidden.push("sibling")
	if (!$("#child").prop("checked")){
		groupHidden.push("child"); 
		$("#childrenMenu").prop("disabled","disabled"); 
		$("#organism").prop("disabled",true); $("#organismText").css("color","#d1d1d1"); 
	}
	else { 
		$("#childrenMenu").prop("disabled",""); 
		$("#organism").prop("disabled",false); $("#organismText").css("color","black"); 
	}
	// // // ---children level options---
	var cLevel = parseInt($('#childrenMenu').val());
	// // // ---organism options---
	var oHidden = !$("#organism").prop("checked");
	// // // ---catName options---
	// var catHidden = [];
	// $('input[name="catName"]:not(:checked)').each(function(){
		// catHidden.push(this.value);
		// if (this.value == "complex") catHidden.push('\t\t');
	// });
	// // // ---annotation options---
	// if (!$("#annotation").prop("checked")){
		// groupHidden.push("annotation");
		// cy.$('edge[Interaction$="interaction"]').hide();
	// }
	// else cy.$('edge[Interaction$="interaction"]').show();
	// // // ---node type options--- based on shape
	var shapeHidden = [];
	if (!$('#shapeProtein').prop("checked")) shapeHidden.push('');
	if (!$('#shapeComplex').prop("checked")) shapeHidden.push('complex');
	// // // ---core---
	if ($('#showHier').prop("checked")) groupHidden.push('addition');
	// // // ---core---
	var hideEles = cy.filter(function(i, element){
		if(element.isNode() 
		&& requestIds.indexOf(element.data("id"))<0
		&& (
			groupHidden.indexOf(element.data("Group"))>-1 
		// || (parseInt(element.data("Level"))>cLevel && element.data("Group")=="child")
		|| (parseInt(element.data("Level"))>cLevel)
		|| (element.data("Category").search('organism')>-1 && oHidden)
		// || catHidden.indexOf(element.data("Category"))>-1
		|| shapeHidden.indexOf(element.data("Shape"))>-1
		|| removeNodeList.indexOf(element.data("id"))>-1
		)){ return true; }
		    return false; 
	});	
	hideEles.remove();
	currentEles = cy.$('node').not(hideEles);
	update_attached_display_options();
	set_autocomplete();
	if (oHidden){
		var currentSel = $("#childrenLevel option:selected").val();
		if (currentSel%2==0)
			$("#childrenMenu option").each(function(){
				if ($(this).val() == currentSel-1)
					$(this).prop("selected","selected");
			});
		$("#childrenLevel option.organism").hide();
	}
	else 
		$("#childrenLevel option.organism").show();
}

function color_options_ptm_checkbox(){
	if ($('#ptmBox').prop("checked")){
			$('#ptmKinaseBox').prop("checked",true);
			$('#ptmOtherBox').prop("checked",true);
		}
		else{
			$('#ptmKinaseBox').prop("checked",false);
			$('#ptmOtherBox').prop("checked",false);
		}
	color_options();
}

function color_options(){
	var cy = $("#cy").cytoscape("get"); 
	// set default
	cy.$('node').css({"background-color": "#a6a6a6","background-image":"none","border-color": "#424242"}); 
	// options
	if (!$("#ptmKinaseBox").prop("checked") || !$("#ptmOtherBox").prop("checked"))
		$('#ptmBox').prop("checked",false);
	// node group
	var request = cy.$('node[Group="request"]');
	var related = cy.$('node[Group="related"]');
	// color
	request.css({"background-color": "#007fff","border-color": "#003f7f"}); //blue
	related.css({"background-color": "#00C600","border-color": "#007600"}); //green
	if ($("#ptmKinaseBox").prop("checked")){
		var ptmKinase = cy.$('node[ptm="kinase"]');
		var request_ptmKinase = cy.filter(function(i, element){
			if(element.isNode() 
			&& element.data("Group").search('request')>-1
			&& element.data("ptm").search('kinase')>-1
			){ return true; } 
			   return false; 
		});	
		var related_ptmKinase = cy.filter(function(i, element){
			if(element.isNode() 
			&& element.data("Group").search('related')>-1
			&& element.data("ptm").search('kinase')>-1
			){ return true; } 
			   return false; 
		});	
		ptmKinase.css({"background-color": "#ff007e", "border-color": "#7f003f"}); //pink
		request_ptmKinase.css({ "background-image":"url (./images/node-bg-blue-pink.PNG)", "border-color": "#40205f" }); //blue-pink
		related_ptmKinase.css({ "background-image":"url (./images/node-bg-green-pink.PNG)", "border-color": "#403b20" }); //green-pink
	};
	if ($("#ptmOtherBox").prop("checked")){
		var ptmOther = cy.$('node[ptm="acetylase"]');
		var request_ptmOther = cy.filter(function(i, element){
			if(element.isNode() 
			&& element.data("Group").search('request')>-1
			&& element.data("ptm").search('acetylase')>-1
			){ return true; } 
			   return false; 
		});	
		var related_ptmOther = cy.filter(function(i, element){
			if(element.isNode() 
			&& element.data("Group").search('related')>-1
			&& element.data("ptm").search('acetylase')>-1
			){ return true; } 
			   return false; 
		});	
		ptmOther.css({"background-color": "#ff0000","border-color": "#7f0000"});  //red
		request_ptmOther.css({ "background-image":"url (./images/node-bg-blue-red.PNG)", "border-color": "#402040"}); //blue-red
		related_ptmOther.css({ "background-image":"url (./images/node-bg-green-red.PNG)", "border-color": "#403b00"}); //green-red
	};
}

function property_table_node(ele){
	create_property_table(ele.renderedPosition().x,ele.renderedPosition().y);
	
	var data = ele.data();
	if ((data.ID).indexOf("UniProtKB:")>-1){ // need change
		$('#propertyTable').append('<tr><td colspan="2" class="property-header">'+data.ID+'</td></tr>');
		$('#propertyTable').append('<tr><td colspan="2">'+
			alink(uniurl,(data.id).substr(10),'UniProt report')+
			'</td></tr>');
	}
	else{
		$('#propertyTable').append('<tr><td colspan="2" class="property-header">'+data.ID+'<span style="font-weight:normal;">\
			<a class="tlink" href="'+cytourl+data.id+'#top" target="_blank" style="float:right;">Jump to its Cytoscape view</a></span></td></tr>');
		$('#propertyTable').append('<tr><td colspan="2" class="property-table-link">'+
			alink(dagurl,data.id,'DAG view')+
			alink(prourl,data.id,'PRO report')+
			alink(obourl,data.id,'OBO Stanza')+
			alink(pafurl,data.id,'PAF')+
			'</td></tr>');
	}
	var outList = [].concat(nodeProp);
	for (var i in data)
		if (nodeProp.indexOf(i)==-1 && nodeNonProp.indexOf(i)==-1 && data[i] != null && data[i] != '') 
			outList.push(i);
	for (var i in outList)	
		$('#propertyTable').append('<tr><td class="property-table-td1">'+outList[i]+'</td><td class="property-table-td2">'+data[outList[i]],'</td></tr>');
	$("#propertyTable tr:even").addClass("property-table-gray");
}

function property_table_edge(ele){
	var eles = ele.connectedNodes();
	var x=eles[0].renderedPosition().x + eles[1].renderedPosition().x;
	var y=eles[0].renderedPosition().y + eles[1].renderedPosition().y;
	create_property_table(x/2,y/2);
	
	$('#propertyTable').append('<tr><td colspan="2" class="property-header"> Edge: </td></tr>');
	var data = ele.data();
	var outList = [].concat(edgeProp);
	for (var i in data)
		if (edgeProp.indexOf(i)==-1 && edgeNonProp.indexOf(i)==-1 && data[i] != null && data[i] != '') 
			outList.push(i);
	for (var i in outList)	
		$('#propertyTable').append('<tr><td class="property-table-td1">'+outList[i]+'</td><td class="property-table-td2">'+data[outList[i]],'</td></tr>');
	$("#propertyTable tr:odd").addClass("property-table-gray");
}
