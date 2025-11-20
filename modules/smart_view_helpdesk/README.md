# Smart View - Helpdesk Wrapper

## Overview

This is a **lightweight wrapper module** that integrates the battle-tested **OCA `helpdesk_mgmt`** module into the Smart View ecosystem.

## Why Use OCA's Module?

Instead of building a custom helpdesk from scratch, we leverage the [OCA Helpdesk Management module](https://github.com/OCA/helpdesk) which provides:

✅ **Production-ready** - Used by thousands of companies worldwide  
✅ **Well-maintained** - Active development by the Odoo Community  
✅ **Feature-rich** - Teams, stages, SLA, portal access, and more  
✅ **Secure** - Proper access rights and record rules  
✅ **Extensible** - 20+ companion modules available  

## Requirements Covered

- **REQ-00036**: Helpdesk Activation - ✅ Fully satisfied

## Installation

1. Install `helpdesk_mgmt` (OCA module)
2. Install `smart_view_helpdesk` (this wrapper)

## Features (via helpdesk_mgmt)

- **Ticket Management**: Create, track, and resolve customer support tickets
- **Team Organization**: Assign tickets to different support teams
- **Stage Tracking**: Customizable stages (New, In Progress, Solved, Closed)
- **Priority Levels**: Low, Normal, High, Urgent
- **Portal Access**: Customers can view and create tickets from the portal
- **Email Integration**: Create tickets from incoming emails
- **Categories & Tags**: Organize tickets with categories and tags
- **Activity Tracking**: Full chatter integration for communication history

## Usage

Go to **Helpdesk** from the main menu to:

- View all tickets in Kanban, List, or Form view
- Create new tickets for customers
- Assign tickets to team members
- Track ticket resolution time
- Communicate with customers via the portal

## Maintenance

This wrapper module requires minimal maintenance since all functionality is handled by the OCA `helpdesk_mgmt` module. 

For updates or additional features, check the [OCA Helpdesk repository](https://github.com/OCA/helpdesk) for available add-ons like:

- `helpdesk_mgmt_sla` - Service Level Agreements
- `helpdesk_mgmt_project` - Link tickets to projects
- `helpdesk_mgmt_timesheet` - Track time spent on tickets
- `helpdesk_mgmt_rating` - Customer satisfaction ratings

## License

LGPL-3 (wrapper)  
AGPL-3 (OCA helpdesk_mgmt)
