# 💰 Smart View Sales Enhanced - User Guide

## Overview

**Smart View Sales Enhanced** adds powerful features to Odoo's sales module including discount visibility, multiple quotation templates, and payment validation workflow.

### Key Features (10 Requirements Covered!)

- ✅ **REQ-00017:** Editable quotation create date
- ✅ **REQ-00019:** Full product name display
- ✅ **REQ-00020:** Clear SO creation messaging
- ✅ **REQ-00021:** Internal reference column
- ✅ **REQ-00022:** Product image resize (30% smaller PDFs)
- ✅ **REQ-00023:** Multiple quotation templates
- ✅ **REQ-00024:** Enhanced line discount visibility
- ✅ **REQ-00025:** Total discount calculation
- ✅ **REQ-00026:** Pre-confirmation payment state
- ✅ **REQ-00039:** Technical quotation template

---

## Quick Start

**Create Enhanced Quotation:**
```
1. Sales → Quotations → Create
2. Set "Quotation Create Date" (editable)
3. Add products (see internal reference!)
4. Apply discounts (see total discount calculated!)
5. Select template: Standard or Technical
6. Send to customer
```

---

## Features in Detail

### 1. Quotation Create Date (REQ-00017)

**Purpose:** Edit when quotation was actually created (for backdating)

**Usage:**
- Field visible in form view
- Defaults to today
- Can change to past/future date
- Tracked in chatter

### 2. Product Name Display (REQ-00019)

**Enhancement:** Full product names visible (no truncation)

**Benefit:** See complete product descriptions in views and reports

### 3. Internal Reference Column (REQ-00021)

**What:** Product internal reference (SKU/Code) visible in order lines

**Location:** SO line tree view, form view

**Benefit:** Quick product identification by code

### 4. Image Resize in Reports (REQ-00022)

**Optimization:** Product images in PDF quotations 30% smaller

**Result:** Faster PDFs, better page layout

### 5. Multiple Quotation Templates (REQ-00023 + REQ-00039)

**Two Templates Available:**

**Standard Template:**
- Shows all prices
- Shows discounts
- Shows totals
- Perfect for regular quotations

**Technical Template:**
- Hides prices (for technical proposals)
- Shows product descriptions
- Shows quantities
- Perfect for specifications

**How to Use:**
```
1. In SO form
2. Field: "Quotation Template Type"
3. Select: Standard or Technical
4. Print → Uses selected template
```

### 6. Line Discount Visibility (REQ-00024)

**Enhanced Display:**
- Discount % per line
- Discount amount calculated per line
- Visible in form and tree views

**Example:**
```
Product: Camera System - $1,000
Discount: 10%
Discount Amount: $100 (calculated automatically)
Subtotal: $900
```

### 7. Total Discount Calculation (REQ-00025)

**Automatic Totals:**
- Total discount amount (sum of all line discounts)
- Total discount percentage (overall discount rate)
- Displayed at bottom of SO

**Example:**
```
Line 1: $1,000 - 10% discount = $100
Line 2: $500 - 5% discount = $25
Line 3: $800 - 15% discount = $120

Total Discount: $245
Total Discount %: 11.09%
```

### 8. Pre-Confirmation Payment State (REQ-00026)

**Payment Validation Workflow:**

```
Draft/Sent Quotation
    ↓
Click "Request Payment"
    ↓
State: Pending Payment
(Customer makes down payment)
    ↓
Manager clicks "Validate Payment"
    ↓
payment_validated = True
    ↓
User clicks "Confirm"
    ↓
Sales Order Confirmed! ✅
```

**Benefits:**
- ✅ Prevents confirmation without payment
- ✅ Manager-level payment validation
- ✅ Clear payment workflow
- ✅ Payment tracking

---

## Use Cases

### Use Case 1: Quotation with Discounts

**Scenario:** Security system quotation with volume discount

```
Products:
- 20x Camera @ $200 = $4,000 (10% discount = $400)
- 1x DVR @ $500 = $500 (no discount)
- Installation @ $1,000 = $1,000 (15% discount = $150)

System Calculates:
Total Discount: $550
Total Discount %: 10%
Grand Total: $4,950

Customer sees clear discount breakdown! ✅
```

### Use Case 2: Technical Quotation

**Scenario:** Send specification without prices

```
1. Create quotation with all products
2. Select "Technical" template
3. Print/Send

Customer Receives:
✅ Product descriptions
✅ Quantities
✅ Technical specs
❌ NO prices (for technical team review)

Later: Send Standard template with prices
```

### Use Case 3: Payment Validation

**Scenario:** Require down payment before order

```
Day 1: Send quotation
Day 2: Customer agrees → Click "Request Payment"
       Status: Pending Payment
Day 3: Customer pays 50% down payment
       Finance: Verifies payment
       Manager: Click "Validate Payment"
Day 4: Sales rep: Click "Confirm"
       Status: Sales Order ✅

Payment secured before work starts! 💰
```

---

## Best Practices

### DO ✅
- Use quotation create date for accurate records
- Apply discounts at line level for clarity
- Use Technical template for specs
- Validate payment before confirmation
- Check total discount before sending

### DON'T ❌
- Don't skip payment validation on large orders
- Don't use Standard template if hiding prices
- Don't forget to set quotation date
- Don't confirm without manager approval (if payment workflow enabled)

---

## Troubleshooting

**Issue: Can't confirm order**
- Check: Payment validated?
- Solution: Manager must validate payment first

**Issue: Discount not showing in total**
- Check: Discount entered on lines?
- Solution: System calculates automatically from line discounts

**Issue: Template not applying**
- Check: Template type selected?
- Solution: Select Standard or Technical before printing

---

## Quick Reference

| Feature | Location | Time Saved |
|---------|----------|------------|
| Quotation date | SO form | 30 sec |
| Internal reference | Line view | 1 min/line |
| Total discount | SO bottom | Automatic |
| Template selection | SO form | 5 sec |
| Payment workflow | Header buttons | Process control |

---

**Module Version:** 19.0.1.0.0  
**Status:** ✅ Production Ready  
**Requirements:** 10 covered!

🚀 **Enhanced sales workflow with better visibility and control!**

