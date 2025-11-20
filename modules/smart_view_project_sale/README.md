# Smart View - Project Sale Integration

## Overview

Bridge between Sales Orders and Projects with CRM approval validation. Creates projects from sales orders only after client approval, with template support and enhanced field mapping.

## Version

- **Version:** 19.0.1.0.0
- **Odoo Version:** 19.0 Community
- **License:** LGPL-3

## Features

### REQ-00042: Project Creation from Sales Orders ✅

**Complete Implementation of Tasks 45-48:**

#### Task 45: Create Project Button ✅
- **Manual "Create Project" button** in Sales Order form
- Visible only when conditions are met:
  - SO is confirmed (sale/done state)
  - No existing project
  - Client approval validated (if opportunity linked)

#### Task 46: Client Approval Validation ✅
- **Automatic approval checking** from linked CRM opportunity
- **Blocks project creation** if:
  - Opportunity is not approved
  - Opportunity is rejected
  - Approval is still pending
- **Clear error messages** explaining why creation is blocked

#### Task 47: Project Template System ✅
- **Create projects from templates**
- Template selection field in SO
- Copies entire project structure:
  - Stages
  - Tasks  
  - Settings
  - Custom configurations
- **Template management interface**

#### Task 48: Enhanced SO-Project Linking ✅
- **Bi-directional linking**:
  - SO → Project
  - Project → SO
- **Automatic field mapping**:
  - Project Location (from CRM opportunity)
  - Customer
  - Salesperson
  - Company
  - Start date
  - Notes with SO reference
- **Smart buttons** for easy navigation

---

## Installation

### Prerequisites
- Odoo 19 Community Edition
- Required modules:
  - `sale_management` ✅
  - `project` ✅
  - `sale_project` ✅ (Odoo standard)
  - `smart_view_crm_enhanced` ✅ (for approval validation)

### Install Steps

1. Ensure `smart_view_crm_enhanced` is installed first
2. Copy module to Odoo addons directory
3. Update apps list
4. Search for "Smart View - Project Sale Integration"
5. Click **Install**

**Dependencies:** Automatically installs required dependencies.

---

## Configuration

### 1. Create Project Templates (Optional but Recommended)

**Create reusable project structures:**

1. Go to `Project > Configuration > Project Templates`
2. Click **Create**
3. Fill template details:
   - **Name**: e.g., "Standard Installation Project"
   - **Template Name**: Short identifier
   - **Check "Is Template"** ☑️
4. Add stages (or wait for `smart_view_project_enhanced`)
5. Add tasks (optional)
6. Save

**Recommended Templates:**
- Standard Installation Project
- Complex Installation Project  
- Service-Only Project
- Quick Setup Project

### 2. Configure Sales Order Workflow

No additional configuration needed! The module works automatically with:
- Standard Sales flow
- CRM opportunity linking
- Client approval workflow (from `smart_view_crm_enhanced`)

---

## Usage

### Complete Workflow: CRM → SO → Project

#### Step 1: CRM Opportunity with Approval

```
1. Create Opportunity in CRM
   ↓
2. Add Project Location: "Cairo - New Capital"
   ↓
3. Move through pipeline:
   - Site Visit
   - Technical Description
   - Client Approval ✅
   ↓
4. Click "Client Approved" button
```

#### Step 2: Create Sales Order

```
1. From approved opportunity, create quotation
   ↓
2. Add products/services
   ↓
3. Confirm quotation → becomes Sales Order
```

#### Step 3: Create Project

```
1. Open confirmed Sales Order
   ↓
2. (Optional) Select "Project Template"
   ↓
3. Click "Create Project" button (green)
   ↓
4. Project created automatically! ✅
```

**Project includes:**
- ✅ Name: "Project - SO001"
- ✅ Customer: From SO
- ✅ Salesperson: From SO
- ✅ Project Location: From CRM opportunity
- ✅ Start Date: SO confirmation date
- ✅ Link back to SO
- ✅ If template used: All stages & tasks copied

---

## Features in Detail

### 1. Manual Project Creation Button (Task 45)

**Location:** Sales Order form, header area

**Visibility Conditions:**
- ✅ SO is in "Sale" or "Done" state
- ✅ No existing project linked
- ✅ If opportunity linked: Must be approved

