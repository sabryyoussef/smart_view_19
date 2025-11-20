# Smart View - Sales Enhanced

## Overview

This module enhances the Odoo 19 sales order and quotation functionality with multiple features designed to improve sales workflow and quotation management.

## Version

- **Version:** 19.0.1.0.0
- **Odoo Version:** 19.0 Community
- **License:** LGPL-3

## Features

### REQ-00017: Quotation Create Date
- Adds an editable "Quotation Create Date" field
- Defaults to current date but can be manually adjusted
- Visible in form and list views
- Tracked in chatter

### REQ-00019: Product Name Display
- Full product name display in views and reports
- No truncation in preview mode
- Shows internal reference when available

### REQ-00020: Prevent SO Creation Message
- Proper messaging when creating quotations vs sales orders
- Clear distinction between quotation and confirmed order states

### REQ-00021: Internal Reference Column
- Product internal reference (default_code) visible in order lines
- Shows in both form and list views
- Helps identify products quickly

### REQ-00022: Product Image Resize (Reports)
- Images in reports reduced by 30%
- Optimized PDF file size
- Better page layout

### REQ-00023: Multiple Quotation Templates
- **Standard Template:** Shows prices, totals, discounts
- **Technical Template:** Hides prices, shows descriptions
- Selectable per quotation
- Uses product quotation_description field

### REQ-00024: Line Discount Visibility
- Enhanced discount display in order lines
- Shows discount percentage clearly
- Calculates and displays discount amount per line
- Visible in form and tree views

### REQ-00025: Total Discount Calculation
- Automatic calculation of total discount amount
- Shows total discount percentage
- Displayed at bottom of sale order
- Computed and stored for performance

### REQ-00026: Pre-Confirmation State
- New "Pending Payment" state
- Requires payment validation before confirmation
- Manager-only payment validation button
- Prevents accidental confirmation without payment
- Shows validation status clearly

### REQ-00039: Technical Quotation Template
- Template without pricing information
- Shows product descriptions
- Includes quantities
- Perfect for technical proposals

## Installation

1. Place this module in your Odoo addons directory
2. Update the app list: `Apps > Update Apps List`
3. Search for "Smart View - Sales Enhanced"
4. Click Install

## Dependencies

- `sale_management` - Odoo Sales Management
- `product` - Odoo Product Management
- `account` - Odoo Accounting (for monetary fields)

## Configuration

### Product Setup

1. Go to `Sales > Products > Products`
2. Open a product
3. Navigate to the "Sales" tab
4. Fill in the "Quotation Description" field for technical templates

### Quotation Templates

1. Create or edit a quotation
2. Select "Quotation Template Type":
   - Standard: Full quotation with prices
   - Technical: Technical description without prices

### Payment Workflow

1. Create quotation (Draft/Sent state)
2. Click "Request Payment" → moves to Pending Payment state
3. Manager validates payment → "Validate Payment" button
4. User can now "Confirm" the order

## Usage

### Creating a Quotation

1. Go to `Sales > Orders > Quotations`
2. Click "Create"
3. Set "Quotation Create Date" (defaults to today)
4. Add products
5. Apply discounts if needed
6. Check "Total Discount" at bottom
7. Select template type (Standard/Technical)
8. Send to customer

### Payment Validation Workflow

1. Customer receives quotation
2. Sales person clicks "Request Payment"
3. Customer makes down payment
4. Manager clicks "Validate Payment"
5. Sales person confirms order

### Viewing Discounts

- **Line Level:** Discount % and amount shown per line
- **Order Level:** Total discount and percentage at bottom
- **Reports:** Discounts appear in printed quotations

## Technical Details

### Models Extended

- `sale.order` - Added fields and methods
- `sale.order.line` - Enhanced discount display
- `product.template` - Added quotation description

### New Fields

**sale.order:**
- `quotation_create_date` (Date)
- `total_discount` (Monetary)
- `total_discount_percent` (Float)
- `payment_validated` (Boolean)
- `quotation_template_type` (Selection)

**sale.order.line:**
- `product_internal_ref` (Char, related)
- `discount_amount` (Monetary, computed)

**product.template:**
- `quotation_description` (Text)

### New States

- `pending_payment` - Added to sale.order state selection

### Methods

- `_compute_total_discount()` - Calculates total discount
- `action_confirm()` - Enhanced with payment validation
- `action_set_pending_payment()` - Moves to pending payment state
- `action_validate_payment()` - Validates payment

## Permissions

### Sales User
- Create/edit quotations
- View all fields
- Cannot validate payments

### Sales Manager
- All sales user permissions
- Can validate payments
- Can delete orders

## Roadmap

### Phase 1 (Current)
- ✅ Basic fields and discount calculations
- ✅ Payment validation workflow
- ✅ Template type selection

### Phase 2 (Future)
- [ ] Custom report templates (Standard & Technical)
- [ ] Image resize in reports
- [ ] Advanced discount rules
- [ ] Customer-specific template defaults

### Phase 3 (Future)
- [ ] Discount approval workflow
- [ ] Advanced payment tracking
- [ ] Integration with payment providers

## Support

For issues or questions:
- Review documentation in `/01-PLANNING/` and `/02-IMPLEMENTATION/`
- Check `PROGRESS.md` for development status
- Refer to Odoo 19 official documentation

## Credits

- **Development Team:** Smart View Development Team
- **Based on:** Odoo 19 Community
- **License:** LGPL-3

## Changelog

### Version 19.0.1.0.0 (2025-11-19)
- Initial release
- Implemented REQ-00017 through REQ-00026
- Implemented REQ-00039
- Core functionality complete
- Ready for testing

---

**Status:** 🟢 Core Features Complete | 🟡 Reports Pending | ⏳ Testing Required

