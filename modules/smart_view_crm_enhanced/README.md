# Smart View - CRM Enhanced

## Overview

Comprehensive CRM enhancements for Smart View including custom fields, pipeline stages, and client approval workflow.

## Version

- **Version:** 19.0.1.0.0
- **Odoo Version:** 19.0 Community
- **License:** LGPL-3

## Features

### REQ-00037: Project Location Field ✅

**Custom field in leads/opportunities:**
- 📍 **Project Location** field added to CRM
- Visible in forms, lists, and kanban
- Tracking enabled for audit trail
- Appears in kanban tooltips
- Searchable and filterable

### REQ-00038: Enhanced Pipeline Stages ✅

**Three new stages added:**

1. **🏗️ Site Visit**
   - For scheduling and conducting site visits
   - Special marker field: `is_site_visit_stage`
   - Clear requirements displayed

2. **📋 Technical Description**
   - For preparing technical proposals
   - Special marker field: `is_technical_stage`
   - Technical details tracking

3. **✓ Client Approval**
   - Waiting for client decision
   - Special marker field: `is_approval_stage`
   - Approval workflow activated

**Client Approval Workflow:**
- ✅ **Approve Button** - Mark as client approved
- ❌ **Reject Button** - Opens rejection wizard
- 📝 **Rejection Tracking** - Category + reason + date
- 🔒 **SO Prevention** - Cannot create quotation if rejected
- 🔒 **Approval Required** - Must approve before creating SO
- 📧 **Team Notifications** - Alert sales team on rejection
- 📊 **Rejection Categories**: Price, Timeline, Scope, Competitor, Budget, Postponed, Other

## Installation

### Prerequisites
- Odoo 19 Community Edition
- `crm` module (installed)
- `sale_crm` module (installed)

### Install Steps

1. Copy module to Odoo addons directory
2. Update apps list: `Settings > Apps > Update Apps List`
3. Search for "Smart View - CRM Enhanced"
4. Click **Install**

**Note:** New stages will be created automatically upon installation.

## Configuration

### 1. View New Pipeline Stages

After installation, new stages appear in CRM pipeline:

1. Go to `CRM > Configuration > Stages`
2. You'll see:
   - **Site Visit** (sequence 15)
   - **Technical Description** (sequence 20)
   - **Client Approval** (sequence 25)

### 2. Adjust Stage Sequences

Customize stage order if needed:

1. Go to `CRM > Configuration > Stages`
2. Drag stages to reorder
3. Or edit sequence numbers manually

**Recommended Pipeline:**
```
New → Qualified → Proposition → Site Visit (15) 
→ Technical Description (20) → Client Approval (25) → Won
```

### 3. Configure Stage Settings

Mark existing stages for special handling:

1. Open any stage
2. Go to "Smart View Settings" section
3. Check appropriate boxes:
   - ☑️ Is Site Visit Stage
   - ☑️ Is Technical Stage
   - ☑️ Is Approval Stage

## Usage

### Adding Project Location (REQ-00037)

**In Opportunity Form:**

1. Open any opportunity (not lead)
2. Find **Project Location** field (after Customer)
3. Enter location:
   ```
   Examples:
   - "Cairo - New Capital, Building A"
   - "Alexandria - Sidi Gaber, Floor 3"
   - "Giza - 6th October, Villa 45"
   ```
4. Save

**Field appears in:**
- ✓ Opportunity form view
- ✓ List view (optional column)
- ✓ Kanban cards (with map marker icon)
- ✓ Search filters
- ✓ Activity history (tracked)

### Using Site Visit Stage

**Moving to Site Visit:**

1. Open opportunity
2. Drag to **Site Visit** stage (or click stage)
3. Schedule activities:
   - Plan site visit appointment
   - Assign team member
   - Set reminder

### Using Technical Description Stage

**Moving to Technical Stage:**

1. Complete site visit
2. Move to **Technical Description** stage
3. Prepare technical proposal
4. Attach technical documents

### Using Client Approval Workflow (REQ-00038)

#### **Moving to Client Approval:**

1. Complete technical description
2. Move opportunity to **Client Approval** stage
3. Status automatically set to "Pending Approval"
4. Approval buttons appear in header

#### **Client Approves:**

1. Open opportunity in **Client Approval** stage
2. Click **"✓ Client Approved"** button (green)
3. Status changes to "Approved"
4. Green ribbon appears: "Client Approved"
5. Can now create quotation normally

#### **Client Rejects:**

1. Open opportunity in **Client Approval** stage
2. Click **"✗ Client Rejected"** button (red)
3. **Rejection Wizard opens:**

   **Select Category:**
   - ◉ Price Too High
   - ◉ Timeline Issues
   - ◉ Scope Mismatch
   - ◉ Chose Competitor
   - ◉ Budget Constraints
   - ◉ Project Postponed
   - ◉ Other Reason

   **Enter Reason:**
   ```
   Example: "Client found our timeline too long. 
   They need completion in 3 months instead of 6."
   ```

   **Options:**
   - ☑️ Notify Sales Team (checked by default)

