// Main JavaScript for BMS Bites

// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

// Live order status updates
function updateOrderStatus(orderId) {
    fetch(`/api/order/${orderId}/status`)
        .then(response => response.json())
        .then(data => {
            if (data.status) {
                const statusBadge = document.querySelector(`#order-${orderId}-status`);
                if (statusBadge) {
                    statusBadge.textContent = data.status.toUpperCase();
                    statusBadge.className = `badge bg-${data.status === 'kitchen' ? 'warning' :
                            data.status === 'prepared' ? 'info' :
                                'success'
                        }`;
                }
            }
        })
        .catch(error => console.error('Error fetching order status:', error));
}

// Poll for order status updates every 10 seconds on order detail page
if (window.location.pathname.includes('/order/')) {
    const orderId = window.location.pathname.split('/').pop();
    setInterval(() => updateOrderStatus(orderId), 10000);
}

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Add to cart animation
document.querySelectorAll('form[action*="add_to_cart"]').forEach(form => {
    form.addEventListener('submit', function (e) {
        const btn = this.querySelector('button[type="submit"]');
        btn.innerHTML = '<span class="loading"></span> Adding...';
        btn.disabled = true;
    });
});

console.log('BMS Bites - Ready to serve! 🍔');
