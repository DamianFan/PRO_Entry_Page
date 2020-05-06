var batchSelect= [];
var batchUnselect = [];
var batchAlert = [];

function check_uniprot(id){
	if (/uniprotKB/i.test(id) || /PR:\w{6}(-\d\d?)?/i.test(id) || /\w{6}(-\d\d?)?/i.test(id)) return true;
	else return false;
}

function check_pro(id){
	if (/PR:\d{9}/.test(id)) return true;
	else return false;
}

function check_go(id){
	if (/GO:\d{7}/.test(id)) return true;
	else return false;
}

function check_chebi(id){
	if (/CHEBI:\d{5}/.test(id)) return true;
	else return false;
}

function modify(id){
	id = id.toUpperCase();
	if (/PR/i.test(id) && (check_pro(id) || check_uniprot(id)))
		return id;
	else if (/^\d+$/g.test(id)){
		var newid = "PR:000000000".substr(0,12-(id.length))+id;
		if (check_pro(newid)==true) return newid;
		else alert(errorInvalidPro,id);
	}
	else if (/GO/i.test(id)){
		if (check_go(id)) return id;
		else if (/GO:?\d+/.test(id)){
			id = new String(/\d+/.exec(id));
			var newid = "GO:0000000".substr(0,10-(id.length))+id;
			if (check_go(newid)==true) return newid;
			else alert(errorInvalidGo,id);
		}
		else alert(errorInvalidGo,id);
	}
	else if (/CHEBI/i.test(id)){
		if (check_chebi(id)) return id;
		else if (/CHEBI:?\d+/.test(id)){
			id = new String(/\d+/.exec(id));
			var newid = "CHEBI:00000".substr(0,11-(id.length))+id;
			if (check_chebi(newid)==true) return newid;
			else alert(errorInvalidChebi,id);
		}
		else alert(errorInvalidChebi,id);
	}
	else if (/\w{6}(-\d\d?)?/.test(id)){
		var newid = "PR:"+id;
		if (check_uniprot(newid)==true) return newid;
		else alert(errorInvalidUniprot,id);
	}
	else alert(errorId,id);
	return false;
}	

function batch_input_keystroke(e){
	switch(e.keyCode){
		case 13: //enter
			$( "#batchInput" ).autocomplete( "close" );
			batch_addInput();
			return;
		case 27: //esc
			$("#batchInput").val("");
			return;
	}
}

function batch_addEle(ele){ 
	var id = ele.data().id;
	if (batchSelect.indexOf(id)>-1)
		batchAlert.push(id);
	else if (batchUnselect.indexOf(id)>-1) {
		$('input[name="batchId"]').filter(function(){
			return this.value == id;
		}).prop("checked","true");
		remove(batchUnselect,id);
		batchSelect.push(id);
	}
	else {
		$("#batchTable").append('<tr class="click-row"><td valign=top>\
			<input type="checkbox" class="batch-checkbox" name="batchId" value="'+id+'" onchange="batch_checkbox_click(this)" checked></td>\
			<td valign=top onclick="select_node(\''+id+'\')">'+id+'</td>\
			<td valign=top onclick="select_node(\''+id+'\')">'+ele.data().Label+'</td></tr>');
		batchSelect.push(id);
	}
	batch_count();
}

function batch_addId(id){
	if (batchSelect.indexOf(id)>-1)
		batchAlert.push(id);
	else if (batchUnselect.indexOf(id)>-1) {
		$('input[name="batchId"]').filter(function(){
			return this.value == id;
		}).prop("checked","true");
		remove(batchUnselect,id);
		batchSelect.push(id);
	}
	else {
		$("#batchTable").append('<tr class="click-row">\
			<td valign=top><input type="checkbox" class="batch-checkbox" name="batchId" value="'+id+'" onchange="batch_checkbox_click(this)" checked></td>\
			<td valign=top>'+id+'</td> <td valign=top></td></tr>');
		batchSelect.push(id);
	}
	batch_count();
}

function batch_addCurrent(){
	for(var i in requestIds)
		batch_addEle(get_ele_by_id(requestIds[i]));
	batch_alert();
}

function batch_addInput(){
	var text = $("#batchInput").val();
	if (text=="") alert(errorId);
	else{
		var ids = text.split(',');
		for (var i in ids) {
			var id = modify(ids[i]);
			if (id==false) continue
			var ele = get_ele_by_id(id);
			if (ele.length==0) 
				batch_addId(id);
			else batch_addEle(ele);
		}
		batch_alert();
	}
	$("#batchInput").val("");
}

function batch_headCheckbox(){
	batchSelect = [];
	batchUnselect = [];
	if ($('#batchHeadCheckbox').prop("checked"))
		$('input[name="batchId"]').each(function(){
			$(this).prop('checked', true);
			batchSelect.push(this.value);
		});
	else
		$('input[name="batchId"]').each(function(){
			$(this).prop('checked', false);
			batchUnselect.push(this.value);
		});
	batch_count();
}

function batch_count(){
	$("#batchCount").html('('+batchSelect.length+')');
}

function batch_checkbox_click(source){
	if($(source).prop("checked")){
		batchSelect.push(source.value);
		remove(batchUnselect,source.value);
	}
	else{
		batchUnselect.push(source.value);
		remove(batchSelect,source.value);
	}
	batch_count();
}

function batch_clearAll(){
	if (confirm("Empty the list?")==true){
		$("#batchTable").empty();
		batchSelect = [];
		batchUnselect = [];
		batch_count();
	}
	else return;
}

function batch_query(){
	var ids = batchSelect.join(',');
	if (ids=='')  alert(errorId);
	else {
		if (ids.length>400){ //post submit when PRO ids>40
			$("#batchQueryInput").val(ids);
			$("#batchQueryForm").submit();
		}
		else window.open(cytourl+"#top",'_blank'); //get submit
	}
}

function batch_alert(){
	batchAlert = jQuery.unique(batchAlert);
	var len = batchAlert.length;
	if (len>=1) alert('"'+batchAlert.join(",")+'" '+((len>1)?'are':'is')+' already in the list.');
	else return;
	batchAlert = [];
}
