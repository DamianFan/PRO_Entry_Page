function setActiveStyleSheet(changeType,sTitle) {
	var i, a, main;
	var title, sTitle;
	
	if (changeType==0) 
	
	{	sTitle=getActiveStyleSheet();
		if (sTitle=="Preferred")
			{
			title="Alternative";
			myleftnav_Img1.src = "images/SizeTextRnd_f2.gif";
			myleftnav_Img1.alt = "decrease font size"; 
			}
		else
		{title="Preferred";
		myleftnav_Img1.src = "images/SizeTextRnd.gif";
		myleftnav_Img1.alt = "increase font size";
		}
	}
	if (changeType==1)
	{
		title=sTitle;
		

	}
	for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
		if(a.getAttribute("rel").indexOf("style") !=-1 && a.getAttribute("title"))
		{
		a.disabled = true;
		
		if (a.getAttribute("title")==title) a.disabled=false;
		}
		}
		
	}
	function getActiveStyleSheet() {
  var i, a;
  for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("title") && !a.disabled) return a.getAttribute("title");
  }
  return null;
}	
function createCookie(name,value,days) {
  if (days) {
    var date = new Date();
    date.setTime(date.getTime()+(days*24*60*60*1000));
    var expires = "; expires="+date.toGMTString();
  }
  else expires = "";
  document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1,c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

window.onload = function(e) {
  var cookie = readCookie("style");
  var title = cookie ? cookie : getPreferredStyleSheet();
  setActiveStyleSheet(1,title);
}

window.onunload = function(e) {
  var title = getActiveStyleSheet();
  createCookie("style", title, 365);
}

var cookie = readCookie("style");
var title = cookie ? cookie : getPreferredStyleSheet();
setActiveStyleSheet(1,title);