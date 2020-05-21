// $(document).ready(function(){
// 	//init_mod_source();
// 	//init_mod_enzyme();
// 	//init_mod_note();
// 	init_tooltip("pro");
// });

function msa_pro_related_links(id){
	var id = id.trim();
	links = '<a href="'+prourl.slice(0, -3)+id+'" target="_blank">'+prologo+'</a>\
			 <a href="'+cytourl+id+'" target="_blank">'+cytologo+'</a>\
			 <a href="'+dagurl+id+'"#top target="_blank">'+daglogo+'</a>';
	return links
}
