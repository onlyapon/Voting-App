# RMEDUSC Voting App

A simple voting application for RMEDUSC club elections.

## Quick Start

### Option 1: Using Python (Simplest)
```bash
# If Python is installed:
python -m http.server 8080
```
Then open http://localhost:8080 in your browser

### Option 2: Using Node.js
```bash
# If Node.js is installed:
npm install
npm start
```
Then open http://localhost:8080 in your browser

## Files Included
- `index.html` - Main entry page with batch selection
- `voting.html` - Voting page for batches 1-9
- `rme10.html` - Special voting page for batch 10
- `thankyou.html` - Thank you page after voting
- `votes.js` - Vote management and storage
- `server.js` - Simple Node.js server for testing
- `package.json` - Node.js project configuration

## Features
- Batch-specific voting pages
- Support for 20-30 voters per batch
- Vote counting and tracking
- Thank you page after voting
- Responsive design for mobile devices

## Deployment
See `DEPLOYMENT.md` for detailed deployment instructions.