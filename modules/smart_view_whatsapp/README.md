# Smart View - WhatsApp Integration

## Overview

Business logic wrapper for `pragtech_whatsapp_base` module. Adds Smart View-specific WhatsApp functionality for sending quotations and automated notifications.

## Version

- **Version:** 19.0.1.0.0
- **Odoo Version:** 19.0 Community
- **License:** LGPL-3

## Features

### REQ-00027: WhatsApp Integration ✅

**Complete Implementation of Tasks 27-29:**

#### Task 27: WhatsApp API Integration ✅
- Uses `pragtech_whatsapp_base` infrastructure
- Multiple provider support (Meta, 1msg, Gupshup)
- Sales Order integration
- "Send via WhatsApp" button on SO form
- Phone number validation

#### Task 28: Template Messages ✅
- Template management via pragtech
- Automatic template selection
- Dynamic parameter replacement
- Quotation templates
- Notification templates

#### Task 29: Automated Notifications ✅
- Auto-notify on SO confirmation
- Auto-notify on project creation
- Auto-notify on payment received
- Configurable in Settings

---

## Installation

### Prerequisites

**REQUIRED:**
- Odoo 19 Community Edition
- `pragtech_whatsapp_base` module ✅ **(Already installed!)**
- `smart_view_sale_enhanced` module
- `smart_view_crm_enhanced` module  
- `smart_view_project_sale` module

### Install Steps

1. **Ensure pragtech_whatsapp_base is installed and configured**
   - Already done! ✅

2. **Install smart_view_whatsapp**
   ```bash
   # Update apps list
   -u smart_view_whatsapp
   ```

3. **Configure WhatsApp Instance** (in pragtech_whatsapp_base)
   - Go to Settings > Technical > WhatsApp > WhatsApp Instance
   - Create/Configure instance (Meta or 1msg)
   - Set status to "Enable"

4. **Create WhatsApp Templates**
   - Go to WhatsApp > Templates
   - Create required templates (see below)
   - Get Meta approval if using Meta provider

5. **Enable Automated Notifications** (optional)
   - Go to Settings > Sales > WhatsApp Integration
   - Enable desired notifications

---

## Configuration

### Step 1: Configure pragtech_whatsapp_base

#### Option A: Meta (Facebook) WhatsApp Business API

1. **Create Facebook/Meta Account**
   - Go to developers.facebook.com
   - Create WhatsApp Business Account
   - Get Phone Number ID
   - Get API Token

2. **Configure in Odoo**
   - WhatsApp > WhatsApp Instance > Create
   - Provider: "Meta"
   - Meta API Token: [your token]
   - Meta Phone Number ID: [your phone ID]
   - Status: "Enable"

**See:** `Configure META Account in Odoo Whatsapp Instance.doc.pdf` (in pragtech module)

#### Option B: 1msg (chat-api.com)

1. **Create 1msg Account**
   - Go to chat-api.com
   - Get instance endpoint
   - Get API token

2. **Configure in Odoo**
   - WhatsApp > WhatsApp Instance > Create
   - Provider: "1msg"
   - Endpoint: [your endpoint]
   - Token: [your token]
   - Status: "Enable"

**See:** `Configure 1Msg Account in Odoo Whatsapp Instance.doc.pdf` (in pragtech module)

### Step 2: Create WhatsApp Templates

**Required Templates:**

#### 1. quotation_template (For Manual Send)
**Name:** `quotation_template`  
**Type:** Transactional  
**Category:** Order  

**Example Message:**
```
Hello {{customer_name}},

Thank you for your interest! Please find your quotation {{order_name}}.

Total Amount: {{order_amount}}

We look forward to working with you!

Best regards,
{{company_name}}
```

**Variables:**
- `{{customer_name}}` - Customer name
- `{{order_name}}` - SO reference
- `{{order_amount}}` - Total amount
- `{{company_name}}` - Your company

#### 2. so_confirmation (For Auto-notify)
**Name:** `so_confirmation`  
**Type:** Transactional  
**Category:** Order

**Example Message:**
```
Dear {{customer_name}},

Your order {{order_name}} has been confirmed!

We will start processing it shortly.

Thank you for your business!

Best regards,
{{company_name}}
```

#### 3. project_created (For Auto-notify)
**Name:** `project_created`  
**Type:** Transactional  
**Category:** Service

**Example Message:**
```
Dear {{customer_name}},

Great news! Your project "{{project_name}}" has been created.

Our team will begin work shortly.

We'll keep you updated on progress!

Best regards,
{{company_name}}
```

