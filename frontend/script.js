fetch("http://127.0.0.1:5000/api/hello")
  .then(res => res.json())
  .then(data => {
    document.getElementById("api-response").textContent = data.message;
  })
  .catch(err => {
    console.error("API error:", err);
  });
