# 🎯 Smart View CRM Enhanced - Quick Reference Card

## 🚀 Quick Start (30 Seconds)

**Complete Sales Flow:**
```
1. CRM → Create Opportunity
2. Add Project Location field
3. Move through stages: Site Visit → Technical Description
4. Present to client → Move to Client Approval
5. Click Approve ✅ or Reject ❌
6. Create quotation (if approved)
```

---

## 📍 Navigation

| What | Where |
|------|-------|
| View Pipeline | CRM → Pipeline |
| Create Opportunity | CRM → Create |
| View Stages | CRM → Configuration → Stages |
| Reports | CRM → Reporting |
| My Pipeline | CRM → My Pipeline |

**Note:** No custom menus - uses standard Odoo CRM navigation

---

## 🏗️ New Pipeline Stages

### Stage Sequence

```
Standard Stages:
New (10) → Qualified (5) → Proposition (10)

↓

Smart View Stages:
→ 🏗️ Site Visit (15)
→ 📋 Technical Description (20)
→ ✅ Client Approval (25)

↓

Standard:
→ Won (70) / Lost (90)
```

### Stage Quick Reference

| Stage | Icon | Purpose | Duration | Next Action |
|-------|------|---------|----------|-------------|
| **Site Visit** | 🏗️ | Conduct assessment | 1-3 days | Document findings |
| **Technical Description** | 📋 | Prepare proposal | 3-7 days | Present to client |
| **Client Approval** | ✅ | Awaiting decision | 1-14 days | Approve/Reject |

---

## 📝 Project Location Field

### Quick Add

**Method 1: In Form**
```
Open Opportunity → Find "Project Location" → Enter → Save
```

**Method 2: List View**
```
CRM → Pipeline (list) → Click field → Type → Auto-saves
```

### Format Examples

✅ **Good:**
```
"Dubai Marina - Tower A, Floor 25"
"Riyadh - King Fahd Road, Plot 123"
"Cairo - New Capital, R7, Villa 456"
```

❌ **Bad:**
```
"Dubai" (too vague)
"Site 1" (unclear)
"TBD" (should update)
```

---

## ✓❌ Client Approval Workflow

### Approve Opportunity

```
1. Opportunity in "Client Approval" stage
2. Click "Approve" button in header
3. Status → "Client Approved" ✅
4. Can now create quotation
5. Move to "Won"
```

**Time:** 20 seconds

---

### Reject Opportunity

```
1. Click "Reject" button
2. Rejection Wizard opens:
   └→ Select Category
   └→ Enter Reason
   └→ Click "Submit Rejection"
3. Status → "Client Rejected" ❌
4. Cannot create quotation
5. Move to "Lost"
```

**Time:** 2 minutes

---

## 📊 Rejection Categories

| Category | When to Use |
|----------|-------------|
| **Price Too High** | Budget exceeded |
| **Timeline Not Suitable** | Timeline doesn't work |
| **Scope Changed** | Requirements changed |
| **Competitor Chosen** | Lost to competitor |
| **Budget Constraints** | No budget available |
| **Project Postponed** | Delayed by client |
| **Other Reason** | Custom reason |

---

## 🔒 Validation Rules

### Cannot Create Quotation If:

❌ **In Client Approval stage, not yet approved**
```
Error: "Opportunity in Client Approval stage 
        but not yet approved by client"

Fix: Get approval first, then create SO
```

❌ **Client rejected the proposal**
```
Error: "Opportunity was rejected by client 
        on [date]. Reason: [rejection reason]"

Fix: This is correct - cannot proceed with rejected opportunities
```

### Can Create Quotation If:

✅ **Approved in Client Approval stage**  
✅ **Not in Client Approval stage**  
✅ **Any other stage** (normal flow)

---

## ⚡ Common Tasks

### Add Project Location (30 seconds)

```
1. Open opportunity
2. Edit
3. Find "Project Location"
4. Enter: "City - District, Building/Plot"
5. Save
```

---

### Move Through Sales Pipeline

```
Initial Contact → Qualified
    ↓ (Send proposal)
Proposition
    ↓ (Schedule visit)
Site Visit (document findings)
    ↓ (Prepare specs)
Technical Description
    ↓ (Present to client)
Client Approval
    ↓ (Get decision)
Approve ✅ → Won → Create SO
OR
Reject ❌ → Lost
```

---

### Conduct Site Visit