**Button Appearance:**
- **Green "Create Project"** - When conditions met
- **Gray "View Project"** - After project created
- **Smart Button** - Shows "1 Project" after creation

### 2. Approval Validation (Task 46)

**Automatic Checks:**

**Scenario 1: SO Not Confirmed**
```
❌ Error: "Cannot create project. 
Sales order must be confirmed first."
```

**Scenario 2: Opportunity Not Approved**
```
❌ Error: "Cannot create project. 
Client approval is pending.

The linked opportunity must be approved 
by the client before creating a project.
Please go to the opportunity and click 
'Client Approved' button."
```

**Scenario 3: Opportunity Rejected**
```
❌ Error: "Cannot create project. 
Client has rejected the opportunity.

Rejection Reason: [Category]
Detailed reason text...

Please revise the proposal or create 
a new opportunity."
```

**Scenario 4: All Checks Pass** ✅
```
✓ Project created successfully!
→ Opens project form automatically
```

### 3. Project Template System (Task 47)

**How Templates Work:**

1. **Select Template** (optional):
   - In SO form, go to "Project" tab
   - Field: "Project Template"
   - Choose from list of templates

2. **Click "Create Project"**:
   - If template selected: **Copies everything**
     - All stages
     - All tasks
     - Task assignments
     - Stage settings
     - Custom fields
   - If no template: **Creates empty project**
     - Just basic structure
     - Can add stages/tasks manually

3. **Customization After Creation**:
   - Template is copied, not linked
   - Customize freely
   - Changes don't affect template

**Template Benefits:**
- ✅ Consistency across projects
- ✅ Time savings (no manual setup)
- ✅ Best practices encoded
- ✅ Easy onboarding for new users

### 4. Enhanced Field Mapping (Task 48)

**Automatic Field Copying:**

| Source | Field | Target | Field |
|--------|-------|--------|-------|
| SO | name | Project | name (prefixed) |
| SO | partner_id | Project | partner_id |
| SO | user_id | Project | user_id |
| SO | company_id | Project | company_id |
| SO | date_order | Project | date_start |
| SO | id | Project | sale_order_id |
| **CRM Opportunity** | **project_location** | **Project** | **project_location** |
| CRM Opportunity | name | Project | notes (reference) |

**Special Handling:**
- **Project Location**: Only copied if opportunity has it
- **Notes**: Includes SO reference + opportunity info
- **Name**: Formatted as "Project - SO001"

---

## User Interface Enhancements

### Sales Order Form

**Header Buttons:**
- **"Create Project"** (primary, green) - When can create
- **"View Project"** (secondary) - After created

**Ribbon Badge:**
- **Green "Project Created"** ribbon when linked

**Smart Button:**
- **"1 Project"** with tasks icon
- Click to open project

**Project Tab:**
- Project Template selector (before creation)
- Linked Project display (after creation)
- Project details

**Computed Fields:**
- `can_create_project` - Controls button visibility
- `project_count` - For smart button

### Project Form

**Added Fields:**
- **Sales Order** - Link back to SO (readonly)
- **Project Location** - From CRM opportunity
- **Is Template** - Mark as template
- **Template Name** - Template identifier

**Smart Button:**
- **"Sales Order"** - Click to view linked SO

**Settings Section:**
- Template checkbox
- Template name (if template)

### Search & Filters

**Sales Orders:**
- Filter: "Has Project"
- Filter: "No Project"
- Filter: "Can Create Project"
- Group By: "Project"

**Projects:**
- Filter: "From Sales Order"
- Filter: "Templates"
- Filter: "Active Projects"
- Group By: "Sales Order"
- Group By: "Location"

---

## Technical Details

### Models Extended

#### sale.order

**New Fields:**
- `project_id` (Many2one) - Linked project
- `project_count` (Integer, computed) - Number of projects
- `can_create_project` (Boolean, computed) - Can create flag
- `project_template_id` (Many2one) - Template selection

**New Methods:**
- `action_create_project()` - Main creation method (Tasks 45-48)
- `_validate_project_creation()` - Task 46 validation
- `_create_project_from_so()` - Task 47 implementation
- `_prepare_project_values()` - Task 48 field mapping
- `action_view_project()` - Open linked project
- `_compute_project_count()` - Count projects
- `_compute_can_create_project()` - Check if can create

#### project.project

