#!/usr/bin/env python3
"""
GitHub Deployment Guide Generator for FDOT D5 Analysis
Generates setup instructions for deploying to GitHub Pages
"""

import os
from pathlib import Path

deploy_dir = Path('c:\\Users\\anand\\Desktop\\FDOT_D5_Public_Release')

github_guide = """# 🚀 GitHub Deployment Guide

## Step-by-Step Instructions

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. **Repository name:** `fdot-d5-analysis` (or your preferred name)
3. **Description:** FDOT District 5 Demographic Analysis 2025-2050
4. **Visibility:** Public
5. **Initialize with README:** No (we have our own)
6. Click **Create repository**

### 2. Prepare Your Local Files

Your folder should contain:
```
FDOT_D5_Public_Release/
├── index.html                          (Interactive dashboard)
├── analysis_results.json               (Complete dataset)
├── metadata.json                       (Project metadata)
├── FDOT_D5_Summary_Tables.xlsx        (Excel summary tables)
├── README.md                          (Project overview)
├── DOCUMENTATION.md                   (Technical documentation)
├── LICENSE                            (CC0 Public Domain)
├── .gitignore                         (Git ignore rules)
└── GITHUB_SETUP.md                    (This file)
```

### 3. Initialize Git Repository

```bash
cd FDOT_D5_Public_Release
git init
git add .
git commit -m "Initial commit: FDOT D5 Analysis Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fdot-d5-analysis.git
git push -u origin main
```

### 4. Enable GitHub Pages

1. Go to your repository: https://github.com/YOUR_USERNAME/fdot-d5-analysis
2. Click **Settings** (top menu)
3. Scroll to **Pages** section (left sidebar)
4. **Source:** Select **Deploy from a branch**
5. **Branch:** Select **main** and **/ (root)**
6. Click **Save**

**Your site will be live at:**
```
https://YOUR_USERNAME.github.io/fdot-d5-analysis
```

(Note: GitHub Pages typically takes 1-2 minutes to deploy)

### 5. Share the Link

Your analysis is now publicly available at:
```
https://YOUR_USERNAME.github.io/fdot-d5-analysis
```

Share this link with:
- 📊 Stakeholders for interactive viewing
- 📋 Planners for data analysis
- 📈 Decision makers for insights
- 🔗 Anyone interested in FL demographics

---

## File-by-File Explanation

### index.html
- **Purpose:** Main interactive dashboard
- **Features:** Download buttons, key statistics, formatted tables
- **Access:** Opens automatically when visiting GitHub Pages URL
- **No dependencies:** Works offline after first load

### analysis_results.json
- **Purpose:** Complete dataset with 3,216 records
- **Contents:** County time series, growth rates, regression results
- **Usage:** Download via dashboard or direct link
- **Format:** JSON (universal data format)

### metadata.json
- **Purpose:** Project information and specifications
- **Contents:** Data source details, methodology, key metrics
- **Usage:** Reference or download for documentation
- **Format:** JSON

### FDOT_D5_Summary_Tables.xlsx
- **Purpose:** Professional summary tables
- **Format:** Excel workbook with 6 sheets
- **Usage:** Ready for presentations and reports
- **Note:** Upload to repository for download capability

### README.md
- **Purpose:** Project overview and quick start
- **Displayed:** Automatically on GitHub repository page
- **Contents:** Instructions, key findings, data summary

### DOCUMENTATION.md
- **Purpose:** Technical methodology details
- **Contents:** Data processing, statistical methods, limitations
- **Audience:** Technical users and researchers

### LICENSE
- **License:** CC0 1.0 Universal (Public Domain)
- **Meaning:** Free to use, no attribution required
- **Displayed:** On GitHub repository page

### .gitignore
- **Purpose:** Tell Git which files to ignore
- **Includes:** OS files, IDE files, temporary files

---

## Customization

### Change Repository Name
Replace `fdot-d5-analysis` with your preferred name in:
- GitHub repository creation
- Git remote URL
- Shared link

### Update Header
Edit `index.html` line 25:
```html
<h1>🌍 FDOT District 5 Demographic Analysis</h1>
```

### Change Colors
Edit CSS in `index.html` around line 42:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add More Data
Place additional JSON files in the folder:
1. Update `index.html` download buttons
2. Create matching metadata
3. Commit and push changes

---

## Troubleshooting

### Page doesn't load
- ✓ Ensure index.html is in the root folder
- ✓ Wait 2-3 minutes for GitHub Pages to deploy
- ✓ Try clearing browser cache (Ctrl+Shift+Del)
- ✓ Check repository Settings > Pages

### Download buttons don't work
- ✓ Ensure data files (.json, .xlsx) are uploaded
- ✓ Verify files are in root folder
- ✓ Check browser console for errors (F12)
- ✓ Try direct link: `https://raw.githubusercontent.com/USERNAME/REPO/main/filename`

### Charts don't display
- ✓ Check browser console (F12) for errors
- ✓ Ensure Plotly.js CDN is accessible
- ✓ Verify JSON file is valid (use jsonlint.com)
- ✓ Try refreshing page

### Not seeing latest changes
- ✓ Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
- ✓ Clear GitHub Pages cache (takes 1-5 minutes)
- ✓ Check git push was successful

---

## Advanced Options

### Custom Domain
1. Buy domain (e.g., fdot-d5.org)
2. Go to repository Settings > Pages
3. Enter custom domain
4. Update DNS records (see GitHub docs)

### Analytics
Add Google Analytics to index.html (after `<head>`):
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

### Automated Updates
1. Update files locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update: [description]"
   git push origin main
   ```
3. Changes live in seconds

---

## Project Structure for GitHub

```
📁 fdot-d5-analysis/
├── 📄 index.html                      (Start here)
├── 📊 analysis_results.json           (3,216 records)
├── 📋 metadata.json                   (Project info)
├── 📈 FDOT_D5_Summary_Tables.xlsx    (Excel tables)
├── 📖 README.md                       (Overview)
├── 📚 DOCUMENTATION.md                (Technical)
├── ⚖️ LICENSE                         (CC0 Public Domain)
├── 🚫 .gitignore                      (Git settings)
└── 🚀 GITHUB_SETUP.md                 (This guide)
```

---

## Quick Git Commands

```bash
# First time setup
git init
git config user.name "Your Name"
git config user.email "your@email.com"

# Add all files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push origin main

# View status
git status

# View commit history
git log

# View remote
git remote -v
```

---

## Success Indicators

✅ Repository created at: https://github.com/USERNAME/fdot-d5-analysis
✅ Files pushed successfully
✅ GitHub Pages enabled in Settings
✅ Live site accessible at: https://USERNAME.github.io/fdot-d5-analysis
✅ Download buttons functional
✅ Data visible in dashboard

---

## Support Resources

- **GitHub Help:** https://docs.github.com/
- **GitHub Pages Guide:** https://docs.github.com/en/pages
- **Git Basics:** https://git-scm.com/book/en/v2
- **HTML/CSS Reference:** https://developer.mozilla.org/
- **JSON Format:** https://www.json.org/

---

## After Going Live

### Share Your Work
- Post link on social media
- Share in GitHub discussions
- Include in project documentation
- Send to stakeholders

### Maintain the Project
- Monitor page analytics
- Fix broken links
- Update data annually
- Add new features as needed

### Engage Community
- Enable GitHub Discussions
- Add issue templates
- Create contribution guidelines
- Star and fork counts as metrics

---

## Example Commands to Deploy

```bash
# Navigate to folder
cd "C:\\Users\\anand\\Desktop\\FDOT_D5_Public_Release"

# Initialize Git
git init
git add .
git commit -m "Initial commit: FDOT D5 Analysis Dashboard"

# Add GitHub remote (replace USERNAME and REPO)
git remote add origin https://github.com/USERNAME/fdot-d5-analysis.git

# Push to GitHub
git push -u origin main
```

---

**Deployment Complete! 🎉**

Your FDOT D5 Analysis is now live and accessible to everyone!

**Live URL:** https://YOUR_USERNAME.github.io/fdot-d5-analysis

---

Generated: November 10, 2025
"""

# Write the guide
guide_path = deploy_dir / 'GITHUB_SETUP.md'
with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(github_guide)

print("✅ GitHub Setup Guide created successfully!")
print(f"\nFile: {guide_path}")
print("\n📋 Contents:")
print("  - Step-by-step GitHub deployment instructions")
print("  - GitHub Pages setup guide")
print("  - Troubleshooting section")
print("  - Advanced options (custom domain, analytics)")
print("  - Git commands reference")
print("\n🚀 Next Steps:")
print("  1. Read GITHUB_SETUP.md")
print("  2. Create GitHub repository")
print("  3. Initialize git locally")
print("  4. Push files to GitHub")
print("  5. Enable GitHub Pages")
print("  6. Share link with stakeholders")
