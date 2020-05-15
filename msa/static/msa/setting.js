var iconPlus  = '<span class="glyphicon glyphicon-zoom-in icon-view" onclick="msa_view_switch_click(); event.stopPropagation();" title="show detail view"></span>';
var iconMinus  = '<span class="glyphicon glyphicon-zoom-out icon-view" onclick="msa_view_switch_click(); event.stopPropagation();" title="show overview"></span>';
// var prologo =  '<img id="iconPRO" class="icon-link" src="http://pir.georgetown.edu/pirwww/images/pirlogo3.gif" alt="PRO" title="PRO Entry Report">';
//var prologo =  '<img id="iconPRO" class="icon-link" src=images+"PRO.gif" alt="PRO" title="PRO Entry Report">';
//// var cytologo = '<img id="iconCyto" class="icon-link" src="http://pir.georgetown.edu/pirwww/images/cyto-logo-smaller.gif" alt="Cyto" title="Cytoscape View">';
//var cytologo = '<img id="iconCyto" class="icon-link" src=images+"cyto-logo.gif" alt="Cyto" title="Cytoscape View">';
var daglogo = '<img id="iconDAG" class="icon-link" src="http://pir.georgetown.edu/pirwww/images/hierarchy.png" alt="DAG" title="DAG View">';
//var blanklogo = '<img id="iconBlank" class="icon-link" src=images+"icon-blank.gif">';
//
//var iptmnetlogo = '<img id="iconiPtm" class="icon-link" src=images+"iptmnet-logo.gif" alt="iPTMnet" title="iPTMnet Entry Report">';

var prourl = 'http://research.bioinformatics.udel.edu/pro/entry/';
var cytourl = 'http://research.bioinformatics.udel.edu/pro/visual/cytoscape/pro/';
var dagurl = 'http://pir.georgetown.edu/cgi-bin/pro/browser_pro?ids=';

var msaModTypeDict = {"mod-p":"Phosphorylation","mod-ac":"Acetylation","mod-g":"Glycosylation","mod-m":"Methylation","mod-ub":"Ubiquitination","mod-o":"Other"};

var emptyEntryLine = '<tr class="msa-divider"><td class="msa-empty"> </td><td class="msa-empty"></td></tr>';
