# 🎯 Smart View CRM Enhanced - Complete User Guide

## Table of Contents
1. [Overview](#overview)
2. [What This Module Does](#what-this-module-does)
3. [New CRM Pipeline Stages](#new-crm-pipeline-stages)
4. [Project Location Field](#project-location-field)
5. [Client Approval Workflow](#client-approval-workflow)
6. [Using the Enhanced Features](#using-the-enhanced-features)
7. [Use Case Examples](#use-case-examples)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Overview

**Smart View CRM Enhanced** extends Odoo's CRM with custom fields and an intelligent approval workflow designed for project-based businesses. It adds structured pipeline stages and client approval tracking to ensure no opportunity is missed and every client decision is documented.

**Key Purpose:**
- ✅ Track project locations (REQ-00037)
- ✅ Add custom pipeline stages (REQ-00038)
- ✅ Implement client approval workflow
- ✅ Track rejection reasons
- ✅ Prevent premature quotations

**Perfect For:**
- Construction companies
- Real estate developers
- Engineering firms
- Consulting services
- Any project-based business

---

## What This Module Does

### Core Features

#### 1. **Project Location Field** 📍 (REQ-00037)

**Adds "Project Location" to every lead/opportunity:**
- Visible in form, list, and kanban views
- Searchable and filterable
- Tracked for audit trail
- Shows in kanban tooltips

**Example Values:**
- "Dubai Marina, Plot 123"
- "Riyadh - King Fahd District"
- "Abu Dhabi - Al Reem Island"

---

#### 2. **Three New Pipeline Stages** 🏗️ (REQ-00038)

**Structured sales process with:**

**Stage 1: 🏗️ Site Visit**
- Schedule and conduct site visits
- Document site conditions
- Take measurements
- Meet stakeholders

**Stage 2: 📋 Technical Description**
- Prepare technical proposal
- Create specifications
- Calculate costs
- Design solution

**Stage 3: ✅ Client Approval**
- Present proposal to client
- Wait for decision
- Track approval status
- Document response

---

#### 3. **Client Approval Workflow** ✓❌

**Smart approval management:**

**Before Approval Stage:**
- Normal opportunity flow
- Can create quotations anytime
- Standard CRM behavior

**In Approval Stage:**
- **Approve Button** appears ✅
- **Reject Button** appears ❌
- Buttons visible in form header
- Must record decision before proceeding

**After Approval:**
- ✅ **If Approved:** Can create quotation, move to Won
- ❌ **If Rejected:** Cannot create quotation, track reason

**Rejection Tracking:**
- Rejection category (7 options)
- Detailed reason
- Rejection date
- Automatic tracking
- Team notification

---

#### 4. **Rejection Prevention** 🔒

**Smart validation rules:**

❌ **Cannot create quotation if:**
- Opportunity is rejected
- Still in approval stage (not yet approved)

✅ **Can create quotation only if:**
- Client has approved
- Or opportunity not in approval stage

**Why:** Prevents wasted effort on rejected opportunities!

---

## New CRM Pipeline Stages

### Complete Pipeline View

```
Standard Odoo Stages:
New → Qualified → Proposition

↓

Smart View Enhanced Stages:
→ 🏗️ Site Visit (sequence 15)
→ 📋 Technical Description (sequence 20)
→ ✅ Client Approval (sequence 25)

↓

Standard Odoo Stages:
→ Won / Lost
```

### Stage Details

#### 🏗️ Site Visit Stage

**Purpose:** Conduct on-site assessment

**Activities:**
- Schedule visit with client
- Visit project location
- Take measurements
- Document conditions
- Take photos
- Meet stakeholders
- Assess requirements

**Requirements Displayed:**
> "Schedule and conduct site visit with client"

**When to Use:**
- After initial proposal
- Before detailed technical work
- When site assessment needed
- For complex projects

**Duration:** Typically 1-3 days

---

#### 📋 Technical Description Stage

**Purpose:** Prepare detailed technical proposal

**Activities:**
- Create technical specifications
- Design solution
- Calculate costs
- Prepare drawings
- List materials
- Define timeline
- Create presentation

**Requirements Displayed:**
> "Prepare and present technical description to client"

**When to Use:**
- After site visit
- When details are confirmed
- Before seeking approval
- For technical projects

**Duration:** Typically 3-7 days

---

#### ✅ Client Approval Stage

**Purpose:** Get client's decision

**Activities:**
- Present proposal to client
- Answer questions
- Wait for decision
- Track approval status
- Document response

**Requirements Displayed:**
> "Waiting for client approval decision"

**Special Features:**
- **Approve Button** ✅ (marks as approved)
- **Reject Button** ❌ (opens rejection wizard)
- **Approval Status** indicator
- **Cannot create SO** until approved

**When to Use:**
- After presenting proposal
- Before creating quotation
- When waiting for decision

**Duration:** Typically 1-14 days (depends on client)

---

## Project Location Field

### What It Does

**Tracks where the project will be executed**

**Field Type:** Text field (Char)  
**Visible In:**
- Opportunity form view
- List view
- Kanban view (tooltip)
- Search/filters

**Tracking:** Yes (audit trail)

---

### How to Use

#### Adding Project Location

**Method 1: During Lead Creation**
```
1. CRM → Create (New Lead/Opportunity)
2. Fill basic info (Customer, Expected Revenue)
3. Scroll to "Project Details" or find "Project Location"
4. Enter location: "Dubai Marina, Tower A"
5. Save
```

**Method 2: From Existing Opportunity**
```
1. Open any opportunity
2. Click Edit
3. Find "Project Location" field
4. Enter or update location
5. Save
```

**Method 3: Quick Edit (List View)**
```
1. CRM → Pipeline (list view)
2. Find opportunity
3. Click on Project Location column
4. Type directly
5. Auto-saves
```

---

### Best Practices for Location Format

#### ✅ Good Examples

**Specific and Complete:**
```
"Dubai Marina - Plot 123, Block A"
"Riyadh - King Fahd Road, near Al Faisaliah Tower"
"Abu Dhabi - Yas Island, West Zone"
"Cairo - New Capital, R7 District, Plot 456"
```

**With Context:**
```
"Client Office: Downtown Dubai, Emirates Towers"
"Project Site: Sharjah Industrial Area 12"
"Renovation: Existing building at Al Barsha 1"
```

#### ❌ Bad Examples

**Too Vague:**
```
"Dubai" (which area?)
"Near mall" (which mall?)
"City center" (unclear)
```

**Missing Context:**
```
"Plot 123" (where?)
"Building A" (which building?)
```

---

### Searching by Location

**Use the search bar:**

```
CRM → Search → "Dubai Marina"
Result: All opportunities in Dubai Marina

CRM → Search → "Tower"
Result: All opportunities with "Tower" in location
```

**Use filters:**
```
CRM → Filters → Add Custom Filter
→ Project Location contains "Dubai"
→ Apply
```

---

## Client Approval Workflow

### Complete Workflow

```
1. Opportunity Created
   └→ Standard stages (New, Qualified, Proposition)

2. Site Visit Conducted
   └→ Move to "Site Visit" stage
   └→ Document findings

3. Technical Proposal Prepared
   └→ Move to "Technical Description" stage
   └→ Complete specifications

4. Presented to Client
   └→ Move to "Client Approval" stage
   └→ Approve/Reject buttons appear ✅❌

5. Client Decision
   ├→ Approved ✅
   │  └→ Can create quotation
   │  └→ Move to Won
   │
   └→ Rejected ❌
      └→ Open rejection wizard
      └→ Select category + reason
      └→ Cannot create quotation
      └→ Move to Lost
```

---

### Using Approve/Reject Buttons

#### ✅ Approving an Opportunity

**When:** Client has agreed to proceed

**Steps:**
```
1. Open opportunity in "Client Approval" stage
2. See header buttons: [Approve] [Reject]
3. Click "Approve" button
4. Status changes to "Client Approved" ✅
5. Can now create quotation
6. Usually move to "Won" stage
```

**What Happens:**
- ✅ `client_approval_state` = 'approved'
- ✅ Change tracked in chatter
- ✅ Can create quotation
- ✅ Green indicator shows approval

---

#### ❌ Rejecting an Opportunity

**When:** Client has declined the proposal

**Steps:**
```
1. Open opportunity in "Client Approval" stage
2. Click "Reject" button
3. Rejection Wizard opens 📝

4. In Wizard:
   └→ Select Rejection Category:
      • Price Too High
      • Timeline Not Suitable
      • Scope Changed
      • Competitor Chosen
      • Budget Constraints
      • Project Postponed
      • Other Reason
   
   └→ Enter Detailed Reason:
      "Client found another contractor 
       offering 15% lower price"
   
   └→ Click "Submit Rejection"

5. Opportunity marked as rejected ❌
6. Rejection reason saved
7. Rejection date recorded
8. Cannot create quotation
9. Usually move to "Lost" stage
```

**What Happens:**
- ❌ `client_approval_state` = 'rejected'
- 📝 Rejection reason stored
- 📅 Rejection date recorded
- 🔒 Quotation creation blocked
- 📢 Team notified (optional)
- 📊 Tracked in chatter

---

### Rejection Categories Explained

| Category | When to Use | Example |
|----------|-------------|---------|
| **Price Too High** | Client finds price unacceptable | "Budget only allows $50K, we quoted $75K" |
| **Timeline Not Suitable** | Project timing doesn't work | "Client needs completion in 2 months, we need 4" |
| **Scope Changed** | Client changed requirements | "Now wants 3-story building instead of 2-story" |
| **Competitor Chosen** | Client selected another vendor | "Went with ABC Company who offered faster timeline" |
| **Budget Constraints** | Client has no budget | "Company budget frozen due to economic conditions" |
| **Project Postponed** | Client delayed project | "Will reconsider in Q3 2026" |
| **Other Reason** | Doesn't fit above categories | Custom reason |

---

### Validation Rules

#### Cannot Create Quotation If:

**Rule 1: In Approval Stage, Not Yet Approved**
```
Error: "Cannot create quotation: 
        Opportunity is in Client Approval stage 
        but not yet approved by client."

Solution: Wait for client decision, then approve
```

**Rule 2: Client Rejected the Proposal**
```
Error: "Cannot create quotation: 
        Opportunity was rejected by client on [date]. 
        Reason: [rejection reason]"

Solution: This is by design - cannot proceed with rejected opportunities
```

#### Can Create Quotation If:

✅ **Approved in Client Approval stage**
✅ **Not in Client Approval stage** (before or after)
✅ **Any other stage** (normal flow)

---

## Using the Enhanced Features

### Daily Workflow for Sales Team

#### Morning Routine

**1. Check Opportunities in Approval Stage**
```
CRM → Pipeline → Filter: "Client Approval" stage
→ See list of opportunities awaiting decision
→ Follow up with clients
→ Process approvals/rejections
```

**2. Move Opportunities Through Pipeline**
```
After initial proposal → "Site Visit"
After site visit → "Technical Description"
After presenting proposal → "Client Approval"
After approval → "Won" (create quotation)
After rejection → "Lost"
```

---

### Complete Opportunity Lifecycle

**Example: Construction Project**

```
Day 1: Inquiry Received
└→ Create opportunity
   Name: "Villa Construction - Mr. Ahmed"
   Customer: Ahmed Mohammed
   Project Location: "Dubai Hills Estate, Plot 789"
   Expected Revenue: $500,000
   Stage: New

Day 2-3: Qualify Lead
└→ Call client, confirm interest
   Move to: Qualified

Day 5: Initial Proposal
└→ Send basic proposal
   Move to: Proposition

Day 7: Site Visit Scheduled
└→ Move to: Site Visit
   Schedule visit for Day 10
   Note: "Client available 10 AM"

Day 10: Site Visit Conducted
└→ Visit site, take measurements
   Photos added to chatter
   Note: "Site ready, utilities connected"

Day 11-14: Technical Proposal
└→ Move to: Technical Description
   Prepare detailed specs
   Create cost estimate
   Design floor plans
   Note: "3-story villa, 400 sqm"

Day 15: Present to Client
└→ Move to: Client Approval
   Present proposal in meeting
   Approve/Reject buttons appear
   Note: "Waiting for decision by Day 20"

Day 18: Client Responds
└→ Click "Approve" button ✅
   client_approval_state: approved
   Note: "Client approved! Ready to proceed"

Day 19: Create Quotation
└→ Click "New Quotation"
   Creates SO with details
   Move to: Won
   Note: "Quotation sent, contract signing scheduled"

Day 25: Contract Signed
└→ Opportunity Won! 🎉
```

---

## Use Case Examples

### Use Case 1: Real Estate Development Company

**Business:** Luxury villa construction in UAE

**Challenge:**
- Multiple site visits needed
- Complex technical specifications
- Client approval crucial
- High-value deals ($500K-$5M)
- Need structured process

#### Before Smart View CRM Enhanced:
```
❌ No structured stages for site visits
❌ Technical details lost in notes
❌ Unclear approval status
❌ Sales reps creating quotes before approval
❌ Wasted effort on rejected projects
❌ No rejection tracking
❌ Hard to analyze why deals lost
```

#### After Smart View CRM Enhanced:
```
✅ Clear "Site Visit" stage
✅ Dedicated "Technical Description" stage
✅ "Client Approval" stage with workflow
✅ Cannot quote without approval
✅ Rejection reasons tracked
✅ Can analyze loss reasons
✅ Structured, professional process
```

**Workflow:**

```
Lead: "Client wants 5-bedroom villa"
└→ Project Location: "Palm Jumeirah, Frond M"
   Expected Revenue: $3,500,000

↓ [Qualified]

Site Visit Scheduled
└→ Move to "Site Visit" stage
   Architect visits site
   Documents: Plot 456 sqm, sea-facing
   Photos uploaded

↓ [Site Visit Complete]

Technical Proposal
└→ Move to "Technical Description"
   Architectural drawings prepared
   3D renders created
   Material specifications listed
   Timeline: 18 months
   Cost breakdown detailed

↓ [Proposal Ready]

Client Meeting
└→ Move to "Client Approval"
   Present proposal to client family
   Answer questions
   Await decision (1 week)

↓ [Decision]

Scenario A: Approved ✅
└→ Click "Approve"
   Create quotation
   Move to Won
   Contract signed
   Project begins!

Scenario B: Rejected ❌
└→ Click "Reject"
   Category: "Budget Constraints"
   Reason: "Family budget reduced due to market conditions.
            Will reconsider in 6 months."
   Move to Lost
   Set follow-up reminder for 6 months
   Lesson: Focus on budget-conscious designs
```

**Results:**
- ✅ 30% fewer wasted quotations
- ✅ 95% approval rate when reaching approval stage
- ✅ Clear rejection analysis for improvement
- ✅ Professional client experience
- ✅ Better resource allocation

---

### Use Case 2: Engineering Consulting Firm

**Business:** Industrial facility design and engineering

**Challenge:**
- Technical assessments required
- Client approvals take time
- Multiple stakeholders
- Long sales cycles (3-6 months)
- Complex specifications

#### Complete Project Flow:

```
Inquiry: "Factory Expansion Project"
Customer: ABC Manufacturing
Project Location: "Dammam Industrial City, Phase 2"
Expected Revenue: $850,000

Week 1-2: Initial Contact
└→ Stage: New → Qualified
   Understand requirements
   Assess feasibility

Week 3: Site Assessment
└→ Stage: Proposition → Site Visit
   Engineers visit factory
   Measure existing facility
   Assess infrastructure
   Document constraints
   Photos: Current layout, utilities
   
   Site Visit Notes:
   "Existing building 2,000 sqm
    Need expansion 1,500 sqm
    Power supply adequate
    Drainage needs upgrade"

Week 4-6: Engineering Design
└→ Stage: Technical Description
   Structural engineers design
   MEP (Mechanical, Electrical, Plumbing) specs
   Equipment layouts
   Cost estimates
   Timeline projections
   
   Technical Description:
   "Steel structure expansion
    Load capacity: 500 tons
    Crane installation required
    Duration: 8 months
    Investment: $850,000"

Week 7: Stakeholder Presentation
└→ Stage: Client Approval
   Present to:
   - Factory Manager
   - CFO
   - Operations Director
   - CEO
   
   Await approval (2-3 weeks)

Week 9: Decision
└→ Scenario: Approved ✅
   Click "Approve" button
   Approval notes: "Board approved 
                    in meeting on XX/XX/XXXX
                    Budget allocated"
   
   Create quotation immediately
   Move to Won
   Contract negotiation begins

Alternative: Rejected ❌
└→ Category: "Timeline Not Suitable"
   Reason: "Company needs completion in 5 months
            for production deadline. We proposed 8 months.
            Will source local contractor with faster timeline."
   
   Learning: Offer fast-track options
   Follow-up: Consider smaller scope for faster delivery
```

**Benefits:**
- ✅ Clear stage for complex technical work
- ✅ Approval tracking for multiple stakeholders
- ✅ Rejection analysis improves future proposals
- ✅ Professional documentation
- ✅ Better project planning

---

### Use Case 3: Interior Design Studio

**Business:** Commercial interior design and fit-out

**Challenge:**
- Site visits essential
- Design approvals critical
- Clients often indecisive
- Budget changes common
- Multiple revisions

#### Example Project:

```
Project: "Restaurant Interior Design"
Customer: Mr. Khalid (Restaurant Owner)
Project Location: "Jeddah - Red Sea Mall, Unit 205"
Expected Revenue: $120,000

Day 1-3: Initial Inquiry
└→ Stage: New
   Customer wants modern restaurant
   Capacity: 80 seats
   Budget: $100-150K

Day 5: Site Visit
└→ Stage: Site Visit
   Designer visits empty retail unit
   Measures: 250 sqm
   Photos: Space layout, ceiling height
   Notes: "Good natural light
           Plumbing available
           Ventilation needs work"
   
   Project Location updated:
   "Jeddah - Red Sea Mall, Unit 205
    250 sqm, 2nd floor, corner unit"

Day 6-12: Design Phase
└→ Stage: Technical Description
   3D renders created
   Mood boards prepared
   Material samples selected
   Furniture layout designed
   Lighting plan detailed
   Cost breakdown:
   - Flooring: $15K
   - Furniture: $45K
   - Lighting: $20K
   - Kitchen fit-out: $25K
   - Misc: $15K
   Total: $120K

Day 15: Client Presentation
└→ Stage: Client Approval
   Show 3D renders
   Present material samples
   Explain timeline (6 weeks)
   Await decision

Day 18: First Response
└→ Client loves design BUT...
   Wants changes:
   - Different color scheme
   - More budget-friendly furniture
   
   NOT rejected yet!
   Return to "Technical Description"
   Revise proposal

Day 22: Revised Presentation
└→ Back to "Client Approval"
   Present updated design
   Cost reduced to $110K
   Timeline maintained

Day 25: Final Decision
└→ Click "Approve" ✅
   Client satisfied with revisions
   Ready to proceed
   
   Create quotation
   Move to Won
   Contract signed
   Design implementation begins!

Alternative Scenario: Rejection
└→ Click "Reject" ❌
   Category: "Price Too High"
   Reason: "Even after revisions, budget exceeded.
            Owner decided to do basic fit-out instead.
            Will use in-house team for simple design."
   
   Learning: Offer tiered packages:
            - Basic: $60-80K
            - Standard: $100-120K
            - Premium: $150K+
```

**Results:**
- ✅ Structured revision process
- ✅ Clear approval tracking
- ✅ Multiple stakeholder coordination
- ✅ Rejection reasons inform pricing strategy
- ✅ Better scope definition upfront

---

### Use Case 4: IT Solutions Provider

**Business:** Custom software and IT infrastructure

**Challenge:**
- Site assessments needed
- Technical specifications complex
- Long decision-making process
- Budget approval delays
- Competitor comparisons

#### Project Example:

```
Project: "ERP System Implementation"
Customer: XYZ Trading LLC
Project Location: "Dubai - Head Office + 3 Branches"
Expected Revenue: $250,000

Week 1: Initial Contact
└→ Stage: New → Qualified
   Customer needs ERP system
   50 users across 4 locations
   Modules: Finance, Inventory, HR, CRM

Week 2: Site Survey
└→ Stage: Site Visit
   IT team visits:
   - Head office: 30 users
   - Branch 1 (Sharjah): 8 users
   - Branch 2 (Abu Dhabi): 7 users
   - Branch 3 (Al Ain): 5 users
   
   Infrastructure assessed:
   - Current systems documented
   - Network capacity checked
   - Server requirements noted
   - Data migration scope defined
   
   Project Location detailed:
   "Dubai Head Office (main server)
    + 3 branches (cloud access)
    Total 50 users, 200GB data"

Week 3-4: Solution Design
└→ Stage: Technical Description
   Prepare comprehensive proposal:
   - ERP system: Odoo Enterprise
   - Customizations listed
   - Data migration plan
   - Training schedule
   - Support package
   - Timeline: 4 months
   - Investment breakdown:
     * Licenses: $60K
     * Implementation: $100K
     * Training: $30K
     * Support (1 year): $30K
     * Data migration: $30K
     Total: $250K

Week 5: Management Presentation
└→ Stage: Client Approval
   Present to IT Manager and CFO
   Demo system
   Answer questions
   Competitive comparison provided
   
   Awaiting board approval (3 weeks)

Week 8: Decision Delayed
└→ Still in "Client Approval"
   CFO requests competitor quotes
   Additional demo scheduled
   Budget approval pending

Week 10: Final Decision

Scenario A: Approved ✅
└→ Click "Approve"
   Board approved budget
   Note: "Contract committee meeting 
          approved on XX/XX/XXXX
          Purchase order issued"
   
   Create quotation
   Schedule kickoff meeting
   Move to Won

Scenario B: Rejected ❌
└→ Click "Reject"
   Category: "Competitor Chosen"
   Reason: "Board selected Company ABC
            Reasons:
            - 20% lower price
            - Existing relationship
            - Faster implementation (3 months vs 4)
            
            Feedback for future:
            - Consider flexible pricing
            - Highlight quality over speed
            - Build relationships earlier"
   
   Move to Lost
   Analysis: Improve competitive positioning
```

**Insights from Rejection Tracking:**

After 10 rejections tracked:
- 4 x "Price Too High" → Offer tiered packages
- 3 x "Competitor Chosen" → Improve differentiation
- 2 x "Timeline Not Suitable" → Fast-track options
- 1 x "Project Postponed" → Follow-up in 6 months

**Actions Taken:**
- Created "Quick Start" package (2 months, $150K)
- Added "Premium Support" differentiator
- Improved proposal presentation
- Better competitor analysis

**Results:**
- ✅ Win rate increased 25%
- ✅ Better proposal quality
- ✅ Faster decision cycles
- ✅ Improved pricing strategy

---

### Use Case 5: Construction Materials Supplier

**Business:** Supply building materials for large projects

**Challenge:**
- Site logistics assessment needed
- Technical specifications vary by project
- Price competition intense
- Payment terms negotiation
- Multiple decision makers

#### Sales Process:

```
Opportunity: "Marble Supply - Luxury Hotel Project"
Customer: Grand Hotels Group
Project Location: "Abu Dhabi - Corniche, New Hotel Site"
Expected Revenue: $180,000

Day 1-3: Initial Inquiry
└→ Stage: New → Qualified
   Hotel needs Italian marble
   Quantity: 2,000 sqm
   Types: Lobby, bathrooms, corridors

Day 5: Site Visit
└→ Stage: Site Visit
   Sales + Technical team visit
   Assess:
   - Delivery access
   - Storage space
   - Installation timeline
   - Existing progress
   
   Site Visit Report:
   "Construction at 30%
    Delivery access: Via service entrance
    Storage: Covered area available
    Timeline: Material needed in 3 months
    Installation team: Client arranging"
   
   Project Location updated:
   "Abu Dhabi Corniche - Grand Hotel Site
    Block A (6 floors), delivery via Gate 3"

Day 6-8: Technical Proposal
└→ Stage: Technical Description
   Prepare detailed quote:
   - Marble types with samples
   - Quantity calculations
   - Delivery schedule
   - Installation guidelines
   - Quality certifications
   - Payment terms
   
   Technical specs:
   "Carrara Marble - 1,200 sqm @ $75/sqm
    Emperador Dark - 500 sqm @ $95/sqm
    Calacatta Gold - 300 sqm @ $120/sqm
    
    Delivery: 3 shipments over 2 months
    Total: $180,000 + shipping"

Day 10: Procurement Meeting
└→ Stage: Client Approval
   Present to:
   - Procurement Manager
   - Project Manager
   - Interior Designer
   - CFO (via video)
   
   Samples displayed
   Certificates provided
   Timeline confirmed

Day 15: Awaiting Decision
└→ Still "Client Approval"
   Competing quotes received
   Price negotiation ongoing
   Designer prefers our samples

Day 18: Final Outcome

Success Case: Approved ✅
└→ Click "Approve"
   Note: "Procurement approved
          Contract signed
          PO #12345 received
          Advance payment 30%"
   
   Create quotation
   Schedule first delivery
   Move to Won
   Begin material ordering

Rejection Case: ❌
└→ Click "Reject"
   Category: "Price Too High"
   Reason: "Client budget only $150K
            Competitor offered local marble
            at $120K total. We couldn't match
            price while maintaining Italian quality.
            
            Designer wanted our quality but
            budget decision made by CFO."
   
   Move to Lost
   
   Action Items:
   - Add "Value Alternative" option
   - Local + Italian mix
   - Offer payment terms flexibility
   - Build CFO relationships earlier

Postponed Case:
└→ Click "Reject"
   Category: "Project Postponed"
   Reason: "Hotel construction delayed 6 months
            due to permit issues. Client confirmed
            still interested. Will re-engage Q2 2026."
   
   Set follow-up task
   Mark as "warm lead" for future
```

**Value of Rejection Tracking:**

After 20 opportunities:
- **Won:** 12 (60%)
- **Lost - Price:** 4 (20%)
- **Lost - Competitor:** 2 (10%)
- **Lost - Postponed:** 2 (10%)

**Strategic Insights:**
- Price is main concern (20% of losses)
- Quality appreciated but budget-sensitive
- Local alternatives increasing
- Timeline flexibility important

**Business Actions:**
- Introduced "Value Line" (mix of local + imported)
- Flexible payment terms (60 days vs 30 days)
- Faster delivery options
- Better competitor analysis

**Results:**
- ✅ Win rate improved to 70%
- ✅ Average deal size maintained
- ✅ Customer satisfaction higher
- ✅ More informed pricing decisions

---

## Best Practices

### Pipeline Stage Management

#### ✅ DO:

**1. Move Stages Sequentially**
```
✅ New → Qualified → Proposition → Site Visit → 
   Technical Description → Client Approval → Won
```

**2. Document Stage Changes**
```
✅ Add note when moving stages:
   "Moving to Site Visit - scheduled for Monday 10 AM"
   "Moving to Client Approval - proposal presented today"
```

**3. Use All Relevant Stages**
```
✅ If site visit needed → Use "Site Visit" stage
✅ If technical work needed → Use "Technical Description"
✅ If awaiting approval → Use "Client Approval"
```

**4. Set Expected Dates**
```
✅ In "Site Visit" → Set visit date
✅ In "Technical Description" → Set proposal delivery date
✅ In "Client Approval" → Set decision deadline
```

#### ❌ DON'T:

**1. Skip Important Stages**
```
❌ Don't jump: Proposition → Client Approval
   (Missing site visit and technical work)
```

**2. Leave Opportunities Stuck**
```
❌ Don't leave in "Client Approval" for months without follow-up
```

**3. Create Quotations Prematurely**
```
❌ Don't create SO while still in "Client Approval"
   (Wait for actual approval)
```

---

### Project Location Best Practices

#### ✅ DO:

**1. Be Specific**
```
✅ "Dubai Marina - Tower A, Floor 25, Unit 2501"
✅ "Riyadh - King Abdullah Financial District, Plot 12-34"
✅ "Cairo - New Administrative Capital, R8, Villa 456"
```

**2. Include Key Details**
```
✅ City/District
✅ Building/Plot number
✅ Any unique identifiers
✅ Nearby landmarks if helpful
```

**3. Update as Information Improves**
```
Initially: "Dubai - Al Barsha area"
After site visit: "Dubai - Al Barsha 1, Street 18, Villa 234"
```

**4. Use Consistent Format**
```
✅ Establish company standard:
   "[City] - [District/Area], [Building/Plot], [Unit/Floor]"
```

#### ❌ DON'T:

**1. Leave Blank**
```
❌ Empty project location = lost opportunity later
```

**2. Be Too Vague**
```
❌ "Dubai" (Too broad)
❌ "Client site" (Meaningless)
❌ "TBD" (Should update when known)
```

**3. Use Inconsistent Formats**
```
❌ Different format for each opportunity
   Makes filtering and reporting difficult
```

---

### Client Approval Workflow Best Practices

#### ✅ DO:

**1. Document Presentations**
```
✅ Add note: "Presented proposal to CFO and Project Manager on XX/XX"
✅ Attach presentation files to opportunity
✅ Note who attended, their reactions
```

**2. Set Follow-Up Tasks**
```
✅ After presentation: "Follow up on decision - 1 week"
✅ If delayed: "Check approval status - every 3 days"
```

**3. Use Rejection Wizard Properly**
```
✅ Select accurate category
✅ Write detailed reason (helps future sales)
✅ Be honest about why lost
```

**4. Learn from Rejections**
```
✅ Review rejection reasons monthly
✅ Identify patterns
✅ Adjust sales strategy
✅ Improve proposals
```

**5. Approve Promptly**
```
✅ When client says yes, click "Approve" immediately
✅ Don't delay - capture decision
```

#### ❌ DON'T:

**1. Skip Rejection Details**
```
❌ Don't just pick "Other" without explanation
❌ Don't leave reason blank
❌ Don't oversimplify complex situations
```

**2. Approve Without Confirmation**
```
❌ Don't approve based on "maybe"
❌ Wait for clear client commitment
❌ Verify decision makers approved
```

**3. Create Quotation for Pending Approvals**
```
❌ Don't create SO while waiting for decision
❌ Respect the workflow
❌ Wait for actual approval
```

**4. Forget to Move After Decision**
```
❌ Don't leave approved opportunities in "Client Approval"
❌ Move to Won after approval
❌ Move to Lost after rejection
```

---

### Reporting and Analysis

#### Monthly Review Checklist

**1. Pipeline Health**
```
- How many in each stage?
- Average time in each stage?
- Bottlenecks?
- Stuck opportunities?
```

**2. Approval Success Rate**
```
- Opportunities reaching Client Approval: X
- Approved: Y (Y/X = approval rate)
- Target: >70% approval rate
```

**3. Rejection Analysis**
```
- Top rejection categories
- Common patterns
- Actionable improvements
```

**4. Location Analysis**
```
- Which locations/areas most successful?
- Geographic trends?
- Resource allocation?
```

---

## Troubleshooting

### Issue 1: Cannot Create Quotation

**Symptoms:**
```
Error: "Cannot create quotation: Opportunity is in 
        Client Approval stage but not yet approved by client."
```

**Cause:** Opportunity is in "Client Approval" stage but status is still "Pending"

**Solutions:**

✅ **Solution 1: Get Client Approval**
```
1. Follow up with client
2. Get their decision
3. Click "Approve" button when confirmed
4. Then create quotation
```

✅ **Solution 2: Move Back if Not Ready**
```
1. If client needs more time
2. Move back to "Technical Description"
3. Make revisions
4. Re-present when ready
```

✅ **Solution 3: Lost the Deal**
```
1. If client said no
2. Click "Reject" button
3. Fill rejection wizard
4. Move to "Lost" stage
```

---

### Issue 2: Cannot Find Approve/Reject Buttons

**Symptoms:**
- Opportunity in "Client Approval" stage
- No approve/reject buttons visible

**Causes & Solutions:**

✅ **Cause 1: Wrong Stage**
```
Check: Is opportunity actually in "Client Approval" stage?
Fix: Move to correct stage
```

✅ **Cause 2: Buttons in Header**
```
Check: Look at top of form, in header area
Location: Near Edit/Send by Email buttons
```

✅ **Cause 3: Browser Issue**
```
Fix: Refresh page (Ctrl+F5)
Try: Different browser
```

✅ **Cause 4: Permissions**
```
Check: Do you have sales user rights?
Fix: Administrator assigns proper group
```

---

### Issue 3: Project Location Not Visible

**Symptoms:**
- Cannot find "Project Location" field
- Field not in form

**Solutions:**

✅ **Solution 1: Check View**
```
1. Ensure using correct form view
2. May be in different tab/section
3. Try editing opportunity
```

✅ **Solution 2: Refresh View**
```
1. Ctrl+F5 to hard refresh
2. Log out and back in
3. Clear browser cache
```

✅ **Solution 3: Verify Installation**
```
1. Apps → Search "Smart View CRM"
2. Should show "Installed"
3. If not, install module
4. Upgrade if needed
```

---

### Issue 4: Stages Not Appearing

**Symptoms:**
- New stages (Site Visit, Technical Description, Client Approval) not in pipeline

**Solutions:**

✅ **Solution 1: Check Installation**
```
1. Apps → Smart View - CRM Enhanced
2. Verify "Installed" status
3. If issues, uninstall and reinstall
```

✅ **Solution 2: Check Stage Configuration**
```
1. CRM → Configuration → Stages
2. Look for:
   - Site Visit
   - Technical Description
   - Client Approval
3. If not there, stages weren't created
4. Contact administrator
```

✅ **Solution 3: Refresh Pipeline**
```
1. Go to CRM → Pipeline
2. Hard refresh (Ctrl+F5)
3. Stages should appear in kanban
```

---

### Issue 5: Rejection Wizard Doesn't Save

**Symptoms:**
- Fill rejection wizard
- Click submit
- Nothing happens

**Solutions:**

✅ **Solution 1: Fill All Required Fields**
```
Required:
- Rejection Category (select one)
- Rejection Reason (enter text)

Then: Click "Submit Rejection"
```

✅ **Solution 2: Check Permissions**
```
Need: Sales User or Sales Manager role
Fix: Contact administrator
```

✅ **Solution 3: Browser Issue**
```
Try:
- Refresh page
- Different browser
- Clear cache
```

---

## Quick Reference

### Pipeline Stages Quick Guide

| Stage | Purpose | Duration | Next Step |
|-------|---------|----------|-----------|
| **New** | Initial contact | 1 day | Qualify |
| **Qualified** | Confirmed interest | 2-3 days | Send proposal |
| **Proposition** | Proposal sent | 3-5 days | Site visit or approval |
| **🏗️ Site Visit** | Conduct assessment | 1-3 days | Technical work |
| **📋 Technical Description** | Detailed proposal | 3-7 days | Client approval |
| **✅ Client Approval** | Awaiting decision | 1-14 days | Approve/Reject |
| **Won** | Deal closed | - | Create SO |
| **Lost** | Deal lost | - | Analyze |

### Approval Workflow Quick Steps

```
1. Move to "Client Approval" stage
2. Wait for client decision
3. Click "Approve" ✅ OR "Reject" ❌
4. If approved: Create quotation
5. If rejected: Fill reason, move to Lost
```

### Common Tasks Time Estimates

| Task | Time |
|------|------|
| Add project location | 30 seconds |
| Move stage | 10 seconds |
| Approve opportunity | 20 seconds |
| Reject with details | 2 minutes |
| Complete site visit stage | 2-4 hours |
| Prepare technical description | 1-3 days |

---

## Getting Help

### Documentation

- 📚 This User Guide (complete reference)
- 🎯 QUICK_REFERENCE.md (one-page card)
- 📖 README.md (overview)
- 📊 COMPLETION_SUMMARY.md (technical details)

### Support

- **Odoo CRM:** Standard Odoo CRM documentation
- **Smart View:** Internal support team
- **Issues:** Contact administrator

---

## Conclusion

Smart View CRM Enhanced transforms your sales pipeline with structured stages and intelligent approval workflow. The project location field and client approval tracking ensure nothing falls through the cracks and every decision is documented.

**Key Benefits:**
- ✅ Structured sales process
- ✅ Professional client experience
- ✅ Better decision tracking
- ✅ Rejection analysis for improvement
- ✅ Prevents wasted effort
- ✅ Clear audit trail

**Perfect for project-based businesses that need:**
- Site visits
- Technical proposals
- Client approvals
- Location tracking
- Structured pipeline

---

**Module Version:** 19.0.1.0.0  
**Last Updated:** November 2025  
**Status:** ✅ Production Ready

**Need Help?** Check QUICK_REFERENCE.md or contact your administrator!

