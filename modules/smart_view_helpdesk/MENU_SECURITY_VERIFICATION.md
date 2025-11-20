# 🔒 Smart View Helpdesk - Menu & Security Verification

## Overview

This document verifies the menu structure and security configuration for **smart_view_helpdesk** wrapper module.

**Important Note:**  
Since `smart_view_helpdesk` is a **wrapper module**, it does NOT define its own menus or security groups. Instead, it inherits ALL menu and security features from the OCA `helpdesk_mgmt` module.

---

## Architecture

```
smart_view_helpdesk (Wrapper)
    ↓ depends on
helpdesk_mgmt (OCA Module)
    ↓ provides
Menus ✅
Security Groups ✅
Access Rights ✅
Record Rules ✅
```

**Result:** Full helpdesk menu and security available through dependency!

---

## Menu Structure (Inherited from helpdesk_mgmt)

### Main Menu: Helpdesk

**Location:** Top menu bar  
**Technical ID:** `helpdesk_mgmt.helpdesk_menu_root`  
**Visibility:** Users with Helpdesk User or Helpdesk Manager group

```
Helpdesk (Main Menu)
├── Tickets
│   ├── All Tickets
│   ├── My Tickets
│   └── My Team's Tickets
├── Dashboard
├── Configuration
│   ├── Teams
│   ├── Stages
│   ├── Categories
│   └── Tags
└── Reports
    └── Ticket Analysis
```

---

### Menu Items Detail

#### 1. **Helpdesk** (Root Menu)
- **ID:** `helpdesk_mgmt.helpdesk_menu_root`
- **Type:** Main menu
- **Groups:** `group_helpdesk_user`, `group_helpdesk_manager`
- **Status:** ✅ Available to all helpdesk users

#### 2. **Tickets → All Tickets**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_menu`
- **Model:** `helpdesk.ticket`
- **View Modes:** kanban, list, form, activity, pivot, graph
- **Groups:** `group_helpdesk_user`, `group_helpdesk_manager`
- **Status:** ✅ Available

#### 3. **Tickets → My Tickets**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_menu_my`
- **Model:** `helpdesk.ticket`
- **Filter:** Assigned to current user
- **Groups:** `group_helpdesk_user`
- **Status:** ✅ Available

#### 4. **Tickets → My Team's Tickets**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_menu_team`
- **Model:** `helpdesk.ticket`
- **Filter:** Team = current user's team
- **Groups:** `group_helpdesk_user`
- **Status:** ✅ Available

#### 5. **Configuration → Teams**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_team_menu`
- **Model:** `helpdesk.ticket.team`
- **Groups:** `group_helpdesk_manager`
- **Status:** ✅ Managers only

#### 6. **Configuration → Stages**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_stage_menu`
- **Model:** `helpdesk.ticket.stage`
- **Groups:** `group_helpdesk_manager`
- **Status:** ✅ Managers only

#### 7. **Configuration → Categories**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_category_menu`
- **Model:** `helpdesk.ticket.category`
- **Groups:** `group_helpdesk_manager`
- **Status:** ✅ Managers only

#### 8. **Configuration → Tags**
- **ID:** `helpdesk_mgmt.helpdesk_ticket_tag_menu`
- **Model:** `helpdesk.ticket.tag`
- **Groups:** `group_helpdesk_manager`
- **Status:** ✅ Managers only

---

## Security Groups (Inherited from helpdesk_mgmt)

### Group Hierarchy

```
Base Access (Portal User)
    ↓
Helpdesk User
    ↓
Helpdesk Manager
```

### 1. **Helpdesk User**

**Technical ID:** `helpdesk_mgmt.group_helpdesk_user`  
**Category:** Helpdesk  
**Implied Groups:** `base.group_user`

**Permissions:**
- ✅ View assigned tickets
- ✅ View team tickets
- ✅ Create tickets
- ✅ Update tickets
- ✅ Reply to customers
- ✅ Change ticket stage
- ✅ Add attachments
- ✅ Add internal notes
- ❌ Delete tickets (limited)
- ❌ Configure teams
- ❌ Configure stages

**Menu Access:**
- ✅ Helpdesk → Tickets (All)
- ✅ Helpdesk → My Tickets
- ✅ Helpdesk → My Team's Tickets
- ✅ Helpdesk → Dashboard
- ❌ Helpdesk → Configuration

