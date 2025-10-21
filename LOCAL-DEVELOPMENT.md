# Local Development Guide for doctorhump.com

This guide explains how to test your website locally before pushing changes live.

## Quick Start

### Start Local Server

1. Open a terminal/command prompt
2. Navigate to the project folder:
   ```bash
   cd "c:\Users\jarro\OneDrive - Light Blue Solutions LLC\doctorhump"
   ```
3. Run the local server:
   ```bash
   python -m http.server 8000
   ```
4. Open your browser to: **http://localhost:8000**

### Stop Local Server

Press `Ctrl+C` in the terminal where the server is running.

---

## Development Workflow

### 1. Test Changes Locally

```bash
# Start the local server
python -m http.server 8000
```

- Open http://localhost:8000 in your browser
- Edit HTML/CSS/JS files in your editor
- Refresh browser (F5) to see changes
- Keep server running while you work

### 2. Commit and Push When Ready

```bash
# Stop the server first (Ctrl+C)

# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Description of what you changed"

# Push to GitHub (triggers automatic Azure deployment)
git push
```

### 3. Wait for Deployment

- GitHub Actions automatically deploys to Azure
- Takes ~2 minutes
- Check deployment status: https://github.com/jarrodhumphrey/doctorhump/actions
- Live site: https://www.doctorhump.com

---

## Project Structure

```
doctorhump/
├── index.html          # Main homepage
├── styles.css          # Styling
├── LOCAL-DEVELOPMENT.md # This guide
└── .github/
    └── workflows/
        └── azure-static-web-apps-*.yml  # Auto-deployment config
```

---

## Common Tasks

### Add a New Page

1. Create new HTML file (e.g., `about.html`)
2. Test locally: http://localhost:8000/about.html
3. Link from index.html: `<a href="about.html">About</a>`
4. Commit and push when ready

### Edit Existing Content

1. Make sure local server is running
2. Edit the file in your code editor
3. Save the file
4. Refresh browser to see changes
5. When satisfied, commit and push

### Check if Server is Running

```bash
# Windows - check if port 8000 is in use
netstat -ano | findstr :8000
```

---

## Troubleshooting

### "ERR_EMPTY_RESPONSE" or Browser Can't Connect

If http://localhost:8000 shows "ERR_EMPTY_RESPONSE" or "didn't send any data", multiple server processes may be running on port 8000.

**Solution:**
1. Check what's using port 8000:
```bash
netstat -ano | findstr :8000
```

2. Kill any processes (replace XXXX with the PID numbers shown):
```bash
taskkill //F //PID XXXX
```

3. Start the server fresh:
```bash
python -m http.server 8000
```

### "Address already in use" Error

The server is already running on port 8000.

**Solution 1:** Find and stop the existing server
- Look for the terminal window where it's running
- Press `Ctrl+C`

**Solution 2:** Kill the process manually
```bash
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace XXXX with the PID)
taskkill //F //PID XXXX
```

**Solution 3:** Use a different port
```bash
python -m http.server 8001
# Then visit http://localhost:8001
```

### Python Not Found

Make sure Python is installed:
```bash
python --version
```

Should show: `Python 3.11.9` or similar

If not installed, download from: https://www.python.org/downloads/

### Changes Not Showing Up

1. **Hard refresh** your browser:
   - Windows: `Ctrl+F5` or `Ctrl+Shift+R`
   - Mac: `Cmd+Shift+R`

2. **Clear browser cache** if hard refresh doesn't work

3. **Check if you saved the file** in your editor

---

## Deployment Information

### Hosting Setup

- **Hosting**: Azure Static Web Apps (Free tier)
- **Domain**: doctorhump.com (via NameBright)
- **Repository**: https://github.com/jarrodhumphrey/doctorhump
- **Auto-deploy**: Enabled via GitHub Actions

### Live URLs

- Primary: https://www.doctorhump.com
- Alternate: https://doctorhump.com (redirects to www)
- Azure direct: https://white-wave-066d3a810.3.azurestaticapps.net

### DNS Configuration

Managed in NameBright:
- CNAME: `www` → `white-wave-066d3a810.3.azurestaticapps.net`
- URL Forwarding: `doctorhump.com` → `https://www.doctorhump.com`
- TXT records for Azure domain validation

---

## For Teaching/Students

### Collaborative Development

Students can:
1. Clone the repository
2. Make changes locally
3. Test with local server
4. Create pull requests on GitHub
5. Review and merge to deploy live

### Repository Access

Share this with students: https://github.com/jarrodhumphrey/doctorhump

---

## Resources

- **Azure Portal**: https://portal.azure.com (Static Web Apps)
- **NameBright Domain Manager**: https://www.namebright.com
- **GitHub Repository**: https://github.com/jarrodhumphrey/doctorhump
- **Python Documentation**: https://docs.python.org/3/library/http.server.html

---

## Quick Reference Commands

```bash
# Start local server
python -m http.server 8000

# Check git status
git status

# See recent changes
git diff

# Stage all changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub (triggers deployment)
git push

# Pull latest changes
git pull

# View commit history
git log --oneline
```

---

**Last Updated**: October 21, 2025
**Maintained By**: Dr. Hump / Jarrod Humphrey
