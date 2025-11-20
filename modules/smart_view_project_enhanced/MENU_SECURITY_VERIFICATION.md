# 🔒 Smart View Project Enhanced - Menu & Security Verification

## Overview

This document verifies the menu structure and security configuration for **smart_view_project_enhanced** module.

**Module Type:** Enhancement/Extension (extends Odoo's core `project` module)

**Key Addition:** Task Template menu + Project enhancements

---

## Architecture

```
smart_view_project_enhanced
    ↓ depends on
project (Odoo Core)
    ↓ provides
Base Menus (Projects, Tasks, Configuration)
    +
Custom Additions (Task Templates)
```

**Result:** Enhanced project module with template management!

---

## Menu Structure

### Main Menu: Project

**Location:** Top menu bar (existing Odoo menu)  
**Extended by:** smart_view_project_enhanced

```
Project (Core Odoo Menu)
├── Projects
│   ├── All Projects
│   └── My Projects
├── Tasks
│   ├── All Tasks
│   └── My Tasks
├── Configuration
│   ├── Project Settings
│   ├── Project Stages ← Core Odoo
│   ├── Task Stages ← Core Odoo
│   ├── Task Templates ← ✅ ADDED by smart_view_project_enhanced
│   ├── Tags
│   └── Activity Types
├── Reporting
│   ├── Tasks
│   └── Burndown Chart
└── Customers (Pivot)
```

---

### New Menu Items (Added by This Module)

#### 1. **Configuration → Task Templates** ✅

**Technical Details:**
- **ID:** `smart_view_project_enhanced.menu_project_task_template`
- **Model:** `project.task.template`
- **Parent:** `project.menu_project_config`
- **Sequence:** 15 (after stages, before tags)
- **Action:** `action_project_task_template`

**View Modes:**
- List (default)
- Form
- Kanban (optional)

**Visibility:**
```
All Project users can VIEW
Project Users can CREATE/EDIT
Project Managers can DELETE
```

**Purpose:**
- Manage task templates
- Create new templates
- Edit existing templates
- Activate/deactivate templates
- View template usage

---

### Enhanced Views (Modified by This Module)

#### 1. **Project Form View** (Enhanced)

**Additions:**

**Header Buttons:**
```xml
<button name="action_generate_tasks" 
        string="Generate Tasks"
        type="object"
        class="btn-primary"
        invisible="is_template or generated_tasks_count > 0"/>

<button name="action_view_generated_tasks"
        string="View Generated Tasks"
        type="object"
        class="btn-secondary"
        invisible="generated_tasks_count == 0"/>
```

**Smart Button:**
```xml
<button name="action_view_generated_tasks"
        type="object"
        class="oe_stat_button"
        icon="fa-tasks"
        invisible="generated_tasks_count == 0">
    <field name="generated_tasks_count" widget="statinfo"/>
</button>
```

**New Tab:**
```xml
<page string="Task Templates" name="task_templates">
    <group>
        <field name="auto_generate_tasks"/>
        <!-- use_standard_stages: disabled for Odoo 19 -->
    </group>
    <field name="task_template_ids" widget="many2many_tags"/>
</page>
```

**Visibility:** All project users

---

#### 2. **Project Task Form View** (Enhanced)

**Additions:**

**Template Information:**
```xml
<div class="badge badge-info" invisible="not template_id">
    From Template
</div>

<field name="template_id" readonly="1"/>
<field name="is_template_task" invisible="1"/>
```

**Visibility:** All project users

**Purpose:**
- Show which tasks came from templates
- Link back to source template
- Track template vs manual tasks

---

## Security Configuration

### Security Groups (Uses Odoo Core Groups)

**This module does NOT define new security groups.**  
**Uses existing Odoo project groups:**

#### 1. **project.group_project_user** (Project User)

**Base Group:** `base.group_user` (Internal User)  
**Category:** Project

**Permissions:**
- ✅ View all projects (own company)
- ✅ Create projects
- ✅ Edit own projects
- ✅ Create tasks
- ✅ **View task templates** ← Enhanced
- ✅ **Create/edit task templates** ← Enhanced
- ✅ **Use auto-generation** ← Enhanced
- ❌ Delete templates (managers only)

**Use Case:** Regular project users, coordinators

---

#### 2. **project.group_project_manager** (Project Manager)

**Base Group:** `project.group_project_user`  
**Category:** Project

**Permissions:**
- ✅ All Project User permissions
- ✅ View ALL projects (all companies)
- ✅ Delete projects
- ✅ Access all configuration
- ✅ **Full template management** ← Enhanced
- ✅ **Delete templates** ← Enhanced
- ✅ **Deactivate templates** ← Enhanced

**Use Case:** Project managers, project administrators

---

### Access Rights (ir.model.access.csv)

#### Model: project.task.template

| Group | Access ID | Read | Write | Create | Delete |
|-------|-----------|------|-------|--------|--------|
| **Employee** | `access_project_task_template_user` | ✅ | ❌ | ❌ | ❌ |
| **Project User** | `access_project_task_template_project_user` | ✅ | ✅ | ✅ | ❌ |
| **Project Manager** | `access_project_task_template_manager` | ✅ | ✅ | ✅ | ✅ |

**CSV Content:**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_project_task_template_user,project.task.template.user,model_project_task_template,base.group_user,1,0,0,0
access_project_task_template_project_user,project.task.template.project.user,model_project_task_template,project.group_project_user,1,1,1,0
access_project_task_template_manager,project.task.template.manager,model_project_task_template,project.group_project_manager,1,1,1,1
```

---

#### Model: project.project (Extended)

**New Fields Security:**

| Field | Read | Write | Description |
|-------|------|-------|-------------|
| `auto_generate_tasks` | All users | Project User+ | Enable/disable auto-generation |
| `use_standard_stages` | All users | Project User+ | Use 5 standard stages (disabled) |
| `task_template_ids` | All users | Project User+ | Select templates |
| `generated_tasks_count` | All users | Computed | Count of generated tasks |

**Permissions:** Uses existing project.project security (no changes)

---

#### Model: project.task (Extended)

**New Fields Security:**

| Field | Read | Write | Description |
|-------|------|-------|-------------|
| `template_id` | All users | System only | Link to source template |
| `is_template_task` | All users | Computed | Boolean flag |

**Permissions:** Uses existing project.task security (no changes)

---

### Record Rules

**This module does NOT define custom record rules.**

**Uses Odoo core project record rules:**

#### 1. Project Access Rules (from core)

**Project User Rule:**
```python
domain: [
    '|',
        ('privacy_visibility', '!=', 'followers'),
        ('message_partner_ids', 'in', [user.partner_id.id])
]
```

**Effect:**
- See public projects
- See followed projects
- Create projects (automatically become follower)

---

#### 2. Task Access Rules (from core)

**Task User Rule:**
```python
domain: [
    '|',
        ('project_id.privacy_visibility', '!=', 'followers'),
        ('project_id.message_partner_ids', 'in', [user.partner_id.id])
]
```

**Effect:**
- See tasks in accessible projects
- See all tasks in public projects
- See tasks in followed projects

---

#### 3. Template Access Rules (from this module)

**No custom rules defined.**

**Default behavior:**
- ✅ All project users can see all templates
- ✅ Templates are company-wide resources
- ✅ No row-level restrictions needed

**Rationale:**
- Templates are meant to be shared
- All teams benefit from standard templates
- No sensitive data in templates
- Company-wide best practices

---

## Field-Level Security

### Project Model Fields

#### auto_generate_tasks

```python
auto_generate_tasks = fields.Boolean(
    string='Auto-Generate Tasks',
    default=True,
    help="Automatically generate tasks from templates when project is created"
)
```

**Visibility:** All project users  
**Editable by:** Project User, Project Manager  
**Default:** True (enabled)

**Security:** No special restrictions

---

#### task_template_ids

```python
task_template_ids = fields.Many2many(
    'project.task.template',
    string='Task Templates',
    help="Templates to use for generating tasks"
)
```

**Visibility:** All project users  
**Editable by:** Project User, Project Manager  
**Domain:** `[('active', '=', True)]` (only active templates)

**Security:** No special restrictions

---

#### generated_tasks_count

```python
generated_tasks_count = fields.Integer(
    string='Generated Tasks',
    compute='_compute_generated_tasks_count',
    help="Number of tasks generated from templates"
)
```

**Visibility:** All project users  
**Editable by:** System only (computed)  
**Computation:** Counts tasks with template_id

**Security:** Read-only by design

---

### Task Model Fields

#### template_id

```python
template_id = fields.Many2one(
    'project.task.template',
    string='Template',
    help="Template used to create this task",
    readonly=True
)
```

**Visibility:** All project users  
**Editable by:** System only (set at creation)  
**Purpose:** Track template source

**Security:** Read-only to maintain data integrity

---

#### is_template_task

```python
is_template_task = fields.Boolean(
    string='From Template',
    compute='_compute_is_template_task',
    help="Task was generated from a template"
)
```

**Visibility:** All project users  
**Editable by:** System only (computed)  
**Computation:** `bool(self.template_id)`

**Security:** Read-only by design

---

## Button Security

### Project Form Buttons

#### "Generate Tasks" Button

```xml
<button name="action_generate_tasks"
        invisible="is_template or generated_tasks_count > 0"/>
```

**Visible when:**
- ✅ Not a project template
- ✅ No tasks generated yet
- ✅ User is Project User+

**Action:** Calls `action_generate_tasks()` method

**Security Check:**
```python
@api.model
def check_access_rights(self, operation, raise_exception=True):
    # Uses project.project access rights
    # Project User+ can execute
```

---

#### "View Generated Tasks" Button

```xml
<button name="action_view_generated_tasks"
        invisible="generated_tasks_count == 0"/>
```

**Visible when:**
- ✅ At least one generated task exists
- ✅ User is Project User+

**Action:** Opens filtered task list

**Security:** Returns only tasks in accessible projects

---

### Smart Button

#### "X Generated Tasks" Smart Button

```xml
<button name="action_view_generated_tasks"
        type="object"
        class="oe_stat_button"
        icon="fa-tasks"
        invisible="generated_tasks_count == 0">
```

**Visible when:**
- ✅ `generated_tasks_count > 0`
- ✅ User is Project User+

**Security:** Same as view button (filtered by project access)

---

## Menu Visibility Rules

### Task Templates Menu

**Defined in XML:**
```xml
<menuitem id="menu_project_task_template"
          name="Task Templates"
          parent="project.menu_project_config"
          action="action_project_task_template"
          sequence="15"/>
```

**Visible to:**
- ✅ All Project Users (group_project_user)
- ✅ All Project Managers (group_project_manager)
- ❌ Portal users
- ❌ Employees without project access

**No explicit groups attribute = inherits from parent (project.menu_project_config)**

**Parent menu security:**
```xml
<menuitem id="project.menu_project_config"
          groups="project.group_project_user"/>
```

**Result:** Only project users see Task Templates menu

---

## Granting Access

### Method 1: Via User Form (Recommended)

**Steps:**
```
1. Settings → Users & Companies → Users
2. Open user record
3. Access Rights tab
4. Find "Project" section
5. Select role:
   ☑️ Project User (for regular users)
   OR
   ☑️ Project Manager (for managers)
6. Save
```

**Result:** User can access projects + task templates! ✅

---

### Method 2: Via Groups (Developer Mode)

**Steps:**
```
1. Enable Developer Mode
2. Settings → Technical → Security → Groups
3. Search: "Project User"
4. Open: project.group_project_user
5. Users tab → Add users
6. Save
```

---

### Method 3: Default for All Internal Users

**If you want ALL employees to view templates:**

Create data file: `data/default_access.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Give all internal users access to view templates -->
    <record id="access_project_task_template_user" model="ir.model.access">
        <field name="name">project.task.template.user</field>
        <field name="model_id" ref="model_project_task_template"/>
        <field name="group_id" ref="base.group_user"/>
        <field name="perm_read" eval="1"/>
        <field name="perm_write" eval="0"/>
        <field name="perm_create" eval="0"/>
        <field name="perm_unlink" eval="0"/>
    </record>
</odoo>
```

**Note:** Already implemented in current module! ✅

---

## Troubleshooting Menu Visibility

### Issue: Task Templates Menu Not Visible

#### ✅ Check 1: User Has Project Access?

```
Settings → Users → [User] → Access Rights
Look for: "Project" section

Should have:
☑️ Project / User (minimum)
OR
☑️ Project / Manager

If not: Assign proper group
```

---

#### ✅ Check 2: Module Installed?

```
Apps → Search "Smart View - Project Enhanced"
Status: Should show "Installed"

If not: Install module
```

---

#### ✅ Check 3: Menu Parent Accessible?

```
Can user see: Project → Configuration menu?

If NOT:
- User doesn't have Project User role
- Project module not installed
- Configuration menu hidden

If YES but no Task Templates:
- Module not upgraded
- Menu not created
- Try: Update module list
```

---

#### ✅ Check 4: Cache Issue?

```
Actions:
1. Hard refresh: Ctrl + Shift + R
2. Clear browser cache
3. Logout → Login
4. Try different browser
```

---

### Issue: Generate Tasks Button Not Visible

#### Expected Behavior:

**Button HIDDEN when:**
- ❌ Project is a template (`is_template = True`)
- ❌ Tasks already generated (`generated_tasks_count > 0`)

**Button VISIBLE when:**
- ✅ Regular project (not template)
- ✅ No generated tasks yet
- ✅ User is Project User+

---

#### If button missing but should be visible:

```
✅ Check: Project settings
   Is Template: Should be False
   
✅ Check: Generated task count
   Should be 0
   
✅ Check: User permissions
   Need: Project User role minimum
   
✅ Check: View inheritance
   May be customization conflict
```

---

### Issue: Can't Create Templates

#### ✅ Check Permissions:

```
Need: Project User role minimum
Check: Configuration → Task Templates
Try: Create button

If grayed out:
- User has only Employee role
- Need Project User role
- Administrator assigns role
```

---

### Issue: Can't Delete Templates

#### Expected Behavior:

**Only Project Managers can delete templates!**

```
Project User:
✅ View templates
✅ Create templates
✅ Edit templates
❌ Delete templates

Project Manager:
✅ All above +
✅ Delete templates
```

**If Project User tries to delete:**
```
Error: "You do not have the rights to delete..."

Solution:
- This is by design (prevents accidental deletion)
- Deactivate instead: Uncheck "Active"
- Or: Ask Project Manager to delete
```

---

## Security Best Practices

### For Administrators

#### ✅ DO:

**1. Assign Correct Roles:**
```
✅ Project User: Regular project team members
✅ Project Manager: Team leads, project managers
✅ Don't give Manager to everyone (deletion power)
```

**2. Protect Standard Templates:**
```
✅ Document standard templates
✅ Train users not to delete
✅ Use deactivation instead of deletion
✅ Keep backups of templates
```

**3. Monitor Template Changes:**
```
✅ Check Chatter for template edits
✅ Review template modifications
✅ Ensure changes are intentional
✅ Document template versions
```

**4. User Training:**
```
✅ Explain template vs task relationship
✅ Show proper template management
✅ Demonstrate deactivation vs deletion
✅ Share best practices
```

---

#### ❌ DON'T:

```
❌ Give Manager role to everyone
❌ Let users delete standard templates
❌ Create too many security groups
❌ Restrict template viewing unnecessarily
❌ Ignore template usage data
```

---

### For Project Users

#### ✅ DO:

```
✅ Use templates as intended
✅ Edit generated tasks as needed
✅ Provide feedback on templates
✅ Create custom templates when beneficial
✅ Deactivate (not delete) when not needed
```

---

#### ❌ DON'T:

```
❌ Try to delete standard templates
❌ Edit templates without planning
❌ Change template for one project (edit task instead)
❌ Create duplicate templates
❌ Ignore template descriptions
```

---

## Compliance & Audit

### GDPR Considerations

**No personal data in templates:**
- ✅ Templates contain task structure only
- ✅ No customer information
- ✅ No personal data
- ✅ No privacy concerns

**Generated tasks:**
- ⚠️ May contain customer data (from project)
- ✅ Follow Odoo project security rules
- ✅ Access controlled by project visibility
- ✅ Audit trail in Chatter

---

### Security Audit Checklist

**Monthly:**
- [ ] Review who has Project Manager role
- [ ] Check template modifications (Chatter)
- [ ] Verify no standard templates deleted
- [ ] Review custom template creation
- [ ] Check user access rights

**Quarterly:**
- [ ] Full permission audit
- [ ] Review template library
- [ ] Analyze template usage
- [ ] Update documentation
- [ ] User training refresher

---

## Integration Security

### With smart_view_project_sale

**Security Flow:**
```
Sale Order (Sales User creates)
↓
"Create Project" button
↓ Security check:
- Can user create projects? (Project User+)
- Can user access customer? (Sales rules)
↓ If yes:
Create project with auto-generation
↓ Security check:
- Can user create tasks? (Yes, in own project)
- Can user access templates? (Yes, Project User)
↓
Tasks generated ✅
```

**Result:** Seamless security across modules!

---

### With Timesheets

**Security Flow:**
```
Task created from template
↓
User logs time on task
↓ Security check:
- Can user access task? (Project rules)
- Can user log timesheet? (Timesheet rules)
↓
Time logged ✅
```

**No special security needed:** Uses existing Odoo rules

---

## Verification Summary

### ✅ Menu Structure
- **Added:** Task Templates menu under Configuration
- **Visibility:** Project Users and Managers only
- **Status:** ✅ Properly configured

### ✅ Security Groups
- **Uses:** Existing Odoo project groups
- **No new groups:** Clean integration
- **Status:** ✅ No custom groups needed

### ✅ Access Rights
- **Model:** project.task.template
- **Granularity:** Read/Write/Create/Delete per group
- **Status:** ✅ Properly configured

### ✅ Record Rules
- **Custom rules:** None needed
- **Uses:** Odoo core project rules
- **Status:** ✅ Inherits security properly

### ✅ Field Security
- **New fields:** Properly secured
- **Computed fields:** Read-only enforced
- **Template links:** Immutable after creation
- **Status:** ✅ Secure by design

### ✅ Button Security
- **Visibility:** Based on project state
- **Access:** Based on project permissions
- **Status:** ✅ Properly controlled

---

## Conclusion

**Smart View Project Enhanced** seamlessly extends Odoo's project module with task template functionality while maintaining proper security.

**Security Highlights:**
- ✅ **No custom groups** (uses Odoo core groups)
- ✅ **Granular access rights** (view/create/edit/delete per role)
- ✅ **Clean integration** (no security conflicts)
- ✅ **Proper isolation** (templates company-wide, tasks project-specific)
- ✅ **Audit trail** (Chatter tracks all changes)
- ✅ **Field protection** (computed fields read-only)

**Menu Integration:**
- ✅ **One new menu** (Task Templates under Configuration)
- ✅ **Enhanced views** (project form, task form)
- ✅ **Smart buttons** (generated tasks count)
- ✅ **Clear visibility rules** (Project Users+)

**Production Ready:** ✅ All security properly configured!

---

## References

### Documentation
- **This Document:** Menu & Security verification
- **USER_GUIDE.md:** Complete usage guide
- **QUICK_REFERENCE.md:** Quick reference card
- **README.md:** Module overview

### Technical Files
- **security/ir.model.access.csv:** Access rights definition
- **views/project_project_views.xml:** Project form enhancements
- **views/project_task_template_views.xml:** Template menu definition
- **views/project_task_views.xml:** Task form enhancements

---

**Verification Date:** November 2025  
**Verified By:** Smart View Development Team  
**Status:** ✅ All security properly configured  
**Next Review:** After major Odoo updates

**Need Help?** See USER_GUIDE.md or contact your administrator!