**Use Case:** Support agents, IT staff, customer service reps

---

### 2. **Helpdesk Manager**

**Technical ID:** `helpdesk_mgmt.group_helpdesk_manager`  
**Category:** Helpdesk  
**Implied Groups:** `group_helpdesk_user`

**Permissions:**
- ✅ All Helpdesk User permissions
- ✅ View ALL tickets (any team)
- ✅ Delete tickets
- ✅ Create/edit teams
- ✅ Configure stages
- ✅ Manage categories
- ✅ Manage tags
- ✅ Access reports
- ✅ Full configuration access

**Menu Access:**
- ✅ All Helpdesk User menus
- ✅ Helpdesk → Configuration → Teams
- ✅ Helpdesk → Configuration → Stages
- ✅ Helpdesk → Configuration → Categories
- ✅ Helpdesk → Configuration → Tags
- ✅ Helpdesk → Reports

**Use Case:** Support managers, helpdesk administrators

---

### 3. **Portal User** (Special)

**Technical ID:** `base.group_portal`  
**Category:** Base  
**Special Rules:** Portal-specific record rules

**Permissions:**
- ✅ View OWN tickets only
- ✅ Create tickets
- ✅ Reply to own tickets
- ✅ Upload attachments to own tickets
- ❌ View other customer tickets
- ❌ View internal notes
- ❌ Access configuration

**Portal Access:**
- ✅ My Account → My Tickets
- ✅ Submit New Ticket (from portal)
- ✅ View ticket status
- ✅ Reply to tickets

**Use Case:** Customers, external users

---

## Access Rights (ir.model.access)

### Model: helpdesk.ticket

| Group | Read | Write | Create | Delete |
|-------|------|-------|--------|--------|
| Helpdesk User | ✅ | ✅ | ✅ | ⚠️ Limited |
| Helpdesk Manager | ✅ | ✅ | ✅ | ✅ |
| Portal User | ✅ Own | ✅ Own | ✅ | ❌ |

### Model: helpdesk.ticket.team

| Group | Read | Write | Create | Delete |
|-------|------|-------|--------|--------|
| Helpdesk User | ✅ | ❌ | ❌ | ❌ |
| Helpdesk Manager | ✅ | ✅ | ✅ | ✅ |

### Model: helpdesk.ticket.stage

| Group | Read | Write | Create | Delete |
|-------|------|-------|--------|--------|
| Helpdesk User | ✅ | ❌ | ❌ | ❌ |
| Helpdesk Manager | ✅ | ✅ | ✅ | ✅ |

### Model: helpdesk.ticket.category

| Group | Read | Write | Create | Delete |
|-------|------|-------|--------|--------|
| Helpdesk User | ✅ | ❌ | ❌ | ❌ |
| Helpdesk Manager | ✅ | ✅ | ✅ | ✅ |

### Model: helpdesk.ticket.tag

| Group | Read | Write | Create | Delete |
|-------|------|-------|--------|--------|
| Helpdesk User | ✅ | ❌ | ❌ | ❌ |
| Helpdesk Manager | ✅ | ✅ | ✅ | ✅ |

---

## Record Rules (Security Filters)

### 1. Helpdesk User - Own/Team Tickets

**Rule ID:** `helpdesk_mgmt.helpdesk_ticket_rule_user`  
**Model:** `helpdesk.ticket`  
**Groups:** `group_helpdesk_user`

**Domain:**
```python
[
    '|',
    ('user_id', '=', user.id),              # Assigned to me
    ('team_id.member_ids', 'in', [user.id]) # Or my team
]
```

**Permissions:**
- Read: ✅ Own + Team tickets
- Write: ✅ Own + Team tickets
- Create: ✅ Any ticket
- Delete: ⚠️ Own tickets only

---

### 2. Helpdesk Manager - All Tickets

**Rule ID:** `helpdesk_mgmt.helpdesk_ticket_rule_manager`  
**Model:** `helpdesk.ticket`  
**Groups:** `group_helpdesk_manager`

**Domain:**
```python
[(1, '=', 1)]  # All records
```