**New Fields:**
- `sale_order_id` (Many2one) - Link to SO
- `project_location` (Char) - From CRM
- `is_template` (Boolean) - Template marker
- `template_name` (Char) - Template identifier

**Override Methods:**
- `name_get()` - Show [TEMPLATE] prefix
- `_name_search()` - Improve template search

### Computed Field Logic

#### can_create_project

```python
Conditions (ALL must be true):
1. SO state in ['sale', 'done']
2. project_id is False (no existing project)
3. IF opportunity_id:
     opportunity.client_approval_state == 'approved'
   ELSE:
     True (no opportunity, allow)
```

### Validation Logic (Task 46)

```python
def _validate_project_creation(self):
    # Check 1: SO confirmed
    if self.state not in ['sale', 'done']:
        raise UserError("SO must be confirmed")
    
    # Check 2: No existing project
    if self.project_id:
        raise UserError("Project already exists")
    
    # Check 3: CRM approval (if linked)
    if self.opportunity_id:
        state = self.opportunity_id.client_approval_state
        
        if state == 'pending' or not state:
            raise UserError("Approval pending")
        
        if state == 'rejected':
            raise UserError(f"Rejected: {reason}")
        
        # state == 'approved' → OK!
    
    return True
```

### Project Creation Logic (Task 47)

```python
def _create_project_from_so(self):
    # Prepare base values
    values = self._prepare_project_values()
    
    # Template or new?
    if self.project_template_id:
        # Copy from template
        project = self.project_template_id.copy(
            default=values
        )
    else:
        # Create new
        project = self.env['project.project'].create(values)
    
    return project
```

### Field Mapping Logic (Task 48)

```python
def _prepare_project_values(self):
    values = {
        'name': f'Project - {self.name}',
        'partner_id': self.partner_id.id,
        'user_id': self.user_id.id,
        'company_id': self.company_id.id,
        'sale_order_id': self.id,
    }
    
    # Copy project_location from CRM
    if self.opportunity_id and \
       self.opportunity_id.project_location:
        values['project_location'] = \
            self.opportunity_id.project_location
    
    # Add notes
    values['description'] = f"""
    Project created from SO: {self.name}
    Linked Opportunity: {self.opportunity_id.name}
    Project Location: {location}
    """
    
    return values
```

---

## Integration

### With smart_view_crm_enhanced

**Tight Integration:**
- ✅ Reads `client_approval_state` field
- ✅ Validates approval before project creation
- ✅ Copies `project_location` field
- ✅ Shows approval status in error messages
- ✅ Links to opportunity for context

**Required Fields from CRM:**
- `client_approval_state` (Selection)
- `rejection_reason` (Text)
- `project_location` (Char)

### With smart_view_project_enhanced (Future)

**Will integrate with:**
- Project stage templates
- Task templates
- Automatic task generation
- Stage locking

**Preparation:**
- Template system ready
- Field structure compatible
- Copy mechanism supports stages/tasks

### With Standard Odoo

**Uses Standard Modules:**
- `sale_project` - Base SO-Project integration
- `project` - Core project management
- `sale_management` - Sales orders

**Enhances Standard:**
- Adds manual control (vs automatic)
- Adds approval validation
- Adds template support
- Adds field mapping

---

## Use Cases

### Use Case 1: Standard Project Creation

**Scenario:** Create project after client approves

**Steps:**
1. Opportunity reaches "Client Approval" stage
2. Salesperson clicks "Client Approved"
3. Create quotation → confirm → SO
4. In SO, select template (optional)
5. Click "Create Project"
6. Project ready with all details! ✅

**Result:**
- Project created with correct location
- All fields mapped
- Team can start work immediately

### Use Case 2: Blocked by Pending Approval

**Scenario:** Try to create project too early

**Steps:**
1. SO confirmed
2. Opportunity still in "Pending Approval"
3. Click "Create Project"
4. ❌ Error message appears
5. Go to opportunity
6. Click "Client Approved"
7. Return to SO
8. Click "Create Project" again
9. ✅ Success!

**Result:**
- Workflow enforced
- No premature project creation
- Clear guidance to user

### Use Case 3: Using Templates

**Scenario:** Standardize project structure

**Steps:**
1. Create template once:
   - Name: "Standard Installation"
   - Add 5 stages
   - Add common tasks
   - Mark as template
