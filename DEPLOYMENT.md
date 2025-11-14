# 🚀 Dragonfly AI - Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Community Cloud

### Prerequisites
- GitHub account
- OpenAI API key
- LangChain API key (optional)

### 🔧 Deployment Steps

#### 1. **Push to GitHub**
```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Dragonfly AI app"

# Add GitHub remote (replace with your repository)
git remote add origin https://github.com/yourusername/dragonfly-ai.git

# Push to GitHub
git push -u origin master
```

#### 2. **Deploy to Streamlit Cloud**

1. **Go to** [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select your repository:** `yourusername/dragonfly-ai`
5. **Main file path:** `streamlit_app.py`
6. **Click "Deploy!"**

#### 3. **Configure Secrets**

In the Streamlit Cloud dashboard:

1. **Go to your app settings**
2. **Click "Secrets"**
3. **Add the following:**

```toml
[secrets]
OPENAI_API_KEY = "your-actual-openai-api-key"
LANGCHAIN_API_KEY = "your-actual-langchain-api-key"
LANGCHAIN_PROJECT = "dragonfly"
```

4. **Click "Save"**

### 🌐 Your Public URL

Once deployed, you'll get a public URL like:
`https://your-app-name.streamlit.app`

**Share this URL with anyone!** 🎉

### 📁 File Structure for Deployment
```
dragonfly/
├── streamlit_app.py          # Main Streamlit app
├── main.py                   # Core StudyBuddy logic
├── prompt.py                 # AI prompts and metadata
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── .streamlit/
│   └── secrets.toml         # Local secrets (not uploaded)
└── cleaned_data/            # Knowledge base files
    ├── StudySkills.txt
    ├── TimeManagement.txt
    ├── ProcrastinationHack.txt
    ├── CrunchTime.txt
    ├── Introduction.txt
    └── Procrastination DF SCRIPTS.docx
```

### 🔒 Security Notes

- ✅ API keys are stored securely in Streamlit secrets
- ✅ `.streamlit/secrets.toml` is excluded from Git
- ✅ Environment variables handled properly

### 🛠️ Local Testing

To test locally with the new configuration:

```bash
# Set your API keys in .streamlit/secrets.toml
# Then run:
streamlit run streamlit_app.py
```

### 🎯 Features

✅ **Public Access** - Anyone can use the URL  
✅ **Study Categories** - Multiple knowledge domains  
✅ **AI Chat Interface** - Natural conversation  
✅ **Memory Persistence** - Remembers chat history  
✅ **Secure** - API keys protected  

---

**Need help?** Check the [Streamlit documentation](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app) for more deployment options.