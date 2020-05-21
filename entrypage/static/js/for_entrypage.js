var msav=document.getElementById('msa');
$(document).ready(function () {
    $('#tg_msa').click(function () {
        if (document.getElementById("tg_msa").checked){
            msav.style.display="block";
            msav.scrollIntoView(true);
        }
        else{
            msav.style.display="none";
        }
    })

});


var funano=document.getElementById('functional-annotation');
$(document).ready(function () {
    $('#tg_annotation').click(function () {
        if (document.getElementById("tg_annotation").checked){
            funano.style.display="block";
            funano.scrollIntoView(true);
        }
        else{
            funano.style.display="none";
        }
    })

});