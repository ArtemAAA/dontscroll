interface PageData {
  title: string;
  url: string;
  keywords: string[];
  timestamp: number;
}

// Listen for tab updates
chrome.tabs.onUpdated.addListener((_tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    // TODO: Analyze the URL and store relevant information
    console.log('Tab updated:', tab.url);
  }
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((message, _sender, _sendResponse) => {
  if (message.type === 'PAGE_ANALYZED') {
    const pageData: PageData = {
      ...message.data,
      timestamp: Date.now(),
    };

    // Store the analyzed page data
    chrome.storage.local.get(['pageHistory'], (result) => {
      const pageHistory: PageData[] = result.pageHistory || [];
      pageHistory.push(pageData);
      
      // Keep only the last 50 pages
      const recentHistory = pageHistory.slice(-50);
      
      chrome.storage.local.set({ pageHistory: recentHistory }, () => {
        console.log('Page data stored:', pageData);
      });
    });
  }
}); 