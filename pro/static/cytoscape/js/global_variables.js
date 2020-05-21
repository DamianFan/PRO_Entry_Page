var obourl = 'http://proconsortium.org/cgi-bin/entry_pro?stanza_id=';
var pafurl = 'http://proconsortium.org/cgi-bin/batch_pro?PAF=SEL&opt_dsp_list2=PRO_NAME_TXT,PRO_DEF_TXT,CATEGORY,PARENT&page=1&db=&idlist=';
var prourl = '/pro2/entry/';
var uniurl = 'http://www.uniprot.org/uniprot/';
var dagurl = 'http://proconsortium.org/cgi-bin/browser_pro?ids=';

var C2L= {'family':'3','gene':'5','organism-gene':'6','sequence':'7','organism-sequence':'8','modification':'9','organism-modification':'10','complex':'11','organism-complex':'12'};
var L2C = {'3':'family', '5':'gene','6':'organism-gene','7':'sequence','8':'organism-sequence','9':'modification','10':'organism-modification','11':'complex','12':'organism-complex'};

var nodeProp = ["ID","Label","Name","Def","Category"];
var nodeNonProp = ["id","Level","Group","Shape","ptm"];
var edgeProp = ["ID","Interaction","Source"];
var edgeNonProp = ["id","target","source"];

var errorInvalidUniprot="Please enter a valid UniProtKB AC (6 alphanumerical characters)";
var errorInvalidGo="Please enter a valid GO ID: \"GO:xxxxxxx\"(7 digits): ";
var errorInvalidPro="Please enter a valid PRO ID: \"PR:xxxxxxxxx\"(9 digits): ";
var errorInvalidChebi="Please enter a valid CHEBI ID: \"CHEBI:xxxxx\"(5 digits): ";
var errorId="Please enter a valid ID";
var errorExcessNodes1="Current Network has too many nodes ("
var errorExcessNodes2="), labels are hidden automatically. To turn on node label, check corresponded checkbox in \"Display Options\"."
