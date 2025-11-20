# Smart View - Base Module

## Overview

Foundation module for Smart View customizations. Provides shared utilities, custom security groups, and enhanced user permission management.

## Version

- **Version:** 19.0.1.0.0
- **Odoo Version:** 19.0 Community
- **License:** LGPL-3

## Features

### REQ-00018: User Permissions Management

✅ **Enhanced Settings Access** including:

### 1. Custom Security Groups

Four specialized groups for Smart View:

**Settings Access**
- Full access to system settings
- Configuration management
- Advanced features
- For: Mr. Khaled and other key users

**Enhanced Administrator**
- Complete administrative privileges
- All Settings Access features
- System-wide permissions
- For: Super administrators

**Smart View Manager**
- Full access to Smart View modules
- Team management
- Configuration control
- For: Module managers

**Smart View User**
- Basic access to Smart View features
- Read and use functionality
- Limited configuration
- For: Regular users

### 2. User Management Enhancements

**Quick Actions:**
- **Grant Settings Access** button - One-click permission grant
- **Revoke Settings Access** button - One-click permission removal

**Additional Fields:**
- **Smart View Access Level** - Track user's access tier
- **Smart View Manager** indicator - Auto-computed flag
- **Smart View Notes** - Internal permission notes

**Enhanced User Form:**
- Dedicated "Smart View" tab
- Clear permission overview
- Group descriptions
- Easy management

### 3. User Interface Improvements

**User List View:**
- Smart View access level column
- Manager indicator
- Quick filtering

**User Form View:**
- Permission action buttons in header
- Dedicated Smart View tab
- Clear group descriptions
- Internal notes field

## Installation

### Prerequisites
- Odoo 19 Community Edition
- No special dependencies (only `base`, `web`)

### Install Steps

1. Copy module to Odoo addons directory
2. Update apps list
3. Search for "Smart View - Base"
4. Click Install

**Note:** Install this before other Smart View modules for optimal integration.

## Configuration

### 1. Grant Settings Access to Users

**Method 1: Quick Buttons**
1. Go to `Settings > Users > [User]`
2. Click "Grant Settings Access" button
3. User now has full settings access

**Method 2: Manual Group Assignment**
1. Go to `Settings > Users > [User]`
2. Go to "Access Rights" tab
3. Add user to "Settings Access" group
4. Save

### 2. Assign Smart View Roles

**For Managers:**
1. Open user
2. Access Rights tab
3. Add to "Smart View Manager" group

**For Regular Users:**
1. Open user
2. Access Rights tab
3. Add to "Smart View User" group

### 3. Set Access Levels

1. Open user
2. Go to "Smart View" tab
3. Set "Smart View Access Level":
   - None: No Smart View access
   - User: Basic features
   - Manager: Full module access
   - Administrator: Complete access
4. Add notes if needed

## Usage

### Granting Settings Access (REQ-00018)

**For Mr. Khaled or other key users:**

1. Navigate to `Settings > Users & Companies > Users`
2. Find and open the user (e.g., "Khaled")
3. Click **"Grant Settings Access"** button in header
4. Confirmation message appears
5. User now has full settings access

**Verification:**
- Check "Access Rights" tab
- "Settings Access" group should be listed
- User can access all settings menus

### Revoking Settings Access

1. Open user
2. Click **"Revoke Settings Access"** button
3. Confirm action
4. Settings access removed

### Managing Smart View Users

**View All Smart View Users:**
1. Go to `Settings > Users > Smart View Users` menu
2. See list of users with Smart View access
3. Filter by access level or manager status

### Using Smart View Tab

**In User Form:**
1. Open any user
2. Go to "Smart View" tab
3. View:
   - Current access level
   - Manager status
   - Group descriptions
4. Add internal notes as needed

## Permissions

### Settings Access Group
- ✓ Full access to Settings menu
- ✓ Configuration management
- ✓ Advanced features
- ✓ System parameters
- ✗ Does not include user management (unless admin)

### Enhanced Administrator
- ✓ All Settings Access privileges
- ✓ User management
- ✓ Complete system control
- ✓ All Smart View features

### Smart View Manager
- ✓ Access all Smart View modules
- ✓ Configure Smart View features
- ✓ Manage teams/data
- ✗ Limited system settings

