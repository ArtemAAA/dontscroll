import React, { useEffect, useState } from 'react';

interface Book {
  title: string;
  author: string;
  description: string;
}

interface PageData {
  title: string;
  url: string;
  keywords: string[];
  timestamp: number;
}

const Popup: React.FC = () => {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch page history from storage
    chrome.storage.local.get(['pageHistory'], (result) => {
      const pageHistory: PageData[] = result.pageHistory || [];
      
      if (pageHistory.length > 0) {
        // Generate mock book recommendations based on keywords
        const mockBooks: Book[] = pageHistory
          .slice(-5) // Get the 5 most recent pages
          .map(page => ({
            title: `Book about ${page.keywords[0] || 'your interests'}`,
            author: 'Recommended Author',
            description: `Based on your interest in ${page.keywords.slice(0, 3).join(', ')} from ${page.title}`,
          }));
        
        setBooks(mockBooks);
      }
      
      setLoading(false);
    });
  }, []);

  return (
    <div className="w-96 p-4">
      <h1 className="text-2xl font-bold mb-4">DontSurf</h1>
      {loading ? (
        <p>Loading recommendations...</p>
      ) : books.length > 0 ? (
        <div className="space-y-4">
          {books.map((book, index) => (
            <div key={index} className="border p-4 rounded hover:bg-gray-50 transition-colors">
              <h2 className="text-lg font-semibold">{book.title}</h2>
              <p className="text-gray-600">{book.author}</p>
              <p className="mt-2 text-sm text-gray-700">{book.description}</p>
            </div>
          ))}
        </div>
      ) : (
        <p>No book recommendations yet. Start browsing to get recommendations!</p>
      )}
    </div>
  );
};

export default Popup; 