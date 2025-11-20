# 🔒 Smart View WhatsApp - Menu & Security

## Overview

**Module Type:** Wrapper/Integration  
**Installable:** False (requires pragtech_whatsapp_base)  
**Purpose:** Business logic for WhatsApp in Smart View workflow

## Architecture

```
smart_view_whatsapp (Wrapper)
    ↓ depends on
pragtech_whatsapp_base (Infrastructure)
    ↓ provides
WhatsApp Connectivity ✅
```

## Enhanced Views

### Sales Order Form
- ✅ "Send via WhatsApp" button (header)
- ✅ WhatsApp sent indicator
- ✅ WhatsApp Messages smart button
- ✅ Mobile number display

**Visibility:** Sales User+

## No New Menus

**Uses existing pragtech menus:**
- WhatsApp → Instances
- WhatsApp → Templates
- WhatsApp → Messages

## Security Groups

**Uses Odoo Core Groups:**
- `sales_team.group_sale_salesman` (Sales User)
- `sales_team.group_sale_manager` (Sales Manager)

**No custom groups added** ✅

## Permissions

| Action | Sales User | Sales Manager |
|--------|------------|---------------|
| Send WhatsApp | ✅ | ✅ |
| View messages | ✅ | ✅ |
| Configure templates | ❌ | ✅ |
| Configure instance | ❌ | ⚠️ Admin |
| Enable automation | ❌ | ✅ |

## Field Security

**SO Fields:**
- `whatsapp_sent`: Readonly (system sets)
- `whatsapp_sent_date`: Readonly (system sets)
- `partner_whatsapp`: Related from partner
- `can_send_whatsapp`: Computed (validation)

## Button Security

**"Send via WhatsApp":**
- Visible when: `can_send_whatsapp = True`
- Requires: Customer mobile number
- Executes: Sales User+

## Validation Logic

**Before Send:**
1. ✅ Customer exists
2. ✅ Mobile number exists
3. ✅ Mobile valid format (8+ digits)
4. ✅ WhatsApp instance active
5. ✅ Template exists (if using template)

**Result:** Clear error messages if validation fails

## Integration Security

**With pragtech_whatsapp_base:**
- ✅ Read-only access to instances
- ✅ Read-only access to templates
- ✅ Create access to messages (for logging)

**API Credentials:**
- ⚠️ Stored in pragtech module (secure)
- ⚠️ Admin-only access
- ⚠️ Never exposed to regular users

## Data Privacy

**Customer Data:**
- Mobile number: Required for sending
- Name: Used in templates
- Order details: Sent in message

**Compliance:**
- ✅ GDPR: Get customer consent
- ✅ Opt-out: Provide unsubscribe mechanism
- ✅ Data: Sent only to WhatsApp provider
- ✅ Logs: Stored locally in Odoo

## Access Rights (ir.model.access.csv)

**Models:**
- All standard sale.order permissions apply
- No additional restrictions

**Wizard:**
- `send.whatsapp.wizard`: Temporary (session-only)
- Auto-cleaned after sending

## Best Practices

### DO ✅
- Get customer consent before sending
- Use international phone format
- Test with test numbers first
- Monitor logs regularly
- Respect privacy laws

### DON'T ❌
- Don't spam customers
- Don't share customer data
- Don't store API credentials in code
- Don't bypass phone validation
- Don't send without opt-in

## Installation Security

**Why `installable: False`?**
- ✅ Requires pragtech_whatsapp_base (not in standard Odoo)
- ✅ Prevents partial installation
- ✅ Ensures proper setup order
- ✅ Clear dependency management

**Installation Steps:**
1. Install pragtech_whatsapp_base
2. Configure WhatsApp instance
3. Enable smart_view_whatsapp
4. Test thoroughly

## Troubleshooting Security

**Issue: Can't send WhatsApp**
- Check: Sales User role assigned?
- Check: Customer has mobile?
- Check: Instance configured?

**Issue: Can't configure**
- Expected: Only managers configure
- Solution: Request manager access

**Issue: Messages not private**
- Check: Record rules working?
- Check: Multi-company setup?
- Solution: Verify Odoo security

## Verification Summary

✅ **No New Menus:** Uses pragtech menus  
✅ **No Custom Groups:** Uses Odoo core  
✅ **Clean Integration:** Wrapper pattern  
✅ **Secure:** Validation + privacy  
✅ **Compliant:** GDPR ready (with consent)

**Verified:** November 2025  
**Status:** ✅ Security properly configured  
**Dependency:** Requires pragtech_whatsapp_base

📱 **Secure WhatsApp integration for sales!**