**Permissions:**
- Read: ✅ ALL tickets
- Write: ✅ ALL tickets
- Create: ✅ Any ticket
- Delete: ✅ ALL tickets

---

### 3. Portal User - Own Tickets Only

**Rule ID:** `helpdesk_mgmt.helpdesk_ticket_rule_portal`  
**Model:** `helpdesk.ticket`  
**Groups:** `base.group_portal`

**Domain:**
```python
[('partner_id', '=', user.partner_id.id)]  # Customer's own tickets
```

**Permissions:**
- Read: ✅ Own tickets only
- Write: ✅ Own tickets (limited fields)
- Create: ✅ Own tickets
- Delete: ❌ Not allowed

---

## Granting Access

### Method 1: Via User Form (Recommended)

**Steps:**
1. Go to: `Settings → Users & Companies → Users`
2. Open user record
3. Go to: `Access Rights` tab
4. Find: `Helpdesk` section
5. Select:
   - ☑️ **Helpdesk User** (for agents)
   - OR ☑️ **Helpdesk Manager** (for managers)
6. Click: `Save`

**Result:** User can now access Helpdesk menu! ✅

---

### Method 2: Via Groups (Advanced)

**Steps:**
1. Developer Mode: ON
2. Go to: `Settings → Technical → Security → Groups`
3. Search: "Helpdesk"
4. Open: `Helpdesk User` or `Helpdesk Manager`
5. Tab: `Users`
6. Click: `Add` → Select users
7. Save

---

### Method 3: Automatic Assignment (XML)

**For admin user (example from helpdesk_mgmt):**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="base.user_admin" model="res.users">
        <field name="groups_id" eval="[(4, ref('helpdesk_mgmt.group_helpdesk_manager'))]"/>
    </record>
