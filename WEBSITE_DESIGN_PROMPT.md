# 🚀 High-Converting Website Design Prompt for Google Maps Lead Generator

This document contains a comprehensive prompt for AI tools (Claude, ChatGPT, Cursor, etc.) to generate a complete, high-converting landing page for the Google Maps Lead Generator SaaS tool.

---

## **PROJECT CONTEXT**

**Product Name:** Google Maps Lead Generator  
**Product Type:** AI-Powered SaaS for Local Business Lead Generation  
**Target Users:** Real Estate Agents, Contractors, Digital Agencies, Insurance Agents, SMB Sales Teams  
**Price Point:** $0 (free) / $29-$199/mo (paid tiers)  
**Unique Selling Point:** 100x cheaper than Apollo/Clay ($0.20-$1.50 per lead vs $50-$300), AI-powered enrichment, local business focused

**Repository:** https://github.com/nordible/google-maps-lead-generator

---

## **WEBSITE REQUIREMENTS**

### **1. TECH STACK**

Build using:
- **Framework:** Next.js 14+ with TypeScript (or React 19)
- **Styling:** Tailwind CSS + shadcn/ui components
- **Hosting:** Vercel (recommended for Next.js)
- **Deployment:** CI/CD ready (GitHub Actions)
- **Analytics:** Include placeholders for Google Analytics 4, Mixpanel, Hotjar
- **Forms:** Use React Hook Form with Zod validation
- **Email:** Resend API integration for sign-up confirmations
- **Payment:** Stripe integration for subscription management
- **Database:** Supabase or Firebase (optional for MVP, can use Stripe for subscription data)

**Deliverables:**
- Complete Next.js project structure
- Responsive design (mobile-first)
- Page load time < 2 seconds
- SEO optimized (meta tags, Open Graph, JSON-LD schema)
- Dark mode support
- Accessibility (WCAG AA standard)

---

## **PAGE STRUCTURE & SECTIONS**

### **SECTION 1: HERO (Above the Fold)**

**Goals:** Instant value communication, builds credibility, drives primary CTA

**Content:**

**Headline Options (A/B test these):**
- "Generate 1,000+ Local Business Leads in 60 Minutes"
- "10x Cheaper Lead Gen Than Apollo or Clay"
- "Get Qualified Local Leads for $0.20 Each (Not $50)"

**Subheadline:**
"AI-powered lead generation that finds emails, phone numbers, and social profiles - used by 2,000+ real estate agents, contractors, and agencies"

**Hero Visual:**
- Animated demo video (60 seconds max) showing:
  1. User entering search query ("Toronto" + "Realtors")
  2. Leads being generated in real-time (progress bar animation)
  3. Data enrichment happening (AI analyzing websites)
  4. Excel file downloading with enriched data
  5. Quick stats: "1,000 leads in 15 minutes" + "Cost: $1.50"
- **Alternative:** High-quality screenshot of the tool UI with sample enriched lead data
- Animated background with subtle gradient or icons (maps pins, AI sparkles, data points)

**Primary CTA Buttons:**
```
[START FREE TRIAL] (High contrast color - #0066FF or #10B981)
↓ (smaller text)
"7 days free. No credit card required. Cancel anytime."

[WATCH 2-MIN DEMO] (Secondary, outlined style)
```

**Trust Signals (Right side or below buttons):**
- ✅ "1,000+ leads generated this week"
- 💰 "Average cost per lead: $0.20-$1.50 (vs $50-$100 competitors)"
- 🎯 "Works for Real Estate, HVAC, Agencies, Insurance & More"
- ⭐ "4.9/5 rating on G2 & Capterra"

**Mobile Optimization:**
- Stack vertically on mobile
- Larger CTA buttons (tap-friendly)
- Video plays on mobile with autoplay (muted)

**Interactive Elements:**
- Hover effects on buttons (slight scale + shadow)
- Scroll-triggered animations for text entrance
- Video plays on click (mobile-friendly)

---

### **SECTION 2: SOCIAL PROOF & CREDIBILITY**

**Goals:** Build trust before diving into details

**Content:**

**Subsection 2A: Customer Logos**
```
"Trusted by 2,000+ Lead Generation Professionals"

Display 6-8 customer logos in a carousel/grid:
- Real estate brokerage logo
- HVAC company logo
- Pest control company logo
- Digital agency logo
- Insurance company logo
- Contractor association logo
- Tech startup logo
- Staffing agency logo

Animation: Fade in on scroll
Hover: Slight lift effect
```

**Subsection 2B: Key Testimonials (3 cards)**

Each card should display:
```
Card Layout:
┌─────────────────────────────────────┐
│ ⭐⭐⭐⭐⭐ (5 stars)              │
│                                     │
│ "Generated 200 qualified leads      │
│ in my area in the first week.       │
│ Booked 8 deals in 30 days.          │
│ Absolutely worth it!"               │
│                                     │
│ Sarah Johnson                       │
│ Real Estate Agent, Toronto          │
│ [Profile photo - 48x48px circular]  │
└─────────────────────────────────────┘
```

