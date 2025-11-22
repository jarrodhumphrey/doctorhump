# doctorhump - Current Priorities & Active Work

**Last Updated:** Based on recent commits and planning documents
**Status:** Early development - iterative building phase

---

## What's Working Well

### ✅ Completed & Live
1. **Homepage (docs/index.html)**
   - Space-themed design with James Webb background
   - Cosmic button effects with shooting stars
   - Brief bio and prominent AI Leadership CTA
   - Contact/social links (Email, LinkedIn, YouTube)
   - Responsive mobile design

2. **AI Leadership Page (docs/ai.html)**
   - Full showcase with 6 major sections
   - Executive education section with featured testimonial
   - Statistics bar (87% NPS, 9.8/10, 96%, 15+ orgs)
   - Client logo carousel (15 organizations)
   - AI Initiatives carousel (4 slides with images)
   - Xavier testimonials carousel (rotating quotes)
   - All responsive with mobile adaptations

3. **Blog Infrastructure**
   - Blog listing page exists (blog.html)
   - Sample posts created
   - Agentic blog framework ready for content
   - "Generative Blog" concept established

4. **Design System**
   - Consistent cosmic/space theme across pages
   - Ice blue/gray color palette established
   - Warm amber accent gradient for emphasis
   - Reusable button pattern (cosmic stars/shooting stars)
   - Carousel patterns established

---

## Current Gaps & Known Issues

### 🟡 Incomplete Features

**1. Case Race Page**
- **Status:** Not built yet
- **Priority:** Medium
- **What's needed:**
  - Explanation of what Case Race is
  - Why it matters to Dr. Hump
  - Links to the game
  - Case Race logos/branding
  - YouTube channel links
  - Social media integration
- **Complexity:** Low - similar to AI page structure

**2. About/Personal Page**
- **Status:** Not built yet
- **Priority:** Low (personal pillar is 2/10 importance)
- **What's needed:**
  - Personal background (Cincinnati, family, interests)
  - Professional bio (third-person)
  - Contact information
  - Minimal photo usage
- **Complexity:** Low - simple page

**3. Global Navigation**
- **Status:** Not implemented
- **Priority:** Medium (important for multi-page site)
- **What's needed:**
  - Consistent navigation bar across all pages
  - Logo/home link
  - Links: AI | Case Race | About | Contact
  - Sticky/fixed on scroll
  - Mobile hamburger menu
- **Complexity:** Medium - requires updating all existing pages

**4. Blog Content**
- **Status:** Infrastructure ready, content sparse
- **Priority:** Medium
- **What's needed:**
  - Regular "Generative Blog" posts (dictated to AI, written by AI)
  - Consistent post template
  - Blog listing page enhancement
  - Categories/tags (future)
- **Complexity:** Low per post, ongoing effort

---

## Technical Debt & Refactoring Opportunities

### 🔧 Code Quality Issues

**1. Style Duplication**
- **Issue:** Cosmic button styles repeated in every HTML file
- **Impact:** Hard to maintain consistency, larger file sizes
- **Solution:** Extract to shared `docs/styles.css`
- **Priority:** Medium

**2. JavaScript Duplication**
- **Issue:** Carousel JavaScript duplicated in each page
- **Impact:** Maintenance burden, larger files
- **Solution:** Extract to shared `docs/scripts.js`
- **Priority:** Medium

**3. No Template System**
- **Issue:** Navigation/footer will need manual updates across all pages
- **Impact:** Time-consuming, error-prone updates
- **Solution:** Build process with templates OR accept manual approach
- **Priority:** Low (only 3-4 pages currently)

**4. Legacy Files in Root**
- **Issue:** `index.html` and `styles.css` in root are not used (legacy)
- **Impact:** Confusion, outdated code sitting around
- **Solution:** Delete or archive
- **Priority:** Low

---

## Content Gaps

### 📝 Missing Content

**1. AI Services Description**
- **Status:** Not written yet
- **Need:** Clear description of what AI consulting/services Dr. Hump offers
- **Location:** Should go on AI page
- **Priority:** High (key for potential clients)

**2. Contact Form**
- **Status:** Not implemented
- **Need:** Way for visitors to reach out (beyond email links)
- **Location:** AI page and/or dedicated Contact page
- **Priority:** Medium
- **Options:** Formspree, Netlify Forms, or simple mailto link

**3. Generative Blog Posts**
- **Status:** Only 2 sample posts exist
- **Need:** Regular content to populate blog
- **Process:** Jarrod dictates to AI, AI writes
- **Priority:** Medium (ongoing)

**4. Case Race Content**
- **Status:** Not written
- **Need:** Explanation, links, branding, why it matters
- **Priority:** Medium (needed before Case Race page can be built)

---

## Design Polish Opportunities

### 🎨 Visual Enhancements

**1. Favicon**
- **Status:** Not set
- **Need:** Small icon for browser tab
- **Priority:** Low (nice-to-have)

**2. Open Graph / Social Meta Tags**
- **Status:** Not implemented
- **Need:** Better link previews when shared on social media
- **Priority:** Low (not currently sharing)

