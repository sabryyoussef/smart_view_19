# 🚀 Quick Start Guide - Smart View Odoo 19

## 📋 Pre-Development Checklist

Before starting development, ensure you have:

- [ ] Odoo 19 Community installed
- [ ] PostgreSQL database set up
- [ ] Python 3.10+ installed
- [ ] Git repository initialized
- [ ] Development environment configured
- [ ] Client requirements confirmed
- [ ] Architecture approved

---

## ⚡ Fast Track: Create All Module Skeletons

### Step 1: Create Directory Structure

```bash
cd /home/sabry3/smart_view

# Create module directories
mkdir -p smart_view_company_branding/{static/src/img,report}
mkdir -p smart_view_sale_enhanced/{models,views,report,wizard,data,security}
mkdir -p smart_view_whatsapp/{models,views,wizard,data,security}
mkdir -p smart_view_crm_enhanced/{models,views,wizard,data,security}
mkdir -p smart_view_project_sale/{models,views,wizard,security}
mkdir -p smart_view_project_enhanced/{models,views,data,security}
mkdir -p smart_view_helpdesk/{models,views,security}

# Optional base module
mkdir -p smart_view_base/{models,views,security}
```

---

## 📝 Step 2: Create Basic __init__.py Files

Each module needs an `__init__.py` in the root and models directory.

### Template for root __init__.py:

```python
# -*- coding: utf-8 -*-

from . import models
from . import wizard  # If module has wizards
```

### Template for models/__init__.py:

```python
# -*- coding: utf-8 -*-

from . import model_name
```

---

## 📦 Step 3: Module Priority Order

### **Start with these 3 modules first:**

#### 1️⃣ smart_view_company_branding (Easiest)
**Why first?** Simple, visible impact, independent

**Tasks:**
1. Get header/footer images from client
2. Create external_layout_custom.xml
3. Test on quotation report

**Estimated time:** 1-2 days

---

#### 2️⃣ smart_view_sale_enhanced (Most Critical)
**Why second?** Core business logic, needed for testing

**Priority features:**
1. Quotation create date (REQ-00017)
2. Total discount (REQ-00025)
3. Internal reference (REQ-00021)
4. Standard quotation template (REQ-00023)

**Estimated time:** 2-3 weeks

---

#### 3️⃣ smart_view_crm_enhanced (Foundation for Projects)
**Why third?** Required for project creation workflow

**Priority features:**
1. Project location field (REQ-00037)
2. New stages (REQ-00038)
3. Approval workflow

**Estimated time:** 1-2 weeks

---

## 🔨 Development Workflow

### Daily Routine:

```bash
# 1. Update module in dev database
cd /home/sabry3/smart_view
# Note: User mentioned using PyCharm, so they'll update from there

# 2. Test in browser
# Open: http://localhost:8069

# 3. Check logs for errors
# tail -f /var/log/odoo/odoo.log

# 4. Commit changes
git add .
git commit -m "feat: implement REQ-00XXX - feature description"
git push
```

---

## 🧪 Testing Strategy

### Unit Tests (Optional but Recommended)

```python
# tests/__init__.py
from . import test_sale_order

# tests/test_sale_order.py
from odoo.tests import TransactionCase

class TestSaleOrder(TransactionCase):
    def setUp(self):
        super().setUp()
        self.SaleOrder = self.env['sale.order']
    
    def test_total_discount_calculation(self):
        # Your test here
        pass
```

### Manual Testing Checklist

For each feature:
- [ ] Field appears in form view
- [ ] Field appears in list view (if applicable)
- [ ] Field appears in report
- [ ] Field saves correctly
- [ ] Field computes correctly (if computed)
- [ ] Permissions work correctly

---

## 📊 Progress Tracking

### Module Completion Checklist

#### smart_view_company_branding
- [ ] Header image integrated
- [ ] Footer image integrated
- [ ] External layout created
- [ ] Tested on quotation
- [ ] Tested on invoice
- [ ] Tested on delivery order

#### smart_view_sale_enhanced
- [ ] REQ-00017: Quotation date ✓
- [ ] REQ-00019: Product name fix ✓
- [ ] REQ-00020: Prevent SO creation ✓
- [ ] REQ-00021: Internal reference ✓
- [ ] REQ-00022: Image resize ✓
- [ ] REQ-00023: Templates ✓
- [ ] REQ-00024: Line discount ✓
- [ ] REQ-00025: Total discount ✓
- [ ] REQ-00026: Pre-confirmation ✓
- [ ] REQ-00039: Technical template ✓

#### smart_view_crm_enhanced
- [ ] REQ-00037: Project location ✓
- [ ] REQ-00038: New stages ✓
- [ ] Approval wizard ✓
- [ ] Rejection wizard ✓
- [ ] SO blocking logic ✓

#### smart_view_project_sale
- [ ] REQ-00042: Create button ✓
- [ ] Stage validation ✓
- [ ] Project linking ✓

#### smart_view_project_enhanced
- [ ] REQ-00043: Stage templates ✓
- [ ] REQ-00043: Task templates ✓
- [ ] Auto-generation ✓

#### smart_view_whatsapp
- [ ] REQ-00027: API integration ✓
- [ ] Template messages ✓
- [ ] Send quotation ✓

#### smart_view_helpdesk
- [ ] REQ-00036: Activation ✓
- [ ] Menu visibility ✓

---

## 🐛 Common Issues & Solutions