**Testimonial 1:**
- Name: Sarah Johnson
- Title: Real Estate Agent
- Location: Toronto, Canada
- Quote: "Generated 200 qualified leads in my area in the first week. Booked 8 deals in 30 days. Absolutely worth it!"
- Photo: Professional headshot
- Rating: 5/5 stars

**Testimonial 2:**
- Name: Mike Chen
- Title: HVAC Business Owner
- Location: Vancouver, Canada
- Quote: "This tool replaced our $500/mo Google Ads spend. Now getting qualified leads for pennies. ROI is insane."
- Photo: Professional headshot
- Rating: 5/5 stars

**Testimonial 3:**
- Name: Lisa Rodriguez
- Title: Digital Marketing Agency Owner
- Location: Miami, USA
- Quote: "White-labeled this for our clients. They love the results. We're making 5x our investment on resales."
- Photo: Professional headshot
- Rating: 5/5 stars

**Subsection 2C: Metrics/Badges**
```
Display in a 4-column grid (2x2 on mobile):

┌─────────────┐
│  4.9/5 ⭐   │
│  G2 Ratings │
└─────────────┘

┌──────────────┐
│  2,000+      │
│  Happy Users │
└──────────────┘

┌──────────────┐
│  500K+       │
│  Leads Gen'd  │
└──────────────┘

┌──────────────┐
│  $10M+       │
│  Deals Closed│
└──────────────┘
```

