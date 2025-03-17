document.addEventListener('DOMContentLoaded', function() {
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize payment processing
    initializePayment();
    
    // Update booking summary
    updateBookingSummary();
    
    // Handle step navigation
    initializeStepNavigation();
});

function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            if (validateForm(this)) {
                processNextStep();
            }
        });
    });
}

function initializePayment() {
    // Initialize card input formatting
    const cardNumber = document.getElementById('cardNumber');
    if (cardNumber) {
        cardNumber.addEventListener('input', function() {
            this.value = formatCardNumber(this.value);
        });
    }
    
    const expiryDate = document.getElementById('expiry');
    if (expiryDate) {
        expiryDate.addEventListener('input', function() {
            this.value = formatExpiryDate(this.value);
        });
    }
}

function initializeStepNavigation() {
    const steps = document.querySelectorAll('.step');
    steps.forEach((step, index) => {
        step.addEventListener('click', function() {
            if (this.classList.contains('completed')) {
                goToStep(index);
            }
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required]');
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            showError(input, 'This field is required');
        } else {
            clearError(input);
        }
    });
    
    return isValid;
}

function processNextStep() {
    const currentStep = document.querySelector('.step.active');
    const nextStep = currentStep.nextElementSibling;
    
    if (nextStep) {
        currentStep.classList.remove('active');
        currentStep.classList.add('completed');
        nextStep.classList.add('active');
        showStepContent(nextStep.dataset.step);
    } else {
        completeBooking();
    }
}

function completeBooking() {
    // Simulate booking API call
    showLoadingSpinner();
    
    setTimeout(() => {
        hideLoadingSpinner();
        showConfirmation();
    }, 2000);
}

// Utility functions
function formatCardNumber(value) {
    return value.replace(/\s/g, '')
                .replace(/(\d{4})/g, '$1 ')
                .trim();
}

function formatExpiryDate(value) {
    return value.replace(/\D/g, '')
                .replace(/(\d{2})(\d)/, '$1/$2');
}

function showError(input, message) {
    const errorDiv = input.parentElement.querySelector('.error-message') 
        || document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    input.parentElement.appendChild(errorDiv);
    input.classList.add('error');
}

function clearError(input) {
    const errorDiv = input.parentElement.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
    input.classList.remove('error');
}