//------------- tables-data.js -------------//
$(document).ready(function() {

	

	//------------- Data tables -------------//
	//basic datatables
	$('#basic-datatables').dataTable({
		"oLanguage": {
		    "sSearch": "",
		    "sLengthMenu": "<span>_MENU_</span>"
		},
		"sDom": "<'row'<'col-md-6 col-xs-12 'l><'col-md-6 col-xs-12'f>r>t<'row'<'col-md-4 col-xs-12'i><'col-md-8 col-xs-12'p>>"
	});

	//vertical scroll
	$('#vertical-scroll-datatables').dataTable( {
		"scrollY":        "200px",
		"scrollCollapse": true,
		"paging":         false
	});

	//responsive datatables
	$('#responsive-datatables').dataTable({
		"oLanguage": {
		    "sSearch": "",
		    "sLengthMenu": "<span>_MENU_</span>"
		},
		"sDom": "<'row'<'col-md-6 col-xs-12 'l><'col-md-6 col-xs-12'f>r>t<'row'<'col-md-4 col-xs-12'i><'col-md-8 col-xs-12'p>>"
	});

	//with tabletools
	$('#tabletools').DataTable( {
		"oLanguage": {
		    "sSearch": "",
		    "sLengthMenu": "<span>_MENU_</span>"
		},
		"sDom": "T<'row'<'col-md-6 col-xs-12 'l><'col-md-6 col-xs-12'f>r>t<'row'<'col-md-4 col-xs-12'i><'col-md-8 col-xs-12'p>>",
		tableTools: {
			"sSwfPath": "http://cdn.datatables.net/tabletools/2.2.2/swf/copy_csv_xls_pdf.swf",
			"aButtons": [ 
		      "copy", 
		      "csv", 
		      "xls",
		      "print",
		      "select_all", 
		      "select_none" 
		  ]
		}
	});
	
});