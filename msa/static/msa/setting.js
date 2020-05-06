var iconPlus  = '<span class="glyphicon glyphicon-zoom-in icon-view" onclick="msa_view_switch_click(); event.stopPropagation();" title="show detail view"></span>';
var iconMinus  = '<span class="glyphicon glyphicon-zoom-out icon-view" onclick="msa_view_switch_click(); event.stopPropagation();" title="show overview"></span>';
var daglogo = '<img id="iconDAG" class="icon-link" src="app/static/pro/pirwww/images/hierarchy.png" alt="DAG" title="DAG View">';

var prourl = '/app/entry/';
var cytourl = '/app/visual/cytoscape/pro/';
var dagurl = '/cgi-bin/browser_pro?ids=';

var msaModTypeDict = {"mod-p":"Phosphorylation","mod-ac":"Acetylation","mod-g":"Glycosylation","mod-m":"Methylation","mod-ub":"Ubiquitination","mod-o":"Other"};

var emptyEntryLine = '<tr class="msa-divider"><td class="msa-empty"> </td><td class="msa-empty"></td></tr>';
