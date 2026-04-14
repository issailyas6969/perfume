// shopify-integration.js

// Assuming `fetch` and `Shopify` are available globally.

const SHOPIFY_API_URL = 'https://your-shopify-store.myshopify.com/admin/api/2021-07/products.json';
const CHECKOUT_API_URL = 'https://your-shopify-store.myshopify.com/admin/api/2021-07/checkouts.json';

// Function to fetch products from Shopify
async function fetchProducts() {
    try {
        const response = await fetch(SHOPIFY_API_URL, {
            method: 'GET',
            headers: {
                'X-Shopify-Access-Token': 'your-access-token',
                'Content-Type': 'application/json',
            },
        });
        const data = await response.json();
        return data.products;
    } catch (error) {
        console.error('Error fetching products:', error);
        return []; // Return empty array on error
    }
}

// Function to create a checkout session
async function createCheckout(lineItems) {
    try {
        const response = await fetch(CHECKOUT_API_URL, {
            method: 'POST',
            headers: {
                'X-Shopify-Access-Token': 'your-access-token',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ checkout: { line_items: lineItems } }),
        });
        const data = await response.json();
        return data.checkout;
    } catch (error) {
        console.error('Error creating checkout:', error);
        return null; // Return null on error
    }
}

export { fetchProducts, createCheckout };