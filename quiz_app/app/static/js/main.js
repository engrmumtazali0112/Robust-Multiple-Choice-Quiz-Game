/**
 * Main JavaScript file for the Quiz Application
 * Handles common functionality across pages
 */

// Check if an element exists in the DOM
function elementExists(selector) {
  return document.querySelector(selector) !== null;
}

// Format a message with a proper icon
function formatMessage(message, type = 'info') {
  const icons = {
    'success': '✓',
    'error': '✗',
    'info': 'ℹ️',
    'warning': '⚠️'
  };
  const icon = icons[type] || icons.info;
  return `${icon} ${message}`;
}

// Show a notification message
function showNotification(message, type = 'info', duration = 3000) {
  // Check if notification container exists, if not create it
  let notificationContainer = document.getElementById('notification-container');
  
  if (!notificationContainer) {
    notificationContainer = document.createElement('div');
    notificationContainer.id = 'notification-container';
    notificationContainer.style.position = 'fixed';
    notificationContainer.style.top = '20px';
    notificationContainer.style.right = '20px';
    notificationContainer.style.zIndex = '1000';
    document.body.appendChild(notificationContainer);
  }
  
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = formatMessage(message, type);
  
  // Style the notification
  notification.style.backgroundColor = 
    type === 'success' ? '#2ecc71' : 
    type === 'error' ? '#e74c3c' : 
    type === 'warning' ? '#f39c12' : '#3498db';
  notification.style.color = 'white';
  notification.style.padding = '12px 20px';
  notification.style.marginBottom = '10px';
  notification.style.borderRadius = '5px';
  notification.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
  notification.style.transition = 'all 0.5s ease';
  notification.style.opacity = '0';
  
  // Add to container
  notificationContainer.appendChild(notification);
  
  // Fade in
  setTimeout(() => {
    notification.style.opacity = '1';
  }, 10);
  
  // Remove after duration
  setTimeout(() => {
    notification.style.opacity = '0';
    setTimeout(() => {
      notificationContainer.removeChild(notification);
    }, 500);
  }, duration);
}

// Handle form validation
function validateForm(formElement) {
  const inputs = formElement.querySelectorAll('input, select, textarea');
  let isValid = true;
  
  inputs.forEach(input => {
    if (input.hasAttribute('required') && !input.value.trim()) {
      isValid = false;
      input.classList.add('error');
      
      // Add error message if it doesn't exist
      const errorId = `${input.id}-error`;
      if (!document.getElementById(errorId)) {
        const errorMsg = document.createElement('div');
        errorMsg.id = errorId;
        errorMsg.className = 'error-message';
        errorMsg.textContent = 'This field is required';
        errorMsg.style.color = '#e74c3c';
        errorMsg.style.fontSize = '0.8rem';
        errorMsg.style.marginTop = '5px';
        input.parentNode.appendChild(errorMsg);
      }
    } else {
      input.classList.remove('error');
      const errorId = `${input.id}-error`;
      const errorMsg = document.getElementById(errorId);
      if (errorMsg) {
        errorMsg.parentNode.removeChild(errorMsg);
      }
    }
  });
  
  return isValid;
}

// Initialize common events
document.addEventListener('DOMContentLoaded', function() {
  // Add validation to all forms
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
      if (!validateForm(form)) {
        e.preventDefault();
        showNotification('Please fill in all required fields', 'error');
      }
    });
  });
  
  // Remove error styling on input
  document.querySelectorAll('input, select, textarea').forEach(input => {
    input.addEventListener('input', function() {
      this.classList.remove('error');
      const errorId = `${this.id}-error`;
      const errorMsg = document.getElementById(errorId);
      if (errorMsg) {
        errorMsg.parentNode.removeChild(errorMsg);
      }
    });
  });
});

// Utility function to shuffle an array
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// Utility function to format time (used for timers)
function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}