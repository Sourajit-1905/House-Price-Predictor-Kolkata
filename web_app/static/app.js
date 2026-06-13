document.addEventListener("DOMContentLoaded", () => {
    
    const form = document.getElementById("prediction-form");
    const resultSection = document.getElementById("result-section");
    const priceOutput = document.getElementById("price-output");
    const submitBtn = document.querySelector(".predict-btn");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const sqft = document.getElementById("sqft").value;
        const bhk = document.getElementById("bhk").value;
        const location = document.getElementById("location").value;

        const originalBtnText = submitBtn.innerText;
        submitBtn.innerText = "PROCESSING MATRIX MODEL...";
        submitBtn.disabled = true;

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    total_sqft: parseFloat(sqft),
                    bhk: parseInt(bhk),
                    location: location
                }),
            });

            const data = await response.json();

            if (response.ok) {
               
                priceOutput.innerText = `₹ ${data.estimated_price_crores.toFixed(2)} Cr`;
                resultSection.classList.remove("hidden");
            } else {
                priceOutput.innerText = "Execution Failure.";
                resultSection.classList.remove("hidden");
            }

        } catch (error) {
            console.error("Transmission Error:", error);
            priceOutput.innerText = "Server Unreachable.";
            resultSection.classList.remove("hidden");
        } finally {
            submitBtn.innerText = originalBtnText;
            submitBtn.disabled = false;
        }
    });
});
document.addEventListener("DOMContentLoaded", async () => {

    const locationSelect = document.getElementById("location");

    try {
        const locResponse = await fetch("/get_locations");
        const locData = await locResponse.json();

        if (locResponse.ok && locData.status === 'success') {
            locationSelect.innerHTML = '<option value="" disabled selected>Select location...</option>';

            locData.locations.forEach(loc => {
                const option = document.createElement("option");
                option.value = loc;
                option.textContent = loc;
                locationSelect.appendChild(option);
            });
        } else {
            console.error("Failed to load locations:", locData.error);
            locationSelect.innerHTML = '<option value="" disabled selected>Error loading locations</option>';
        }
    } catch (error) {
        console.error("Network Error fetching locations:", error);
        locationSelect.innerHTML = '<option value="" disabled selected>Server Offline</option>';
    }

    const form = document.getElementById("prediction-form");
    const resultSection = document.getElementById("result-section");
    const priceOutput = document.getElementById("price-output");
    const submitBtn = document.querySelector(".predict-btn");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const sqft = document.getElementById("sqft").value;
        const bhk = document.getElementById("bhk").value;
        const location = document.getElementById("location").value;

        const originalBtnText = submitBtn.innerText;
        submitBtn.innerText = "PROCESSING MATRIX MODEL...";
        submitBtn.disabled = true;

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    total_sqft: parseFloat(sqft),
                    bhk: parseInt(bhk),
                    location: location
                }),
            });

            const data = await response.json();

            if (response.ok) {
                priceOutput.innerText = `₹ ${data.estimated_price_crores.toFixed(2)} Cr`;
                resultSection.classList.remove("hidden");
            } else {
                priceOutput.innerText = "Execution Failure.";
                resultSection.classList.remove("hidden");
            }

        } catch (error) {
            console.error("Transmission Error:", error);
            priceOutput.innerText = "Server Unreachable.";
            resultSection.classList.remove("hidden");
        } finally {
            submitBtn.innerText = originalBtnText;
            submitBtn.disabled = false;
        }
    });
});