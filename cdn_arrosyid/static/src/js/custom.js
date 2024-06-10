$(document).ready(function(){
	$('.btn-delete-pendaftaran').click(function(){
		var pendaftaran = $(this).data('pendaftaran-number');
		alert('Apakah ada yakin dihapus? ' + pendaftaran);
	});
});