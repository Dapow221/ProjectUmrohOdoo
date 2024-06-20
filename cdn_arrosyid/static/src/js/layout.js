document.addEventListener('DOMContentLoaded', function() {
    var copyrightElement = document.querySelector('.o_footer_copyright');
    if (copyrightElement) {
        copyrightElement.style.backgroundColor = '#03172c';
    }
});

    // Ambil semua tautan dengan kelas "nav-link"
    var links = document.querySelectorAll('.nav-link');

    // Loop melalui setiap tautan
    links.forEach(function(link) {
        // Tambahkan event listener untuk setiap tautan
        link.addEventListener('click', function() {
            // Hilangkan kelas "active" dari semua tautan
            links.forEach(function(link) {
                link.classList.remove('active');
            });
            // Tambahkan kelas "active" ke tautan yang diklik
            this.classList.add('active');
        });
        // Periksa apakah href tautan sesuai dengan URL saat ini
        if (window.location.pathname === link.getAttribute('href')) {
            // Tambahkan kelas "active" jika sesuai
            link.classList.add('active');
        }
    });

    $('div.container.mb64').removeClass('container').addClass('container-fluid');
    $('div[class="col-12 col-md col-lg-6"]').removeClass('col-lg-6').addClass('col-lg-9');