```
1. Move to "Site Visit" stage
2. Schedule visit with client
3. Visit site
4. Take photos (attach to chatter)
5. Document findings in notes
6. Update Project Location with details
7. Move to "Technical Description"
```

**Time:** 2-4 hours

---

### Prepare Technical Proposal

```
1. Move to "Technical Description" stage
2. Create specifications
3. Calculate costs
4. Design solution
5. Prepare presentation
6. Attach documents to opportunity
7. Move to "Client Approval"
```

**Time:** 1-3 days

---

### Get Client Approval

```
1. Move to "Client Approval" stage
2. Present proposal to client
3. Wait for decision
4. Follow up as needed
5. When decision received:
   └→ Click "Approve" ✅
   OR
   └→ Click "Reject" ❌ + Fill reason
6. Move to Won/Lost accordingly
```

**Time:** 1-14 days (waiting)

---

## 🎯 Use Case Quick Examples

### Real Estate Development

```
Lead: Villa construction
Location: "Dubai Hills, Plot 789"
Flow: Site Visit → Technical specs → Client Approval
Outcome: Approved ✅ → $3.5M deal
```

---

### Engineering Consulting

```
Lead: Factory expansion
Location: "Dammam Industrial, Phase 2"
Flow: Site assessment → Engineering design → Board approval
Outcome: Rejected ❌
Reason: "Timeline not suitable - needed 5 months, proposed 8"
Learning: Offer fast-track options
```

---

### Interior Design

```
Lead: Restaurant design
Location: "Jeddah - Red Sea Mall, Unit 205"
Flow: Site visit → 3D renders → Client presentation
Outcome: Revised → Approved ✅ → $110K project
```

---

## 🛠️ Troubleshooting

### Cannot Create Quotation

```
✓ Check: In Client Approval stage?
✓ Check: Approved by client?
✓ Fix: Click "Approve" button first
```

---

### Approve/Reject Buttons Missing

```
✓ Check: In "Client Approval" stage?
✓ Check: Looking in form header?
✓ Fix: Refresh page (Ctrl+F5)
```

---

### Project Location Field Not Visible

```
✓ Check: Module installed?
✓ Check: Editing opportunity form?
✓ Fix: Refresh browser, check installation
```

---

### Stages Not Showing

```
✓ Check: Module installed correctly?
✓ Go to: CRM → Configuration → Stages
✓ Should see: Site Visit, Technical Description, Client Approval
✓ Fix: Reinstall module if missing
```

---

## 📋 Best Practices

### DO ✅

