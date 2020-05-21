$(function(){
    form_setup();
});

function forms_bootstarp_label(obj) {
    var complex = obj.complex_count > 0 ? '<span class="label label-success">' +
        '<a href="#complex-'+obj.id+'" title="complex" class="form-tag">'+obj.complex_count+'</a></span>' : '',
        paf = obj.paf_count > 0 ? '<span class="label label-warning">' +
        '<a href="#paf-'+obj.id+'" title="annotation" class="form-tag">' + obj.paf_count+'</a></span>' : '';

    return '&nbsp;&nbsp;&nbsp;' + complex +'&nbsp;'+ paf;
}