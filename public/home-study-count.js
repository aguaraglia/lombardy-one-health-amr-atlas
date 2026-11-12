/* Home-page KPI: studies on the map, from the literature catalog.
   Load after atlas-core.js. The evidence register must not overwrite this number. */
(function () {
  "use strict";
  const config = window.AMR_ATLAS_CONFIG || {};
  const node = document.getElementById("overview-evidence");
  if (!node) return;
  const caption = node.nextElementSibling;
  if (caption) caption.textContent = config.overviewLiteratureLabel || "studi sulla mappa";
  const path = (config.catalogs && config.catalogs.literature) || "public/data/literature-catalog.json";
  const url = window.amrAsset ? window.amrAsset(path) : path;
  const locale = document.documentElement.lang === "en" ? "en-GB" : "it-IT";
  let formatted = "";
  let writing = false;
  const write = (text) => {
    if (node.textContent === text) return;
    writing = true;
    node.textContent = text;
    writing = false;
  };
  new MutationObserver(() => {
    if (!writing && formatted && node.textContent !== formatted) write(formatted);
  }).observe(node, { childList: true, characterData: true, subtree: true });
  fetch(url, { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error(String(response.status));
      return response.json();
    })
    .then((catalog) => {
      const records = Array.isArray(catalog.records) ? catalog.records : [];
      formatted = records.length.toLocaleString(locale);
      write(formatted);
    })
    .catch((error) => {
      console.warn("[AMR Atlas] Study count unavailable", error);
    });
})();