### Smart View User
- ✓ Use Smart View features
- ✓ View own data
- ✗ No configuration access
- ✗ No management features

## Security Model

### Group Hierarchy

```
Enhanced Administrator
    ↓
Settings Access
    ↓
Smart View Manager
    ↓
Smart View User
    ↓
Basic User
```

### Access Rules

**Users see:**
- Own user record
- Team members (if applicable)

**Managers see:**
- All users in system
- Can edit permissions

**Administrators see:**
- Everything
- Full control

## Technical Details

### Models Extended

**res.users**
- Added `smart_view_access_level` field
- Added `smart_view_notes` field
- Added `is_smart_view_manager` computed field
- Added `grant_settings_access()` method
- Added `revoke_settings_access()` method

### Security Groups Created

1. `group_settings_access`
2. `group_enhanced_admin`
3. `group_smart_view_manager`
4. `group_smart_view_user`

### Methods

**grant_settings_access()**
- Adds "Settings Access" group to user
- Shows success notification
- REQ-00018 implementation

**revoke_settings_access()**
- Removes "Settings Access" group
- Shows warning notification
- Permission cleanup

**_compute_is_smart_view_manager()**
- Auto-computes manager status
- Based on group membership
- Updates in real-time

## Integration

### With Other Smart View Modules

This base module provides:
- Common security groups
- Shared utilities
- Consistent permissions

**Other modules can:**
- Inherit from base groups
- Use shared fields
- Reference base security

### Standalone Usage

Can be used independently for:
- Enhanced user management
- Settings access control
- Permission tracking

## Use Cases

### Use Case 1: Grant Settings to Key User

**Scenario:** Mr. Khaled needs full settings access

**Steps:**
1. Open Khaled's user record
2. Click "Grant Settings Access"
3. Done! Khaled can now access all settings

### Use Case 2: Track Permission Changes

**Scenario:** Document why user has special access

**Steps:**
1. Open user
2. Go to Smart View tab
3. Set access level
4. Add note: "Approved by manager on 2025-11-19"
5. Save

### Use Case 3: Audit Smart View Users

**Scenario:** See all users with Smart View access

**Steps:**
1. Go to Settings > Users > Smart View Users
2. View filtered list
3. Check access levels
4. Review and adjust as needed

## Best Practices

### Permission Management

1. **Least Privilege**: Start with minimum access
2. **Document Reasons**: Use notes field
3. **Regular Audits**: Review permissions monthly
4. **Remove Unused**: Revoke when no longer needed

### User Organization

1. **Assign Groups**: Use appropriate group for each user
2. **Set Access Levels**: Match user's role
3. **Add Notes**: Document special permissions
4. **Review Regularly**: Check and update

### Security

1. **Limit Settings Access**: Only grant when truly needed
2. **Use Manager Group**: For module administrators
3. **Track Changes**: Document in notes
4. **Audit Regularly**: Review permissions

## Troubleshooting

### Issue: Settings Menu Not Visible
**Solution:** User needs "Settings Access" group, not just "Smart View Manager"

### Issue: Button Not Working
**Solution:** Make sure user is saved (id exists)

### Issue: Group Not Appearing
**Solution:** Upgrade module: `-u smart_view_base`

### Issue: Permission Not Taking Effect
**Solution:** User needs to log out and log back in

## Customization

### Add Custom Groups

Create new groups inheriting from base groups:

```xml
<record id="group_custom" model="res.groups">
    <field name="name">Custom Group</field>
    <field name="implied_ids" eval="[(4, ref('smart_view_base.group_smart_view_user'))]"/>
</record>
```

### Add Custom Fields

Inherit res.users model:

```python
class ResUsers(models.Model):
    _inherit = 'res.users'
    
    custom_field = fields.Char('Custom Field')
```

## Roadmap

### Future Enhancements
- [ ] Permission templates
- [ ] Bulk permission assignment
- [ ] Permission approval workflow
- [ ] Access audit logs
- [ ] Permission expiration dates

## Credits

- **Development Team:** Smart View Development Team
- **Based on:** Odoo 19 Community
- **License:** LGPL-3

## Changelog

### Version 19.0.1.0.0 (2025-11-19)
- Initial release
- REQ-00018 implemented
- Custom security groups
- User permission management
- Enhanced user interface
- Ready for production

---

**Status:** ✅ Complete and Ready for Use

