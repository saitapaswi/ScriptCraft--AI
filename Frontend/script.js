const API = "http://localhost:5000";

async function generate() {
  const topic = document.getElementById("topic").value;
  const type = document.getElementById("type").value;
  const tone = document.getElementById("tone").value;

  const res = await fetch(API + "/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      topic,
      type,
      tone
    })
  });

  const data = await res.json();

  document.getElementById("output").innerText = data.content;
}