4. Click **"Confirm Rejection"**

**After Rejection:**
- Status changes to "Rejected"
- Red ribbon appears: "Client Rejected"
- Rejection reason logged
- Rejection date recorded
- Message posted to chatter
- Activity created for salesperson (if notify enabled)
- **Cannot create quotation** (blocked with error message)

### Viewing Approval Status

**In List View:**

Add "Client Approval Status" column to see:
- 🟡 Pending Approval
- 🟢 Client Approved
- 🔴 Client Rejected

**In Kanban View:**

Badges appear on cards:
- 🟢 **Approved** (green badge)
- 🔴 **Rejected** (red badge)
- 🟡 **Pending** (yellow badge)

**Filtering:**

Use search filters:
- `Client Approved` - Show only approved
- `Client Rejected` - Show only rejected
- `Pending Approval` - Show only pending
- `In Approval Stage` - Show all in approval stage

**Group By:**

Group opportunities by:
- `Approval Status` - Group by approval state

### Preventing Quotation Creation

**Automatic Protection:**

System prevents SO/quotation creation when:

1. **In approval stage without approval:**
   ```
   ❌ Error: "Cannot create quotation. 
   Client approval is required.
   Current Status: Pending Approval"
   ```

2. **Opportunity is rejected:**
   ```
   ❌ Error: "Cannot create quotation. 
   This opportunity was rejected by the client.
   Rejection Reason: [Price Too High]
   Client found pricing 15% above budget."
   ```

**User must:**
- Get client approval first, OR
- Move out of approval stage, OR
- Handle rejection (revise proposal)

## Workflow Example

### Complete Sales Flow with New Stages:

```
1. Lead Created
   ↓
2. Qualify Lead → Convert to Opportunity
   ↓ (Add Project Location: "Cairo - New Capital")
3. Create Proposition
   ↓
4. Site Visit Stage
   - Schedule visit
   - Conduct site assessment
   - Take measurements/photos
   ↓
5. Technical Description Stage
   - Prepare technical proposal
   - Calculate costs
   - Draft timeline
   ↓
6. Client Approval Stage
   - Send proposal to client
   - Status: Pending Approval
   - Wait for decision
   
   → Client Approves ✓
     - Click "Client Approved" button
     - Status: Approved
     - Create Quotation → Won!
   
   → Client Rejects ✗
     - Click "Client Rejected" button
     - Select category: "Timeline Issues"
     - Enter reason
     - Status: Rejected
     - Revise proposal or mark as Lost
```

## Technical Details

### Models Extended

#### **crm.lead**

**New Fields:**
- `project_location` (Char) - Project location
- `client_approval_state` (Selection) - Approval status
- `rejection_reason` (Text) - Rejection details
- `rejection_date` (Datetime) - When rejected
- `is_in_approval_stage` (Boolean, computed) - In approval stage flag

**New Methods:**
- `action_client_approve()` - Approve opportunity
- `action_client_reject()` - Reject opportunity (opens wizard)
- `action_new_quotation()` - Override to check approval
- `_compute_is_in_approval_stage()` - Compute approval stage flag

#### **crm.stage**

**New Fields:**
- `is_approval_stage` (Boolean) - Mark as approval stage
- `is_site_visit_stage` (Boolean) - Mark as site visit stage
- `is_technical_stage` (Boolean) - Mark as technical stage

### Wizard Model

#### **crm.lead.rejection.wizard**

**Fields:**
- `lead_id` (Many2one) - Related opportunity
- `rejection_reason` (Text, required) - Reason details
- `rejection_category` (Selection, required) - Category
- `notify_team` (Boolean) - Send notifications

**Methods:**
- `action_confirm_rejection()` - Process rejection
- `action_cancel()` - Cancel wizard
- `_check_rejection_reason()` - Validate reason length

### Security

**Access Rights:**
- CRM User: Full access to rejection wizard
- CRM Manager: Full access to rejection wizard

### Data Records

**Created Stages:**
- `stage_site_visit` - Site Visit stage
- `stage_technical_description` - Technical stage  
- `stage_client_approval` - Approval stage

## Views Enhanced

### Form View
- ✅ Project location field
- ✅ Approval/rejection buttons in header
- ✅ Approval status ribbons
- ✅ Client approval section (when in approval stage)
- ✅ Rejection details display

### Tree View
- ✅ Project location column (optional)
- ✅ Approval status badge column (optional)

### Kanban View
- ✅ Project location with map icon
- ✅ Approval status badges
- ✅ Color-coded indicators

### Search View
- ✅ Search by project location
- ✅ Filter by approval status
- ✅ Filter by approval stage
- ✅ Group by approval status

