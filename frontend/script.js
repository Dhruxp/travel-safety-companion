async function evaluateRoute() {
  const context = document.getElementById("context").value;

  const payload = {
    place: "Bengaluru, India",
    origin: [12.9716, 77.5946],
    destination: [12.9784, 77.6408],
    context: context,
    k: 3
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/evaluate-route", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    displayResults(data);

  } catch (error) {
    console.error("Error calling API:", error);
    alert("Failed to fetch route safety data.");
  }
}

function displayResults(data) {
  const resultsDiv = document.getElementById("results");

  const explanations = data.best_route.explanation
    .map(e => `<li>${e}</li>`)
    .join("");

  resultsDiv.innerHTML = `
    <h3>✅ Safest Route</h3>
    <p><strong>Risk Score:</strong> ${data.best_route.risk_score}</p>
    <ul>${explanations}</ul>
  `;
}
