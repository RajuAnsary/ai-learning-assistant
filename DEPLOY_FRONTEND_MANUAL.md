# Deploy Frontend to AWS Amplify - Manual Steps

## Issue: Workspace Path Contains Spaces

Your workspace path has spaces which causes build issues. Follow these manual steps:

---

## Quick Deploy Steps

### Step 1: Open PowerShell in Frontend Directory

```powershell
cd "D:\AI-Powered Learning & Productivity Assistant for Beginner Developers\ai-learning-assistant\frontend"
```

### Step 2: Build the Frontend

```powershell
npm run build
```

This creates a `dist` folder with your production build.

### Step 3: Initialize Amplify

```powershell
amplify init
```

**Answer the prompts**:
- Project name: `ailearningassistant`
- Environment: `production`
- Default editor: (press Enter)
- App type: `javascript`
- Framework: `react`
- Source directory: `src`
- Distribution directory: `dist`
- Build command: `npm run build`
- Start command: `npm run dev`
- AWS Profile: `default`

### Step 4: Add Hosting

```powershell
amplify add hosting
```

**Choose**:
- Hosting with Amplify Console (Managed hosting)
- Manual deployment

### Step 5: Publish

```powershell
amplify publish
```

This will:
- Upload your built files
- Create CloudFront distribution
- Provide you with a live URL

---

## Alternative: Deploy to S3 Directly

If Amplify gives issues, use S3:

### Step 1: Build Frontend

```powershell
cd "D:\AI-Powered Learning & Productivity Assistant for Beginner Developers\ai-learning-assistant\frontend"
npm run build
```

### Step 2: Create S3 Bucket

```powershell
aws s3 mb s3://ai-learning-assistant-app --region us-east-1
```

### Step 3: Enable Static Website Hosting

```powershell
aws s3 website s3://ai-learning-assistant-app --index-document index.html --error-document index.html
```

### Step 4: Make Bucket Public

Create file `bucket-policy.json` in frontend folder:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::ai-learning-assistant-app/*"
    }
  ]
}
```

Apply policy:
```powershell
aws s3api put-bucket-policy --bucket ai-learning-assistant-app --policy file://bucket-policy.json
```

### Step 5: Upload Files

```powershell
aws s3 sync dist/ s3://ai-learning-assistant-app --delete
```

### Step 6: Get Website URL

Your site will be at:
```
http://ai-learning-assistant-app.s3-website-us-east-1.amazonaws.com
```

---

## Recommended: Use Amplify CLI

The Amplify CLI method is better because:
- Automatic HTTPS
- Global CDN (CloudFront)
- Easy updates
- Better performance

**Commands**:
```powershell
cd "D:\AI-Powered Learning & Productivity Assistant for Beginner Developers\ai-learning-assistant\frontend"
npm run build
amplify init
amplify add hosting
amplify publish
```

---

## After Deployment

### Test Your App

1. Visit the URL provided
2. Test all features:
   - Landing page
   - Login/Signup
   - Chat with AI
   - Debug code
   - Learning Path

### Check Console for Errors

Open browser DevTools (F12):
- Check for CORS errors
- Verify API calls to Lambda
- Test chat functionality

---

## What to Share

After deployment, please provide:

1. **Deployment method** (Amplify or S3)
2. **Live URL** of your app
3. **Any errors** encountered
4. **Screenshot** of working app (optional)

---

## Troubleshooting

### Build Fails

Try:
```powershell
cd "D:\AI-Powered Learning & Productivity Assistant for Beginner Developers\ai-learning-assistant\frontend"
npm install
npm run build
```

### Amplify Init Fails

Use S3 method instead (simpler, still works great)

### CORS Errors

Already configured in Lambda, should work fine

---

## Ready?

Open PowerShell and run:

```powershell
cd "D:\AI-Powered Learning & Productivity Assistant for Beginner Developers\ai-learning-assistant\frontend"
npm run build
amplify init
```

Let me know how it goes! 🚀
