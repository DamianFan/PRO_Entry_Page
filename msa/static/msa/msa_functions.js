function init() {
	$("#msaDivDV").hide();
	msa_view_switch("OV");
	init_mod_modType();
	init_add_line();
	init_select();
	init_sortable();
	//// msa_function_pro.js -> init_tooltip("pro");

	$(".dropdown-menu").click(function (event) {
		event.stopPropagation();
	});
	msa_unmod();

	$('td[class*=msa-mod]').tooltip({
		content: function () {
			return $(this).prop('title');
		},
		show: null,
		close: function (event, ui) {
			ui.tooltip.hover(
				function () {
					$(this).stop(true).fadeTo(10, 1);
				},
				function () {
					$(this).fadeOut("10", function () {
						$(this).remove();
					})
				});
		},
		position: {
			my: "left top",
			at: "right center"
		}
	});
	// add pro switch button if mod = entry
	//if (mod=='entry')
	//	msa_pro_switch(true);
	//else {
	//	msa_pro_switch(false);
	//	$("#msaProSwitch").hide();
	//}
}


$(document).click(function(e){
	  if(!$(e.target).is('.msa-align-result *'))
		msa_view_reset();
		$('div[class*=tooltipster]').hide();
});

function msa_pro_switch(btn) {
	if (btn == true)  // hide pro entries
		$("tr[ng-class='msa-ptmform']").addClass('hide');
	else // display pro entries
		$("tr[ng-class='msa-ptmform']").removeClass('hide');
}

function init_mod_modType(){
	// modType: main color
	msa_mod_prop_template("ModType",[]);
	
	$("#msaModTypeAll").prop({"disabled":false, "checked":true});
	$("#msaModTypeAllText").html('Modification');
	$("#msaMenuTableModType").append('\
		<tr><td>\
		<input type="checkbox" name="msaModType" value="con" onchange="msa_mod_type_highlight(this)" checked></td>\
		<td><span class="msa-con">&nbsp;&nbsp;&nbsp;</span> Conserved PTM Site</td></tr>\
		<tr><td>\
		<input type="checkbox" style="visibility:hidden;"></td>\
		<td><span class="msa-con-sub">&nbsp;&nbsp;&nbsp;</span> Conserved substitution </td></tr>\
		<tr><td>\
		<input type="checkbox" style="visibility:hidden;"></td>\
		<td><span class="msa-mod-un">&nbsp;&nbsp;&nbsp;</span> Conserved PTM Site in unmodified form \
		</td></tr>\
		');
	$.each(msaModTypeDict,function(key,value){
		$("#msaMenuTableModType").append('<tr><td>\
		<input type="checkbox" name="msaModType" value="'+key+'" onchange="msa_mod_type_highlight(this)" unchecked disabled></td> \
		<td><span class="msa-'+key+'">&nbsp;&nbsp;&nbsp;</span> <span class="disabled-text">'+value+' </span></td></tr>');
    });
	
	if (stat.modType) {
		stat.modType.forEach(function(modType){
			var opt = $('input[name="msaModType"][value="mod-'+modType+'"]');
			opt.prop({"disabled":false, "checked":true});
			opt.parent().parent().find('span').removeClass("disabled-text");
		});
	}
}

function init_select(){
	// // aa select
	// $(".msa-aa").hover(function(){
		// $(this).toggleClass("aa-selected");
	// });
	
	// cross 
	$(".msa-table td").hover(function(){
		$(this).toggleClass("aa-hover");
		var col = $('.msa-table thead tr td:nth-child('+($(this).index()+1)+ ')');
		col.toggleClass("aa-hover");
		var rowIndex = $(this).closest('tr').prevAll().length;
		// var row = $('.msa-table-entry tbody tr:eq('+rowIndex+') td');
		var row = $('#msaTableEntryOV tbody tr:eq('+rowIndex+') td');
		row.toggleClass("aa-hover");
		var row = $('#msaTableEntryDV tbody tr:eq('+rowIndex+') td');
		row.toggleClass("aa-hover");
	});
	
	// row select
	$(".msa-table-entry td").click(function(){
		msa_view_reset();
		var row = $('.msa-table tbody tr:nth-child('+($(this).parent().index()+1)+ ')')
		row.children('td').addClass("td-row-selected");
		row.children('td.msa-aa').addClass("td-selected");
		row.children('td.msa-gap').addClass("td-selected");
		$(this).parent().children().addClass("th-selected"); 
	});
	
	// column select
	$(".msa-table .msa-table-th").click(function(){
		msa_view_reset();
		$('.msa-table tr td:nth-child('+($(this).index()+1)+ ')').addClass("td-col-selected");
		$('.msa-table tr td:nth-child('+($(this).index()+1)+ ').msa-aa').addClass("td-selected");
		$('.msa-table tr td:nth-child('+($(this).index()+1)+ ').msa-gap').addClass("td-selected");
		$(this).addClass("th-selected"); 
	});
	
	// select reset
	$(".msa-table-entry thead th").click(function(){
		msa_view_reset();
	});
}

