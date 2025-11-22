# doctorhump - Design & Style Guidelines

## Visual Identity

### Three Adjectives
**Simplistic, Beautiful, Cool**

These three words should guide every design decision on doctorhump.com.

---

## Color Palette

### Primary Colors: Ice Theme
**Cool grays and blues - "almost like ice"**

From current implementation:
- **Deep Space Blue:** `#03001e` (dark backgrounds in cosmic buttons)
- **Dark Gray:** `#2d3748` (headings, primary text)
- **Medium Gray:** `#4a5568` (subtitles, secondary text)
- **Light Gray:** `#718096` (tertiary text, context)
- **Divider Gray:** `#cbd5e0` (subtle dividers)

### Accent Colors: Warm Amber Gradient
Used sparingly for emphasis:
- **Warm Amber:** `#e8a560`
- **Burnt Orange:** `#c86d3a`
- **Deep Brown:** `#2a1810`

**Usage:** Statistics, initiative titles, featured links - adds warmth against ice colors

### Space/Cosmic Theme Colors
- **Purple Gradient:** `#667eea` to `#764ba2` (buttons - consider phasing out)
- **White Overlays:** `rgba(255, 255, 255, 0.85)` for containers over space background
- **Black Shadows:** `rgba(0, 0, 0, 0.3)` for depth and elevation

### What to AVOID
- ❌ Red/green combinations (legacy Christmas colors in root styles.css)
- ❌ Highly saturated colors (keep it cool and muted)
- ❌ Too many accent colors (ice + amber is enough)

---

## Typography

