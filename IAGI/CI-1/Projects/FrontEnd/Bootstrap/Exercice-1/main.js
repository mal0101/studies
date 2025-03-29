let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

function showSlide(n) {
    slides[currentSlide].classList.remove('active');
    dots[currentSlide].classList.remove('active');
    
    currentSlide = (n + slides.length) % slides.length;
    
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
}

function autoAdvance() {
    showSlide(currentSlide + 1);
}

setInterval(autoAdvance, 5000);

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => showSlide(index));
});

showSlide(0);