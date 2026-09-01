document.getElementById("corsa-content").style.display = "none";
document.getElementById("palestra-content").style.display = "none";
document.getElementById("profilo").style.display = "none";

const corsaBtn = document.getElementById("corsa-btn");
const palestraBtn = document.getElementById("palestra-btn");
const profiloBtn = document.getElementById("profilo-btn");

corsaBtn.addEventListener("click", () => {
  document.getElementById("corsa-content").style.display = "block";
  document.getElementById("palestra-content").style.display = "none";
  document.getElementById("profilo").style.display = "none";
});

palestraBtn.addEventListener("click", () => {
  document.getElementById("corsa-content").style.display = "none";
  document.getElementById("palestra-content").style.display = "block";
  document.getElementById("profilo").style.display = "none";
});

profiloBtn.addEventListener("click", () => {
  document.getElementById("corsa-content").style.display = "none";
  document.getElementById("palestra-content").style.display = "none";
  document.getElementById("profilo").style.display = "block";
});

// Funzione per caricare gli allenamenti dal server
async function caricaWorkouts() {
  const response = await fetch("/api/workouts");
  const data = await response.json();
  mostraWorkouts(data);
}

// Funzione per mostrare gli allenamenti nella pagina
async function mostraWorkouts(data) {
  const corsaContainer = document.getElementById("corsa-content");
  const palestraContainer = document.getElementById("palestra-content");
  const allenamentiCorsa = data.filter(
    (elemento) => elemento.categoria === "corsa",
  );
  const allenamentiPalestra = data.filter(
    (elemento) => elemento.categoria === "palestra",
  );

  // Ordina gli allenamenti per data in ordine decrescente
  allenamentiCorsa.sort((a, b) => new Date(b.data) - new Date(a.data));
  allenamentiPalestra.sort((a, b) => new Date(b.data) - new Date(a.data));

  // Mostra gli allenamenti di corsa
  const htmlCorsa = allenamentiCorsa
    .map(
      (w) => `
  <p>${w.data} - ${w.tipo_corsa} - ${w.distanza_km} km</p>
`,
    )
    .join("");
  corsaContainer.innerHTML = htmlCorsa;

  // Mostra gli allenamenti di palestra
  const htmlPalestra = allenamentiPalestra
    .map(
      (w) => `
  <p>${w.data} - ${w.esercizio} - ${w.serie} serie - ${w.ripetizioni} rep - ${w.peso} kg</p>
`,
    )
    .join("");
  palestraContainer.innerHTML = htmlPalestra;
}

caricaWorkouts();
