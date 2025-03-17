document.addEventListener('DOMContentLoaded', function() {
    // Date handling for search form
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);
    const dayAfter = new Date(today);
    dayAfter.setDate(dayAfter.getDate() + 2);

    // Guest selector functionality
    const guestSelector = document.querySelector('.guest-selector');
    if (guestSelector) {
        guestSelector.addEventListener('click', function() {
            // Toggle guest selection dropdown
            const dropdown = this.querySelector('.dropdown-content');
            if (dropdown) {
                dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
            }
        });
    }

    // Search form submission
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Collect form data
            const formData = new FormData(this);
            const searchData = {
                location: formData.get('location'),
                checkIn: formData.get('check-in'),
                checkOut: formData.get('check-out'),
                guests: formData.get('guests')
            };
            
            // Redirect to hotels page with search parameters
            window.location.href = `hotels.html?${new URLSearchParams(searchData)}`;
        });
    }

    // Property type card hover effects
    const propertyCards = document.querySelectorAll('.type-card');
    propertyCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Currency selector
    const currencySelect = document.querySelector('.currency-select');
    if (currencySelect) {
        currencySelect.addEventListener('change', function() {
            // Update currency throughout the page
            updateCurrency(this.value);
        });
    }
});

function updateCurrency(currency) {
    // Update prices throughout the page based on selected currency
    const exchangeRates = {
        USD: 1,
        EUR: 0.85,
        GBP: 0.73
    };
    
    const priceElements = document.querySelectorAll('.price');
    priceElements.forEach(element => {
        const basePrice = parseFloat(element.getAttribute('data-base-price'));
        const newPrice = basePrice * exchangeRates[currency];
        element.textContent = `${currency} ${newPrice.toFixed(2)}`;
    });
}