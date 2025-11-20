# 📘 Helpdesk Management - User Guide

## Table of Contents
1. [Overview](#overview)
2. [Module Features](#module-features)
3. [User Roles & Permissions](#user-roles--permissions)
4. [Getting Started](#getting-started)
5. [Managing Helpdesk Teams](#managing-helpdesk-teams)
6. [Managing Tickets](#managing-tickets)
7. [Ticket Workflow](#ticket-workflow)
8. [Portal Access for Customers](#portal-access-for-customers)
9. [Use Case Examples](#use-case-examples)
10. [Tips & Best Practices](#tips--best-practices)

---

## Overview

The Helpdesk Management module provides a complete ticketing system for managing customer support requests, internal IT issues, and general help requests. It allows your team to track, prioritize, and resolve issues efficiently.

**Key Benefits:**
- ✅ Centralized ticket management
- ✅ Multi-team support
- ✅ Customer portal access
- ✅ Email integration
- ✅ SLA tracking
- ✅ Kanban/List/Form views
- ✅ Categories, tags, and priorities

---

## Module Features

### 🎫 Ticket Management
- Create, assign, and track support tickets
- Multiple stages (New → In Progress → Closed)
- Priority levels (Low, Medium, High, Urgent)
- Ticket categories and tags
- Rich text descriptions
- File attachments
- Internal notes and public messages

### 👥 Team Management
- Multiple helpdesk teams
- Team-specific stages
- Team members assignment
- Team dashboard with statistics

### 📊 Reporting & Analytics
- Ticket statistics by team
- Resolution time tracking
- Team performance metrics
- Dashboard views

### 🌐 Portal Integration
- Customers can submit tickets via portal
- View ticket status and updates
- Reply to tickets
- Upload attachments

### 📧 Email Integration
- Create tickets from emails
- Email notifications
- Reply via email

---

## User Roles & Permissions

### 1. **Helpdesk User** 👤
Can view and manage assigned tickets within their team.

**Permissions:**
- ✅ View tickets assigned to them
- ✅ Update ticket status
- ✅ Add comments and notes
- ✅ Assign tickets to themselves
- ❌ Cannot delete tickets
- ❌ Cannot manage teams

### 2. **Helpdesk Manager** 👨‍💼
Full access to all helpdesk features.

**Permissions:**
- ✅ All Helpdesk User permissions
- ✅ Create/edit/delete tickets
- ✅ Manage teams, stages, categories
- ✅ Assign tickets to any user
- ✅ View all team statistics
- ✅ Configure helpdesk settings

### 3. **Portal User** 🌐 (Customer)
Limited access through customer portal.

**Permissions:**
- ✅ Create new tickets
- ✅ View their own tickets
- ✅ Reply to tickets
- ✅ Upload attachments
- ❌ Cannot see other customers' tickets
- ❌ Cannot see internal notes

---

## Getting Started

### Step 1: Configure Helpdesk Teams

1. **Navigate to:** Helpdesk → Configuration → Teams
2. **Click:** Create
3. **Fill in:**
   - **Team Name:** (e.g., "Technical Support", "Customer Service")
   - **Team Members:** Add users who will handle tickets
   - **Email Alias:** (optional) tickets@yourcompany.com
4. **Save**

### Step 2: Set Up Stages

Stages define the workflow of tickets (e.g., New → In Progress → Resolved → Closed).

1. **Navigate to:** Helpdesk → Configuration → Stages
2. **Review default stages** or create custom ones
3. **Configure per stage:**
   - **Name:** Stage name
   - **Closed:** Check if this stage means ticket is resolved
   - **Sequence:** Order in kanban view

### Step 3: Configure Categories & Tags

**Categories:** Group tickets by type (e.g., Bug, Feature Request, Question)
1. **Navigate to:** Helpdesk → Configuration → Categories
2. **Create categories** relevant to your business

**Tags:** Add flexible labels (e.g., Urgent, VIP Customer, Hardware Issue)
1. **Navigate to:** Helpdesk → Configuration → Tags
2. **Create tags** for quick filtering

---

## Managing Helpdesk Teams

### Create a New Team

**Example: IT Support Team**

```
Team Name: IT Support
Description: Internal IT infrastructure and software issues
Team Members:
  - John Smith (IT Manager)
  - Sarah Johnson (IT Technician)
  - Mike Davis (IT Technician)
Email: itsupport@company.com
```

### Team Dashboard

Access the team dashboard to view:
- **Open Tickets:** Current tickets needing attention
- **My Tickets:** Tickets assigned to you
- **Team Statistics:** Resolution rates, average time
- **Stage Distribution:** Tickets per stage

**Navigate to:** Helpdesk → Dashboard

---

## Managing Tickets

### Create a New Ticket

1. **Navigate to:** Helpdesk → Tickets → Create
2. **Fill in the form:**

   | Field | Description | Example |
   |-------|-------------|---------|
   | **Name** | Brief ticket title | "Email not working on iPhone" |
   | **Team** | Assign to team | Technical Support |
   | **Customer** | Related contact/company | John Doe |
   | **Assigned To** | User responsible | Sarah Johnson |
   | **Priority** | Urgency level | High |
   | **Category** | Ticket type | Email Issue |
   | **Tags** | Additional labels | Mobile, iOS |
   | **Stage** | Current status | New |
   | **Description** | Detailed problem description | User unable to receive emails on iPhone 12. Error: "Cannot connect to server" |

3. **Save**

### Ticket Views

#### 📋 **List View**
- See all tickets in a table format
- Quick filtering and sorting
- Bulk actions

**Access:** Helpdesk → Tickets (List view icon)

#### 🗂️ **Kanban View**
- Visual board organized by stages
- Drag-and-drop to change stages
- Quick status overview

**Access:** Helpdesk → Tickets (Kanban view icon)

#### 📄 **Form View**
- Detailed ticket information
- Full editing capabilities
- Chatter for communication

**Access:** Click any ticket

### Assign Tickets

**Method 1: From Ticket Form**
1. Open ticket
2. Click "Assigned To" field
3. Select user
4. Save

**Method 2: Quick Assign (Self)**
1. Open ticket
2. Click "Assign to me" button (if available)

**Method 3: From List View**
1. Select ticket(s)
2. Click "Action" → "Assign"
3. Choose user

### Update Ticket Status

**Drag & Drop (Kanban):**
- Simply drag ticket card to new stage column

**Manual Update (Form):**
1. Open ticket
2. Change "Stage" field
3. Save

### Add Comments & Notes

**Public Message (Customer can see):**
1. Open ticket
2. Scroll to "Chatter" section
3. Click "Send message"
4. Type message
5. Click "Send"

**Internal Note (Private):**
1. Open ticket
2. Click "Log note" tab
3. Type internal note
4. Click "Log"

### Attach Files

1. Open ticket
2. Scroll to "Chatter" section
3. Click attachment icon 📎
4. Upload file
5. File appears in message

### Mark Ticket as Duplicate

If you find duplicate tickets:
1. Open duplicate ticket
2. Click "Mark as duplicate" button
3. Select the original ticket
4. Confirm

---

## Ticket Workflow

### Standard Workflow Example

```
New Ticket Created
    ↓
Assigned to Team Member
    ↓
In Progress (Working on solution)
    ↓
Waiting (Customer feedback needed)
    ↓
Resolved (Solution provided)
    ↓
Closed (Customer confirms)
```

### Stage Transitions

| From Stage | Action Required | To Stage |
|------------|----------------|----------|
| New | Assign to team member | Assigned |
| Assigned | Start working | In Progress |
| In Progress | Request customer info | Waiting |
| Waiting | Customer replies | In Progress |
| In Progress | Solution found | Resolved |
| Resolved | Customer confirms | Closed |

---

## Portal Access for Customers

Customers with portal access can submit and track their own tickets.

### For Portal Users (Customers)

#### Submit a Ticket
1. **Login to Portal:** https://yourcompany.odoo.com
2. **Navigate to:** My Account → Helpdesk Tickets
3. **Click:** Create Ticket
4. **Fill in:**
   - Subject
   - Description
   - Attach files (if needed)
5. **Submit**

#### View Ticket Status
1. **Login to Portal**
2. **Go to:** My Account → Helpdesk Tickets
3. **Click ticket** to view details and progress

#### Reply to Ticket
1. Open your ticket
2. Scroll to messages
3. Type reply
4. Send

### For Helpdesk Staff

Enable portal access for customers:
1. **Navigate to:** Contacts
2. **Open customer contact**
3. **Action** → **Grant portal access**
4. Customer receives email with login credentials

---

## Use Case Examples

### Use Case 1: IT Support Department

**Scenario:** Managing internal IT issues for 100 employees

**Setup:**
- **Team:** IT Support
- **Members:** 3 IT technicians
- **Categories:**
  - Hardware Issues
  - Software Issues
  - Network Problems
  - Access Requests
- **Stages:**
  - New
  - In Progress
  - Waiting for Parts
  - Resolved
  - Closed

**Example Ticket Flow:**

```
📧 Employee emails: "My laptop won't connect to WiFi"
    ↓
🎫 Ticket auto-created: "WiFi Connection Issue - Laptop #1234"
    Team: IT Support
    Category: Network Problems
    Priority: Medium
    ↓
👤 Assigned to: Mike (IT Technician)
    ↓
📝 Mike adds note: "Checked network settings, driver update needed"
    Stage: In Progress
    ↓
✅ Mike updates: "Driver updated, tested successfully"
    Stage: Resolved
    ↓
📨 Employee confirms: "Working perfectly, thanks!"
    Stage: Closed
```

**Metrics Tracked:**
- Average resolution time: 2 hours
- Tickets per category
- Most common issues

---

### Use Case 2: Customer Service for E-commerce

**Scenario:** Online store with customer inquiries

**Setup:**
- **Team:** Customer Service
- **Members:** 5 support agents
- **Categories:**
  - Order Issues
  - Returns & Refunds
  - Product Questions
  - Shipping Delays
  - Account Issues
- **Tags:**
  - VIP Customer
  - Urgent
  - Bug
  - Feature Request

**Example Ticket Flow:**

```
🌐 Customer submits via portal: "Order #5678 not received"
    ↓
🎫 Ticket created: "Missing Order #5678"
    Team: Customer Service
    Category: Shipping Delays
    Priority: High
    Customer: Jane Smith
    ↓
👤 Auto-assigned to: Sarah (next available agent)
    ↓
🔍 Sarah checks: "Order shipped 5 days ago, tracking shows delivered"
    Stage: In Progress
    ↓
📧 Sarah replies (public): "According to tracking, order delivered to mailroom. Can you check there?"
    ↓
📨 Customer replies: "Found it in mailroom! Thank you!"
    Stage: Resolved
    ↓
⏰ Auto-closed after 24 hours (no response)
    Stage: Closed
```

**SLA Targets:**
- First response: < 2 hours
- Resolution: < 24 hours
- Customer satisfaction: > 90%

---

### Use Case 3: Property Management Company

**Scenario:** Handling maintenance requests from tenants

**Setup:**
- **Teams:**
  - Plumbing Team
  - Electrical Team
  - General Maintenance
  - Emergency Response
- **Categories:**
  - Plumbing
  - Electrical
  - HVAC
  - Appliances
  - Structural
  - Emergency
- **Priorities:**
  - Urgent (Water leak, no power)
  - High (Broken appliance)
  - Medium (Minor repair)
  - Low (Cosmetic issue)

**Example Emergency Ticket:**

```
🚨 Tenant calls: "Water leak in apartment 203!"
    ↓
🎫 Staff creates ticket: "EMERGENCY: Water Leak - Apt 203"
    Team: Plumbing Team
    Category: Plumbing
    Priority: Urgent
    Customer: Apartment 203
    ↓
📞 Plumber called immediately
    Assigned to: John (On-call plumber)
    Stage: In Progress
    ↓
🔧 John arrives on-site within 30 minutes
    Note: "Burst pipe under sink, shutting off water"
    ↓
✅ Repair completed
    Note: "Pipe replaced, tested for leaks, cleaned up water"
    Stage: Resolved
    ↓
📝 Tenant signs off
    Stage: Closed
```

---

### Use Case 4: Software Company - Bug Tracking

**Scenario:** Managing bug reports and feature requests

**Setup:**
- **Teams:**
  - Frontend Team
  - Backend Team
  - Mobile App Team
  - DevOps Team
- **Categories:**
  - Bug
  - Feature Request
  - Enhancement
  - Documentation
  - Security Issue
- **Tags:**
  - Critical
  - Easy Fix
  - Needs Investigation
  - Won't Fix
  - Duplicate

**Example Bug Report Flow:**

```
🐛 Customer reports: "App crashes when uploading large images"
    ↓
🎫 Support creates ticket: "Bug: App crash on large image upload"
    Team: Mobile App Team
    Category: Bug
    Priority: High
    Tags: Critical, iOS
    ↓
👨‍💻 Assigned to: Lead Developer
    ↓
🔍 Developer investigates
    Internal Note: "Memory leak in image compression function"
    Stage: In Progress
    ↓
💻 Fix developed
    Internal Note: "Added memory management, updated to v2.1.3"
    ↓
✅ Fix tested and deployed
    Public Message: "Thank you for reporting! Fixed in version 2.1.3"
    Stage: Resolved
    ↓
📨 Customer confirms: "Working great now!"
    Stage: Closed
```

**Integration:**
- Link tickets to development tasks
- Track bug fix releases
- Monitor customer-reported issues

---

## Tips & Best Practices

### 🎯 For Helpdesk Agents

1. **Respond Quickly**
   - Acknowledge tickets within 1 hour
   - Set customer expectations on resolution time

2. **Use Clear Communication**
   - Write clear, concise updates
   - Avoid technical jargon with non-technical users
   - Always be polite and professional

3. **Document Solutions**
   - Add internal notes on solutions
   - Build knowledge base over time
   - Share successful solutions with team

4. **Prioritize Effectively**
   - Handle urgent tickets first
   - Group similar tickets for efficiency
   - Don't let low-priority tickets languish

5. **Keep Tickets Updated**
   - Update stage as you progress
   - Add notes on actions taken
   - Inform customers of delays

### 📊 For Helpdesk Managers

1. **Monitor Team Performance**
   - Review dashboard daily
   - Identify bottlenecks
   - Balance workload among team members

2. **Optimize Workflow**
   - Adjust stages based on actual workflow
   - Create categories that match ticket types
   - Use tags for special cases

3. **Set SLA Targets**
   - Define response time goals
   - Set resolution time expectations
   - Monitor compliance

4. **Regular Training**
   - Train team on common issues
   - Share best practices
   - Review difficult cases as learning opportunities

5. **Customer Satisfaction**
   - Follow up after resolution
   - Collect feedback
   - Address recurring issues at root cause

### 🔧 System Configuration Tips

1. **Email Integration**
   - Set up dedicated email addresses per team
   - Configure automatic ticket creation from emails
   - Enable email notifications for updates

2. **Automation Rules**
   - Auto-assign tickets based on category
   - Send reminders for pending tickets
   - Auto-close resolved tickets after X days

3. **Custom Fields**
   - Add fields specific to your business
   - Examples: Device Serial Number, Order Number, Location

4. **Portal Configuration**
   - Customize portal look and feel
   - Add help documentation
   - Enable file uploads

---

## Quick Reference Commands

### Keyboard Shortcuts (Odoo)
- `Alt + C`: Create new record
- `Alt + S`: Save
- `Alt + X`: Discard
- `Alt + K`: Kanban view
- `Alt + L`: List view

### Common Filters

**My Tickets:**
- Filter: "Assigned to me"

**Open Tickets:**
- Filter: Stage ≠ Closed

**High Priority:**
- Filter: Priority = High OR Urgent

**Team Tickets:**
- Group by: Team

**Overdue Tickets:**
- Filter: Deadline < Today AND Stage ≠ Closed

---

## Troubleshooting

### "I can't see any tickets"
✅ Check your user permissions (need Helpdesk User role)
✅ Verify tickets are assigned to your team
✅ Clear filters (may be hiding tickets)

### "Customer can't access portal"
✅ Ensure customer contact has portal access enabled
✅ Check email address is correct
✅ Resend portal invitation if needed

### "Email integration not working"
✅ Verify email alias configuration
✅ Check incoming mail server settings
✅ Test email forwarding rules

### "Tickets not appearing in kanban"
✅ Check stage configuration for team
✅ Verify tickets have stages assigned
✅ Refresh browser

---

## Support & Documentation

📚 **Official Documentation:** [OCA Helpdesk Management](https://github.com/OCA/helpdesk)

💬 **Community Forum:** Odoo Community Forums

🐛 **Report Issues:** Submit ticket to IT Support team

📧 **Contact:** helpdesk@yourcompany.com

---

**Last Updated:** November 2025
**Module Version:** 19.0
**Status:** Production Ready ✅

