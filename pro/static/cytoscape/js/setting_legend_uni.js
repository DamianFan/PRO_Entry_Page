var legendTable = '\
	<h1>Nodes:</h1>\
	<table class="legend-table"><tr><td>\
	<img class="legend-node" src="' + imageUrl + "node-circle-grey.PNG" + '" alt="circle-grey">Protein<br>\
	<img class="legend-node" src="' + imageUrl + "node-roundrect-grey.PNG" + '" alt="roundrect-grey">Complex<br>\
	<img class="legend-node" src="' + imageUrl + "node-tri-grey.PNG" + '" alt="triangle-grey">Chemical Entity<br>\
	<br>\
	<img class="legend-node" src="' + imageUrl + "node-circle-blue.PNG" + '" alt="circle-blue">Requested Entry<br>\
	</td><td>\
	<img class="legend-node" src="' + imageUrl + "node-circle-border.PNG" + '" alt="circle-border">Modified Form<br>\
	<img class="legend-node" src="' + imageUrl + "node-circle-grey.PNG" + '" alt="circle-grey">Taxon General<br>\
	<img class="legend-node" src="' + imageUrl + "node-circle-small.PNG" + '" alt="circle-small">Organism Specific<br>\
	<br>\
	<img class="legend-node" src="' + imageUrl + "node-circle-green.PNG" + '" alt="circle-green">Related Entry<img class="legend-node" src="' + imageUrl + "info-icon.PNG" + '" title="Related entries are from the same organism and have the same parent as the requested entry"><br>\
	</td></tr>\
	</table><br>\
	<h1>Edges:</h1>\
	<table class="legend-table">\
	<tr><td><img class="legend-edge" src="' + imageUrl + "edge-is_a.PNG" + '" alt="is_a"></td> <td><b>is_a</b></td> <td>child <i>is_a</i> parent</td></tr>\
	<tr><td><img class="legend-edge" src="' + imageUrl + "edge-is_a.PNG" + '" alt="derives_from"></td> <td><b>derives_from</b></td> <td>xxx <i>derives_from</i> xxx</td></tr>\
	<tr><td><img class="legend-edge" src="' + imageUrl + "edge-has_component.PNG" + '" alt="has_component"></td><td><b>has_component</b></td> <td>complex <i>has_component</i></td></tr>\
	</table>\
	';
	// <tr><td><img class="legend-edge" src="' + imageUrl + "edge-interaction.PNG" + '" alt="interaction"></td> <td><b>interaction (+i)</b></td> <td>A <i>interacted with</i> B</td></tr>\
	// <tr><td><img class="legend-edge" src="' + imageUrl + "edge-dissociation.PNG" + '" alt="dissociation"></td> <td><b>dissociation (-i)</b></td> <td>A <i>NOT interacted with</i> B</td></tr>\
	// <tr><td><img class="legend-edge" src="' + imageUrl + "edge-ptm.PNG" + '" alt="ptm"></td> <td><b>phosphorylation (+p)</b></td> <td>A <i>phosphorylated by</i> B</td></tr>\
	// <tr><td>	</td> <td><b>acetylation (+AC)</b></td> <td>A <i>acetylated by</i> B</td></tr>\
