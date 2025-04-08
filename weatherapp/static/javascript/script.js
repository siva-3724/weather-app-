document.getElementById('weatherForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const city = document.getElementById('cityInput').value;
    fetch('/weather', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `city=${city}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerHTML = `<div class="text-danger">${data.error}</div>`;
        } else {
            document.getElementById('result').innerHTML = `
                <div class="text-dark">
                    <strong>City:</strong> ${data.city}<br>
                    <strong>Temperature:</strong> ${data.temperature} °C<br>
                    <strong>Humidity:</strong> ${data.humidity}%<br>
                    <strong>Condition:</strong> ${data.description}
                </div>
            `;
        }
    });
});
