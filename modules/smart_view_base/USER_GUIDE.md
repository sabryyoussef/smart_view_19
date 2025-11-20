# 👥 Smart View Base - Complete User Guide

## Table of Contents
1. [Overview](#overview)
2. [What This Module Does](#what-this-module-does)
3. [Security Groups Explained](#security-groups-explained)
4. [User Management Features](#user-management-features)
5. [Granting Settings Access](#granting-settings-access)
6. [Managing Smart View Users](#managing-smart-view-users)
7. [Use Case Examples](#use-case-examples)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Overview

**Smart View Base** is the foundation module for all Smart View customizations. It provides enhanced user permission management, custom security groups, and shared utilities that other Smart View modules depend on.

**Key Purpose:**
- ✅ Manage user access to Settings (REQ-00018)
- ✅ Define Smart View security groups
- ✅ Track permission levels
- ✅ Provide quick permission management

**Important:** This module is **optional** but recommended if you're using multiple Smart View modules. It provides centralized permission management and shared functionality.

---

## What This Module Does

### Core Features

#### 1. **Custom Security Groups** 🔐

Four specialized permission groups:

| Group | Purpose | Who Needs It |
|-------|---------|--------------|
| **Settings Access** | Full access to system settings | Key users like Mr. Khaled, IT administrators |
| **Enhanced Administrator** | Complete system control | Super administrators |
| **Smart View Manager** | Full access to Smart View modules | Department managers |
| **Smart View User** | Basic Smart View features | Regular employees |

#### 2. **Quick Permission Actions** ⚡

**One-Click Buttons:**
- 🟢 **Grant Settings Access** - Instantly give settings permissions
- 🔴 **Revoke Settings Access** - Instantly remove settings permissions

**Benefits:**
- No need to navigate through complex menus
- Instant permission changes
- Clear confirmation messages
- Audit trail in user notes

#### 3. **Enhanced User Interface** 🎨

**User List View Additions:**
- Smart View Access Level column
- Manager status indicator
- Quick filters

**User Form View Additions:**
- Dedicated "Smart View" tab
- Permission action buttons
- Clear group descriptions
- Internal notes field

#### 4. **Access Level Tracking** 📊

**Track each user's permission level:**
- None: No Smart View access
- User: Basic features
- Manager: Full module access
- Administrator: Complete control

**Benefits:**
- Clear visibility of permissions
- Easy auditing
- Permission documentation

---

## Security Groups Explained

### Group Hierarchy

```
Enhanced Administrator (Complete Control)
    ↓ includes
Settings Access (Full Settings)
    ↓ separate from
Smart View Manager (Smart View Modules)
    ↓ includes
Smart View User (Basic Features)
    ↓ includes
Internal User (Odoo Base)
```

### Detailed Group Permissions

#### 1. 🔑 Settings Access Group

**What You Can Do:**
- ✅ Access ALL Settings menus
- ✅ Configure system parameters
- ✅ Manage company settings
- ✅ Configure modules
- ✅ View technical settings

**What You CANNOT Do:**
- ❌ Manage users (unless also admin)
- ❌ Install/uninstall modules (unless admin)
- ❌ Access developer mode features

**Best For:**
- Mr. Khaled (as per REQ-00018)
- IT staff who need settings access
- Configuration managers
- Power users

**Example Users:**
- IT Administrator
- Configuration Manager
- System Coordinator

---

#### 2. 👑 Enhanced Administrator Group

**What You Can Do:**
- ✅ **Everything** in Settings Access
- ✅ Manage all users
- ✅ Install/uninstall modules
- ✅ Access developer mode
- ✅ Database management
- ✅ Complete system control

**Best For:**
- Super administrators
- System owners
- IT Directors

**Example Users:**
- System Administrator
- IT Director
- Database Administrator

---

#### 3. 💼 Smart View Manager Group

**What You Can Do:**
- ✅ Access all Smart View modules
- ✅ Configure Smart View features
- ✅ Manage teams and data
- ✅ View all records
- ✅ Create reports

**What You CANNOT Do:**
- ❌ Change system settings (unless also has Settings Access)
- ❌ Manage other modules
- ❌ Create/delete users

**Best For:**
- Department managers
- Team leaders
- Module administrators

**Example Users:**
- Sales Manager
- CRM Manager
- Project Manager

---

#### 4. 👤 Smart View User Group

**What You Can Do:**
- ✅ Use Smart View features
- ✅ View own data
- ✅ Create/edit records
- ✅ Generate basic reports

**What You CANNOT Do:**
- ❌ Configure modules
- ❌ Access settings
- ❌ Manage other users
- ❌ View all records (only own/team)

**Best For:**
- Regular employees
- Sales representatives
- Team members

**Example Users:**
- Sales Representative
- Customer Service Agent
- Project Coordinator

---

## User Management Features

### 1. Grant Settings Access (One-Click)

**REQ-00018 Implementation**: Quick way to give full settings access to specific users like Mr. Khaled.

#### Step-by-Step:

1. **Navigate to Users:**
   ```
   Settings → Users & Companies → Users
   ```

2. **Find the User:**
   - Search for user name (e.g., "Khaled")
   - Open user record

3. **Grant Access:**
   - Click 🟢 **"Grant Settings Access"** button in header
   - See confirmation: "Settings access granted to [User Name]"
   - User now has full settings access ✅

4. **Verify:**
   - Go to "Access Rights" tab
   - See "Settings Access" group listed
   - User can now access Settings menu

**Time Required:** 10 seconds! ⚡

---

### 2. Revoke Settings Access

**When to Use:** Remove settings access when user changes role or leaves

#### Step-by-Step:

1. **Open User:**
   - Settings → Users → Select user

2. **Revoke Access:**
   - Click 🔴 **"Revoke Settings Access"** button
   - Confirm action
   - See confirmation message

3. **Result:**
   - "Settings Access" group removed
   - User can no longer access Settings
   - Change logged in user notes

---

### 3. Set Smart View Access Level

**Purpose:** Track and document user's permission level

#### Step-by-Step:

1. **Open User:**
   - Settings → Users → Select user

2. **Go to Smart View Tab:**
   - Click "Smart View" tab

3. **Set Access Level:**
   - Choose from dropdown:
     - None
     - User (Basic)
     - Manager (Full module access)
     - Administrator (Complete control)

4. **Add Notes:**
   - Document why this level was assigned
   - Example: "Approved by IT Director on 2025-11-20"

5. **Save**

---

### 4. View All Smart View Users

**Purpose:** See everyone with Smart View access

#### Access the Menu:

```
Settings → Users & Companies → Smart View Users
```

**What You See:**
- List of users with Smart View groups
- Access level indicators
- Manager status
- Quick filters

**Useful For:**
- Permission audits
- Access reviews
- Team management

---

## Granting Settings Access

### Complete Walkthrough

This is the primary feature (REQ-00018) - giving specific users like Mr. Khaled full settings access.

#### Method 1: Quick Button (Recommended) ⚡

**Fastest Way: ~10 seconds**

```
1. Settings → Users → Search "Khaled"
2. Open user record
3. Click "Grant Settings Access" button
4. Done! ✅
```

**Verification:**
- User sees Settings menu in top bar
- Can access all configuration options
- "Settings Access" appears in Access Rights tab

---

#### Method 2: Manual Group Assignment

**Traditional Way: ~30 seconds**

```
1. Settings → Users → Open user
2. Click "Access Rights" tab
3. Scroll to "Smart View - Base" section
4. Check ☑️ "Settings Access"
5. Save
6. User logs out and back in
```

**When to Use:**
- Assigning multiple groups at once
- Need fine-grained control
- Batch user setup

---

#### Method 3: Technical (Developer)

**For automation or bulk operations:**

```python
# Grant settings access via Python
user = self.env['res.users'].browse(user_id)
user.grant_settings_access()

# Or manually add group
settings_group = self.env.ref('smart_view_base.group_settings_access')
user.groups_id = [(4, settings_group.id)]
```

---

## Managing Smart View Users

### User Lifecycle Management

#### 1. **New User Onboarding**

**Scenario:** New employee joins, needs Smart View access

**Steps:**
```
1. Create user account (Settings → Users → Create)
2. Set basic info (name, email, login)
3. Go to Smart View tab
4. Set access level: "User"
5. Add note: "Sales team member, started 2025-11-20"
6. Access Rights tab → Add to "Smart View User" group
7. Save
8. Test login
```

**Result:** User can access Smart View features with basic permissions

---

#### 2. **User Promotion**

**Scenario:** User becomes manager, needs elevated access

**Steps:**
```
1. Open user record
2. Smart View tab → Change level to "Manager"
3. Access Rights tab → Add to "Smart View Manager" group
4. Add note: "Promoted to Sales Manager on 2025-11-20"
5. Save
```

**Result:** User can now manage Smart View modules

---

#### 3. **Granting Settings Access**

**Scenario:** User needs to configure system (like Mr. Khaled)

**Steps:**
```
1. Open user record
2. Click "Grant Settings Access" button
3. Smart View tab → Set level to "Administrator"
4. Add note: "Settings access granted per management request"
5. Save
```

**Result:** User can access all system settings

---

#### 4. **User Offboarding**

**Scenario:** Employee leaves company

**Steps:**
```
1. Open user record
2. If has settings access → Click "Revoke Settings Access"
3. Access Rights tab → Remove all Smart View groups
4. Smart View tab → Set level to "None"
5. Add note: "Access removed - left company 2025-11-20"
6. Archive user (Action → Archive)
```

**Result:** User has no access, record archived for history

---

## Use Case Examples

### Use Case 1: Mr. Khaled Needs Settings Access (REQ-00018)

**Business Requirement:** Mr. Khaled is a key user who needs full access to system settings to configure the platform.

#### Before Smart View Base:
```
❌ Navigate through multiple menus
❌ Find correct security group
❌ Add to group manually
❌ No clear documentation
❌ Time: 3-5 minutes
```

#### After Smart View Base:
```
✅ Open Khaled's user record
✅ Click "Grant Settings Access" button
✅ Done!
✅ Time: 10 seconds ⚡
```

**Workflow:**

```
Manager: "Khaled needs settings access"
    ↓
Admin opens Khaled's user record
    ↓
Clicks "Grant Settings Access" button
    ↓
Confirmation: "Settings access granted to Khaled"
    ↓
Khaled refreshes browser
    ↓
Sees "Settings" menu ✅
    ↓
Can configure system
    ↓
Admin adds note: "Granted per manager request"
```

**Benefits:**
- ✅ **10x faster** than manual method
- ✅ Clear audit trail
- ✅ No training needed
- ✅ Reversible with one click

---

### Use Case 2: Sales Team Setup

**Scenario:** New sales team of 5 people needs Smart View CRM access

#### Setup Process:

**Step 1: Create Users (5 minutes)**
```
For each team member:
1. Settings → Users → Create
2. Fill: Name, Email, Login
3. Save
```

**Step 2: Assign Smart View Access (2 minutes)**
```
For each user:
1. Open user
2. Smart View tab → Level: "User"
3. Access Rights → Add "Smart View User"
4. Note: "Sales team member"
5. Save
```

**Step 3: Set Sales Manager (1 minute)**
```
For manager:
1. Open user
2. Smart View tab → Level: "Manager"
3. Access Rights → Add "Smart View Manager"
4. Note: "Sales Team Manager"
5. Save
```

**Result:**
- ✅ 5 sales reps can use CRM features
- ✅ 1 manager can configure and manage
- ✅ Clear permission structure
- ✅ Easy to audit

**Total Time:** 8 minutes for 6 users

---

### Use Case 3: Quarterly Permission Audit

**Scenario:** IT department reviews user permissions every quarter

#### Audit Process:

**Step 1: Generate User List**
```
Settings → Users & Companies → Smart View Users
```

**Step 2: Review Each User**
```
For each user in list:
1. Check access level
2. Verify still needs access
3. Review notes
4. Confirm with manager if unclear
```

**Step 3: Update as Needed**
```
If user no longer needs access:
1. Revoke settings access (if applicable)
2. Remove from Smart View groups
3. Set level to "None"
4. Add note with reason
```

**Step 4: Document Audit**
```
Create report:
- Date of audit
- Users reviewed
- Changes made
- Issues found
```

**Benefits:**
- ✅ Security compliance
- ✅ Proper access control
- ✅ Clear audit trail
- ✅ Prevents permission creep

---

### Use Case 4: IT Administrator Setup

**Scenario:** New IT administrator needs complete system access

#### Complete Setup:

```
1. Create User:
   - Name: John Smith
   - Email: john.smith@company.com
   - Login: john.smith

2. Grant Full Access:
   - Access Rights → Check "Settings Access"
   - Access Rights → Check "Enhanced Administrator"
   - Smart View tab → Level: "Administrator"
   - Note: "IT Administrator - full access granted 2025-11-20"

3. Test Access:
   - User logs in
   - Can see Settings menu ✅
   - Can access Users menu ✅
   - Can install modules ✅
   - Can access developer mode ✅

4. Document:
   - Add to IT team distribution list
   - Document in IT procedures
   - Notify security team
```

**Result:** Fully functional IT administrator in 5 minutes

---

### Use Case 5: Temporary Permission Grant

**Scenario:** External consultant needs temporary settings access for 2 weeks

#### Process:

**Week 1: Grant Access**
```
1. Create consultant user account
2. Grant Settings Access (button)
3. Smart View tab → Level: "Administrator"
4. Note: "Temporary access for project - expires 2025-12-04"
5. Set calendar reminder for expiration date
```

**Week 3: Revoke Access**
```
1. Calendar reminder triggers
2. Open consultant user
3. Click "Revoke Settings Access"
4. Remove from all Smart View groups
5. Archive user account
6. Note: "Access removed on schedule"
```

**Benefits:**
- ✅ Clear expiration tracking
- ✅ Easy to grant and revoke
- ✅ Documented timeline
- ✅ Security maintained

---

## Best Practices

### Permission Management Best Practices

#### 1. **Principle of Least Privilege** 🔒

**Always grant minimum required access:**

✅ **Good:**
```
Sales Rep → Smart View User (basic access)
Sales Manager → Smart View Manager (module management)
IT Admin → Settings Access (system configuration)
```

❌ **Bad:**
```
Sales Rep → Settings Access (too much access)
Everyone → Enhanced Administrator (no security)
```

---

#### 2. **Document Everything** 📝

**Use the notes field consistently:**

✅ **Good Notes:**
```
"Settings access granted per CEO request on 2025-11-20 for ERP configuration project"
"Promoted to Manager on 2025-11-15 - approved by HR Director"
"Temporary access for Q4 audit - expires 2025-12-31"
```

❌ **Bad Notes:**
```
"Access granted"
"Manager"
[Empty]
```

**What to Document:**
- Date of change
- Who requested it
- Reason for access
- Expiration date (if temporary)
- Approval source

---

#### 3. **Regular Audits** 🔍

**Review permissions quarterly:**

```
Schedule: Every 3 months
Process:
1. Export Smart View Users list
2. Review each user's access level
3. Confirm with department managers
4. Revoke unnecessary access
5. Document audit in notes
6. Report to management
```

**Red Flags:**
- ⚠️ Users with settings access but not using it
- ⚠️ Inactive users with high permissions
- ⚠️ No notes explaining why access granted
- ⚠️ Multiple administrators in small company

---

#### 4. **Use Quick Buttons** ⚡

**Prefer one-click actions:**

✅ **Recommended:**
```
Use "Grant Settings Access" button → Fast, clear, logged
```

❌ **Not Recommended:**
```
Manually editing multiple groups → Slow, error-prone
```

**Why:**
- Faster (10 seconds vs 3 minutes)
- No mistakes
- Clear confirmation
- Better audit trail

---

#### 5. **Separate Concerns** 🎯

**Don't confuse Smart View access with Settings access:**

| Need | Group | NOT |
|------|-------|-----|
| Use CRM | Smart View User | Settings Access |
| Configure CRM | Smart View Manager | Settings Access |
| Configure System | Settings Access | Smart View Manager |

**Example:**
- CRM Manager needs: Smart View Manager ✅
- CRM Manager does NOT need: Settings Access ❌
- Unless they also configure system settings

---

### User Organization Best Practices

#### 1. **Access Level Naming**

**Be consistent:**

```
None          → No Smart View access
User          → Basic features (Sales Rep, Agent)
Manager       → Full module access (Department Head)
Administrator → Complete control (IT, System Admin)
```

#### 2. **Team-Based Groups**

**Create logical groupings:**

```
Sales Team:
├── Sales Representatives → Smart View User
├── Sales Manager → Smart View Manager
└── Sales Director → Settings Access (if needed)

IT Team:
├── Help Desk → Smart View User
├── IT Coordinator → Smart View Manager
└── IT Administrator → Enhanced Administrator
```

#### 3. **Regular Reviews**

**Monthly quick check:**
- New users added correctly?
- Departed users archived?
- Permission changes documented?
- Any unusual access patterns?

---

## Troubleshooting

### Issue 1: Settings Menu Not Visible

**Symptoms:**
- User should have settings access
- "Settings" menu not appearing in top bar
- Cannot access configuration options

**Solutions:**

✅ **Solution 1: Check Group Assignment**
```
1. Open user record
2. Go to Access Rights tab
3. Look for "Settings Access" group
4. If not there, click "Grant Settings Access" button
5. User logs out and back in
```

✅ **Solution 2: Force Refresh**
```
1. User presses Ctrl + F5 (hard refresh)
2. Or logs out and logs back in
3. Cache is cleared
4. Menu should appear
```

✅ **Solution 3: Verify Module Installation**
```
1. Apps → Search "Smart View Base"
2. Should show "Installed" ✅
3. If not, install module
4. Upgrade if needed
```

---

### Issue 2: Grant Settings Access Button Not Working

**Symptoms:**
- Click button but nothing happens
- No confirmation message
- Group not added

**Solutions:**

✅ **Solution 1: Save User First**
```
1. Make sure user record is saved (has ID)
2. Cannot grant access to unsaved user
3. Save first, then click button
```

✅ **Solution 2: Check Permissions**
```
1. You need administrator rights
2. Settings → Users → Check your access
3. Should have "Settings Access" yourself
```

✅ **Solution 3: Browser Issue**
```
1. Clear browser cache
2. Hard refresh (Ctrl + F5)
3. Try different browser
```

---

### Issue 3: Smart View Menu Not Showing

**Symptoms:**
- Installed Smart View modules
- User has Smart View User group
- Module menus not visible

**Solutions:**

✅ **Solution 1: Check Module Access**
```
1. Verify module is installed
2. Check if module has security groups
3. Assign appropriate group to user
```

✅ **Solution 2: Log Out/In**
```
1. User logs out
2. Waits 10 seconds
3. Logs back in
4. Menus should appear
```

---

### Issue 4: Cannot See Other Users

**Symptoms:**
- Need to manage users
- User list is empty
- Can only see own user

**Solutions:**

✅ **Solution: Need System Access**
```
1. Users need "Settings Access" to see all users
2. Or need to be system administrator
3. Smart View User/Manager groups don't include user management
4. Add "Settings Access" or "Enhanced Administrator"
```

---

### Issue 5: Permission Not Taking Effect

**Symptoms:**
- Granted permission to user
- User still cannot access feature
- Error: "Access Denied"

**Solutions:**

✅ **Solution 1: Clear Session**
```
1. User logs out completely
2. Closes all browser tabs/windows
3. Waits 30 seconds
4. Logs back in
5. Permissions refreshed
```

✅ **Solution 2: Check Record Rules**
```
1. Some features have record-level rules
2. Check if user's team/company is set correctly
3. Verify user is in correct groups
4. May need multiple groups for full access
```

✅ **Solution 3: Module-Specific Groups**
```
1. Smart View Base provides base groups
2. Each module may have additional groups
3. Check specific module's security
4. Assign module-specific groups
```

---

### Issue 6: Too Many Administrators

**Symptoms:**
- Many users have Settings Access
- Security concern
- Hard to track changes

**Solutions:**

✅ **Solution: Audit and Reduce**
```
1. Settings → Smart View Users
2. Filter by access level: "Administrator"
3. For each user:
   - Still needs settings access?
   - Can use Smart View Manager instead?
   - Revoke if not needed
4. Document decisions
5. Set up quarterly review
```

---

## Security Best Practices

### 1. Access Control

**DO:**
- ✅ Grant minimum required access
- ✅ Review permissions quarterly
- ✅ Document all grants in notes
- ✅ Revoke when user leaves
- ✅ Use temporary access for consultants

**DON'T:**
- ❌ Give everyone settings access
- ❌ Leave inactive users active
- ❌ Grant access without documentation
- ❌ Forget to revoke temporary access

---

### 2. Audit Trail

**Always Document:**
```
Who:     Username or employee name
What:    Permission granted/revoked
When:    Exact date and time
Why:     Business reason
By Whom: Approver name or ticket number
```

**Example:**
```
Note: "Settings Access granted to John Smith on 2025-11-20 
per IT Director approval for ERP configuration project. 
Temporary access - expires 2025-12-20. Ticket #12345"
```

---

### 3. Compliance

**For Audit Compliance:**
1. **Track All Changes**
   - Use notes field
   - Export audit reports
   - Keep change history

2. **Separate Duties**
   - Don't give everyone admin rights
   - Use appropriate group levels
   - Maintain checks and balances

3. **Regular Reviews**
   - Monthly quick check
   - Quarterly full audit
   - Annual security review

---

## Quick Reference

### Common Tasks

| Task | Time | Clicks |
|------|------|--------|
| Grant Settings Access | 10 sec | 2 |
| Revoke Settings Access | 10 sec | 2 |
| Set Access Level | 20 sec | 4 |
| View Smart View Users | 5 sec | 3 |
| Assign Group | 30 sec | 5 |

### Group Assignments

| User Role | Smart View Group | Settings Access |
|-----------|------------------|-----------------|
| Employee | Smart View User | No |
| Team Lead | Smart View Manager | No |
| Dept Manager | Smart View Manager | Maybe |
| IT Staff | Settings Access | Yes |
| System Admin | Enhanced Admin | Yes |

### Access Levels

| Level | Use For |
|-------|---------|
| None | External users, contractors |
| User | Regular employees |
| Manager | Team leaders, supervisors |
| Administrator | IT staff, key users like Mr. Khaled |

---

## Getting Help

### Documentation

- 📚 This User Guide (complete reference)
- 🎯 QUICK_REFERENCE.md (one-page card)
- 📖 README.md (overview)
- 🧪 TESTING_GUIDE.md (for admins)

### Support Channels

- **Odoo Forum:** [odoo.com/forum](https://www.odoo.com/forum)
- **Smart View Team:** Internal support
- **IT Department:** For access issues

---

## Conclusion

Smart View Base provides powerful yet simple user permission management. The one-click "Grant Settings Access" feature makes it easy to fulfill requirements like REQ-00018 (giving Mr. Khaled settings access) in just 10 seconds!

**Key Takeaways:**
- ✅ Use quick buttons for speed
- ✅ Document everything in notes
- ✅ Review permissions regularly
- ✅ Grant minimum required access
- ✅ Follow security best practices

**Status:** ✅ Production Ready

**Module Version:** 19.0.1.0.0  
**Last Updated:** November 2025  
**License:** LGPL-3

---

**Need Help?** Check QUICK_REFERENCE.md or contact your IT administrator!