### Font Family
**Primary:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`

**Why:** System fonts for fast loading, clean appearance, broad compatibility

### Heading Styles

**H1 - Main Page Titles**
```css
font-size: 3rem - 3.5rem (desktop), 2rem - 2.5rem (mobile)
font-weight: 700
color: #2d3748
letter-spacing: -1px
margin-bottom: 10px
```

**H2 - Section Headings**
```css
font-size: 1.5rem
font-weight: 600
color: #2d3748
margin-bottom: 30px
text-align: center
```

### Body Text
```css
font-size: 1rem - 1.1rem
line-height: 1.6 - 1.8
color: #2d3748
```

### Subtitles/Metadata
```css
font-size: 0.9rem - 1rem
color: #4a5568 or #718096
font-weight: 500
```

### Special Text Treatments
- **Italics:** For testimonial quotes
- **Bold (700):** For statistics, testimonial authors
- **Gradient text:** For emphasized titles using warm amber gradient
  ```css
  background: linear-gradient(80deg, #e8a560, #c86d3a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  ```

---

## Layout Principles

### Container Pattern
All content should live in centered, semi-transparent containers:

```css
background: rgba(255, 255, 255, 0.85);
border-radius: 20px;
padding: 60px 50px (desktop), 40px 30px (mobile);
max-width: 600px - 900px;
box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
```

**Why:** Creates depth against space background, readable text, elegant framing

### Spacing System
- **Section margins:** 40px - 60px between major sections
- **Element margins:** 20px - 30px between related elements
- **Padding:** 20px - 50px inside containers
- **Dividers:** 1px gradient lines with 30px - 40px vertical margin

### Grid Layouts
- **Statistics bar:** 4 columns on desktop, 2 columns on mobile/tablet
- **Link buttons:** 2 columns on desktop, 1 column on mobile
- **Carousels:** Full-width with controlled content area

---

## Component Styles

### Buttons: Cosmic Space Theme

**The signature design element** - buttons with animated shooting stars

**Structure:**
```html
<div class="btn-container">
  <a href="..." class="space-btn">
    <span>Button Text</span>
    <div class="star" style="..."></div>
    <!-- Multiple stars -->
    <div class="shooting-star shooting-star-1"></div>
    <!-- Multiple shooting stars -->
  </a>
</div>
```

**Visual Effect:**
- Gradient background: `linear-gradient(80deg, #e8a560, #c86d3a, #2a1810, #03001e)`
- Twinkling star dots scattered across button
- Animated shooting stars that streak diagonally
- Glow effect on hover (blur shadow appears)
- Scale up on hover (1.1x)
- Rounded corners (12px)

**Interaction:**
- Hover: Scale + glow + shooting stars become visible
- Active/Click: Scale back to 1x, glow disappears
- Smooth transitions (0.6s cubic-bezier)

**Usage:**
- Primary CTAs (AI Leadership link)
- Contact/social links
- Navigation elements

### Carousels

**Two types implemented:**

**1. Auto-scrolling Logo Carousel** (client logos)
- Continuous horizontal scroll
- Pauses on hover
- Seamless loop (duplicated items)
- Individual logos scale up on hover
- White cards with subtle shadows

**2. Manual Navigation Carousels** (testimonials, initiatives)
- Left/right arrow buttons
- Fade-in transitions between slides
- Circular navigation dots below (optional)
- White/translucent background
- Centered content

**Common styling:**
```css
background: rgba(255, 255, 255, 0.5);
border-radius: 16px;
padding: 40px - 50px;
min-height: 300px - 350px;
```

### Statistics Display
- Large gradient numbers (2.5rem, warm amber gradient)
- Small gray labels below
- White/translucent background cards
- Hover: Slight lift (translateY -3px)
- Grid layout, centered text

### Testimonials
- Italic quote text (1.1rem - 1.3rem)
- Bolded author name
- Lighter context/role text
- Centered alignment
- Generous padding for readability

### Dividers
```css
height: 1px;
background: linear-gradient(to right, transparent, #cbd5e0, transparent);
margin: 30px - 40px vertical;
```

**Purpose:** Subtle section separation without heavy visual weight

---

## Backgrounds

### Primary Background: Space Theme
**James Webb Telescope image** (`james-webb-background_smallest.jpg`)

```css
background-image: url('james-webb-background_smallest.jpg');
background-size: cover;
background-position: center;
background-attachment: fixed;
background-repeat: no-repeat;
```

**Why:**
- Cool, interesting, unique
- Aligns with "space" theme request
- Not typical academic website
- Provides depth and visual interest
- Fixed attachment creates parallax effect

**Optimization:** Using smallest optimized version for fast loading

---

## Responsive Design

### Breakpoints
```css
@media (max-width: 768px) { /* Tablet/Mobile */ }
@media (max-width: 600px) { /* Mobile only */ }
```

### Mobile Adaptations
- Reduce font sizes (h1: 3.5rem → 2.5rem)
- Reduce padding (60px → 40px → 30px)
- Stack grids vertically (2 cols → 1 col)
- Smaller buttons
- Reduce carousel padding
- Adjust logo sizes in carousel
- Stack initiative carousel content vertically (image on top)

---

## Animation & Motion

### Principles
- **Subtle, not distracting:** Animations enhance, don't overwhelm
- **Purposeful:** Every animation has a reason (feedback, delight, clarity)
- **Smooth timing:** cubic-bezier(0.15, 0.83, 0.66, 1) for organic feel

### Key Animations

**Fade In (page load):**
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

**Button Hover:**
- Scale transform (1.0 → 1.1)
- Shadow blur increase
- Shooting star activation

**Carousel Transitions:**
- Fade in new slide (0.5s)
- Fade out old slide

**Auto-scroll:**
- Linear continuous movement
- 45s full cycle
- Pause on hover

**Blinking Stars:**
```css
@keyframes blink {
  0%, 100% { box-shadow: 0 0 10px 0 white; }
  50% { box-shadow: 0 0 10px 2px white; }
}
```

**Shooting Stars:**
- Diagonal movement (top-right → bottom-left)
- Fade in at start, fade out at end
- Staggered timing for variety
- Looping animation

---

## Design Philosophy Reminders

### What doctorhump.com IS
✅ **Cool and unique** - space theme, cosmic buttons, interesting visuals
✅ **Clean and uncluttered** - white space, clear hierarchy, focused content
✅ **Professional** - credible, polished, well-designed
✅ **Approachable** - friendly tone, not stuffy or overly academic
✅ **Beautiful** - aesthetically pleasing, design matters

### What doctorhump.com is NOT
❌ **Boring academic website** - no gray walls of text, no lifeless layouts
❌ **Highly stylized marketing site** - not flashy, not sales-y, not corporate
❌ **Cluttered** - avoid too many elements competing for attention
❌ **Photo-heavy** - minimal photos of Jarrod, focus on graphics and text
❌ **Generic template site** - custom design that reflects Dr. Hump's personality

---

## Consistency Checklist

When adding new pages or components, ensure:

- [ ] Space background (James Webb image)
- [ ] Semi-transparent white container (rgba(255, 255, 255, 0.85))
- [ ] Rounded corners (12px - 20px)
- [ ] Cool gray/blue color palette (ice theme)
- [ ] System font stack
- [ ] Responsive breakpoints (@768px, @600px)
- [ ] Cosmic button style for CTAs (if applicable)
- [ ] Subtle animations with smooth easing
- [ ] Gradient dividers between sections
- [ ] Warm amber accents for emphasis (sparingly)
- [ ] Box shadows for depth (0 20px 60px rgba(0, 0, 0, 0.3))

---

## Future Refinements

### Potential Style Improvements
- Extract cosmic button styles to shared CSS file (avoid duplication)
- Create CSS custom properties (variables) for colors
- Standardize spacing scale (e.g., 8px base unit)
- Create reusable component classes
- Consider CSS animations for page transitions

### Accessibility Considerations
- Ensure sufficient color contrast for readability
- Add focus states for keyboard navigation
- Consider reduced motion preferences
- Alt text for all images
- Semantic HTML structure

### Performance
- Optimize space background image further
- Consider lazy loading for below-fold images
- Minimize CSS/JS payload
- Use CSS transforms for animations (GPU acceleration)