- ✅ **Add project location** for every opportunity
- ✅ **Use all relevant stages** (don't skip)
- ✅ **Document stage changes** in notes
- ✅ **Fill rejection details** completely
- ✅ **Follow up in approval stage** regularly
- ✅ **Move promptly after approval** to Won
- ✅ **Analyze rejections** monthly
- ✅ **Set follow-up tasks** in each stage

### DON'T ❌

- ❌ **Skip important stages** (Site Visit, Technical)
- ❌ **Leave opportunities stuck** in approval
- ❌ **Create quotations prematurely** (wait for approval)
- ❌ **Use vague locations** (be specific)
- ❌ **Skip rejection details** (select "Other" without reason)
- ❌ **Approve without confirmation** (verify client decision)
- ❌ **Forget to update** Project Location after site visit

---

## 📊 Key Metrics

**Track Monthly:**
- Opportunities reaching Client Approval: X
- Approval rate: Y/X (target >70%)
- Average time in each stage
- Top rejection categories
- Win rate by location

**Review Quarterly:**
- Pipeline health
- Stage bottlenecks
- Rejection patterns
- Location success rates
- Process improvements

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Add project location | 30 sec |
| Move to next stage | 10 sec |
| Site visit stage | 2-4 hours |
| Technical description | 1-3 days |
| Client approval wait | 1-14 days |
| Approve opportunity | 20 sec |
| Reject with details | 2 min |
| Create quotation | 5 min |

---

## 🎓 Training Checklist

### For Sales Reps
- [ ] Understand new pipeline stages
- [ ] Know how to add project location
- [ ] Can move opportunities through stages
- [ ] Knows when to use Approve/Reject
- [ ] Fills rejection details properly
- [ ] Documents stage changes

### For Sales Managers
- [ ] All sales rep skills
- [ ] Can review pipeline health
- [ ] Analyzes rejection reasons
- [ ] Coaches team on process
- [ ] Reviews metrics monthly
- [ ] Identifies improvements

---

## 🔗 Quick Access

| Need | Access |
|------|--------|
| Create Opportunity | CRM → Create |
| View Pipeline | CRM → Pipeline |
| My Opportunities | CRM → My Pipeline |
| Configure Stages | CRM → Config → Stages |
| Reports | CRM → Reporting |
| Won Deals | CRM → Pipeline → Filter Won |
| Lost Deals | CRM → Pipeline → Filter Lost |

---

## 💡 Pro Tips

### 1. Stage Movement

```
✅ Move sequentially through stages
✅ Don't skip unless clear reason
✅ Add note explaining why
```

### 2. Project Location

```
✅ Add during creation
✅ Update after site visit with details
✅ Use consistent format across team
```

### 3. Site Visit Stage

```
✅ Take photos
✅ Document measurements
✅ Update location details
✅ Attach files to opportunity
```

### 4. Technical Description

```
✅ Prepare comprehensive proposal
✅ Attach presentation files
✅ Include cost breakdown
✅ Set realistic timeline
```

### 5. Client Approval

```
✅ Set follow-up tasks
✅ Note decision deadline
✅ Track all client interactions
✅ Document approval verbally first
✅ Then click button to record
```

### 6. Rejection Handling

```
✅ Be honest about reason
✅ Select accurate category
✅ Write detailed explanation
✅ Set follow-up if appropriate
✅ Learn for next opportunity
```

---

## 📈 Success Metrics

### Pipeline Health Indicators

**Good:**
- ✅ <10% opportunities stuck >30 days in any stage
- ✅ >70% approval rate in Client Approval stage
- ✅ <7 days average in Site Visit
- ✅ <14 days average in Technical Description
- ✅ Project location filled for >95% opportunities

**Needs Attention:**
- ⚠️ >20% stuck in Client Approval
- ⚠️ <50% approval rate
- ⚠️ >30 days in Technical Description
- ⚠️ Frequent "Price Too High" rejections

---

## 🎯 Monthly Review Checklist

**Pipeline Review:**
- [ ] Count opportunities per stage
- [ ] Calculate average time per stage
- [ ] Identify stuck opportunities
- [ ] Follow up on overdue approvals

**Rejection Analysis:**
- [ ] Count rejections by category
- [ ] Read all rejection reasons
- [ ] Identify patterns
- [ ] Plan improvements

**Location Analysis:**
- [ ] Which locations most successful?
- [ ] Any geographic trends?
- [ ] Resource allocation optimal?

**Process Improvement:**
- [ ] What's working well?
- [ ] What's causing delays?
- [ ] Team feedback?
- [ ] Actions for next month?

---

## 🆘 Emergency Actions

**Opportunity Stuck in Approval >30 Days:**
```
1. Review notes - last contact?
2. Call client immediately
3. If no response - escalate to manager
4. Set clear deadline
5. If still no response - consider Lost
```

**High Rejection Rate (>40%):**
```
1. Review all rejection reasons
2. Find common pattern
3. Adjust proposal approach
4. Team meeting to discuss
5. Test new approach
6. Monitor improvement
```

**Project Locations Not Filled:**
```
1. Export opportunities list
2. Identify missing locations
3. Contact sales reps
4. Update immediately
5. Make it required practice
```

---

## 📞 Getting Help

**Documentation:**
- 📚 USER_GUIDE.md (complete manual + 5 use cases)
- 🎯 This Quick Reference
- 📖 README.md (overview)

**Support:**
- Odoo CRM standard docs
- Smart View internal support
- Sales team training sessions

---

## 🎉 Key Benefits Summary

**Before Smart View CRM Enhanced:**
- ❌ Unstructured pipeline
- ❌ Site visits not tracked
- ❌ Technical work not visible
- ❌ Unclear approval status
- ❌ No rejection tracking
- ❌ Premature quotations

**After Smart View CRM Enhanced:**
- ✅ Clear, structured stages
- ✅ Site Visit stage with docs
- ✅ Technical Description stage
- ✅ Client Approval workflow
- ✅ Rejection reasons tracked
- ✅ Quotations only when appropriate
- ✅ Better win rates
- ✅ Professional process

---

**Print this card and keep it handy! 📌**

**Need detailed help?** → See USER_GUIDE.md

**Module Version:** 19.0 | **Last Updated:** November 2025

