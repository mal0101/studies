document.addEventListener('DOMContentLoaded', function() {
    // Initialize profile navigation
    initializeProfileNav();
    
    // Initialize edit functionality
    initializeEditForms();
    
    // Initialize booking actions
    initializeBookingActions();
    
    // Initialize saved properties
    initializeSavedProperties();
});

function initializeProfileNav() {
    const navLinks = document.querySelectorAll('.profile-nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            loadSection(this.getAttribute('href'));
        });
    });
}

function initializeEditForms() {
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const section = this.closest('.profile-section');
            toggleEditMode(section);
        });
    });
}

function initializeBookingActions() {
    // Handle booking cancellations
    const cancelButtons = document.querySelectorAll('.action-btn[data-action="cancel"]');
    cancelButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (confirm('Are you sure you want to cancel this booking?')) {
                cancelBooking(this.closest('.booking-card').dataset.bookingId);
            }
        });
    });
}

function initializeSavedProperties() {
    const removeButtons = document.querySelectorAll('.remove-saved');
    removeButtons.forEach(button => {
        button.addEventListener('click', function() {
            removeSavedProperty(this.closest('.property-card').dataset.propertyId);
        });
    });
}

function toggleEditMode(section) {
    const isEditing = section.classList.toggle('editing');
    const fields = section.querySelectorAll('.info-item p');
    const button = section.querySelector('.edit-btn');
    
    if (isEditing) {
        fields.forEach(field => {
            const input = document.createElement('input');
            input.type = 'text';
            input.value = field.textContent;
            field.parentNode.replaceChild(input, field);
        });
        button.innerHTML = '<i class="fas fa-save"></i> Save';
    } else {
        saveChanges(section);
        button.innerHTML = '<i class="fas fa-pen"></i> Edit';
    }
}

async function saveChanges(section) {
    const inputs = section.querySelectorAll('input');
    const data = {};
    
    inputs.forEach(input => {
        data[input.getAttribute('name')] = input.value;
    });
    
    try {
        // Simulate API call
        await updateProfile(data);
        
        inputs.forEach(input => {
            const p = document.createElement('p');
            p.textContent = input.value;
            input.parentNode.replaceChild(p, input);
        });
    } catch (error) {
        console.error('Error saving changes:', error);
        alert('Failed to save changes. Please try again.');
    }
}

async function cancelBooking(bookingId) {
    try {
        // Simulate API call
        await fetch(`/api/bookings/${bookingId}/cancel`, { method: 'POST' });
        
        // Remove booking card from UI
        const bookingCard = document.querySelector(`[data-booking-id="${bookingId}"]`);
        bookingCard.remove();
    } catch (error) {
        console.error('Error canceling booking:', error);
        alert('Failed to cancel booking. Please try again.');
    }
}

async function removeSavedProperty(propertyId) {
    try {
        // Simulate API call
        await fetch(`/api/saved-properties/${propertyId}`, { method: 'DELETE' });
        
        // Remove property card from UI
        const propertyCard = document.querySelector(`[data-property-id="${propertyId}"]`);
        propertyCard.remove();
    } catch (error) {
        console.error('Error removing saved property:', error);
        alert('Failed to remove property. Please try again.');
    }
}

// Utility functions
function loadSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.profile-section').forEach(section => {
        section.style.display = 'none';
    });
    
    // Show selected section
    document.querySelector(sectionId).style.display = 'block';
}