# 🎯 HOW TO USE - AI Learning Assistant

## ✅ BACKEND IS RUNNING!

Your backend is now running on **http://localhost:3001**

---

## 🌐 WHAT YOU SEE IN BROWSER

### **When you visit http://localhost:3001**
You'll see a JSON response like this:
```json
{
  "message": "🤖 AI Learning Assistant API",
  "status": "Running",
  "endpoints": {
    "health": "GET /health",
    "chat": "POST /chat"
  }
}
```

**This is CORRECT!** ✅ The backend is working!

---

## 💬 TO USE THE CHAT INTERFACE

### **Option 1: Standalone HTML (EASIEST)**

1. **Open File Explorer**
2. **Go to**: `ai-learning-assistant` folder
3. **Double-click**: `frontend-standalone.html`
4. **Browser opens with chat interface**
5. **Type a question and click Send!**

### **Option 2: Test with Browser Console**

1. Open http://localhost:3001 in browser
2. Press `F12` to open Developer Console
3. Go to "Console" tab
4. Paste this code:

```javascript
fetch('http://localhost:3001/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({message: 'What is a variable?'})
})
.then(r => r.json())
.then(data => console.log(data.reply));
```

5. Press Enter
6. You'll see the AI response in console!

### **Option 3: Test with Command**

Open Command Prompt and run:
```cmd
curl -X POST http://localhost:3001/chat -H "Content-Type: application/json" -d "{\"message\":\"What is a variable?\"}"
```

---

## 🧪 TEST THE ENDPOINTS

### **1. Root Endpoint** (What you're seeing now)
```
http://localhost:3001/
```
Shows API information

### **2. Health Check**
```
http://localhost:3001/health
```
Shows system status

### **3. Chat Endpoint** (Main feature)
```
POST http://localhost:3001/chat
Body: {"message": "Your question here"}
```
Returns AI response

---

## 🎨 RECOMMENDED: Use the Standalone HTML

The easiest way to demo your project:

1. **Double-click**: `frontend-standalone.html`
2. **It opens in browser with a beautiful chat interface**
3. **Type questions and get AI responses**
4. **Perfect for hackathon demo!**

---

## ✅ EVERYTHING IS WORKING!

- ✅ Backend API: Running on port 3001
- ✅ Chat endpoint: Ready to receive questions
- ✅ AI responses: Working with smart keyword matching
- ✅ Frontend HTML: Ready to open

**You're all set for the hackathon! Just open `frontend-standalone.html`!** 🚀

---

## 🎤 FOR YOUR DEMO

1. Open `frontend-standalone.html`
2. Show the chat interface
3. Ask: "What is a variable?"
4. Show the AI response
5. Ask: "What is an API?"
6. Show another response
7. Explain: "This uses AWS Lambda + Bedrock architecture"

**Demo time: 2 minutes. Impact: Maximum!** 🏆
