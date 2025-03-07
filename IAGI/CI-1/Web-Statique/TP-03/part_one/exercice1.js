function validateForm(event) {
    event.preventDefault();
    
    const dateNaissance = new Date(document.getElementById('date_naissance').value);
    const today = new Date();
    const age = today.getFullYear() - dateNaissance.getFullYear();
    const monthDifference = today.getMonth() - dateNaissance.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < dateNaissance.getDate())) {
        age--;
    }

    if (age < 14) {
        alert("Vous devez avoir plus de 14 ans.");
        return false;
    }

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        alert("Les mots de passe ne correspondent pas.");
        return false;
    }

    alert("Formulaire validé avec succès!");
    return true;
}