</odoo>
```

**Note:** The OCA `helpdesk_mgmt` module includes automatic admin group assignment in `data/assign_admin_group.xml`.

---

## Portal User Setup

### Granting Portal Access to Customers

**Steps:**
1. Go to: `Contacts`
2. Find customer contact
3. Click: `Action` → `Grant Portal Access`
4. System sends email with login credentials
5. Customer logs in to portal
6. Can now submit and view tickets! ✅

**What Customer Sees:**
- Portal homepage
- "My Tickets" menu item
- "Submit Ticket" button
- Own tickets only
- Ticket details
- Ability to reply

**What Customer Does NOT See:**
- Other customers' tickets
- Internal notes
- Configuration menus
- Full Odoo interface

---

## Troubleshooting Menu Visibility

### Issue: Helpdesk Menu Not Visible

#### ✅ Check 1: Module Installed?

```
Apps → Search "Helpdesk Management"
Status should be: Installed ✅
If not: Install module first
```

#### ✅ Check 2: User Has Correct Group?

```
Settings → Users → [User]
Access Rights → Helpdesk section
Should have: Helpdesk User OR Helpdesk Manager
If not: Assign proper group
```

#### ✅ Check 3: User Logged In?

```
Some menus only appear after login
Try: Logout → Login again
Clear browser cache if needed
```

#### ✅ Check 4: Refresh Browser

```
Hard refresh: Ctrl + Shift + R (Windows/Linux)
Or: Cmd + Shift + R (Mac)
Clear cache and refresh
```

---

### Issue: Configuration Menu Not Visible

**Expected Behavior:**  
Configuration menus are **Manager Only** ✅

**Solution:**
- Only `Helpdesk Manager` group sees Configuration
- `Helpdesk User` group does NOT see Configuration (by design)
- To access: Need Manager role

---

### Issue: Can't Create Tickets

#### Check Permissions:
```
Need minimum: Helpdesk User role
Check: Settings → Users → [User] → Access Rights
```

#### Check Team Exists:
```
At least one team must exist
If no teams: Manager creates team first
```

---

## Wrapper Module Security Notes

### What smart_view_helpdesk Provides

**Security-wise:**
```
✅ Ensures helpdesk_mgmt is installed
✅ Inherits all security from OCA module
✅ No additional security defined (none needed)
✅ Clean dependency management
✅ Smart View compatibility verified
```

### What helpdesk_mgmt Provides

**Complete Security:**
```
✅ Security groups defined
✅ Access rights configured
✅ Record rules implemented
✅ Portal access enabled
✅ Field-level security
✅ Menu restrictions
```

**Result:**  
Wrapper + OCA = Complete, secure helpdesk system! 🔒

---

## Best Practices

### For Administrators

**1. Initial Setup:**
```
✅ Install both modules (helpdesk_mgmt + smart_view_helpdesk)
✅ Create at least one team
✅ Assign users to proper groups
✅ Test with regular user account
✅ Verify portal access for customers
```

**2. User Management:**
```
✅ Grant Helpdesk User to support agents
✅ Grant Helpdesk Manager to supervisors
✅ Use Portal access for customers
✅ Review permissions quarterly
✅ Remove access for departed users
```

**3. Security Audit:**
```
✅ Review who has Manager access
✅ Verify portal users see only own tickets
✅ Test record rules regularly
✅ Monitor access logs
✅ Update security as team grows
```

---

## Compliance & Audit

### GDPR Considerations

**Customer Data:**
- ✅ Tickets contain customer info
- ✅ Portal users see only own data
- ✅ Internal users see assigned/team data
- ✅ Managers see all data
- ⚠️ Consider data retention policies

**Data Access Tracking:**
- ✅ Odoo tracks user access
- ✅ Chatter logs all changes
- ✅ Audit trail available
- ✅ Can export customer data

---

### Security Audit Checklist

**Monthly Checks:**
- [ ] Review active Helpdesk Managers
- [ ] Verify user group assignments
- [ ] Check for inactive users with access
- [ ] Review portal user list
- [ ] Test portal isolation (can't see others' tickets)

**Quarterly Checks:**
- [ ] Full permission audit
- [ ] Review record rules
- [ ] Test each role's capabilities
- [ ] Update documentation
- [ ] Security training refresher

---

## Verification Summary

### ✅ Menu Structure
- **Source:** OCA helpdesk_mgmt
- **Status:** ✅ Fully inherited
- **Visibility:** Group-based (User/Manager)
- **Configuration:** No additional setup needed

### ✅ Security Groups
- **Source:** OCA helpdesk_mgmt
- **Count:** 2 main groups + portal
- **Hierarchy:** User → Manager
- **Status:** ✅ Production-ready

### ✅ Access Rights
- **Models:** 5+ models secured
- **Granularity:** Read/Write/Create/Delete per group
- **Status:** ✅ Properly configured

### ✅ Record Rules
- **Count:** 3 main rules
- **Coverage:** All user types
- **Portal Isolation:** ✅ Secure
- **Status:** ✅ Tested and verified

### ✅ Wrapper Integration
- **Dependencies:** Correct
- **Inheritance:** ✅ All features available
- **Maintenance:** ✅ Minimal
- **Status:** ✅ Production-ready

---

## Conclusion

**Smart View Helpdesk** successfully integrates the OCA `helpdesk_mgmt` module, providing:

✅ **Complete menu structure** (inherited)  
✅ **Robust security groups** (User, Manager, Portal)  
✅ **Granular access rights** (model-level)  
✅ **Secure record rules** (row-level)  
✅ **Portal isolation** (customer privacy)  
✅ **Production-ready** (battle-tested by community)

**Architecture Decision:** ✅ **Wrapper approach is optimal!**
- No custom security needed (uses proven OCA security)
- Minimal maintenance (community handles updates)
- Full feature set (everything inherited)
- Zero security gaps (tested by thousands)

---

## References

### Documentation
- **This Document:** Menu & Security verification
- **USER_GUIDE.md:** Complete usage guide
- **QUICK_REFERENCE.md:** Quick reference card
- **README.md:** Module overview

### OCA Module
- **Module:** helpdesk_mgmt
- **Repository:** [OCA/helpdesk](https://github.com/OCA/helpdesk)
- **Version:** 19.0
- **License:** AGPL-3

### Smart View Wrapper
- **Module:** smart_view_helpdesk
- **Version:** 19.0.1.0.0
- **License:** LGPL-3
- **Type:** Wrapper/Integration module

---

**Verification Date:** November 2025  
**Verified By:** Smart View Development Team  
**Status:** ✅ All security properly configured and inherited  
**Next Review:** After major OCA updates

**Need Help?** See USER_GUIDE.md or contact your administrator!

