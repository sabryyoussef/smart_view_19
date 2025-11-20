# 📱 Smart View WhatsApp Integration - User Guide

## Overview

**Smart View WhatsApp** integrates WhatsApp Business messaging into your sales workflow, allowing you to send quotations and automated notifications via WhatsApp.

**Architecture:** Wrapper module that uses `pragtech_whatsapp_base` infrastructure for API connectivity.

### Key Features (REQ-00027)

- ✅ **Task 27:** WhatsApp API Integration (via pragtech)
- ✅ **Task 28:** Template Messages
- ✅ **Task 29:** Automated Notifications

**Status:** ⚠️ Requires `pragtech_whatsapp_base` to be installed separately

---

## Installation

### Prerequisites

**REQUIRED:**
1. ✅ `pragtech_whatsapp_base` module (already provided!)
2. ✅ WhatsApp Business Account (Meta, 1msg, or Gupshup)
3. ✅ Active WhatsApp instance configured

### Installation Note

**Module marked as `installable: False`** by default because it requires pragtech_whatsapp_base. Once pragtech is installed and configured, you can enable this module.

---

## Quick Start

**Send Quotation via WhatsApp:**
```
1. Ensure customer has mobile number
2. Open Sales Order
3. Click "Send via WhatsApp" button (green)
4. Wizard opens:
   - Verify mobile number
   - Select template
   - Enable "Attach PDF" for quotation
5. Click "Send" 
6. Done! Customer receives WhatsApp message! ✅
```

---

## Features in Detail

### 1. Manual Send from Sales Order

**"Send via WhatsApp" Button:**
- Location: SO form header (green button with WhatsApp icon)
- Opens wizard with message options
- Validates phone number
- Sends message + optional PDF
- Logs message in system

**Wizard Options:**
- Mobile number (pre-filled from customer)
- WhatsApp instance (if multiple configured)
- Message type (Template or Custom)
- Template selection
- Attach PDF quotation (checkbox)
- Preview and edit message

### 2. Phone Number Validation

**Automatic Checks:**
- ✅ Customer has phone number
- ✅ Minimum 8 digits
- ✅ Valid format (+20 1234567890)
- ✅ International format supported

**Visual Indicators:**
- Green checkmark: Valid
- Red X: Invalid
- Clear error messages

### 3. Template Messages

**Pre-Defined Templates:**
- `quotation_template`: For sending quotes
- `so_confirmation`: Order confirmed
- `project_created`: Project notification
- `payment_received`: Payment confirmed

**Dynamic Variables:**
- `{{customer_name}}`: Customer's name
- `{{order_name}}`: SO reference
- `{{order_amount}}`: Total amount
- `{{company_name}}`: Your company
- `{{project_name}}`: Project name

### 4. Automated Notifications

**Auto-Send When:**
- ✅ SO Confirmation: "Your order SO001 confirmed!"
- ✅ Project Creation: "Project PRJ001 created!"
- ✅ Payment Received: "Payment received, thank you!"

