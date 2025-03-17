document.addEventListener('DOMContentLoaded', function() {
    // Initialize image gallery
    initializeGallery();
    
    // Initialize date picker
    initializeDatePicker();
    
    // Initialize room selection
    initializeRoomSelection();
    
    // Initialize booking functionality
    initializeBooking();
});

function initializeGallery() {
    const mainImage = document.querySelector('.gallery-main img');
    const thumbnails = document.querySelectorAll('.gallery-thumbs img');
    
    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', function() {
            mainImage.src = this.src;
            thumbnails.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Image modal functionality
    const viewAllBtn = document.querySelector('.view-all-photos');
    if (viewAllBtn) {
        viewAllBtn.addEventListener('click', openGalleryModal);
    }
}

function initializeDatePicker() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        input.addEventListener('change', function() {
            updatePricing();
        });
    });
}

function initializeRoomSelection() {
    const roomOptions = document.querySelectorAll('.room-option');
    roomOptions.forEach(option => {
        option.addEventListener('click', function() {
            roomOptions.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
            updatePricing();
        });
    });
}

function initializeBooking() {
    const bookingForm = document.querySelector('.booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            processBooking();
        });
    }
}

function updatePricing() {
    const checkIn = new Date(document.getElementById('check-in').value);
    const checkOut = new Date(document.getElementById('check-out').value);
    const selectedRoom = document.querySelector('.room-option.selected');
    
    if (checkIn && checkOut && selectedRoom) {
        const nights = (checkOut - checkIn) / (1000 * 60 * 60 * 24);
        const pricePerNight = parseFloat(selectedRoom.dataset.price);
        const totalPrice = nights * pricePerNight;
        
        updatePriceSummary(totalPrice, nights);
    }
}

function updatePriceSummary(total, nights) {
    const summary = document.querySelector('.price-summary');
    if (summary) {
        summary.innerHTML = `
            <div class="price-row">
                <span>${nights} nights</span>
                <span>$${total.toFixed(2)}</span>
            </div>
            <div class="price-row">
                <span>Taxes and fees</span>
                <span>$${(total * 0.12).toFixed(2)}</span>
            </div>
            <div class="price-total">
                <span>Total</span>
                <span>$${(total * 1.12).toFixed(2)}</span>
            </div>
        `;
    }
}

async function processBooking() {
    try {
        const bookingData = {
            checkIn: document.getElementById('check-in').value,
            checkOut: document.getElementById('check-out').value,
            roomType: document.querySelector('.room-option.selected').dataset.roomType,
            guests: document.getElementById('guests').value
        };
        
        // Redirect to booking page with data
        window.location.href = `booking.html?${new URLSearchParams(bookingData)}`;
    } catch (error) {
        console.error('Error processing booking:', error);
        alert('There was an error processing your booking. Please try again.');
    }
}