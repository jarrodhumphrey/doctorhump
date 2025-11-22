# doctorhump - Site Architecture

## File Structure

```
doctorhump/
├── index.html                  # Root landing page (legacy, not deployed)
├── styles.css                  # Root styles (legacy, not deployed)
│
├── docs/                       # ** LIVE SITE - GitHub Pages deployment **
│   ├── index.html             # Live homepage with space theme
│   ├── ai.html                # AI Leadership showcase page
│   ├── blog.html              # Blog listing page
│   ├── blog/                  # Blog posts folder
│   │   ├── agentic-blog-sample.html
│   │   └── why-ai-wont-replace-good-managers.html
│   ├── james-webb-background_smallest.jpg  # Space background
│   ├── client-logos/          # Client organization logos (15+)
│   ├── academic-leadership.jpg
│   ├── ethics-bot.jpeg
│   ├── cincy-ai-week-panel.jpg
│   ├── AI_Research.png
│   ├── I_Like_the_Bots.pdf    # Research paper
│   ├── High_Intensity_Ambivalence.pdf  # Research paper
│   └── [other pages TBD]
│
├── planning/                   # Strategic planning documents
│   ├── brand-strategy.md      # Core brand pillars and vision
│   ├── website-answers.md     # 53 strategic questions answered
│   ├── site-map.md            # URL structure and page plans
│   ├── testimonials-strategy.md
│   ├── website-planning-questions.md
│   └── README.md
│
├── Feedback/                   # Testimonials and feedback collection
│   ├── MASTER-TESTIMONIALS.md # 54 curated testimonials
│   ├── inventory.md
│   └── [various source folders]
│
└── .claude/                    # Claude Code configuration
    ├── commands/
    │   └── blog.md            # /blog slash command
    └── doctorhump-context/    # Context documentation for onboarding
        ├── overview.md
        ├── architecture.md    # This file
        ├── styles.md
        ├── deployment.md
        └── current-priorities.md
```

---

## URL Structure (Planned)

### Current URLs (Live)
```
doctorhump.com/              → Homepage (docs/index.html)
doctorhump.com/ai.html       → AI Leadership page
doctorhump.com/blog.html     → Blog listing
doctorhump.com/blog/[post]   → Individual blog posts
```

### Future Clean URLs (Aspirational)
```
doctorhump.com/              → Homepage
doctorhump.com/ai            → AI Leadership
doctorhump.com/case-race     → Case Race page (not built yet)
doctorhump.com/about         → Personal/About page (not built yet)
doctorhump.com/blog          → Blog listing
doctorhump.com/blog/[slug]   → Individual posts
```

**Note:** Currently using .html extensions for simplicity with GitHub Pages. Clean URLs may require additional configuration.

---

## Page Breakdown

### Homepage (docs/index.html)
**Purpose:** First impression - introduce Dr. Hump and provide clear pathways to learn more

**Current Implementation:**
- Space-themed background (James Webb Telescope image)
- Semi-transparent white container with rounded corners
- Name: "Jarrod Humphrey" with "aka doctorhump" subtitle
- Brief bio paragraph (Xavier professor, AI focus, Cincinnati, Bengals, family)
- Prominent AI Leadership CTA (large cosmic button)
- Grid of 4 contact/social links (Email Personal, Email Xavier, LinkedIn, YouTube)
- All buttons use cosmic space theme with animated shooting stars

**Key Features:**
- Responsive design (mobile/tablet/desktop)
- Cosmic button effects with shooting stars and glow on hover
- Clean, uncluttered layout
- Immediate sense of unique brand

**Future Enhancements:**
- More prominent presentation of all three pillars (currently AI-heavy)
- Case Race section with link to dedicated page
- Brief personal section expansion

---

### AI Leadership Page (docs/ai.html)
**Purpose:** Showcase AI expertise, testimonials, client work, and initiatives

