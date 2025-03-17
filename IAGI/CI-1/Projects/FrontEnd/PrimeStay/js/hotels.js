document.addEventListener('DOMContentLoaded', function() {
    // Filter functionality
    initializeFilters();
    
    // Sort functionality
    initializeSort();
    
    // Favorite toggle
    initializeFavorites();
    
    // Price range slider
    initializePriceRange();
    
    // Load more hotels on scroll
    initializeInfiniteScroll();
});

function initializeFilters() {
    const filterInputs = document.querySelectorAll('.filters-sidebar input');
    filterInputs.forEach(input => {
        input.addEventListener('change', function() {
            applyFilters();
        });
    });
}

function initializeSort() {
    const sortSelect = document.querySelector('.sort-select');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            sortHotels(this.value);
        });
    }
}

function initializeFavorites() {
    const favButtons = document.querySelectorAll('.favorite-btn');
    favButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.toggle('active');
            const hotelId = this.closest('.hotel-card').dataset.hotelId;
            toggleFavorite(hotelId);
        });
    });
}

function initializePriceRange() {
    const rangeInput = document.querySelector('input[type="range"]');
    const priceInputs = document.querySelectorAll('.price-inputs input');
    
    if (rangeInput && priceInputs.length) {
        rangeInput.addEventListener('input', function() {
            updatePriceInputs(this.value);
        });
        
        priceInputs.forEach(input => {
            input.addEventListener('change', function() {
                updatePriceRange();
            });
        });
    }
}

function initializeInfiniteScroll() {
    let loading = false;
    window.addEventListener('scroll', function() {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 500) {
            if (!loading) {
                loading = true;
                loadMoreHotels().then(() => {
                    loading = false;
                });
            }
        }
    });
}

function applyFilters() {
    // Collect all filter values
    const filters = {
        priceRange: getPriceRange(),
        starRating: getSelectedStarRatings(),
        propertyType: getSelectedPropertyTypes(),
        amenities: getSelectedAmenities()
    };
    
    // Apply filters to hotel list
    filterHotels(filters);
}

function sortHotels(criterion) {
    const hotelsList = document.querySelector('.hotels-list');
    const hotels = Array.from(hotelsList.querySelectorAll('.hotel-card'));
    
    hotels.sort((a, b) => {
        switch(criterion) {
            case 'price-low':
                return getHotelPrice(a) - getHotelPrice(b);
            case 'price-high':
                return getHotelPrice(b) - getHotelPrice(a);
            case 'rating':
                return getHotelRating(b) - getHotelRating(a);
            default:
                return 0;
        }
    });
    
    // Re-append sorted hotels
    hotels.forEach(hotel => hotelsList.appendChild(hotel));
}

function toggleFavorite(hotelId) {
    // Get existing favorites from localStorage
    let favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    
    if (favorites.includes(hotelId)) {
        favorites = favorites.filter(id => id !== hotelId);
    } else {
        favorites.push(hotelId);
    }
    
    localStorage.setItem('favorites', JSON.stringify(favorites));
}

async function loadMoreHotels() {
    try {
        // Simulate API call
        const response = await fetch('/api/hotels?page=' + currentPage);
        const newHotels = await response.json();
        
        // Append new hotels to the list
        appendHotels(newHotels);
        currentPage++;
    } catch (error) {
        console.error('Error loading more hotels:', error);
    }
}