function init_add_line(){
	// add line between different organisms and request 
	if ($("#msaTableEntryDV tr").hasClass("msa-isoform"))
		var cls = "msa-isoform";
	else var cls = "msa-ptmform";
	$("#msaTableEntryDV tbody tr."+cls+":first").before(emptyEntryLine);
	$("#msaTableEntryOV tbody tr."+cls+":first").before(emptyEntryLine);
	var idx = $("#msaTableEntryOV tbody tr."+cls+":first").index();
	if (idx==1) idx = idx;
	$('#msaTableDV tbody tr:nth-child('+idx+ ')').before(new_row($("#msaTableDV tr:first td").length));
	$('#msaTableOV tbody tr:nth-child('+idx+ ')').before(new_row($("#msaTableOV tr:first td").length));
}

function new_row(num){
	var line = '<tr class="msa-divider">';
	for (var i=0; i<num; i++)
		line += '<td class="msa-empty"> </td>';
	line += '</tr>';
	return line;
}

function row_move(table,start,end) {
	if (end<start) end-=1;
	var row = $("#"+table+" tbody tr").eq(start);
	if (end==-1)
		$("#"+table+" tbody tr").eq(0).before(row);
	else 
		$("#"+table+" tbody tr").eq(end).after(row);
}

function init_sortable(){
	var start = 0;
	var end = 0;
	$("#msaTableEntryDV tbody").sortable({
		helper: "clone",
		axis: "y",
		cursor: "move",
		opacity: 0.8,
		delay: 50,
		scroll: false,
		start: function(event, ui) { 
			$("#msaEntryLinks").remove();
			start = ui.item.index();
		},
		update: function(event, ui) { 
			end = ui.item.index();
			row_move("msaTableDV",start,end);
			row_move("msaTableEntryOV",start,end);
			row_move("msaTableOV",start,end);
		},
		placeholder: "sortable-place-holder",
		forcePlaceholderSize: true
	}).disableSelection();
	
	$("#msaTableEntryOV tbody").sortable({
		helper: "clone",
		axis: "y",
		cursor: "move",
		opacity: 0.8,
		delay: 50,
		scroll: false,
		start: function(event, ui) { 
			$("#msaEntryLinks").remove();  
			start = ui.item.index();
		},
		update: function(event, ui) { 
			end = ui.item.index();
			row_move("msaTableOV",start,end);
			row_move("msaTableEntryDV",start,end);
			row_move("msaTableDV",start,end);
		},
		placeholder: "sortable-place-holder",
		forcePlaceholderSize: true
	}).disableSelection();
}

function init_tooltip(ver){
	$('.msa-table-id').each(function(){
		var tr = $(this).parent();
		$(tr).addClass("msa-tooltip");
		$(tr).attr('title',function(){
			var td = $(tr).children('td');
			var id = td.eq(0).text(),
				did = '<b>'+id+'</b>',
				label = '<b>Label</b>:&nbsp;&nbsp;' + td.eq(1).text(),
				def = td.eq(1).attr("def"),
				sites = td.eq(1).attr("sites"),
				enzymes = td.eq(1).attr("enzymes").replace(/_/g,":"),
				links = ((ver=="pro")?msa_pro_related_links(id):msa_iptmnet_related_links(id));

			def = (def!='')?'<b>Def</b>:&nbsp;&nbsp;'+def:'';
			if (id.indexOf('PR:')>-1) {
				sites = (sites != '') ? '<b>PTM Sites</b>:&nbsp;&nbsp;' + sites : '';
				enzymes = (enzymes != '') ? '<b>PTM enzymes</b>:&nbsp;&nbsp;' + enzymes : '';
			}
			else {
				sites = '';
				enzymes = ''
			}

			return [did,label,def,links,enzymes,sites].filter(function(x){
						return x!=''
					}).join("<br>");
		});
	});
	$('.msa-tooltip').tooltipster({
		interactive: true,
		trigger:'click',
		theme: '.tooltipster-shadow',
		position: 'bottom-left',
		offsetX: +5,
		offsetY: -10,
		delay: 100,
		maxWidth: 350
	});
}

function msa_view_reset(){
	$(".msa-table td").removeClass("th-selected td-row-selected td-col-selected td-selected");
	$(".msa-table-entry td").removeClass("th-selected");
}

function msa_view_switch_click(){
	msa_view_reset();
	if($("#msaViewSwitch").attr("msa-view")=="OV"){
		$("#msaViewSwitch").attr("msa-view","DV");
		msa_view_switch("DV");
	}
	else{
		$("#msaViewSwitch").attr("msa-view","OV");
		msa_view_switch("OV");
	}
}

