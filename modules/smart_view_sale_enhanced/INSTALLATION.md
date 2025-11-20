# Installation & Testing Guide

## Smart View - Sales Enhanced Module

---

## 📋 Pre-Installation Checklist

- [ ] Odoo 19 Community installed and running
- [ ] PostgreSQL database ready
- [ ] Module path configured in Odoo config
- [ ] Access to Apps menu (Administrator)

---

## 🚀 Installation Steps

### Step 1: Add Module to Addons Path

```bash
# Copy or symlink module to Odoo addons directory
# Example:
ln -s /home/sabry3/smart_view/modules/smart_view_sale_enhanced /opt/odoo/custom_addons/

# Or add path to odoo.conf:
# addons_path = /opt/odoo/addons,/home/sabry3/smart_view/modules
```

### Step 2: Restart Odoo Server

```bash
# Restart Odoo service
sudo systemctl restart odoo

# Or if running manually:
# odoo-bin -c /etc/odoo/odoo.conf
```

### Step 3: Update Apps List

1. Log in to Odoo as Administrator
2. Go to `Apps`
3. Click `Update Apps List`
4. Click `Update` in the dialog

### Step 4: Install Module

1. In Apps menu, remove "Apps" filter
2. Search for "Smart View - Sales Enhanced"
3. Click `Install`

**Installation should complete in 5-10 seconds**

---

## ✅ Post-Installation Verification

### Check 1: Module Installed
- Go to `Apps` > Search "Smart View"
- Status should show "Installed"

### Check 2: New Fields Visible
Go to `Sales > Orders > Quotations`
Create new quotation, you should see:
- [x] "Quotation Create Date" field
- [x] "Quotation Template Type" dropdown
- [x] "Request Payment" button
- [x] "Total Discount" at bottom (when lines have discounts)

### Check 3: Order Lines Enhanced
Add products to order line:
- [x] "Internal Reference" column visible
- [x] "Discount %" column
- [x] "Discount Amount" visible when discount applied

### Check 4: Product Field Added
Go to `Sales > Products > Products`
Open any product, go to "Sales" tab:
- [x] "Quotation Description" field visible

### Check 5: Reports Available
From a quotation, click "Print" button:
- [x] Multiple report options visible
- [x] "Quotation / Order (Standard)" available
- [x] "Quotation / Order (Technical)" available

---

## 🧪 Testing Guide

### Test 1: Quotation Create Date

**Steps:**
1. Create new quotation
2. Check "Quotation Create Date" defaults to today
3. Change the date to yesterday
4. Save quotation
5. Print quotation

**Expected:**
- ✅ Date changes successfully
- ✅ Changed date appears in printed report

---

### Test 2: Discount Calculations

**Steps:**
1. Create quotation
2. Add product (e.g., quantity: 10, unit price: 100)
3. Set discount to 10%
4. Check "Discount Amount" field
5. Check "Total Discount" at bottom

**Expected:**
- ✅ Discount Amount = 100 (10 * 100 * 10%)
- ✅ Subtotal = 900
- ✅ Total Discount = 100
- ✅ Total Discount % = 10%

---

### Test 3: Internal Reference Display

**Steps:**
1. Go to product, set Internal Reference (e.g., "PROD001")
2. Add product to quotation
3. Check order line

**Expected:**
- ✅ Internal Reference "PROD001" visible in line
- ✅ Reference appears in tree view
- ✅ Reference appears in printed reports

---

### Test 4: Payment Validation Workflow

**Steps:**
1. Create quotation in Draft state
2. Click "Request Payment" button
3. Check state changed to "Pending Payment"
4. Try to click "Confirm" button (should be hidden/disabled)
5. As Manager, click "Validate Payment"
6. Now click "Confirm" button

**Expected:**
- ✅ State changes to "Pending Payment"
- ✅ Confirm button not available until payment validated
- ✅ After validation, confirm becomes available
- ✅ Order confirms successfully

---

### Test 5: Standard Report Template

**Steps:**
1. Create quotation with multiple products
2. Add discounts to some lines
3. Set Quotation Template Type = "Standard"
4. Print quotation

**Expected:**
- ✅ Report shows all prices
- ✅ Unit prices visible
- ✅ Discounts visible
- ✅ Total discount shown at bottom
- ✅ Internal references visible
- ✅ Product images shown (smaller size)
- ✅ Quotation create date visible

