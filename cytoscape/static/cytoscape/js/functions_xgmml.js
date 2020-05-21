var nid = [];
function download_xgmml(){
	var cy = $("#cy").cytoscape("get"); 
	var xgmml = "";
	
	xgmml += xgmmlHead;
	
	cy.$('node').each(function(i, ele){
		nid[ele.data()["id"]]=i;
	});
	
	cy.$('node').each(function(i, ele){
		xgmml += node(ele);
	});
	
	cy.$('edge').each(function(i, ele){
		xgmml += edge(ele);
	});
	
	xgmml += '</graph>';
	
	$("input[name=xgmmlNetwork]").val(xgmml);
}

function node(ele){
	var data = ele.data();
	var id = data["id"];
	var str = '<node label="'+id+'" id="'+nid[id]+'">\n';
	for (var i in data){
		if (i == "id") continue;
		str += "\t"+ att(i,data[i]);
	}
	str += '<graphics type="ELLIPSE" h="15.0" w="15.0" x="'+ele.position()['x']+'" y="'+ele.position()['y']+'" fill="#cccccc" width="1" outline="#ffffff" cy:nodeTransparency="1.0" cy:nodeLabelFont="Arial Bold-0-11" cy:nodeLabel="'+id+'" cy:borderLineType="solid"/>\n';
	str += '</node>\n';
	return str;
}

function edge(ele){
	var data = ele.data();
	var source = data["source"];
	var target = data["target"];
	var str = '<edge label="'+data["id"]+'" source="'+nid[source]+'" target="'+nid[target]+'">\n';
	for (var i in data){
		if (["source","target"].indexOf(i)>-1) continue;
		str += "\t"+ att(i,data[i]);
	}
	str += ' <graphics width="1" fill="#000000" cy:sourceArrow="0" cy:targetArrow="0" cy:sourceArrowColor="#000000" cy:targetArrowColor="#000000" cy:edgeLabelFont="SanSerif-0-10" cy:edgeLabel=" " cy:edgeLineType="SOLID" cy:curved="STRAIGHT_LINES"/>\n';
	str += '</edge>\n';
	return str;
}

function att(name,value){
	return '<att type="string" name="'+name+'" value="'+value+'"/>\n'
}

var xgmmlHead='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n\
<graph label="Cytoscape" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cy="http://www.cytoscape.org" xmlns="http://www.cs.rpi.edu/XGMML"  directed="1">\n\
  <att name="documentVersion" value="1.1"/>\n\
  <att name="networkMetadata">\n\
    <rdf:RDF>\n\
      <rdf:Description rdf:about="http://www.cytoscape.org/">\n\
        <dc:type>Protein-Protein Interaction</dc:type>\n\
        <dc:description>N/A</dc:description>\n\
        <dc:identifier>N/A</dc:identifier>\n\
        <dc:date>2013-10-24 13:16:32</dc:date>\n\
        <dc:title>Cytoscape</dc:title>\n\
        <dc:source>http://www.cytoscape.org/</dc:source>\n\
        <dc:format>Cytoscape-XGMML</dc:format>\n\
      </rdf:Description>\n\
    </rdf:RDF>\n\
  </att>\n\
  <att type="string" name="backgroundColor" value="#ffffff"/>\n\
  <att type="real" name="GRAPH_VIEW_ZOOM" value="1.0"/>\n\
  <att type="real" name="GRAPH_VIEW_CENTER_X" value="40.0"/>\n\
  <att type="real" name="GRAPH_VIEW_CENTER_Y" value="120.0"/>\n\
  <att type="boolean" name="NODE_SIZE_LOCKED" value="true"/>\n\
  <att type="string" name="__layoutAlgorithm" value="grid" cy:hidden="true"/>\n';