function msa_view_switch(opt){
	if(opt=="OV"){
		$("#msaDivOV").show();
		$("#msaDivDV").hide();
		$("#msaViewSwitch").html(iconPlus);
	}
	else{
		$("#msaDivOV").hide();
		$("#msaDivDV").show();
		$("#msaViewSwitch").html(iconMinus);
	}
}

function msa_mod_type_highlight(obj){
	var cls = ".msa-"+obj.value;
	if ($(obj).prop("checked")){
		$(cls).css({"background":"", "color":"", "border":""});
		if (obj.value == "con") {
			$(".msa-con-sub").css({"background":"", "color":"", "border":""});
			$(".msa-mod-un").css({"background":"", "color":"", "border":""});
		}
	}
	else{
		$(cls).css({"background":"#fff", "color":"#000", "border":"1px solid #fff"});
		if (obj.value == "con") {
			$(".msa-con-sub").css({"background":"#fff", "color":"#000", "border":"1px solid #fff"});
			$(".msa-mod-un").css({"background":"#fff", "color":"#000", "border":"1px solid #fff"});
		}
	}
	msa_unmod();
}


function msa_name_check_all(cls,flag) {
	$('input[name="'+cls+'"]').each(function(){
		if (!$(this).prop('disabled')){
			if (flag==true)
				$(this).prop('checked', true).trigger('onchange');
			else
				$(this).prop('checked', false).trigger('onchange');
		}
	});
}

function msa_mod_prop_template(prop,list){
	$("#msaMenuUl").append('<li class="dropdown">\
		<a href="#" class="dropdown-toggle msa-menu-header" data-toggle="dropdown">\
			<span id="msa'+prop+'AllText" >'+prop+'</span><span class="caret"></span></a>\
		<div class="dropdown-menu">\
			<div class="select-all"> \
			Select: <a href="" onclick=msa_name_check_all("msa'+prop+'",true);>All</a>, \
					<a href="" onclick=msa_name_check_all("msa'+prop+'",false);>None</a>\
			</div>\
			<div class="msa-menu-div">\
			<table id="msaMenuTable'+prop+'" class="msa-menu-table">\
			</table></div>\
		</div></li>');
	if (list.length>0 || prop=="ModType") {
		list.forEach(function(elem){
			var value = prop.toLowerCase()+'-'+elem; 
				$("#msaMenuTable"+prop).append('<tr><td>\
				<input type="checkbox" name="msa'+prop+'" value="'+value+'" onchange="msa_mod_prop_highlight(this)" unchecked></td>\
				<td>'+opt(elem,prop)+'</td></tr>\
			');
		});
	}
	else {
		$("#msaMenuTable"+prop).append('<tr><td>None</td></tr>');
		$("#msa"+prop+"All").prop({"disabled":true, "checked":false});
	}
}

function opt(key,prop) {
	if (prop == "Enzyme") 
		return key+"</td><td>"+symbol[key];
	else
		return key
}

function init_mod_source(){
	msa_mod_prop_template("Source",stat.source);
}

function init_mod_enzyme(){
	msa_mod_prop_template("Enzyme",stat.enzyme);
}

function init_mod_note(){
	msa_mod_prop_template("Note",stat.note);
}

function msa_mod_prop_highlight(obj) {
	var cls = ".msa-"+obj.value;
	cls = cls.replace(":","_");
	if ($(obj).prop("checked"))
		$(cls).css({"background":"#ff0", "color":"#000","border":"1px solid #ff0"});
	else
		$(cls).css({"background":"", "color":"","border":""});
	msa_unmod();
}

function msa_unmod(){
	if ($('input[name="msaModType"]').prop("checked")) {
		$("#msaTableEntryDV tr").each(function(i,e){
			var label = $(e).children(".msa-table-label").text();
			if (label.indexOf("UnMod")>-1 || label.indexOf("PhosRes-")>-1 || label.indexOf("unmodified")>-1) {
				$('#msaTableDV tbody tr:nth-child('+i+ ')').children(".msa-con").removeClass("msa-con").addClass("msa-mod-un");
				$('#msaTableDV tbody tr:nth-child('+i+ ')').children(".msa-con-sub").removeClass("msa-con-sub").addClass("msa-mod-un");
				$('#msaTableOV tbody tr:nth-child('+i+ ')').children(".msa-con").removeClass("msa-con").addClass("msa-mod-un");
				$('#msaTableOV tbody tr:nth-child('+i+ ')').children(".msa-con-sub").removeClass("msa-con-sub").addClass("msa-mod-un");
			}
		});
	}
}

function msa_pmid_show(me){
		$(me).next('span').css('display','inline');
		$(me).css('display','none');
}