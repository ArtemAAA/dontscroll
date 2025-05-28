// Analyze the current page
function analyzePage() {
  const title = document.title;
  const url = window.location.href;
  const text = document.body.innerText;

  // TODO: Implement more sophisticated analysis
  const keywords = text
    .split(/\s+/)
    .filter(word => word.length > 4)
    .slice(0, 10);

  return {
    title,
    url,
    keywords,
  };
}

// Send analyzed data to background script
chrome.runtime.sendMessage({
  type: 'PAGE_ANALYZED',
  data: analyzePage(),
}); 