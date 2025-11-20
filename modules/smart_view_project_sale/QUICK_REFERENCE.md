# 🔗 Smart View Project-Sale Integration - Quick Reference Card

## 🚀 Quick Start (30 Seconds)

**Create Project from Approved Sale Order:**
```
1. CRM: Click "✓ Client Approved" button
2. Sales: Open confirmed SO
3. (Optional) Select template in "Project" tab
4. Click: "Create Project" (green button, top right)
5. Done! Project opens automatically ✅
```

**Result:** Project with customer, location, and all details from CRM!

---

## ⚡ What This Module Does

**The Bridge:**
```
CRM Opportunity (Approved)
    ↓
Sale Order (Confirmed)
    ↓
Click "Create Project" Button
    ↓
Project Created with:
✅ Customer (from SO)
✅ Location (from CRM!)
✅ Salesperson (from SO)
✅ Start date (from SO)
✅ Stages & Tasks (from template)
✅ Link back to SO
    ↓
Team Starts Work! 🎉
```

**Key Innovation:** Copies **Project Location** from CRM to Project automatically!

---

## 📍 Navigation

| What | Where |
|------|-------|
| Create Project | SO form → "Create Project" button (header) |
| View Project | SO form → "1 Project" smart button |
| Select Template | SO form → "Project" tab → "Project Template" |
| Approve Opportunity | Opportunity form → "✓ Client Approved" button |
| Create Template | Project → Configuration → Projects → Check "Is Template" |
| View Linked SO | Project form → "Sales Order" field (click link) |

---

## ✅ The 4 Requirements (Tasks 45-48)

### Task 45: Create Project Button ✅

**Button Location:** SO form header (top right)

**Visibility Rules:**
```
Visible when ALL true:
✅ SO state = 'sale' or 'done' (confirmed)
✅ project_id = False (no existing project)
✅ IF opportunity linked:
   opportunity.client_approval_state = 'approved'
```

**Button States:**
- **Green "Create Project"** → Ready to create!
- **Hidden** → Conditions not met
- **Gray "View Project"** → Already created

---

### Task 46: Approval Validation ✅

**The Gate-Keeper:**

Prevents project creation without real client approval!

**Validation Checks:**
```
1. SO confirmed? ✓
2. No existing project? ✓
3. IF opportunity linked:
   - Approved? → ✅ Allow
   - Pending? → ❌ Block with guidance
   - Rejected? → ❌ Block with reason
```

**Error Messages:**

| Status | Error | Action |
|--------|-------|--------|
| **Pending** | "Client approval is pending..." | Go to opportunity → Click "✓ Client Approved" |
| **Rejected** | "Client has rejected... [reason]" | Revise proposal or accept loss |
| **Not Confirmed** | "SO must be confirmed first" | Confirm SO |

---

### Task 47: Template System ✅

**Quick Template Use:**
```
1. Create template once:
   - Project → Create
   - Check "Is Template" ☑️
   - Add stages/tasks
   - Save

2. Use many times:
   - SO → "Project" tab
   - Select template
   - Create project
   - All stages/tasks copied! ✅
```

**Without template:** Empty project (add stages/tasks manually)  
**With template:** Complete project (instant structure!)

---

### Task 48: Field Mapping ✅

**Auto-Copied Fields:**

| From | Field | → | To | Field | Special |
|------|-------|---|----|----|---------|
| SO | name | → | Project | name | Prefixed "Project - " |
| SO | partner_id | → | Project | partner_id | Customer |
| SO | user_id | → | Project | user_id | Salesperson |
| SO | company_id | → | Project | company_id | Company |
| SO | date_order | → | Project | date_start | Start date |
| SO | id | → | Project | sale_order_id | Back-link |
| **CRM** | **project_location** | → | **Project** | **project_location** | **KEY!** |

**No manual re-entry needed!** ✅

---

## 🔄 Complete Workflow

### The Golden Path