---

### Test 6: Technical Report Template

**Steps:**
1. Go to product, fill "Quotation Description" field
2. Add product to quotation
3. Set Quotation Template Type = "Technical"
4. Print quotation

**Expected:**
- ✅ NO prices shown
- ✅ Product descriptions visible
- ✅ Quotation description field content shown
- ✅ Quantities visible
- ✅ Internal references visible
- ✅ Product images shown (smaller size)
- ✅ Technical details section visible
- ✅ "This is technical quotation" notice shown

---

### Test 7: Multiple Lines with Discounts

**Steps:**
1. Create quotation
2. Add 3 products:
   - Product A: Qty 5, Price 100, Discount 10%
   - Product B: Qty 2, Price 200, Discount 5%
   - Product C: Qty 10, Price 50, Discount 0%
3. Check calculations

**Expected:**
- ✅ Line A discount = 50 (5 * 100 * 10%)
- ✅ Line B discount = 20 (2 * 200 * 5%)
- ✅ Line C discount = 0
- ✅ Total discount = 70
- ✅ Total discount % = calculated correctly
- ✅ Grand total correct

---

### Test 8: Template Auto-Selection

**Steps:**
1. Create quotation, set type = "Standard"
2. Click Print (default print button)
3. Create another quotation, set type = "Technical"
4. Click Print (default print button)

**Expected:**
- ✅ First quotation prints with prices (Standard)
- ✅ Second quotation prints without prices (Technical)
- ✅ System auto-selects correct template

---

## 🐛 Common Issues & Solutions

### Issue 1: Module Not Appearing
**Solution:**
```bash
# Update module list
# In Odoo: Apps > Update Apps List
# Make sure to remove "Apps" filter
```

### Issue 2: Fields Not Showing
**Solution:**
```bash
# Upgrade module
odoo-bin -d your_db -u smart_view_sale_enhanced --stop-after-init
```

### Issue 3: Report Not Printing
**Solution:**
- Check `wkhtmltopdf` is installed
- Check report logs: `/var/log/odoo/odoo.log`
- Verify XML syntax is correct

### Issue 4: Permission Errors
**Solution:**
- Log out and log back in
- Check user has Sales User or Sales Manager role
- Check `security/ir.model.access.csv` is loaded

### Issue 5: Discount Not Calculating
**Solution:**
- Save the quotation first
- Check discount field has value > 0
- Check `_compute_total_discount` method in logs

---

## 📊 Performance Testing

### Load Test
Create quotation with:
- 50 order lines
- All with different discounts
- Print both templates

**Expected:**
- ✅ Calculations complete in < 1 second
- ✅ PDF generation in < 5 seconds
- ✅ No timeout errors

---

## 🔧 Troubleshooting

### Check Logs
```bash
# View Odoo logs
tail -f /var/log/odoo/odoo.log

# Look for errors related to:
# - smart_view_sale_enhanced
# - sale.order
# - QWeb reports
```

### Verify Installation
```python
# In Odoo shell
module = env['ir.module.module'].search([('name', '=', 'smart_view_sale_enhanced')])
print(module.state)  # Should be 'installed'
```

### Check Dependencies
```bash
# Verify required modules are installed
# In Odoo: Apps > search:
# - sale_management ✓
# - product ✓
# - account ✓
```

---

## ✅ Sign-Off Checklist

Before marking as complete, verify:

- [ ] Module installs without errors
- [ ] All new fields visible and editable
- [ ] Discount calculations work correctly
- [ ] Payment validation workflow functions
- [ ] Standard report prints with all features
- [ ] Technical report prints correctly
- [ ] Internal references display properly
- [ ] Images are resized in reports
- [ ] No Python errors in logs
- [ ] No XML errors in logs
- [ ] Permissions work as expected
- [ ] Template auto-selection works

---

## 📞 Support

If you encounter issues:
1. Check this guide first
2. Review module README.md
3. Check PROGRESS.md for known issues
4. Review Odoo logs
5. Verify all requirements met

---

## 🎯 Success Criteria

**Module is ready for production when:**
- ✅ All tests pass
- ✅ No errors in logs
- ✅ Client approval obtained
- ✅ Performance acceptable
- ✅ All features working as designed

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-19  
**Status:** Ready for Testing