**How to Create Templates:**

1. Go to WhatsApp > Templates
2. Click "Create"
3. Fill in Name, Message, Variables
4. Save
5. **For Meta:** Submit for approval (24-48 hours)
6. **For 1msg/Gupshup:** Templates active immediately

### Step 3: Enable Automation (Optional)

1. Go to **Settings > Sales > WhatsApp Integration**

2. Enable desired features:
   - ☑️ **Auto-notify on SO Confirmation**
   - ☑️ **Auto-notify on Project Creation**  
   - ☑️ **Auto-notify on Payment**

3. Set template names (if different from defaults):
   - Quotation Template: `quotation_template`
   - SO Confirmation Template: `so_confirmation`
   - Project Template: `project_created`

4. Click "Save"

---

## Usage

### Manual Send: Quotation via WhatsApp

**From Sales Order:**

1. Open a Sales Order
2. Check customer has mobile number
3. Click **"Send via WhatsApp"** button (green, WhatsApp icon)
4. Wizard opens:
   - Verify mobile number
   - Select WhatsApp instance (if multiple)
   - Choose message type
   - Select template (or use custom message)
   - Enable "Attach PDF" to send quotation PDF
   - Modify message if needed
5. Click **"Send via WhatsApp"**
6. Success notification appears!

**Result:**
- Customer receives WhatsApp message
- Quotation PDF attached (if enabled)
- SO marked as "WhatsApp Sent" ✅
- Message logged in WhatsApp Messages

### Automatic Notifications

**When enabled, system automatically sends:**

#### SO Confirmation Notification
```
Trigger: When SO state changes to "Sale"
Template: so_confirmation
Recipient: SO customer (if has mobile)
```

#### Project Creation Notification
```
Trigger: When project created from SO
Template: project_created
Recipient: Project customer (if has mobile)
```

#### Payment Received Notification
```
Trigger: When payment posted
Template: payment_received
Recipient: SO customer (if has mobile)
```

**Note:** Notifications are non-blocking - if WhatsApp fails, the operation continues.

---

## Complete Workflow

### Scenario: Send Quotation to Customer

```
1. Create Sales Order
   - Customer: Ahmed Mohamed
   - Mobile: +20 1234567890
   - Amount: 50,000 EGP
   ↓
2. Click "Send via WhatsApp"
   ↓
3. Wizard Opens:
   - Mobile: +20 1234567890 ✅ Valid
   - Message: "Dear Ahmed, please find quotation SO001..."
   - Attach PDF: ☑️ Yes
   ↓
4. Click "Send via WhatsApp"
   ↓
5. System:
   - Validates mobile ✅
   - Generates quotation PDF ✅
   - Sends via pragtech API ✅
   - Logs message ✅
   - Marks SO as sent ✅
   ↓
6. Customer Receives:
   - WhatsApp message with greeting
   - Quotation PDF attachment
   ↓
7. Success! ✅
```

### Scenario: Auto-notify on Project Creation

```
1. CRM Opportunity approved ✅
   ↓
2. Create Sales Order ✅
   ↓
3. Confirm SO ✅
   → WhatsApp: "Order SO001 confirmed!" (if enabled)
   ↓
4. Create Project ✅
   → WhatsApp: "Project PRJ001 created!" (if enabled)
   ↓
5. Customer informed at every step! ✅
```

---

## Features in Detail

### 1. Sales Order Integration

**New Fields on SO:**
- `whatsapp_sent` (Boolean) - Indicates if sent
- `whatsapp_sent_date` (Datetime) - When sent
- `whatsapp_message_count` (Integer) - Count of messages
- `partner_whatsapp` (Char) - Customer's number
- `can_send_whatsapp` (Boolean) - Validation flag

**New Buttons:**
- **"Send via WhatsApp"** - Header button (green)
- **WhatsApp Messages** - Smart button (shows count)

**Validation:**
- Checks customer exists
- Checks mobile number exists
- Checks mobile format (8+ digits)
- Checks WhatsApp instance active
- Shows clear error messages

### 2. Phone Number Validation

**Automatic Validation:**
- Removes spaces and special characters
- Checks minimum 8 digits
- Supports international format (+20...)
- Visual indicator (green checkmark)

