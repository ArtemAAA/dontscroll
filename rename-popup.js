import { renameSync, existsSync } from 'fs';

const from = './dist/index.html';
const to = './dist/popup.html';

if (existsSync(from)) {
  renameSync(from, to);
  console.log('Renamed index.html to popup.html');
} else {
  console.log('index.html not found in dist');
} 