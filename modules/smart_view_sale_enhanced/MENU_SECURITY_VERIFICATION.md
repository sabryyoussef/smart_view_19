# 🔒 Smart View Sales Enhanced - Menu & Security

## Overview

Enhances **existing** Sales Order views. No new menus added.

## Enhanced Views

### Sales Order Form
- ✅ Quotation Create Date field
- ✅ Internal Reference column in lines
- ✅ Discount amount calculated
- ✅ Total discount displayed
- ✅ Payment validation buttons
- ✅ Template type selector

### Reports
- ✅ Standard Quotation Template
- ✅ Technical Quotation Template
- ✅ Resized product images (30% smaller)

## Security Groups

**Uses Odoo Core Groups:**
- `sales_team.group_sale_salesman` (Sales User)
- `sales_team.group_sale_manager` (Sales Manager)

**No custom groups added** ✅

## Permissions

| Action | Sales User | Sales Manager |
|--------|------------|---------------|
| Create quotation | ✅ | ✅ |
| Edit quotation date | ✅ | ✅ |
| Apply discounts | ✅ | ✅ |
| View total discount | ✅ | ✅ |
| Request payment | ✅ | ✅ |
| **Validate payment** | ❌ | ✅ |
| Select template | ✅ | ✅ |

## Field Security

- `quotation_create_date`: Editable by Sales User+
- `total_discount`: Computed (system only)
- `payment_validated`: Manager-level approval
- `quotation_template_type`: Editable by Sales User+

## Button Security

**"Request Payment":** Sales User+  
**"Validate Payment":** Sales Manager only  
**"Confirm":** Sales User+ (if payment validated)

## Status

✅ Clean integration with Odoo core  
✅ No custom security conflicts  
✅ Manager-level payment control

**Verified:** November 2025  
**Status:** ✅ Production Ready