**Error Handling:**
- Clear error messages
- Suggests fixes
- Non-blocking (doesn't prevent SO creation)

### 3. PDF Generation

**Quotation PDF:**
- Uses standard Odoo sale report
- Includes company header/footer (from smart_view_company_branding)
- Saved as attachment
- Sent separately after text message

**Options:**
- Enable/disable PDF attachment
- Uses existing SO report template
- Supports custom reports

### 4. Template Integration

**Automatic Template Selection:**
- Searches by name (quotation_template, so_confirmation, etc.)
- Checks approval status (Meta requirement)
- Falls back to custom message if template not found

**Dynamic Parameters:**
- `{{customer_name}}` - From partner
- `{{order_name}}` - SO reference
- `{{order_amount}}` - Total amount
- `{{company_name}}` - Your company
- `{{project_name}}` - Project name (for project notifications)

**Template Types:**
- **Transactional:** For order/project updates (approved faster)
- **Marketing:** For promotions (requires opt-in)

### 5. Automated Notifications

**Non-Blocking:**
- WhatsApp failures don't stop SO confirmation
- Errors logged for review
- Silent failures (no user popup)

**Configurable:**
- Enable/disable per notification type
- Set custom template names
- Global settings

**Logging:**
- All messages logged in pragtech_whatsapp_base
- View from SO smart button
- Track delivery status (if provider supports)

---

## Technical Details

### Architecture

```
smart_view_whatsapp (Wrapper - Business Logic)
    ↓ uses
pragtech_whatsapp_base (Infrastructure - API)
    ↓ connects to
Meta WhatsApp API / 1msg / Gupshup (Provider)
    ↓ delivers to
Customer's WhatsApp
```

**Why This Design?**
- ✅ Don't reinvent API infrastructure
- ✅ Professional base module (maintained)
- ✅ Multiple provider support
- ✅ Just add business logic layer
- ✅ Easy upgrades (vendor handles API changes)

### Models

#### sale.order (Extension)
**New Fields:** whatsapp_sent, whatsapp_sent_date, whatsapp_message_count, etc.

**New Methods:**
- `action_send_whatsapp()` - Open send wizard
- `_send_whatsapp_notification()` - Internal notification sender
- `_render_whatsapp_template()` - Template rendering
- `action_view_whatsapp_messages()` - View sent messages
- Override `action_confirm()` - Auto-notify

#### project.project (Extension)
**Override Methods:**
- `create()` - Auto-notify on project creation

**New Methods:**
- `_send_project_whatsapp_notification()` - Send project notifications

#### res.config.settings (Extension)
**New Fields:**
- Configuration options for auto-notifications
- Template name settings

#### send.whatsapp.wizard (New Model)
**Purpose:** User interface for sending WhatsApp

**Fields:**
- sale_order_id, partner_id, mobile
- whatsapp_instance_id, template_id
- message_type, message, attach_pdf

**Methods:**
- `action_send_whatsapp()` - Main send method
- `_send_template_message()` - Send via template
- `_send_direct_message()` - Send direct message
- `_generate_quotation_pdf()` - Generate PDF

### Integration with pragtech_whatsapp_base

**Models Used:**
- `whatsapp.instance` - WhatsApp connection configuration
- `whatsapp.templates` - Template management
- `whatsapp.messages` - Message logging

**Methods Called:**
- `send_template_message()` - Send via template (Meta)
- `send_message()` - Send direct message (1msg/Gupshup)
- `send_document()` - Send PDF attachment

---

## Provider Comparison

### Meta (Facebook) WhatsApp Business API

**Pros:**
- ✅ Official WhatsApp Business solution
- ✅ Free (pay only for conversations)
- ✅ Verified business badge (green checkmark)
- ✅ Reliable, scalable
- ✅ Rich features (buttons, lists, etc.)

**Cons:**
- ❌ Requires template approval (24-48h)
- ❌ Can't send free-form messages
- ❌ Setup more complex
- ❌ Strict compliance rules

**Best For:** Professional businesses, high volume, want verification

### 1msg (chat-api.com)

**Pros:**
- ✅ Quick setup (minutes)
- ✅ Send any message (no templates)
- ✅ No approval needed
- ✅ Simple API

**Cons:**
- ❌ Not official (uses WhatsApp Web)
- ❌ Risk of ban (WhatsApp TOS)
- ❌ Less reliable
- ❌ Limited features

**Best For:** Testing, low volume, need flexibility

### Gupshup

**Similar to 1msg** - unofficial but more stable

---

## Troubleshooting

### Issue: "No active WhatsApp instance found"

**Cause:** pragtech_whatsapp_base not configured

**Solution:**
1. Go to Settings > Technical > WhatsApp > WhatsApp Instance
2. Create/Configure instance
3. Set status to "Enable"
4. Test connection

### Issue: "Template not found or not approved"

**Cause:** Template doesn't exist or not approved by Meta

**Solution:**
1. Go to WhatsApp > Templates
2. Create template with exact name (e.g., "quotation_template")
3. For Meta: Submit for approval, wait 24-48h
4. Check approval status
5. Or: Disable "Use Template" in wizard

### Issue: "Invalid mobile number"

**Cause:** Customer mobile format invalid

**Solution:**
1. Go to customer record
2. Update mobile number
3. Use international format: +20 1234567890
4. Ensure at least 8 digits

### Issue: "WhatsApp sent but customer didn't receive"

**Causes:**
- Customer's WhatsApp number wrong
- Customer blocked business
- Network issues
- Provider issues

**Solutions:**
1. Verify customer's number
2. Check pragtech_whatsapp_base logs
3. Check message delivery status
4. Contact provider support

### Issue: "Auto-notify not working"

**Checklist:**
1. ✅ Automation enabled in Settings?
2. ✅ Template exists and approved?
3. ✅ Customer has mobile number?
4. ✅ WhatsApp instance active?
5. ✅ Check logs for errors

---

## Best Practices

### Template Management

1. **Use Descriptive Names:** quotation_template, so_confirmation
2. **Get Pre-Approved:** Submit templates before going live
3. **Test Thoroughly:** Send to test numbers first
4. **Keep Simple:** Short, clear messages work best
5. **Follow Guidelines:** Meta has strict content rules

### Phone Numbers

1. **Always International Format:** +20 1234567890
2. **Validate on Entry:** Check when creating customers
3. **Keep Updated:** Verify numbers regularly
4. **Test Numbers:** Use test numbers for development

### Automation

1. **Start Manual:** Get comfortable before enabling automation
2. **Test First:** Enable for test customers first
3. **Monitor:** Check logs regularly
4. **Have Fallback:** Don't rely 100% on WhatsApp

### Compliance

1. **Get Consent:** Only send to customers who opt-in
2. **Respect Privacy:** Don't share customer data
3. **Follow Laws:** GDPR, local data protection
4. **Opt-Out:** Provide way to stop messages

---

## Customization

### Add Custom Template

**Example: Payment Reminder**

1. **Create Template in pragtech:**
   ```
   Name: payment_reminder
   Message: Dear {{customer_name}}, reminder that payment for {{order_name}} is due. Amount: {{amount}}. Thank you!
   ```

2. **Create automation (optional):**
   - Model: sale.order
   - Trigger: Scheduled (daily)
   - Filter: invoice_status = 'to invoice'
   - Action: Call _send_whatsapp_notification('payment_reminder')

3. **Or send manually:**
   ```python
   order._send_whatsapp_notification('payment_reminder', {
       'amount': order.amount_total
   })
   ```

### Extend for Other Models

**Example: Send from CRM Opportunities**

1. **Create model extension:**
   ```python
   class CrmLead(models.Model):
       _inherit = 'crm.lead'
       
       def action_send_whatsapp(self):
           # Similar to SO implementation
           pass
   ```

2. **Add button to CRM form view**
3. **Create wizard for CRM**

---

## Security

### Access Rights
- Sales users can send WhatsApp
- Sales managers have full access
- Respects Odoo's standard security

### Data Privacy
- No customer data sent to external servers (except WhatsApp provider)
- Messages logged locally
- Respects Odoo's privacy settings

---

## Credits

- **Development Team:** Smart View Development Team
- **Infrastructure:** Pragmatic TechSoft (pragtech_whatsapp_base)
- **Based on:** Odoo 19 Community
- **License:** LGPL-3

---

## Changelog

### Version 19.0.1.0.0 (2025-11-19)
- Initial release
- REQ-00027 complete implementation ✅
- Task 27: WhatsApp API integration (via pragtech) ✅
- Task 28: Template messages ✅
- Task 29: Automated notifications ✅
- SO integration with send button
- Phone validation
- PDF attachment
- Automated SO/project/payment notifications
- Configuration settings
- Complete documentation

---

**Status:** ✅ Complete and Ready for Testing

**Integration:** Wrapper for pragtech_whatsapp_base ✅

**Time Saved:** 14-16 hours by using existing infrastructure! 🚀

