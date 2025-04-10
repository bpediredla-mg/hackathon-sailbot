document.getElementById("qa-form").addEventListener("submit", async function(e) {
  e.preventDefault();
  const question = document.getElementById("question").value;
  const model = document.getElementById("model").value;
  const answerBox = document.getElementById("answer-box");
  answerBox.innerHTML = "Thinking...";

  try {
    const response = await fetch("http://localhost:5000/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, model })
    });
    const data = await response.json();
    answerBox.innerHTML = "<strong>Answer:</strong> " + (data.answer || data.error);
  } catch (err) {
    console.error(err);
    answerBox.innerHTML = "Failed to fetch answer.";
  }
});