```
Phase 1: CRM (Sales)
├── Create opportunity
├── Add project location
├── Move through pipeline
├── Stage: Client Approval
└── Click: "✓ Client Approved" ✅

Phase 2: Sales (SO)
├── Create quotation (from opportunity)
├── Add products/services
├── Send to customer
├── Customer approves
└── Confirm → SO state = 'sale' ✅

Phase 3: Project Creation
├── Open SO
├── (Optional) Select template
├── Click: "Create Project"
├── System validates approval ✅
├── Creates project with all details
└── Opens project form ✅

Phase 4: Execution
├── Team reviews project
├── Location already set (from CRM)
├── Stages ready (from template)
├── Tasks ready (from template)
└── Start work immediately! 🚀
```

**Time:** ~2 minutes from opportunity to project!

---

## 🎯 Common Scenarios

### Scenario 1: Everything Ready (Happy Path)

```
✅ Opportunity: Approved
✅ SO: Confirmed
✅ Template: Selected

Steps:
1. Open SO
2. Select template (optional)
3. Click "Create Project"
4. Done! ✅

Time: 30 seconds
```

---

### Scenario 2: Approval Pending

```
⚠️ Opportunity: NOT approved yet
✅ SO: Confirmed
❌ Can't create project

Steps:
1. Try to create → Button hidden
2. Go to opportunity
3. Click "✓ Client Approved"
4. Return to SO
5. Now can create! ✅

Time: 1-2 minutes
```

---

### Scenario 3: Client Rejected

```
❌ Opportunity: Rejected
✅ SO: Confirmed
❌ Can NOT create project (and shouldn't!)

System blocks with reason:
"Client rejected: [reason text]"

Options:
A) Revise proposal → New opportunity
B) Accept loss → Cancel SO
C) Wait → Follow up later

Protection: System prevents wasted effort ✅
```

---

### Scenario 4: Using Templates

```
📋 Template: "Standard Installation"
✅ Want structured project

Steps:
1. SO → "Project" tab
2. Select: "Standard Installation"
3. Create project
4. Result: Project with ALL stages/tasks! ✅

Time saved: ~10-15 minutes per project
```

---

## 🏗️ Project Templates

### Create Template

```
Project → Configuration → Projects → Create

Name: "Standard Installation Project"
Is Template: ☑️ (IMPORTANT!)
Template Name: "standard_install"

Add: Stages, Tasks, Settings
Save: Template ready! ✅

Use: Select in SO when creating project
```

**Time:** 10-15 minutes (once)  
**Benefit:** Reuse forever!

---

### Template Types (Recommended)

| Template | Duration | Use For |
|----------|----------|---------|
| **Standard Installation** | 4-6 weeks | Most projects |
| **Complex Installation** | 8-12 weeks | Large buildings |
| **Service Only** | 1-2 weeks | Maintenance |
| **Quick Setup** | 1 week | Small projects |

---

### With vs Without Template

**Without Template:**
```
Create project
→ Empty project
→ Manually add 5 stages (5 min)
→ Manually add 4 tasks (10 min)
→ Total: 15 minutes setup

Per Project: 15 minutes ❌
```

**With Template:**
```
Select template
→ Create project
→ All stages copied ✅
→ All tasks copied ✅
→ Total: 30 seconds

Per Project: 30 seconds ✅
Saved: 14.5 minutes! 🎉
```

---

## 🔐 Approval Status Guide

### Status Meanings

| Status | Icon | Meaning | Can Create? | Action |
|--------|------|---------|-------------|--------|
| **Approved** | ✅ | Client confirmed | ✅ YES | Create project! |
| **Pending** | ⚠️ | Awaiting decision | ❌ NO | Wait or get approval |
| **Rejected** | ❌ | Client declined | ❌ NO | Revise or move on |
| *(empty)* | ❓ | Not reviewed | ❌ NO | Get client approval |

---

### Approval Actions

**To Approve:**
```
Opportunity form
→ Click: "✓ Client Approved" (green button)
→ Status: 'approved' ✅
→ Can now create project from SO
```