**3. Testimonial Carousel Auto-rotation**
- **Status:** Manual navigation only (arrows)
- **Option:** Add auto-rotation every 10-15 seconds
- **Priority:** Low (current implementation works fine)

**4. Loading States**
- **Status:** No loading indicators
- **Need:** Visual feedback while images load
- **Priority:** Low (site loads fast enough)

---

## Recent Development Trajectory

### Last 10 Commits Focus Areas
1. **Agentic blog infrastructure** - Setting up blog framework
2. **UI polish** - Removing carousel dots, adjusting layouts
3. **Content updates** - D'Artagnan RAG emphasis, testimonials
4. **Homepage refinement** - Prominent AI CTA
5. **AI page enhancements** - Carousels, statistics, client logos
6. **Performance optimization** - Smaller background image
7. **Visual theme** - Space background, cosmic buttons
8. **Asset organization** - Moving files to /docs

**Pattern:** Iterative refinement of existing pages, not adding new pages yet

---

## Recommended Next Steps

### Short-term (Next 1-2 Sessions)

**High Priority:**
1. ✅ **Create `/doctorhump-context` documentation** (THIS SESSION)
   - Overview, architecture, styles, deployment, priorities
   - Slash command for quick onboarding

2. **Extract shared styles to docs/styles.css**
   - Move cosmic button styles
   - Move carousel styles
   - Move common layout styles
   - Update all HTML files to reference external CSS
   - **Benefit:** Easier maintenance, consistency

3. **Add global navigation bar**
   - Design navigation component
   - Add to all existing pages (index.html, ai.html, blog.html)
   - Make responsive (hamburger on mobile)
   - **Benefit:** Better UX, clear site structure

**Medium Priority:**
4. **Write AI services content**
   - Define what consulting/services are offered
   - Add section to AI page
   - Include contact CTA
   - **Benefit:** Actionable for potential clients

5. **Build Case Race page**
   - Create docs/case-race.html (or similar)
   - Write content explaining Case Race
   - Add logos, links to game, YouTube, social
   - Match space theme and design system
   - **Benefit:** Complete the three-pillar promise

### Medium-term (Next Few Weeks)

6. **Populate blog with content**
   - Write/dictate 3-5 generative blog posts
   - Establish posting rhythm
   - Enhance blog listing page
   - **Benefit:** Fresh content, SEO, thought leadership

7. **Build About/Personal page**
   - Simple page with personal background
   - Third-person bio
   - Minimal photos
   - **Benefit:** Complete site map

8. **Refactor JavaScript**
   - Extract carousel logic to shared file
   - Reduce duplication
   - **Benefit:** Cleaner code, easier maintenance

### Long-term (Aspirational)

9. **Clean URLs**
   - Configure Azure for /ai instead of /ai.html
   - Update file structure if needed
   - **Benefit:** More professional URLs

10. **Analytics setup**
   - Decide on analytics platform (if desired)
   - Implement tracking
   - **Benefit:** Understand visitor behavior

11. **Template system / build process**
   - If site grows significantly
   - Automate repetitive HTML
   - **Benefit:** Scalability

---

## Open Questions & Decisions Needed

### 🤔 Awaiting Jarrod's Input

**Content:**
- What specific AI consulting services should be listed on AI page?
- What Case Race content exists that can be used for new page?
- How often should generative blog posts be created?

**Design:**
- Should navigation be sticky/fixed on scroll or static?
- Preference for hamburger menu icon style on mobile?
- Any photos of Jarrod to use on About page?

**Features:**
- Contact form service preference (Formspree, other)?
- Analytics desired (Google Analytics, Plausible, none)?
- Newsletter signup (future consideration)?

**Technical:**
- Is GitHub repository private or public?
- Who has access to Azure deployment settings?
- Domain registrar details (for DNS troubleshooting)?

---

## Success Metrics

### How We'll Know We're Done (for v1.0)

- [ ] All three pillars have dedicated pages (AI ✅, Case Race ❌, Personal ❌)
- [ ] Global navigation works across all pages
- [ ] AI services clearly described with contact method
- [ ] Blog has 5+ posts published
- [ ] Mobile responsive across all pages ✅
- [ ] Code is maintainable (shared CSS/JS extracted)
- [ ] No major technical debt blocking progress
- [ ] Jarrod's personal brand "flows through the website" ✅ (partially)

---

## Known Constraints

**Time:** Jarrod is busy (professor, consultant) - development is iterative
**Resources:** Solo project (Jarrod + Claude Code) - no team
**Budget:** Minimal (static site, free hosting tier likely)
**Complexity:** Intentionally simple - static HTML, no backend
**SEO:** Not a current priority - direct traffic expected

---

## Notes for Future Sessions

**When starting a new Claude Code session:**
1. Run `/doctorhump-context` to load all context
2. Review this current-priorities.md file for latest status
3. Ask Jarrod what he wants to work on today
4. Update this file if priorities shift

**Communication pattern:**
- Jarrod dictates high-level goals
- Claude explores codebase, proposes implementation
- Iterative back-and-forth
- Commit frequently with descriptive messages

**Working style:**
- Start simple, enhance over time
- Don't over-engineer
- Test locally before pushing
- Keep design consistent with established patterns
- Update documentation as we go
