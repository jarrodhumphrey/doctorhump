# doctorhump - Deployment & Technical Setup

## Hosting Platform

**Platform:** Azure Static Web Apps
**Domain:** doctorhump.com
**Repository:** GitHub (private repository assumed)
**Deployment Method:** Automated via GitHub Actions

---

## Deployment Configuration

### Source Control: Git + GitHub
- **Main branch:** `main` (auto-deploys to production)
- **Remote:** GitHub repository
- **Workflow:** Push to main → GitHub Actions → Azure deployment

### Deployment Source
**Live site deploys from:** `/docs` folder

**Why /docs?**
- GitHub Pages convention (though we're using Azure)
- Separates development/planning files from production files
- Clean organization: root for docs/planning, /docs for live site

### What Gets Deployed
Everything in the `/docs` folder:
- `index.html` (homepage)
- `ai.html` (AI Leadership page)
- `blog.html` (blog listing)
- `blog/*.html` (blog posts)
- `*.jpg`, `*.png`, `*.jpeg` (images)
- `*.pdf` (research papers)
- `client-logos/` (organization logos)

### What Does NOT Get Deployed
Root-level files and folders:
- `index.html` (root - legacy placeholder)
- `styles.css` (root - legacy styles)
- `planning/` (strategic documents)
- `Feedback/` (testimonials source material)
- `.claude/` (Claude Code configuration)
- `README.md`, `LOCAL-DEVELOPMENT.md`
- Git-related files

---

## Git Status & Workflow

### Current Branch
**Main branch:** `main`

### Recent Git Activity (as of latest session)
```
Modified:
- .claude/settings.local.json (Claude Code settings)
- Feedback/04-Survey-Results/XLC_AI_Talk_1.pdf (compressed)
- Feedback/04-Survey-Results/XLC_AI_Talk_2.pdf (compressed)

Untracked:
- Feedback/FA24 AI in Business Roster.xlsx
- Feedback/FA25 AI in Business Roster.xlsx
- Feedback/SP25 AI in Business Roster.xlsx
- nul (temp file)
- potm2504a.tif
```

### Recent Commits (last 20)
```
fecc91f - Prepare agentic blog infrastructure
9a378b7 - Remove carousel dots from testimonials section
868efc1 - Update AI Ethics Chatbot description with D'Artagnan name and RAG emphasis
3fe59e2 - Feature prominent AI Leadership CTA on landing page
5e14ce3 - Update Community Engagement and carousel start position
1c9a8b9 - Update AI Leadership page with enhanced structure and content
3d68607 - Add AI Initiatives & Impact carousel section
d391df6 - Update AI page with Xavier testimonials heading and warm gradient statistics
fbc2545 - Fix asset paths for ai.html - add client logos and fix background
7eb69e7 - Move ai.html to docs folder for GitHub Pages deployment
d3baa63 - Add AI in Business consulting page with verified statistics
0f2fed2 - Add AI in Business consulting page with client logo carousel
e3f42f1 - Slight typo correction
9e4cc41 - Add cosmic space-themed buttons with warm amber gradient
889e274 - Use optimized smallest James Webb background for fast loading
26bded0 - Optimize homepage with smaller James Webb background image
76d8d02 - Add James Webb Telescope space background to homepage
2b03a2a - Add student success testimonials to chatbot sections
e626b17 - Add coach photos and LinkedIn bios reference file
e27a56f - Fix Azure deployment - point to /docs folder
```

**Pattern:** Iterative development with frequent small commits

---

## Deployment Workflow

### Standard Development Flow

1. **Make changes locally** (in /docs folder for live changes)
2. **Test locally** (open files in browser, or run local server)
3. **Git add** (stage changes)
4. **Git commit** (descriptive message)
5. **Git push** (to main branch)
6. **GitHub Actions triggers** (automatically)
7. **Azure deployment** (automatically)
8. **Live at doctorhump.com** (within minutes)

### Command Examples
```bash
# Stage all changes in docs folder
git add docs/

# Commit with descriptive message
git commit -m "Add new testimonial to AI page"

# Push to main (triggers deployment)
git push origin main
```

### Branch Strategy
Currently using **single branch (main)** for simplicity.

**Future consideration:** If collaboration increases or major redesigns are planned:
- Create `development` branch for work-in-progress
- Use `main` for production-ready code
- Merge development → main when ready to deploy

---

## Local Development

### Setup
No build process required - static HTML files.

**To preview locally:**

**Option 1: Direct file opening**
- Navigate to `/docs/index.html`
- Open in browser (double-click or File > Open)
- **Limitation:** Some paths may not work correctly

**Option 2: Local development server**
```bash
# Python 3
cd docs
python -m http.server 8000

# Then visit: http://localhost:8000
```

**Option 3: VS Code Live Server extension**
- Install "Live Server" extension
- Right-click `docs/index.html`
- Select "Open with Live Server"

### File Editing
- Use any text editor (VS Code recommended)
- Claude Code for AI-assisted development
- Edit HTML/CSS directly (no build step)

---

## Domain & DNS

### Domain: doctorhump.com
**Registrar:** (Unknown - likely GoDaddy, Namecheap, or similar)
**DNS Configuration:** Points to Azure Static Web App

**Typical DNS setup:**
- A record or CNAME pointing to Azure endpoint
- Managed through domain registrar or Azure DNS

**Custom domain setup:** Configured through Azure Static Web Apps settings

---

## Performance Optimization

### Image Optimization
- **Space background:** Using `james-webb-background_smallest.jpg` (optimized for web)
- **Client logos:** Compressed images in `/docs/client-logos/`
- **Photos:** Academic leadership, ethics bot, panel photos optimized

**Future improvements:**
- WebP format for better compression
- Lazy loading for below-fold images
- Responsive images (srcset) for different screen sizes

### File Size Monitoring
- Keep HTML files under 100KB when possible
- Compress images before adding to repo
- Monitor total page weight (aim for <2MB per page)

### Caching Strategy
Handled by Azure Static Web Apps (automatic):
- Static assets cached by CDN
- HTML files have shorter cache times
- Images/PDFs have longer cache times

---

## Monitoring & Analytics

### Current Setup
**Analytics:** Not implemented yet

**Future consideration:**
- Google Analytics (if tracking desired)
- Privacy-focused alternative (Plausible, Fathom)
- Azure Application Insights

**Note from planning docs:** "Not specified" - analytics not a priority initially

---

## Backup & Version Control

### Git as Backup
- All code versioned in Git
- Remote repository on GitHub serves as backup
- Commit history allows rollback to any previous version

### Asset Backup
- Images, PDFs, and all assets stored in Git
- Consider separate backup for large binary files if repo grows too large

---

## Deployment Checklist

Before pushing changes to main:

- [ ] Test all changes locally (open in browser or local server)
- [ ] Check responsive design (resize browser window)
- [ ] Verify all links work correctly
- [ ] Ensure images load properly
- [ ] Check for typos/content errors
- [ ] Review git diff to see what's changing
- [ ] Stage only intended files (`git add`)
- [ ] Write descriptive commit message
- [ ] Push to main
- [ ] Wait for deployment (check GitHub Actions if needed)
- [ ] Visit live site to verify changes

---

## Troubleshooting

### Common Issues

**Images not loading:**
- Check file paths (case-sensitive on Linux servers)
- Ensure images are in /docs folder
- Verify image file names match HTML references

**Links broken:**
- Use relative paths within /docs (`ai.html` not `/ai.html`)
- Don't use absolute paths that reference local filesystem

**Changes not appearing:**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait a few minutes for deployment to complete
- Check GitHub Actions for deployment status

**CSS not applying:**
- Check for inline styles vs external CSS conflicts
- Verify CSS syntax (missing semicolons, brackets)
- Use browser dev tools to inspect elements

---

## Future Technical Enhancements

### Potential Improvements
- **Build process:** Templating system to avoid repeating navigation/footer
- **CSS preprocessing:** SCSS/LESS for better style organization
- **Minification:** Compress HTML/CSS for smaller file sizes
- **Service worker:** Offline support, faster repeat visits
- **Search functionality:** For blog posts (client-side with Lunr.js or similar)

### Clean URLs
Currently using `.html` extensions (e.g., `ai.html`)

**To achieve clean URLs** (e.g., `/ai` instead of `/ai.html`):
- Azure Static Web Apps configuration (routes.json)
- Rename files to directories with index.html (e.g., `ai/index.html`)
- Update all internal links

**Priority:** Low - not urgent, but would be nice for polish

---

## Security Considerations

### Static Site Benefits
- No server-side code = reduced attack surface
- No database = no SQL injection risk
- No user authentication = no credential management

### Current Vulnerabilities: None significant
- Contact forms (when added) should use secure services (Formspree, Netlify Forms, etc.)
- Avoid storing sensitive data in repository (already following this)

### HTTPS
- Provided by Azure Static Web Apps (automatic)
- Custom domain should have SSL certificate (verify in Azure)

---

## Contact for Deployment Issues

If deployment breaks or domain stops working:
1. Check GitHub Actions for error logs
2. Review Azure Static Web Apps portal
3. Verify domain DNS settings
4. Check Git commit history for recent changes
5. Roll back if needed (`git revert` or `git reset`)

**Key personnel:** Jarrod Humphrey (owner)