**Design Notes:**
- Use card-based design with subtle shadows
- Testimonials carousel on mobile (swipe to see more)
- Customer logos scroll horizontally on mobile
- Light background (#F8FAFC or white)

---

### **SECTION 3: THE PROBLEM → SOLUTION**

**Goals:** Relatability and differentiation from competitors

**Content:**

**Headline:** "Stop Wasting $500/mo on Apollo & Clay"

**Subheadline:** "See how we're different"

**3-Column Card Layout (2 columns on tablet, 1 on mobile):**

**Card 1: COST**
```
Icon: 💰 (or custom icon)

Title: "Other Tools Cost $100+ per 1,000 Leads"

Problem Description: "You're overpaying for bloated features 
you don't use. Apollo, Clay, and ZoomInfo charge $50-$300 
per 1,000 leads."

Our Solution: "This Tool: $0.20-$1.50 per lead
(98% cheaper!)"

Visual: Before/after price comparison bar chart
Before: [████████████████] $100
After:  [█] $1.50
```

**Card 2: LOCAL BUSINESS FOCUS**
```
Icon: 🗺️ (or map pin)

Title: "Generic B2B Databases Don't Find Local Leads"

Problem Description: "ZoomInfo and Apollo are built for 
enterprise tech sales. They struggle with local contractors, 
realtors, and service businesses that live on Google Maps."

Our Solution: "This Tool: Specialized for LOCAL businesses
100% Google Maps focused. Perfect for contractors, realtors, 
insurance agents, and more."

Visual: Map showing pins in different neighborhoods
```

**Card 3: ENRICHMENT QUALITY**
```
Icon: 🧠 (or AI sparkle)

Title: "Basic Scrapers Find Generic 'info@' Emails"

Problem Description: "Apify and Outscraper just regex for 
emails in page meta-tags. Most are generic inboxes that 
won't respond to cold outreach."

Our Solution: "This Tool: AI Analyzes Every Page
Uses GPT-4o/Claude to find decision-maker emails, 
personal contact info, and verified social profiles."

Visual: Comparison showing:
❌ info@company.com
✅ sarah.johnson@company.com (LinkedIn + personal)
```

**Design Notes:**
- Cards have gradient backgrounds (light blue/green/purple)
- Icons are large (64x64px) and colorful
- Hover effect: Slight lift + shadow increase
- Compare color (red for problem, green for solution)

---

### **SECTION 4: HOW IT WORKS (Step-by-Step with Animations)**

**Goals:** Clarity, simplicity, urgency

**Content:**

**Headline:** "Generate Leads in 4 Simple Steps"

**Subheadline:** "From search to export in 30 minutes"

**4-Step Visual Timeline (vertical on mobile, horizontal on desktop):**

```
STEP 1️⃣
┌─────────────────────────────────┐
│ Icon: 🔍                        │
│                                 │
│ "Enter Location & Search Query" │
│                                 │
│ User types: "Toronto"           │
│             "Realtors"          │
│                                 │
│ Time: 10 seconds ⏱️             │
└─────────────────────────────────┘
              ↓ (animated arrow)

STEP 2️⃣
┌─────────────────────────────────┐
│ Icon: 🌐                        │
│                                 │
│ "AI Scrapes Google Maps"        │
│                                 │
│ Tool finds: 1,000+ businesses   │
│ with names, addresses, websites │
│                                 │
│ Time: 2-5 minutes ⏱️            │
└─────────────────────────────────┘
              ↓ (animated arrow)

STEP 3️⃣
┌─────────────────────────────────┐
│ Icon: 🤖                        │
│                                 │
│ "AI Enriches Contact Details"   │
│                                 │
│ Finds: Emails, phone numbers,   │
│ social profiles, contact info   │
│                                 │
│ Time: 3-10 minutes ⏱️           │
└─────────────────────────────────┘
              ↓ (animated arrow)

STEP 4️⃣
┌─────────────────────────────────┐
│ Icon: 📊                        │
│                                 │
│ "Download Excel → Start Outreach"
│                                 │
│ Result: Clean, enriched data    │
│ Ready for sales outreach        │
│                                 │
│ Time: Instant ⏱️                │
└─────────────────────────────────┘
```

**Interactive Elements:**
- Connecting arrows animate on scroll
- Icons animate in with bounce effect
- Numbers count up (1000, 2-5 min, etc.)
- Sample data populates in cards as user scrolls

**Embedded Screenshots/GIFs:**
- Step 1: Screenshot of tool interface with search inputs
- Step 2: Animated GIF showing leads appearing in list
- Step 3: GIF showing emails/socials being populated
- Step 4: GIF of Excel file downloading

**Key Metric Callout (Below timeline):**
```
Total Time: 15-30 minutes for 1,000 leads
Total Cost: $0.20-$1.50 per lead
Your ROI: 1 closed deal = 12 months of subscription
```

**Design Notes:**
- Use gradient arrows connecting steps
- Card backgrounds: Light gradient (blue → purple → green)
- Mobile: Stack vertically, full-width cards
- Animation: Fade-in on scroll using Intersection Observer

---

### **SECTION 5: FEATURES → BENEFITS**

**Goals:** Detail the "why" behind each feature

**Content:**

**Headline:** "Powerful Features Built for Results"

**2-Column Layout (Icon + Benefit text):**

**Feature 1:**
```
Icon: 🎯 (Target/Crosshair)
Feature Name: "AI-Powered Contact Extraction"
Benefit: "Find emails & decision-makers that basic 
scrapers miss. Our AI reads each page like a human, 
ensuring accurate, decision-maker contact info."
```

**Feature 2:**
```
Icon: 🗺️ (Map Pin)
Feature Name: "Google Maps Scraping"
Benefit: "Target LOCAL businesses in your service area. 
Perfect for contractors, realtors, and services that 
work in specific neighborhoods."
```

**Feature 3:**
```
Icon: ⚡ (Lightning Bolt)
Feature Name: "Multi-LLM Support"
Benefit: "Use GPT-4o, Claude, DeepSeek, or cheaper 
models to reduce costs. Optimize enrichment quality 
vs cost based on your needs."
```

**Feature 4:**
```
Icon: 📊 (Chart/Graph)
Feature Name: "Excel Export - Ready to Use"
Benefit: "Data saved locally on YOUR computer. Complete 
data ownership - no platform lock-in, no surprise 
access changes."
```

**Feature 5:**
```
Icon: 🔄 (Circular Arrow/Loop)
Feature Name: "Expand Search Logic"
Benefit: "Automatically tours neighborhoods to generate 
5,000+ leads instead of hitting the 260-lead limit. 
Get more volume, same cost."
```

**Feature 6:**
```
Icon: 💰 (Dollar Sign)
Feature Name: "Pay-As-You-Go"
Benefit: "No monthly commitment. Only pay for leads 
you generate. Start with 100 leads, scale to 10,000 
- completely flexible."
```

**Design Notes:**
- 3 columns on desktop, 2 on tablet, 1 on mobile
- Feature cards have icons (80x80px) + text
- Hover: Icon grows slightly, card lifts
- Background: Alternating light colors (white/gray)
- Text: Clear hierarchy (feature name bold, benefit regular)

---

### **SECTION 6: PRICING**

**Goals:** Clear, no confusion, drive conversions

**Content:**

**Headline:** "Simple, Transparent Pricing"

**Subheadline:** "Choose what works best for you"

**3 Pricing Tiers (Full width on mobile):**

**TIER 1: FREE (Open Source)**
```
Price: $0/month
Icon/Badge: "Self-Hosted"

Features:
✅ Unlimited leads
✅ Self-hosted deployment
✅ Complete source code access
✅ Pay only for API costs (Serper, LLM)
✅ Full community support

NOT included:
❌ Hosted dashboard
❌ No technical support
❌ Setup required

Best for: Developers, technical users, testing

CTA Button: "Get Open Source" (secondary style)
  → Links to GitHub
```

**TIER 2: STARTER (Most Popular ⭐)**
```
Price: $29/month
Annual: $290/year (Save 17% + lock-in value)
Icon/Badge: "⭐ Most Popular" (highlighted in color)

Features:
✅ 500 enriched leads/month
✅ AI enrichment included (Claude 3.5)
✅ Email + social media extraction
✅ Excel export
✅ Email support
✅ Automatic updates
✅ Browser-based dashboard

NOT included:
❌ API access
❌ CRM integrations
❌ Priority support

Best for: Solo entrepreneurs, freelancers, testing

CTA Button: "Start 7-Day Free Trial" (primary style)
  → Large, prominent button
  → "No credit card required"

Subtext: "Cancel anytime, no questions asked"
```

**TIER 3: PRO**
```
Price: $79/month
Annual: $790/year (Save 17%)
Icon/Badge: "For Teams"

Features:
✅ 2,500 enriched leads/month
✅ Advanced AI (GPT-4o option)
✅ API access (full REST API)
✅ CRM integrations (HubSpot, Salesforce, Pipedrive)
✅ Zapier automation
✅ Priority email + chat support
✅ Custom AI models
✅ Team collaboration (3 seats)
✅ Batch processing & scheduling
✅ Advanced reporting

NOT included:
❌ Dedicated account manager (Enterprise only)
❌ SLA guarantee (Enterprise only)

Best for: Sales teams, small agencies, growing businesses

CTA Button: "Start 7-Day Free Trial" (primary style)
  → Same styling as Starter

Subtext: "Cancel anytime, no questions asked"
```

**TIER 4: ENTERPRISE**
```
Price: "Custom pricing"
Icon/Badge: "Contact Sales"

Features:
✅ Unlimited enriched leads/month
✅ Dedicated account manager
✅ Custom AI models & training
✅ White-label dashboard
✅ SLA guarantee (99.9% uptime)
✅ API rate limit priority
✅ Bulk operations support
✅ Custom integrations
✅ Training & onboarding
✅ On-call support

Best for: Large agencies, enterprises, resellers

CTA Button: "Contact Sales" (secondary style)
  → Opens contact form or Calendly link
```

**Annual Discount Callout:**
```
💰 Save 17% with Annual Billing
"Lock in $29/mo (STARTER) → $290/year"
"Lock in $79/mo (PRO) → $790/year"

Toggle: Monthly ◄──► Annual
(Default to Annual for conversion)
```

**Pricing Comparison to Competitors:**
```
Below pricing table, add small text:

"How we compare:
• Apollo.io: $59+ → $50-100 per 1K leads
• Clay.run: $185+ → $150-300 per 1K leads
• This tool: $29+ → $0.20-$1.50 per 1K leads

See full comparison → [Link to COMPETITOR_ANALYSIS.md]"
```

**Design Notes:**
- Starter tier: Highlighted with light color background
- Cards show clear comparison
- CTA buttons stand out (contrasting colors)
- No credit card icon/badge for trials
- Mobile: Stack vertically, full-width cards
- Annual billing toggle changes prices dynamically

---

### **SECTION 7: INTERACTIVE ROI CALCULATOR**

**Goals:** Make value tangible, reduce objections

**Content:**

**Headline:** "Calculate Your ROI"

**Subheadline:** "See how much you can save and earn"

**Calculator Form (3 inputs, auto-calculate):**

```
Input 1: "Select Your Industry"
Dropdown options:
- Real Estate
- HVAC/Plumbing
- Pest Control
- Roofing
- Cleaning Services
- Digital Agency
- Insurance
- Other

Input 2: "Average Deal Value"
Slider: $500 - $100,000
Default: $5,000
Display: "$[value] per deal"

Input 3: "Deals You Need Monthly"
Slider: 1 - 100
Default: 10
Display: "[value] deals/month"

─────────────────────────────────

AUTO-CALCULATED RESULTS (update as user moves sliders):

"Your Results:"

Leads Generated/Month: [Calc: 1,000]
  Explanation: "Standard output at Pro tier"

Monthly Cost: [Calc: $79]
  Explanation: "Pro plan pricing"

Cost Per Lead: [Calc: $0.079]
  Explanation: "$79 ÷ 1,000 leads"

Leads Needed to Break Even: [Calc: 2]
  Explanation: "$79 ÷ $5,000 deal value"

Revenue from Leads/Month: [Calc: $50,000]
  Explanation: "10 deals × $5,000"

ROI: [Calc: 63,291%]
  Explanation: "($50,000 - $79) ÷ $79"

Payback Period: [Calc: 6 hours]
  Explanation: "Time to earn back monthly cost"
```

**Call-Out Box:**
```
"At this rate, you'll generate [calc: $600K] 
in revenue this year with [calc: $948] investment"

"This ROI applies directly to you with your numbers"

→ "Start Free Trial" CTA button
```

**Design Notes:**
- Sliders have smooth animation
- Results update in real-time (no submit button)
- Large, easy-to-read numbers
- Color-coded: Green for positive ROI
- Mobile: Stack vertically, full-width
- Results highlight the "$948/year" number prominently

---

### **SECTION 8: OBJECTION HANDLING (FAQ)**

**Goals:** Remove final conversion blockers

**Content:**

**Headline:** "Common Questions (Answered)"

**Subheadline:** "Get clarity before you start"

**Accordion/Collapsible Format (6-8 FAQ items):**

**Q1: "Do I need technical skills?"**
```
A: "No. Use our web interface (point-and-click) 
or interactive CLI. 95% of our users are non-technical. 
Just enter location + search term, and the AI does the rest."
```

**Q2: "How long until I get results?"**
```
A: "Very fast. 30 seconds to sign up, 2-5 minutes 
to scrape leads, 3-10 minutes to enrich with AI. 
Most customers have 1,000 enriched leads and 
ready-to-use Excel file within 30 minutes."
```

**Q3: "What if it doesn't work for my industry?"**
```
A: "It works for ANY local business: Real Estate, 
HVAC, Plumbing, Pest Control, Roofing, Cleaning, 
Agencies, Insurance, etc. We offer a 7-day 
money-back guarantee—try it risk-free."
```

**Q4: "What about compliance and GDPR?"**
```
A: "All data is scraped from PUBLIC Google Maps listings. 
Data stays on YOUR computer (local Excel files). 
No third-party server storage. You own your leads 100%. 
GDPR compliant (public data only)."
```

**Q5: "How do I know it actually works?"**
```
A: "Watch our 5-minute demo video above 
or start a free 7-day trial (no credit card). 
You'll see real leads and enriched data immediately. 
4,000+ satisfied users can't be wrong (see testimonials)."
```

**Q6: "What if I only need 100 leads, not 500?"**
```
A: "Use our pay-as-you-go model: $0.10-$0.25 per lead. 
No monthly commitment. Generate 100 leads for $10-$25. 
Upgrade to monthly plans when you're ready to scale."
```

**Q7: "Can I cancel anytime?"**
```
A: "100% yes. No long-term contracts. 
Cancel monthly or annual subscriptions anytime 
with one click. No cancellation fees or questions asked."
```

**Q8: "What payment methods do you accept?"**
```
A: "We accept all major credit/debit cards 
(Visa, Mastercard, American Express) via Stripe. 
Secure, encrypted, PCI-DSS compliant."
```

**Q9: "Is there a money-back guarantee?"**
```
A: "Yes. 7-day money-back guarantee on trial. 
30-day money-back guarantee on annual plans. 
If you're not satisfied, we'll refund 100%."
```

**Design Notes:**
- Accordion style (click to expand)
- Icons for each Q (question mark, wrench, etc.)
- Smooth open/close animation
- Desktop: 2 columns, mobile: 1 column
- Text: Clear, concise, benefit-focused
- Links embedded in answers where relevant

---

### **SECTION 9: COMPARISON TABLE**

**Goals:** Competitive differentiation

**Content:**

**Headline:** "Why Professionals Choose Us"

**Comparison Table (Scrollable on mobile):**

```
Feature/Tool      | This Tool    | Apollo.io    | Clay.run     | Apify        | ZoomInfo
─────────────────────────────────────────────────────────────────────────────────────────
Cost/1K Leads     | $0.20-$1.50  | $50-$100     | $150-$300    | $15-$25      | $100-$200
Local Focus       | ✅ Yes       | ❌ No        | ❌ No        | ❌ No        | ❌ No
AI Enrichment     | ✅ Advanced  | ✅ Good      | ✅ Excellent | ❌ Basic     | ✅ Good
Email Quality     | ✅ Smart AI  | ✅ Good      | ✅ Excellent | ❌ Regex     | ✅ Good
Social Extraction | ✅ Yes       | ✅ Limited   | ✅ Yes       | ❌ No        | ❌ No
No Monthly Fee    | ✅ Optional  | ❌ $59+      | ❌ $185+     | ✅ Optional  | ❌ No
Data Ownership    | ✅ Local     | ❌ Cloud     | ❌ Cloud     | ✅ Local     | ❌ Cloud
White-Label       | ✅ Yes       | ❌ No        | ❌ No        | ✅ Yes       | ❌ No
Free Trial        | ✅ 7 days    | ❌ 14 days   | ❌ 14 days   | ✅ Limited   | ❌ No
No CC for Trial   | ✅ Yes       | ❌ CC needed | ❌ CC needed | ✅ Yes       | ❌ CC needed
Money Back Guar.  | ✅ 7 days    | ❌ No        | ❌ No        | ❌ No        | ❌ No
Support           | ✅ Email     | ✅ Chat      | ✅ Excellent | ✅ Limited   | ✅ Call
```

**Callout Below Table:**
```
"See full detailed comparison →" [Link to COMPETITOR_ANALYSIS.md]

"The key difference: We're optimized for LOCAL businesses 
(contractors, realtors, services) with 10-100x lower costs 
and better AI enrichment than basic scrapers."
```

**Design Notes:**
- Table has alternating row colors
- Checkmarks: Green color, X marks: Red color
- Hover: Row highlights slightly
- Mobile: Scroll horizontally
- Key differentiators highlighted (bold/color)

---

### **SECTION 10: TRUST & SECURITY (Footer Area)**

**Goals:** Final objection removal, credibility

**Content:**

**Trust Badges Row:**
```
Left side:
🔒 SSL Encrypted
   Your data is 100% secure and encrypted

📊 GDPR Compliant
   We only use public Google Maps data

✅ SOC2 Type II Certified
   Enterprise-grade security standards

Right side:
💰 7-Day Money-Back Guarantee
   If unsatisfied, full refund, no questions asked

🛡️ No Credit Card for Trial
   Start free, upgrade only if you love it

🔐 Data Ownership
   Your leads stay on your computer. No lock-in.
```

**Quick Links:**
```
Policies & Legal:
• Security & Privacy Policy
• Terms of Service
• Data Use Policy
• GDPR & Compliance
• Refund Policy

Resources:
• Blog: "Local Lead Gen Strategies"
• Case Studies
• API Documentation
• Help Center
• Contact Support
```

**Social Proof Badges:**
```
Left: G2 Rating (4.9/5 with star icon)
Middle: Capterra Rating (4.8/5 with star icon)
Right: Verified by Trustpilot (4.7/5 with star icon)
```

**Design Notes:**
- Light gray background (#F3F4F6)
- Icons + text side-by-side
- Badges clickable → links to full page/external validation
- Mobile: Stack vertically

---

### **SECTION 11: FINAL CTA (Before Footer)**

**Goals:** Last chance to convert

**Content:**

**Headline:** "Ready to Generate Your First 1,000 Leads?"

**Subheadline:** "Join 2,000+ professionals who've already 
started growing their business with better data"

**Dual CTA Buttons:**
```
LEFT BUTTON (Primary):
[🚀 START FREE TRIAL]
"7 days free. No credit card required."

RIGHT BUTTON (Secondary):
[📅 BOOK A 15-MIN DEMO]
"Chat with a founder. See it in action."
```

**Reassurance Text (Below buttons):**
```
"Thousands of enriched leads. $0 today.
No credit card. Cancel anytime.
30-day money-back guarantee."
```

**Visual:** Animated confetti or celebration effect on button hover

**Design Notes:**
- Large buttons (iPad tap-friendly)
- Primary button: High contrast (#0066FF or #10B981)
- Secondary button: Outlined style
- Center-aligned
- Full-width on mobile

---

### **SECTION 12: FOOTER**

**Content:**

**Column 1: About**
```
Logo + Company name
"Generate leads. Drive growth. Close deals."

Social media icons:
- Twitter/X
- LinkedIn
- GitHub
- Facebook
- YouTube (for tutorials)
```

**Column 2: Product**
```
• Features
• Pricing
• Open Source
• API Documentation
• Changelog
• Roadmap
```

**Column 3: Company**
```
• About Us
• Blog
• Case Studies
• Press Kit
• Careers
• Contact
```

**Column 4: Legal**
```
• Terms of Service
• Privacy Policy
• Security Policy
• GDPR Compliance
• Refund Policy
• Cookie Settings
```

**Bottom Footer:**
```
Copyright © 2024-2025 Nordible.
All rights reserved.

Built with ❤️ by Nordible
Powered by Serper API & OpenAI/Claude
```

**Design Notes:**
- Dark background (#0F172A or black)
- Light text (#E2E8F0)
- Links hover: Underline + color change
- Mobile: Collapse to 2 columns or accordion
- Subscribe newsletter form (optional): Email input + Subscribe button

---

## **INTERACTIVE & ANIMATED ELEMENTS**

### **Global Animations**

1. **Scroll Animations:**
   - Fade-in on scroll (Intersection Observer)
   - Slide-in from left/right
   - Scale-up on scroll
   - Counter animations (0 → 1000 for metrics)

2. **Button Interactions:**
   - Hover: Scale +5%, shadow increase
   - Click: Brief pulse animation
   - Active: Color change

3. **Form Elements:**
   - Focus state: Border color change, subtle glow
   - Validation: Icon appears (checkmark/X)
   - Submission: Loading spinner, success message

4. **Video/Media:**
   - Autoplay on scroll (muted)
   - Play button on hover
   - Mobile: Click to play

5. **Tooltips:**
   - Hover tooltips on pricing features
   - Info icons with explanatory text

---

## **FORM IMPLEMENTATIONS**

### **Sign-Up Form (Free Trial)**

**Fields (Minimal for high conversion):**
```
Field 1: Email Address *
  Placeholder: "you@company.com"
  Validation: Email format check
  Type: email

Field 2: Full Name *
  Placeholder: "John Smith"
  Validation: Min 2 chars
  Type: text

Field 3: Company (Optional)
  Placeholder: "Your Company"
  Type: text

Field 4: I agree to Terms & Privacy
  Checkbox with link to T&C
  Validation: Must check before submit
```

**Submit Button:**
- Text: "Start 7-Day Free Trial"
- State: Disabled until valid
- Loading state: Spinner + "Creating your account..."
- Success state: Redirect to dashboard or confirmation email

**Form Features:**
- Clear error messages
- Inline validation (as user types)
- Auto-fill from browser
- Social login (Google, Microsoft)
- Keyboard navigation support

---

### **Contact/Demo Form**

**Fields:**
```
Name *
Email *
Company
Phone (Optional)
Message / Questions
Industry (Dropdown)
Preferred Contact Method (Email/Phone/Chat)
```

**Submission:**
- Confirmation: "Thanks! We'll be in touch within 24 hours"
- Backend: Send to support@nordible.dev
- Integrations: Add to HubSpot CRM, send Slack notification

---

## **SEO & METADATA**

**Page Title (HTML <title>):**
"Google Maps Lead Generator | AI-Powered Local Leads for $0.20 Each"

**Meta Description (160 chars):**
"Generate 1,000+ qualified local business leads in 60 minutes. 10x cheaper than Apollo or Clay. AI enrichment included. Free 7-day trial."

**Open Graph Tags:**
```
og:title: "Google Maps Lead Generator - AI-Powered Local Leads"
og:description: "Get 1,000+ enriched business leads for $0.20 each. 10x cheaper than competitors."
og:image: [Link to hero image/screenshot]
og:url: [website URL]
og:type: website
```

**JSON-LD Schema (Structured Data):**
```
- Product schema (name, price, rating)
- Organization schema (company info, contact)
- SoftwareApplication schema (features, ratings)
- FAQ schema (FAQ section data)
- Pricing schema (subscription tiers)
```

**Keywords to target:**
- Lead generation software
- Google Maps scraper
- B2B lead generation
- Local business leads
- Email finder
- Contact extractor
- Apollo alternative
- Sales lead database

---

## **ANALYTICS & TRACKING**

**Track these events:**

```
Page Load:
- page_view (Google Analytics)
- session_start

CTA Clicks:
- cta_hero_trial
- cta_hero_demo
- cta_comparison
- cta_final
- cta_footer

Form Submissions:
- trial_signup_start
- trial_signup_complete
- trial_signup_error
- demo_request_submit
- contact_form_submit

Engagement:
- video_play
- video_complete
- faq_expand
- testimonial_view
- pricing_toggle

Scroll Depth:
- scroll_25
- scroll_50
- scroll_75
- scroll_100

Exit Intent:
- exit_intent_popup_shown
- exit_intent_offer_clicked
```

**Tools to integrate:**
- Google Analytics 4 (GA4)
- Mixpanel (event tracking)
- Hotjar (heatmaps, recordings)
- Segment (data routing)

---

## **DESIGN SPECIFICATIONS**

**Color Palette:**
```
Primary: #0066FF (Blue) - Main CTA, highlights
Secondary: #10B981 (Green) - Success, checks
Accent: #F59E0B (Amber) - Warnings, highlights
Dark: #0F172A (Navy) - Text, backgrounds
Light: #F8FAFC (Light gray) - Backgrounds
White: #FFFFFF - Cards, containers
Danger: #EF4444 (Red) - Errors, X marks
```

**Typography:**
```
Headings: "Poppins" or "Inter" (bold, modern)
Body: "Inter" or "Segoe UI" (clean, readable)
Sizes:
- H1: 48px (mobile: 32px)
- H2: 36px (mobile: 24px)
- H3: 24px (mobile: 18px)
- Body: 16px
- Small: 14px
```

**Spacing:**
```
Sections: 80px vertical gap (mobile: 40px)
Padding: 40px horizontal (mobile: 16px)
Card padding: 24px
Button padding: 12px 24px
```

**Border Radius:**
```
Buttons: 8px
Cards: 12px
Inputs: 6px
Images: 12px
```

**Shadows:**
```
Light: 0 1px 2px rgba(0,0,0,0.05)
Medium: 0 4px 6px rgba(0,0,0,0.1)
Heavy: 0 10px 25px rgba(0,0,0,0.1)
```

---

## **MOBILE OPTIMIZATION CHECKLIST**

- [ ] Responsive breakpoints: 320px, 640px, 768px, 1024px, 1280px
- [ ] Touch targets: Min 44x44px (buttons, links)
- [ ] Font sizes: Min 16px on inputs (no iOS zoom)
- [ ] Viewport: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Mobile-first design (design mobile first, scale up)
- [ ] No horizontal scroll
- [ ] Fast load (< 2 sec on 4G)
- [ ] Tap-friendly CTAs
- [ ] Mobile video auto-play (muted)
- [ ] Collapsible menus for long content

---

## **ACCESSIBILITY REQUIREMENTS**

**WCAG AA Compliance:**
- [ ] Color contrast: 4.5:1 for text, 3:1 for UI components
- [ ] Keyboard navigation: All interactive elements accessible via tab
- [ ] Alt text: All images have descriptive alt text
- [ ] Headings: Proper hierarchy (H1 → H2 → H3)
- [ ] Form labels: Associated with inputs via <label>
- [ ] ARIA roles: Proper roles on custom components
- [ ] Focus indicators: Clear visual focus on keyboard nav
- [ ] Motion: Respect prefers-reduced-motion setting

---

## **PERFORMANCE TARGETS**

- **Lighthouse Scores:**
  - Performance: 90+
  - Accessibility: 95+
  - Best Practices: 95+
  - SEO: 100

- **Core Web Vitals:**
  - LCP (Largest Contentful Paint): < 2.5s
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1

- **Page Size:**
  - < 2MB total (gzipped)
  - Hero image: < 500KB (optimized)
  - Videos: Lazy-loaded

---

## **A/B TESTING ROADMAP**

**High-Impact Tests (Run these first):**

1. **Headline Test:**
   - Variant A: "Generate 1,000+ Local Business Leads in 60 Minutes"
   - Variant B: "10x Cheaper Lead Gen Than Apollo or Clay"
   - Metric: Sign-up rate

2. **Hero CTA Text:**
   - Variant A: "Start Free Trial"
   - Variant B: "Get Started Now"
   - Metric: CTA click rate

3. **Trial Duration:**
   - Variant A: 7 days
   - Variant B: 14 days
   - Metric: Trial conversion to paid

4. **Pricing Display:**
   - Variant A: Show all pricing upfront
   - Variant B: Show simplified, "Contact for pricing" for enterprise
   - Metric: Sign-up rate

5. **Form Fields:**
   - Variant A: 3 fields (name, email, company)
   - Variant B: 1 field (email only)
   - Metric: Form completion rate

6. **Social Proof Position:**
   - Variant A: After hero (current)
   - Variant B: Before features
   - Metric: Scroll depth, sign-ups

7. **Video vs Screenshot:**
   - Variant A: Demo video in hero
   - Variant B: Static screenshot
   - Metric: Engagement, CTA click

---

## **DEPLOYMENT & LAUNCH CHECKLIST**

- [ ] Domain configured (nordible.com or gmaps-leads.com)
- [ ] SSL certificate installed
- [ ] All links tested (internal + external)
- [ ] Forms working (sign-up, demo request, contact)
- [ ] Analytics implemented (GA4, Mixpanel, Hotjar)
- [ ] Email integration working (confirmation emails)
- [ ] Stripe integration ready for payments
- [ ] 404 page designed
- [ ] Sitemap.xml created
- [ ] Robots.txt configured
- [ ] Google Search Console verified
- [ ] Meta verification completed
- [ ] Email deliverability tested
- [ ] Performance optimized (Lighthouse 90+)
- [ ] Mobile tested on real devices
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Security headers configured
- [ ] Rate limiting configured
- [ ] Error tracking (Sentry) integrated
- [ ] CDN configured for fast delivery

---

## **POST-LAUNCH OPTIMIZATION PLAN**

**Week 1-2:**
- Monitor analytics for user flow issues
- Check for broken links/forms
- Optimize based on early user feedback
- Run first A/B tests

**Week 3-4:**
- Analyze conversion funnel drop-offs
- Iterate on top 3 high-impact elements
- Gather user feedback via surveys/chat
- Optimize images/videos for speed

**Month 2:**
- Full funnel analysis (awareness → conversion)
- Expand A/B testing to secondary elements
- Launch organic content marketing
- Optimize for search engines (SEO)

**Ongoing:**
- Monitor user behavior (heatmaps)
- Monthly performance reviews
- Continuous A/B testing
- Iterate based on customer feedback

---

## **FINAL DELIVERABLES**

When complete, provide:

1. ✅ Full Next.js project (GitHub repo)
2. ✅ Deployed website (production URL)
3. ✅ Performance report (Lighthouse scores)
4. ✅ SEO audit (keywords, meta tags)
5. ✅ Analytics dashboard setup
6. ✅ A/B testing framework ready
7. ✅ Documentation (setup, deployment, maintenance)
8. ✅ Component library (Storybook)
9. ✅ CI/CD pipeline (GitHub Actions)
10. ✅ Monitoring & alerts configured

---

## **SUCCESS METRICS**

The website is successful when:

- ✅ **Sign-up rate:** 3-5% of visitors
- ✅ **Free trial → Paid conversion:** 20-30%
- ✅ **Average time on page:** 3-5 minutes
- ✅ **Bounce rate:** < 40%
- ✅ **Mobile conversion rate:** ≥ Desktop rate
- ✅ **Form completion rate:** > 80%
- ✅ **Customer acquisition cost (CAC):** < $10 (organic)
- ✅ **Page load time:** < 2 seconds
- ✅ **Lighthouse score:** 90+

---

**This prompt is comprehensive and ready for AI tools (Claude, ChatGPT, v0, Cursor, etc.) to generate a complete, production-ready landing page.**

**Last Updated:** May 24, 2026