**To Reject:**
```
Opportunity form
→ Click: "✗ Client Rejected" (red button)
→ Add: Rejection reason
→ Status: 'rejected' ❌
→ Project creation blocked
```

---

## 🛠️ Troubleshooting Quick Fixes

### Button Not Visible?

```
Check:
□ SO confirmed? (not draft/sent)
□ Project doesn't exist? (check smart button)
□ Opportunity approved? (if linked)

Fix:
→ Confirm SO if needed
→ Approve opportunity if pending
→ Check for existing project link
```

---

### Approval Pending Error?

```
Error: "Client approval is pending"

Fix:
1. Click opportunity smart button
2. Click "✓ Client Approved"
3. Return to SO
4. Try again ✅
```

---

### Client Rejected Error?

```
Error: "Client has rejected... [reason]"

Options:
A) Revise: Create new opportunity
B) Accept: Cancel SO, move on
C) Wait: Follow up later

Note: System correctly blocks ✅
```

---

### Location Not Copied?

```
Cause: Location not in opportunity

Fix:
1. Open opportunity
2. Add "Project Location" field
3. For existing project: Add manually
4. For future: Always add in CRM first!
```

---

### No Templates Available?

```
Cause: No templates created yet

Fix:
1. Project → Configuration
2. Create project
3. Check "Is Template" ☑️
4. Save
5. Now available in SO! ✅
```

---

## 📊 Field Mapping Details

### What Gets Copied

**From SO:**
```
✅ Name → "Project - SO001"
✅ Customer → Project customer
✅ Salesperson → Project manager
✅ Company → Project company
✅ Confirmation date → Start date
✅ SO ID → Back-link
```

**From CRM Opportunity:**
```
✅ Project Location → Project location (KEY!)
✅ Opportunity name → Project notes
```

**From Template (if used):**
```
✅ All stages
✅ All tasks
✅ Task hours
✅ Settings
✅ Configurations
```

---

### Special: Project Location

**The Problem:**
```
❌ Enter location in CRM
❌ Re-enter in project
❌ Manual work, risk of error
```

**The Solution:**
```
✅ Enter once in CRM opportunity
✅ Automatically copied to project
✅ No re-entry needed! 🎉
```

**Example:**
```
CRM: "Cairo - New Capital, Building A"
    ↓ (automatic)
Project: "Cairo - New Capital, Building A" ✅
```

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Approve opportunity | 30 sec |
| Create project (no template) | 1 min |
| Create project (with template) | 30 sec |
| Create template (once) | 10-15 min |
| Verify project details | 1-2 min |
| Total: Opportunity → Project | ~2 min ✅ |

**Time Saved with Templates:** ~14 min per project!

---

## 🎓 Best Practices

### DO ✅

**For Sales Reps:**
- ✅ **Add project location** in CRM (IMPORTANT!)
- ✅ **Get real approval** before clicking "Approved"
- ✅ **Select template** before creating project
- ✅ **Notify PM** when project created
- ✅ **Verify details** after creation

**For Project Managers:**
- ✅ **Check approval status** before starting
- ✅ **Verify location** is correct
- ✅ **Customize project** after template copy
- ✅ **Track back to SO** for scope reference
- ✅ **Update templates** based on actuals

**For Administrators:**
- ✅ **Create standard templates** for common projects
- ✅ **Train users** on approval workflow
- ✅ **Monitor approvals** are real
- ✅ **Update templates** quarterly
- ✅ **Require location** in CRM

---

### DON'T ❌

```
❌ Click "Approved" without real client confirmation
❌ Skip approval step (system won't let you anyway)
❌ Forget project location in CRM
❌ Create project before SO confirmed
❌ Try to create multiple projects from same SO
❌ Force project on rejected opportunity
❌ Delete templates (deactivate instead)
```

---

## 🔗 Integration Points

### With CRM (smart_view_crm_enhanced)

