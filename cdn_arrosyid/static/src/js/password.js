function isValidPassword(password) {
    // Kriteria minimal password
    var minLength = 8;
    
    // Regex untuk memeriksa apakah password mengandung angka
    var hasNumber = /\d/;
    // Regex untuk memeriksa apakah password mengandung huruf besar
    var hasUpperCase = /[A-Z]/;
    // Regex untuk memeriksa apakah password mengandung huruf kecil
    var hasLowerCase = /[a-z]/;
    // Regex untuk memeriksa apakah password mengandung karakter khusus
    var hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/;

    // Memeriksa panjang password
    if (password.length < minLength) {
        return false;
    }

    // Memeriksa keberadaan angka, huruf besar, huruf kecil, dan karakter khusus
    if (!hasNumber.test(password) ||
        !hasUpperCase.test(password) ||
        !hasLowerCase.test(password)) {
        return false;
    }

    return true;
}