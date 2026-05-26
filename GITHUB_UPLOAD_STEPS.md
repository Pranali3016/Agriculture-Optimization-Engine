# 📤 How to Upload to GitHub — Step by Step

Follow these exact steps on your Windows computer.

---

## ✅ Step 1 — Install Git (if not installed)

1. Go to https://git-scm.com/download/win
2. Download and install with all default settings
3. After install, open **Git Bash** (search it in Start menu)

---

## ✅ Step 2 — Create a GitHub Account

If you don't have one: https://github.com/signup  
Use your real name — this will be on your resume/LinkedIn.

---

## ✅ Step 3 — Create a New Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `crop-recommendation-app`
   - **Description:** `AI-powered crop recommendation system using Random Forest ML — Flask API + Web Frontend`
   - **Public** ✅ (so recruiters can see it)
   - **Do NOT** check "Add a README" (we already have one)
3. Click **Create repository**
4. Copy the URL shown — it will look like:
   `https://github.com/YOUR_USERNAME/crop-recommendation-app.git`

---

## ✅ Step 4 — Set Up Git on Your Computer

Open **Command Prompt** (Win + R → cmd) and run:

```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Replace with your actual name and the email you used for GitHub.

---

## ✅ Step 5 — Upload the Project

Open Command Prompt and paste these commands **one by one**:

```
cd C:\Users\pranali\OneDrive\Desktop\crop-recommendation-app
```

```
git init
```

```
git add .
```

```
git commit -m "Initial commit: CropSense Agriculture Optimization Engine with Random Forest ML"
```

```
git branch -M main
```

```
git remote add origin https://github.com/YOUR_USERNAME/crop-recommendation-app.git
```
⚠️ Replace YOUR_USERNAME with your actual GitHub username!

```
git push -u origin main
```

It will ask for your GitHub **username** and **password**.  
> ⚠️ GitHub no longer accepts your password — you need a **Personal Access Token** instead.

---

## ✅ Step 6 — Create a Personal Access Token (for password)

1. GitHub → your profile photo → **Settings**
2. Left sidebar → **Developer settings** (at the bottom)
3. **Personal access tokens → Tokens (classic)**
4. **Generate new token (classic)**
5. Note: `crop-app-upload`
6. Expiration: 90 days
7. Check ✅ **repo** (full control)
8. Click **Generate token**
9. **COPY IT NOW** — you won't see it again!

When git asks for password → paste this token.

---

## ✅ Step 7 — Enable GitHub Pages (for the website)

1. Go to your repo on GitHub
2. Click **Settings** tab
3. Left sidebar → **Pages**
4. Under **Source** → select **GitHub Actions**
5. The `deploy.yml` file will auto-deploy your frontend!
6. Wait ~2 minutes → your website will be live at:
   `https://YOUR_USERNAME.github.io/crop-recommendation-app`

---

## ✅ Step 8 — Add Screenshots to Your README

1. Run your project locally (see main README)
2. Take screenshots of the website
3. Save them as:
   - `assets/screenshot-home.png`
   - `assets/screenshot-result.png`
4. Upload them:
   ```
   git add assets/
   git commit -m "Add screenshots"
   git push
   ```

---

## ✅ Step 9 — Update Your LinkedIn & Resume

Add this to your resume under Projects:

```
CropSense — Agriculture Production Optimization Engine
• Built end-to-end ML web app recommending crops from soil/climate parameters
• Random Forest model achieving 99.32% accuracy on 22-class classification
• Full-stack: Flask REST API + responsive web frontend + GitHub Pages deployment
• GitHub: github.com/YOUR_USERNAME/crop-recommendation-app
```

---

## 🎉 You're Done!

Share your GitHub link with recruiters confidently. This project shows:
- ✅ End-to-end ML project (not just a notebook)
- ✅ REST API design with Flask
- ✅ Frontend development
- ✅ Deployment knowledge
- ✅ GitHub and CI/CD usage
