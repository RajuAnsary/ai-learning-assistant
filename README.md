# 🤖 AI Learning Assistant

An interactive web application that helps beginner developers learn JavaScript through AI-powered assistance, code debugging, and structured learning paths.

## 🌟 Features

- **AI Chat Assistant**: Get instant help with programming questions using AWS Bedrock
- **Code Debugger**: Analyze and fix JavaScript code with AI-powered suggestions
- **Learning Path**: 20 structured lessons covering JavaScript fundamentals
- **Progress Tracking**: Track your learning progress with XP and completion badges
- **User Authentication**: Secure login and registration system
- **Cloud-Native**: Fully deployed on AWS with DynamoDB, Lambda, and CloudFront

## 🚀 Live Demo

Visit the live application: [https://di21r9s7dmq4q.cloudfront.net](https://di21r9s7dmq4q.cloudfront.net)

## 🏗️ Architecture

### Frontend
- **Framework**: React + Vite
- **Styling**: Custom CSS with teal/dark gradient theme
- **Deployment**: AWS S3 + CloudFront CDN
- **Features**: 
  - Public landing page
  - User authentication
  - AI chat interface
  - Code debugger
  - Interactive learning path
  - Lesson viewer

### Backend
- **Runtime**: Node.js on AWS Lambda
- **Framework**: Serverless Framework
- **API**: REST API via AWS API Gateway
- **AI**: AWS Bedrock (Amazon Nova Micro model)
- **Database**: AWS DynamoDB
- **Features**:
  - User authentication with bcrypt
  - Chat history management
  - Learning progress tracking
  - AI-powered code analysis

## 📋 Prerequisites

- Node.js 18+ and npm
- AWS Account with:
  - AWS CLI configured
  - Bedrock access (Amazon Nova Micro model)
  - DynamoDB permissions
  - Lambda and API Gateway permissions
  - S3 and CloudFront permissions

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-learning-assistant
```

### 2. Backend Setup

```bash
cd backend
npm install

# Create .env file
cp .env.example .env
# Edit .env with your AWS credentials
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

### 4. Create DynamoDB Tables

```bash
cd backend
node create-dynamodb-tables.js
```

This creates three tables:
- `ai-learning-users` - User accounts
- `ai-learning-chat-history` - Chat conversations
- `ai-learning-progress` - Learning progress

### 5. Deploy Backend

```bash
cd backend
npx serverless deploy
```

Note the API Gateway URL from the deployment output.

### 6. Configure Frontend

Update `frontend/src/utils/constants.js` with your API Gateway URL:

```javascript
export const API_URL = 'https://your-api-gateway-url.amazonaws.com/dev';
```

### 7. Build and Deploy Frontend

```bash
cd frontend
npm run build

# Deploy to S3
aws s3 sync dist/ s3://your-bucket-name/

# Create CloudFront distribution (optional but recommended)
```

## 📁 Project Structure

```
ai-learning-assistant/
├── backend/
│   ├── handler.js              # Lambda function handlers
│   ├── bedrock-integration.js  # AWS Bedrock AI integration
│   ├── dynamodb-helper.js      # Database operations
│   ├── serverless.yml          # Serverless configuration
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── pages/              # React page components
│   │   ├── components/         # Reusable components
│   │   ├── utils/              # Utility functions
│   │   └── assets/             # Images and static files
│   ├── package.json
│   └── vite.config.js
├── docs/                       # Documentation
└── README.md
```

## 🔧 Configuration

### Environment Variables

Create `backend/.env`:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
```

### AWS Bedrock Model

The application uses `amazon.nova-micro-v1:0`. Ensure this model is enabled in your AWS account:

1. Go to AWS Bedrock console
2. Navigate to Model access
3. Enable Amazon Nova Micro

## 📚 Learning Path Topics

1. Variables & Data Types
2. Operators & Expressions
3. Conditionals (if/else)
4. Loops (for/while)
5. Functions Basics
6-20. Coming Soon!

## 🎨 Features in Detail

### AI Chat Assistant
- Natural language Q&A about programming
- Structured responses with explanations, examples, and key points
- Chat history saved to DynamoDB
- Voice input support

### Code Debugger
- Paste or type JavaScript code
- AI analyzes for errors and issues
- Provides detailed explanations and fixed code
- Learning tips for common mistakes

### Learning Path
- Sequential lesson unlocking
- XP-based progress system
- Completion tracking
- Review completed lessons anytime

## 🔐 Security Notes

- Never commit `.env` files or AWS credentials
- Use IAM roles with minimal required permissions
- Enable CloudFront for HTTPS
- Passwords are hashed with bcrypt
- API endpoints validate user authentication

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Created as part of an AWS learning project.

## 🙏 Acknowledgments

- AWS Bedrock for AI capabilities
- React and Vite for frontend framework
- Serverless Framework for easy deployment
- AWS Free Tier for hosting

## 📞 Support

For issues or questions, please open a GitHub issue.

---

**Note**: This is an educational project. For production use, implement additional security measures, error handling, and monitoring.