**Configuration:**
- Settings → Sales → WhatsApp Integration
- Enable/disable per notification type
- Non-blocking (failures don't stop operations)

### 5. PDF Attachment

**Quotation PDF:**
- Uses standard Odoo sale report
- Includes company branding
- Attached to WhatsApp message
- Sent after text message

---

## Complete Workflow

**Example: Send Quotation**

```
Day 1: Create SO
Customer: Ahmed Mohamed  
Mobile: +20 1234567890
Amount: $50,000

Day 2: Click "Send via WhatsApp"
Wizard:
- Mobile: ✅ Valid
- Template: quotation_template
- Message: "Dear Ahmed, please find quotation SO001..."
- Attach PDF: ☑️ Yes

Click: "Send via WhatsApp"

System:
✅ Validates mobile
✅ Generates PDF
✅ Sends via pragtech API
✅ Logs message
✅ Marks SO as sent

Customer Receives:
📱 WhatsApp message
📄 Quotation PDF

Success! ✅
```

---

## Provider Setup

### Option A: Meta (Facebook) WhatsApp

**Best For:** Professional businesses, high volume

**Pros:**
- Official solution
- Verified badge (green checkmark)
- Free (pay per conversation)
- Reliable

**Cons:**
- Template approval needed (24-48h)
- Can't send free-form messages
- More complex setup

**Setup:**
1. Create Facebook Business Account
2. Get Phone Number ID & API Token
3. Configure in Odoo WhatsApp Instance
4. Create and submit templates for approval

### Option B: 1msg / Gupshup

**Best For:** Testing, flexibility

**Pros:**
- Quick setup (minutes)
- Send any message
- No template approval

**Cons:**
- Not official (risk of ban)
- Less reliable
- No verification badge

**Setup:**
1. Create account at chat-api.com
2. Get endpoint & token
3. Configure in Odoo
4. Start sending immediately

---

## Use Cases

### Use Case 1: Send Quotation to Customer

```
Customer requests quote
→ Create SO in Odoo
→ Click "Send via WhatsApp"
→ Customer receives within seconds! ⚡

Benefits:
✅ Instant delivery
✅ Customer can view on phone
✅ PDF attachment for details
✅ Higher open rate than email
```

### Use Case 2: Order Confirmation

```
SO confirmed
→ Auto-send: "Order confirmed!"
→ Customer informed immediately

Benefits:
✅ Automatic notification
✅ Reduces inquiry calls
✅ Professional communication
```

### Use Case 3: Project Updates

```
Project created from SO
→ Auto-send: "Project started!"
→ Customer stays informed

Benefits:
✅ Proactive communication
✅ Customer engagement
✅ Reduces follow-up emails
```

---

## Integration with pragtech_whatsapp_base

**What pragtech Provides:**
- WhatsApp API connectivity
- Multiple provider support (Meta, 1msg, Gupshup)
- Template management
- Message logging
- Instance configuration

**What smart_view_whatsapp Adds:**
- Sales Order integration
- Automated notifications
- Business logic
- Smart View workflow

**Result:** Complete WhatsApp solution! ✅

---

## Best Practices

### DO ✅
- Use international format: +20 1234567890
- Test with test numbers first
- Get template approval before launch (Meta)
- Enable automation gradually
- Monitor message logs
- Get customer consent

### DON'T ❌
- Don't spam customers
- Don't share customer data
- Don't use without opt-in
- Don't rely 100% on WhatsApp (have fallback)
- Don't ignore privacy laws (GDPR)

---

## Troubleshooting

**Issue: "No active WhatsApp instance"**
- Solution: Configure pragtech_whatsapp_base first
- Go to Settings → Technical → WhatsApp Instance

**Issue: "Template not found"**
- Solution: Create template in WhatsApp → Templates
- For Meta: Wait for approval (24-48h)

**Issue: "Invalid mobile number"**
- Solution: Update customer mobile
- Use format: +20 1234567890
- Minimum 8 digits

**Issue: "Message sent but not received"**
- Check: Customer's WhatsApp number
- Check: Customer hasn't blocked business
- Check: Provider logs in pragtech

**Issue: "Auto-notify not working"**
- Check: Enabled in Settings?
- Check: Template approved?
- Check: Customer has mobile?
- Check: WhatsApp instance active?

---

## Quick Reference

| Feature | Location | Requirement |
|---------|----------|-------------|
| Send WhatsApp | SO header button | Customer mobile |
| Configure | Settings → Sales | Manager access |
| Templates | WhatsApp → Templates | pragtech module |
| Logs | SO smart button | After sending |
| Instance | Settings → Technical | Admin access |

---

## Security & Privacy

**Access Rights:**
- Sales User: Can send WhatsApp
- Sales Manager: Full access + configuration

**Data Privacy:**
- Messages sent to WhatsApp only
- Logs stored locally
- Respects Odoo privacy settings
- GDPR compliant (with proper consent)

---

## Documentation

### Setup Guides
See `pragtech_whatsapp_base` module for:
- Meta Account Configuration
- 1msg Account Configuration
- Template Setup
- Provider Comparison

### Support
- **Module:** smart_view_whatsapp (business logic)
- **Infrastructure:** pragtech_whatsapp_base (API)
- **Provider:** Meta / 1msg / Gupshup

---

**Module Version:** 19.0.1.0.0  
**Status:** ✅ Complete | ⚠️ Requires pragtech_whatsapp_base  
**Requirements:** REQ-00027 covered (Tasks 27-29)

📱 **Engage customers instantly via WhatsApp!**

**Time Saved:** 14-16 hours by using pragtech infrastructure! 🚀