```
Reads:
✅ client_approval_state (approval status)
✅ rejection_reason (if rejected)
✅ project_location (key field!)

Validates:
✅ Must be 'approved' to create project
✅ Blocks if 'pending' or 'rejected'
✅ Shows helpful error messages
```

---

### With Project Enhanced (smart_view_project_enhanced)

```
Supports:
✅ Project templates
✅ Task templates
✅ Auto-task generation
✅ Custom stages

Result:
Create project → Template copied → Tasks generated ✅
Complete workflow automation!
```

---

### With Odoo Standard

```
Extends:
✅ sale_project (base SO-Project link)
✅ project (core projects)
✅ sale_management (sales orders)

Adds:
✅ Manual control (not automatic)
✅ Approval validation
✅ Template support
✅ Location mapping
```

---

## 📋 Requirements Checklist

**Before Creating Project:**
- [ ] Opportunity created in CRM
- [ ] Project location added to opportunity
- [ ] Opportunity moved to "Client Approval" stage
- [ ] Client actually approved (not just interest!)
- [ ] "✓ Client Approved" button clicked
- [ ] Quotation created from opportunity
- [ ] Products/services added to SO
- [ ] SO sent to customer
- [ ] SO confirmed (state = 'sale')
- [ ] (Optional) Template selected
- [ ] "Create Project" button visible

**After Creating Project:**
- [ ] Project opens automatically
- [ ] Customer correct
- [ ] Location copied from CRM
- [ ] Salesperson assigned
- [ ] Start date set
- [ ] Template applied (if used)
- [ ] Tasks generated (if template had them)
- [ ] Team notified
- [ ] Work can begin

---

## 💡 Pro Tips

### Tip 1: Always Add Location in CRM

```
✅ Add early in opportunity
✅ Required for project execution
✅ Copied automatically to project
✅ No re-entry needed

Result: Team knows exactly where to go!
```

---

### Tip 2: Create Templates for Common Projects

```
✅ Identify: Types you do often
✅ Create: Template for each type
✅ Use: Speeds up every project
✅ Refine: Update based on actuals

Result: Consistency + Speed!
```

---

### Tip 3: Enforce Approval Workflow

```
✅ Train: Users on process
✅ Monitor: Approvals are real
✅ Respect: Rejection decisions
✅ Document: Approval confirmations

Result: No premature projects!
```

---

### Tip 4: Use Bi-Directional Links

```
✅ SO → Project: Track execution
✅ Project → SO: Verify scope
✅ Quick access: Both directions
✅ Full traceability: Audit trail

Result: Complete visibility!
```

---

### Tip 5: Review Templates Quarterly

```
✅ Compare: Estimated vs actual hours
✅ Adjust: Template hours based on data
✅ Add: New templates for new project types
✅ Archive: Unused templates

Result: Accurate estimates!
```

---

## 🎯 Summary

**One-Line Description:**
> Bridge from Sales to Projects with intelligent CRM approval validation!

**Key Innovation:**
```
Copies project location from CRM to project automatically!
No more re-entering site addresses! 🎉
```

**Key Benefits:**
```
✅ Approval enforcement (no premature projects)
✅ Location tracking (CRM → Project)
✅ Template power (instant structure)
✅ Field mapping (no manual copying)
✅ Bi-directional linking (full traceability)
✅ User-friendly (clear guidance)
```

**Perfect For:**
```
Service companies
Installation projects
Consulting firms
Construction
Any project-based business!
```

**Quick Start:**
```
1. Approve opportunity ✅
2. Confirm SO ✅
3. Click "Create Project" ✅
4. Done! 🚀
```

---

**Print this card and keep it handy! 📌**

**Need detailed help?** → See USER_GUIDE.md

**Module Version:** 19.0.1.0.0 | **Last Updated:** November 2025  
**Status:** ✅ Production Ready | **Integration:** CRM ↔ Sales ↔ Project

🔗 **Seamless workflow from Lead to Delivery!**