### Issue 1: Module Not Appearing
**Solution:**
```bash
# Update apps list
# In Odoo: Apps > Update Apps List
```

### Issue 2: Import Errors
**Solution:**
- Check all `__init__.py` files exist
- Check import statements match file names
- Restart Odoo server

### Issue 3: View Not Updating
**Solution:**
```bash
# Upgrade module
odoo-bin -d your_db -u module_name --stop-after-init
```

### Issue 4: Permissions Error
**Solution:**
- Check `security/ir.model.access.csv` exists
- Ensure all models have access rights
- Log out and log back in

### Issue 5: Report Not Showing
**Solution:**
- Check XML syntax
- Check report is defined in manifest
- Clear browser cache
- Check report template inheritance

---

## 📚 Useful Resources

### Odoo Documentation
- [Odoo 19 Developer Docs](https://www.odoo.com/documentation/19.0/developer.html)
- [QWeb Reports](https://www.odoo.com/documentation/19.0/developer/reference/frontend/qweb.html)
- [ORM API](https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html)

### Code Examples
- [OCA Repositories](https://github.com/OCA) - Look for Odoo 19 branches
- [Odoo Core Modules](https://github.com/odoo/odoo/tree/19.0/addons)

### Tools
- [PyCharm Odoo Plugin](https://plugins.jetbrains.com/plugin/13499-odoo)
- [VSCode Odoo Extension](https://marketplace.visualstudio.com/items?itemName=jigar-patel.OdooSnippets)

---

## 💻 Git Workflow

### Branch Strategy

```bash
# Main branches
main           # Production-ready code
develop        # Integration branch

# Feature branches
feature/REQ-00017-quotation-date
feature/REQ-00023-multiple-templates
feature/REQ-00027-whatsapp

# Bugfix branches
bugfix/discount-calculation
```

### Commit Message Format

```
<type>(<scope>): <subject>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

Examples:
feat(sale): implement quotation create date (REQ-00017)
fix(crm): approval wizard validation logic
docs(readme): update installation instructions
```

---

## 🎯 Week 1 Action Plan

### Monday
- [ ] Review all documentation
- [ ] Set up Git repository
- [ ] Initialize module skeletons
- [ ] Create `smart_view_company_branding` module structure

### Tuesday
- [ ] Get header/footer from client
- [ ] Implement company branding module
- [ ] Test on sample quotation

### Wednesday
- [ ] Start `smart_view_sale_enhanced`
- [ ] Implement REQ-00017 (quotation date)
- [ ] Implement REQ-00021 (internal reference)

### Thursday
- [ ] Implement REQ-00024 (line discount)
- [ ] Implement REQ-00025 (total discount)
- [ ] Write unit tests

### Friday
- [ ] Testing and bug fixes
- [ ] Client demo
- [ ] Sprint retrospective
- [ ] Plan next week

---

## 📞 Need Help?

### Questions to Ask Client

1. **Header/Footer:**
   - Do you have the official company letterhead?
   - What size/format? (PDF, PNG, etc.)
   - Any specific brand guidelines?

2. **Quotation Templates:**
   - Can you provide sample quotations?
   - Which fields are mandatory?
   - Any specific formatting requirements?

3. **WhatsApp:**
   - Do you have WhatsApp Business account?
   - Do you have API access?
   - What messages should be automated?

4. **Project Stages:**
   - Are the 5 stages fixed or customizable?
   - Any specific stage rules?
   - Who can move between stages?

5. **Permissions:**
   - Who is "أ/ خالد"?
   - What exact permissions do they need?
   - Any other users to configure?

---

## 🎓 Best Practices

### Code Quality
- ✅ Follow PEP 8 (Python style guide)
- ✅ Use descriptive variable names
- ✅ Add docstrings to methods
- ✅ Keep methods under 50 lines
- ✅ Don't repeat yourself (DRY)

### Odoo Specific
- ✅ Prefer inheritance over monkey patching
- ✅ Use `_inherit` not `_name` when extending
- ✅ Always call `super()` in overridden methods
- ✅ Use `api.depends` for computed fields
- ✅ Use `api.constrains` for validation

### Security
- ✅ Always define access rights
- ✅ Use record rules when needed
- ✅ Validate user input
- ✅ Don't trust client-side data
- ✅ Log security-relevant actions

### Performance
- ✅ Avoid loops in compute methods
- ✅ Use `search_count()` instead of `len(search())`
- ✅ Use `read()` when you don't need ORM
- ✅ Add database indexes for searched fields
- ✅ Batch operations when possible

---

## ✅ Ready to Start?

Follow this checklist:

- [ ] I've read the MODULE_ARCHITECTURE_PLAN.md
- [ ] I've read the IMPLEMENTATION_ROADMAP.md
- [ ] I've read this QUICK_START_GUIDE.md
- [ ] I understand the module structure
- [ ] I have development environment ready
- [ ] I know which module to start with
- [ ] I have client contact for questions

**If all checked:** 🚀 **You're ready to code!**

**If not:** 📖 **Review the documentation again**

---

## 🎯 Your First Task

**Start Here:**

1. Create `smart_view_company_branding` module
2. Implement basic structure
3. Add placeholder header/footer
4. Test on quotation report

**Success Criteria:**
- Module installs without errors
- Header appears on quotation
- Footer appears on quotation

**Time Estimate:** 2-4 hours

**GO!** 🚀

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-19  
**Status:** Ready for Development