## Rejection Categories

System tracks 7 categories for analysis:

| Category | Usage | Description |
|----------|-------|-------------|
| 💰 Price | Common | Client finds price too high |
| ⏰ Timeline | Common | Timeline doesn't match needs |
| 📋 Scope | Medium | Scope mismatch or incomplete |
| 🏢 Competitor | Common | Chose another provider |
| 💵 Budget | Common | Budget constraints |
| ⏸️ Postponed | Medium | Project delayed/postponed |
| 📝 Other | Fallback | Other reasons |

## Reporting

### Useful Reports

**Rejection Analysis:**
1. Go to `CRM > Reporting`
2. Filter by "Client Rejected"
3. Group by "Rejection Category"
4. Analyze common reasons

**Approval Funnel:**
1. Pipeline view
2. Check conversion rate at approval stage
3. Track time in approval stage

**Location Analysis:**
1. Group opportunities by Project Location
2. See which locations have highest success rate

## Best Practices

### Project Location

1. **Be Specific:**
   - ❌ Bad: "Cairo"
   - ✅ Good: "Cairo - Nasr City, Building 12"

2. **Use Consistent Format:**
   ```
   City - District, Building/Unit
   ```

3. **Update When Changes:**
   - Field is tracked, so updates are logged

### Site Visit Stage

1. **Always Schedule Activity:**
   - Set date/time for visit
   - Assign team member
   - Add location from project_location

2. **Document Results:**
   - Add notes to chatter
   - Upload photos/documents
   - Update opportunity details

### Technical Description

1. **Attach Documents:**
   - Technical specifications
   - Drawings/plans
   - Cost breakdown

2. **Use Internal Notes:**
   - Record assumptions
   - Note client requirements
   - Document constraints

### Client Approval

1. **Set Expectations:**
   - Tell client decision needed
   - Provide deadline
   - Follow up regularly

2. **Handle Rejections Professionally:**
   - Always get detailed reason
   - Select correct category
   - Notify team immediately
   - Don't delete - keep for analysis

3. **Track Time:**
   - Monitor how long approval takes
   - Set activities for follow-up
   - Escalate if delayed

## Troubleshooting

### Issue: Can't Create Quotation

**Error:** "Client approval is required"

**Solution:** 
1. Verify opportunity is in Client Approval stage
2. Click "✓ Client Approved" button
3. Then create quotation

### Issue: Can't See Approval Buttons

**Cause:** Not in Client Approval stage

**Solution:**
1. Move opportunity to "Client Approval" stage
2. Buttons will appear automatically

### Issue: Rejection Wizard Shows Error

**Error:** "Please provide a more detailed rejection reason"

**Solution:** Enter at least 10 characters in reason field

### Issue: New Stages Not Visible

**Solution:**
1. Go to `CRM > Configuration > Stages`
2. Check if stages exist
3. If not, upgrade module: `-u smart_view_crm_enhanced`
4. Check stage visibility settings

### Issue: Project Location Not Visible in Lead

**Cause:** Field only visible for opportunities, not leads

**Solution:**
1. Convert lead to opportunity first
2. Then project_location field appears

## Integration

### With smart_view_sale_enhanced

When creating quotation from approved opportunity:
- Project location can be referenced
- Approval status verified
- Smooth handoff to sales

### With smart_view_project_sale (future)

Project location will be:
- Copied to project
- Used for resource planning
- Available in project details

## Customization

### Add Custom Rejection Categories

Edit `wizard/rejection_reason_wizard.py`:

```python
rejection_category = fields.Selection([
    ('price', 'Price Too High'),
    ('timeline', 'Timeline Issues'),
    # Add your custom category:
    ('location', 'Location Issues'),
], ...)
```

### Add Custom Approval Stage Logic

Override in `models/crm_lead.py`:

```python
def write(self, vals):
    res = super(CrmLead, self).write(vals)
    
    # Your custom logic when entering approval stage
    if 'stage_id' in vals:
        for lead in self:
            if lead.is_in_approval_stage:
                # Custom action here
                pass
    
    return res
```

## Roadmap

### Planned Enhancements
- [ ] Approval expiration dates
- [ ] Multiple approvers support
- [ ] Approval reminder emails
- [ ] Rejection reason templates
- [ ] Advanced approval routing
- [ ] Approval analytics dashboard

## Credits

- **Development Team:** Smart View Development Team
- **Based on:** Odoo 19 Community CRM
- **License:** LGPL-3

## Changelog

### Version 19.0.1.0.0 (2025-11-19)
- Initial release
- REQ-00037: Project location field implemented
- REQ-00038: Custom pipeline stages implemented
- Client approval workflow complete
- Rejection tracking with categories
- Enhanced views (form, tree, kanban)
- Complete documentation
- Ready for production

---

**Status:** ✅ Complete and Ready for Use

