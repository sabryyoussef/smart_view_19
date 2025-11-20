# 🎫 Helpdesk Management - Quick Reference Card

## 🚀 Quick Start (30 seconds)

1. **Create Team:** Helpdesk → Configuration → Teams → Create
2. **Create Ticket:** Helpdesk → Tickets → Create
3. **Assign:** Set "Assigned To" field
4. **Work:** Update "Stage" as you progress
5. **Close:** Move to "Closed" stage when done

---

## 📍 Navigation

| What | Where |
|------|-------|
| View all tickets | Helpdesk → Tickets |
| My tickets | Helpdesk → Tickets → Filter "My Tickets" |
| Create ticket | Helpdesk → Tickets → Create |
| Team dashboard | Helpdesk → Dashboard |
| Configure teams | Helpdesk → Configuration → Teams |
| Manage stages | Helpdesk → Configuration → Stages |
| Set categories | Helpdesk → Configuration → Categories |
| Create tags | Helpdesk → Configuration → Tags |

---

## 🎯 Common Tasks

### Create Ticket
```
1. Helpdesk → Tickets → Create
2. Fill: Name, Team, Customer, Priority
3. Add Description
4. Save
```

### Assign Ticket to Yourself
```
1. Open ticket
2. Click "Assign to me" button
OR
1. Set "Assigned To" = Your Name
2. Save
```

### Update Ticket Status
```
Kanban View: Drag & drop to new stage
Form View: Change "Stage" field → Save
```

### Reply to Customer
```
1. Open ticket
2. Scroll to Chatter
3. Click "Send message"
4. Type reply
5. Send
```

### Add Internal Note
```
1. Open ticket
2. Click "Log note" tab
3. Type note (customer won't see this)
4. Log
```

---

## 👥 User Roles

| Role | Can Do |
|------|--------|
| **Helpdesk User** | View assigned tickets, update status, add comments |
| **Helpdesk Manager** | Everything + create/delete tickets, manage teams, view all stats |
| **Portal User** | Submit tickets, view own tickets, reply |

---

## 🏷️ Priority Levels

| Priority | When to Use | Response Time |
|----------|-------------|---------------|
| **Urgent** | System down, critical bug, emergency | < 1 hour |
| **High** | Major issue affecting work | < 4 hours |
| **Medium** | Standard request | < 24 hours |
| **Low** | Minor issue, enhancement | < 3 days |

---

## 📊 Ticket Workflow

```
New → Assigned → In Progress → Waiting → Resolved → Closed
```

**Stages explained:**
- **New:** Just created, needs assignment
- **Assigned:** Someone is responsible
- **In Progress:** Actively being worked on
- **Waiting:** Need customer feedback/info
- **Resolved:** Solution provided
- **Closed:** Confirmed fixed, ticket complete

---

## 🔍 Quick Filters

| Filter | How |
|--------|-----|
| My tickets | Top bar → "My Tickets" |
| Open tickets | Stage ≠ Closed |
| High priority | Priority = High or Urgent |
| Unassigned | Assigned To = Empty |
| Today's tickets | Created = Today |
| By team | Group By → Team |
| By customer | Group By → Customer |

---

## 💡 Pro Tips

### For Agents ⚡
- ✅ **First response within 1 hour** = Happy customers
- ✅ **Use tags** for quick categorization
- ✅ **Add notes** on solutions for future reference
- ✅ **Link related tickets** using mentions
- ✅ **Set yourself as follower** to get notifications

### For Managers 📊
- ✅ **Check dashboard daily** for bottlenecks
- ✅ **Balance workload** among team members
- ✅ **Review closed tickets** for patterns
- ✅ **Set team SLA goals** and monitor
- ✅ **Export reports** for analysis

---

## 🌐 Customer Portal

### Enable Portal for Customer
```
1. Contacts → Open customer
2. Action → Grant Portal Access
3. Customer receives email with login
```

### Customer Can:
- ✅ Submit new tickets
- ✅ View their tickets
- ✅ Reply and add attachments
- ✅ Track status
- ❌ See internal notes
- ❌ See other customers' tickets

---

## ⚠️ Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| Can't see tickets | Check user role & team assignment |
| Customer can't access portal | Grant portal access from contact |
| Email not creating tickets | Configure email alias in team settings |
| Ticket disappeared | Check filters - may be hidden |
| Can't change stage | Check permissions |

---

## 📱 Use Cases at a Glance

### IT Support 🖥️
```
Categories: Hardware, Software, Network, Access
Average Resolution: 2-4 hours
Team Size: 3-5 technicians
```

### Customer Service 🛒
```
Categories: Orders, Returns, Shipping, Account
Average Resolution: < 24 hours
Team Size: 5-10 agents
```

### Property Maintenance 🏢
```
Categories: Plumbing, Electrical, HVAC, Emergency
Average Resolution: 2-48 hours
Team Size: 10+ technicians
```

### Software Bugs 🐛
```
Categories: Bug, Feature, Enhancement, Security
Average Resolution: 1-7 days
Team Size: 5-10 developers
```

---

## 📧 Email Integration

### Setup Team Email
```
1. Configuration → Teams → Open team
2. Set "Email Alias" (e.g., support@company.com)
3. Configure incoming mail server
4. Test: Send email to alias → Ticket created
```

### Email → Ticket
- Customer emails → Auto-creates ticket
- Email subject → Ticket name
- Email body → Ticket description
- Attachments → Linked to ticket

---

## 🔢 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Alt + C` | Create new ticket |
| `Alt + S` | Save |
| `Alt + K` | Switch to Kanban |
| `Alt + L` | Switch to List |
| `/` | Search |

---

## 📈 Key Metrics to Track

- **Average Resolution Time** per team
- **First Response Time** per agent
- **Tickets Resolved** per day/week/month
- **Customer Satisfaction** score
- **Open vs Closed** ratio
- **Tickets by Category** (identify trends)
- **Reopened Tickets** (quality check)

---

## 🎨 Customization Ideas

### Custom Fields
- Device Serial Number
- Order Number
- Location/Building
- Software Version
- Contract Number

### Custom Stages
- Waiting for Approval
- Escalated
- Waiting for Parts
- Customer Testing
- Scheduled

### Automation Examples
- Auto-assign by category
- Send reminder after 2 days
- Auto-close after 7 days in "Resolved"
- Escalate if no response in 24h

---

## 📞 Quick Contact

| Need | Contact |
|------|---------|
| Technical Support | support@company.com |
| Report Bug | Create ticket in Helpdesk |
| Feature Request | helpdesk@company.com |
| Training | manager@company.com |

---

## 🎓 Training Checklist

### New Agent Checklist ✓
- [ ] User account created
- [ ] Added to team
- [ ] Permissions assigned (Helpdesk User)
- [ ] Completed user guide
- [ ] Shadowed experienced agent
- [ ] Handled first ticket
- [ ] Knows escalation process

### Manager Checklist ✓
- [ ] Team configured
- [ ] Stages customized
- [ ] Categories defined
- [ ] Tags created
- [ ] Email integration tested
- [ ] Portal enabled for test customer
- [ ] Dashboard reviewed
- [ ] Team trained

---

**Print this card and keep it handy! 📌**

**Need detailed help?** → See `USER_GUIDE.md`

**Module Version:** 19.0 | **Last Updated:** November 2025