**Current Sections:**
1. **Hero:** "AI Leadership at Xavier" heading
2. **Executive Education (XLC):** Featured quote from Fifth Third Bank
3. **Statistics Bar:** 4 metrics (87% NPS, 9.8/10, 96% Implementation, 15+ Orgs)
4. **Client Logos Carousel:** Auto-scrolling logos of 15 organizations
5. **AI Initiatives Carousel:** 4 slides with images and descriptions
   - Academic Leadership
   - AI Ethics Chatbot (D'Artagnan with RAG)
   - Community Engagement
   - Research & Scholarship
6. **Testimonials Carousel:** Rotating Xavier/student testimonials

**Technical Details:**
- Embedded styles (not external CSS)
- JavaScript carousels with manual navigation arrows
- Auto-rotating logo carousel (45s loop)
- Space background continuation
- Responsive grid for mobile

**Future Enhancements:**
- Services section (what AI consulting is offered)
- Contact form or CTA for AI services
- Link to blog/generative blog
- Potentially separate XLC page

---

### Blog Pages (docs/blog.html + docs/blog/*)
**Purpose:** "Generative Blog" - content dictated to AI, written by AI

**Current Status:**
- Blog listing page exists (blog.html)
- Sample posts created:
  - `agentic-blog-sample.html`
  - `why-ai-wont-replace-good-managers.html`
- Infrastructure for agentic blog in place

**Future Development:**
- Populate with actual blog posts
- Implement consistent blog post template
- Add filtering/categories
- Consider RSS feed

---

### Case Race Page (NOT YET BUILT)
**Planned URL:** doctorhump.com/case-race

**Planned Content:**
- What Case Race is
- Why it matters to Dr. Hump
- Links to the game
- Case Race logos/branding
- Links to YouTube channel
- Links to social media
- Recent Case Race content/updates

**Priority:** Medium - important for brand completeness but not urgent

---

### About/Personal Page (NOT YET BUILT)
**Planned URL:** doctorhump.com/about

**Planned Content:**
- Personal background (Cincinnati, family, dog, sports, business history)
- Professional position at Xavier
- Third-person bio
- Photo (minimal use)
- Contact information

**Priority:** Low - personal pillar is 2/10 importance

---

## Navigation Strategy

### Current Navigation
- **Homepage:** Links to ai.html, email, LinkedIn, YouTube
- **AI page:** Back button to homepage
- **No global navigation bar yet**

### Planned Navigation
- Simple top navigation bar across all pages
- Links: Dr. Hump (logo/home) | AI | Case Race | About | Contact
- Sticky/fixed navigation on scroll
- Mobile hamburger menu for responsive design
- Ice blue/gray color scheme matching brand

---

## Content Management

### Static HTML Approach
- All pages are static HTML (no CMS, no database)
- Inline styles for most pages (ai.html)
- Separate CSS for homepage (could be consolidated)
- Manually updated content (with Claude assistance)

**Pros:**
- Fast loading
- Simple deployment
- Full control over design
- No backend complexity

**Cons:**
- Manual updates required
- No dynamic features (comments, search, etc.)
- Repetitive code (navigation, footer)

**Future Consideration:**
- Template system for shared components (navigation, footer)
- Build process to generate HTML from templates
- Or embrace simplicity and continue manual HTML

---

## Key Architectural Decisions

### Why docs/ folder?
- GitHub Pages deploys from /docs folder by default
- Allows us to have root-level files (planning docs, README) separate from live site
- Clean separation between "working files" and "deployed files"

### Why inline styles vs external CSS?
- **Current approach:** Inline styles in ai.html for component-specific designs
- **Trade-off:** Easier to see all code in one place vs. reusability
- **Future:** Consider extracting common styles to shared stylesheet

### Why static HTML vs framework?
- **Simplicity:** No build process, no dependencies
- **Speed:** Instant load times
- **Control:** Full design freedom
- **Fits use case:** Not a web app, just a personal brand site

### Component Reusability
- Cosmic button styles are repeated across pages
- Carousel JavaScript is duplicated
- Navigation will need to be consistent

**Future refactor opportunities:**
- Extract shared styles to `docs/styles.css`
- Create `docs/scripts.js` for carousel/interaction logic
- Template system for repeated elements

---

## Pages Summary

| Page | Status | Priority | URL |
|------|--------|----------|-----|
| Homepage | ✅ Live | Critical | doctorhump.com/ |
| AI Leadership | ✅ Live | Critical | doctorhump.com/ai.html |
| Blog Listing | ✅ Live | Medium | doctorhump.com/blog.html |
| Blog Posts | 🟡 Partial | Medium | doctorhump.com/blog/*.html |
| Case Race | ❌ Not built | Medium | doctorhump.com/case-race |
| About/Personal | ❌ Not built | Low | doctorhump.com/about |

---

## Mobile Responsiveness

All live pages include responsive breakpoints:
- **Desktop:** 1024px+
- **Tablet:** 768-1023px
- **Mobile:** 320-767px

**Key responsive behaviors:**
- Stacked layouts on mobile (no side-by-side grids)
- Reduced font sizes
- Adjusted padding/margins
- Touch-friendly button sizes
- Hamburger menu (when navigation is added)
