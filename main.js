// Scroll to form on clicking the "Get Started" button
function scrollToForm() {
    document.getElementById("form-section").scrollIntoView({ behavior: 'smooth' });
}

// Example form submission logic
document.getElementById("gift-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const eventType = document.getElementById("event-type").value;
    const priceRange = document.getElementById("price-range").value;
    alert(`Searching for gifts for a ${eventType} event in the price range: ${priceRange}`);
});
