async function saveFileFromLink(link) {
  const filename = link.dataset.downloadFilename || link.dataset.dotfileDownload;
  const source = link.getAttribute("href");

  if (!filename || !source) {
    return;
  }

  const response = await fetch(source, { cache: "no-store" });

  if (!response.ok) {
    throw new Error(`Failed to fetch ${source}: ${response.status}`);
  }

  const content = await response.text();

  if (window.showSaveFilePicker) {
    const handle = await window.showSaveFilePicker({
      suggestedName: filename
    });
    const writable = await handle.createWritable();
    await writable.write(content);
    await writable.close();
    return;
  }

  const blob = new Blob([content], { type: "application/octet-stream" });
  const blobUrl = URL.createObjectURL(blob);
  const anchor = document.createElement("a");

  anchor.href = blobUrl;
  anchor.download = filename;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();

  window.setTimeout(() => URL.revokeObjectURL(blobUrl), 1000);
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-download-filename], [data-dotfile-download]").forEach((link) => {
    link.addEventListener("click", async (event) => {
      event.preventDefault();

      try {
        await saveFileFromLink(link);
      } catch (error) {
        if (error instanceof DOMException && error.name === "AbortError") {
          return;
        }

        console.error(error);
        window.location.assign(link.getAttribute("href"));
      }
    });
  });
});