2. In SO, select "Standard Installation" template
3. Click "Create Project"
4. Project created with all stages & tasks! ✅

**Result:**
- Consistent project structure
- Time saved (no manual setup)
- Best practices followed

### Use Case 4: Project Location Tracking

**Scenario:** Track where projects are executed

**Steps:**
1. In CRM opportunity, add location:
   "Cairo - New Capital, Building A"
2. Approve opportunity
3. Create SO
4. Create project
5. Project automatically has location! ✅

**Result:**
- Location tracked from start to finish
- No manual re-entry
- Reports can group by location

---

## Best Practices

### Template Management

1. **Create Core Templates:**
   - Standard projects
   - Complex projects
   - Service-only projects
   - Quick projects

2. **Maintain Templates:**
   - Update when process changes
   - Add new stages/tasks as needed
   - Remove outdated steps

3. **Name Clearly:**
   - Use descriptive names
   - Include project type
   - Mention duration if relevant

### Project Creation

1. **Always Check Approval:**
   - Verify opportunity is approved
   - Don't skip approval steps
   - Use workflow as designed

2. **Select Appropriate Template:**
   - Match project complexity
   - Consider timeline
   - Think about resources needed

3. **Verify Fields:**
   - Check project location copied
   - Verify customer is correct
   - Confirm salesperson assigned

### Workflow

1. **CRM First:**
   - Start with opportunity
   - Add project location early
   - Get approval before quotation

2. **SO Second:**
   - Create from approved opportunity
   - Select template before creation
   - Confirm SO before project

3. **Project Last:**
   - Create only when ready to start
   - Verify all details
   - Brief team on project

---

## Troubleshooting

### Issue: Can't See "Create Project" Button

**Cause:** Conditions not met

**Check:**
1. Is SO confirmed? (not draft/sent)
2. Is there already a project?
3. If opportunity linked, is it approved?

**Solution:**
- Confirm SO first
- Check opportunity approval status
- Verify no duplicate project

### Issue: "Client Approval Pending" Error

**Cause:** Opportunity not approved yet

**Solution:**
1. Go to linked opportunity (click smart button)
2. Verify you're in "Client Approval" stage
3. Click "✓ Client Approved" button
4. Return to SO
5. Try "Create Project" again

### Issue: "Client Rejected" Error

**Cause:** Opportunity was rejected

**Solution:**
1. Review rejection reason
2. Options:
   - Revise proposal
   - Create new opportunity
   - Mark SO as cancelled
3. Don't force project creation

### Issue: Project Location Not Copied

**Cause:** Opportunity doesn't have location

**Solution:**
1. Go to opportunity
2. Add "Project Location" field
3. Create project again (or update manually)

### Issue: Template Not Available

**Cause:** No templates created

**Solution:**
1. Go to Project > Configuration > Project Templates
2. Create at least one template
3. Mark "Is Template" checkbox
4. Save
5. Return to SO and select template

---

## Security

### Access Rights

**Create Project Button:**
- Visible to: Sales Users, Sales Managers
- Execution: Sales Users can create

**Templates:**
- View: All users
- Create/Edit: Project Managers only

**Project Fields:**
- SO Link: Readonly for all
- Location: Editable by Project Managers

---

## Reporting

### Useful Reports

**Projects by Sales Order:**
- Group projects by source SO
- See conversion rate
- Track sales → execution

**Projects by Location:**
- Group by project_location
- Geographic analysis
- Resource planning by location

**Template Usage:**
- See which templates most used
- Evaluate template effectiveness
- Identify process improvements

---

## Roadmap

### Future Enhancements
- [ ] Automatic template suggestion based on SO products
- [ ] Project cost estimation from SO amount
- [ ] Milestone creation from SO delivery dates
- [ ] Resource allocation suggestions
- [ ] Integration with scheduling
- [ ] Project analytics dashboard

---

## Credits

- **Development Team:** Smart View Development Team
- **Based on:** Odoo 19 Community
- **License:** LGPL-3

---

## Changelog

### Version 19.0.1.0.0 (2025-11-19)
- Initial release
- REQ-00042 complete implementation
- Task 45: Create Project button ✅
- Task 46: Approval validation ✅
- Task 47: Template system ✅
- Task 48: Enhanced linking ✅
- Complete documentation
- Ready for production

---

**Status:** ✅ Complete and Ready for Use

