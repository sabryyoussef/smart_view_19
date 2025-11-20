# 📱 Smart View WhatsApp - Quick Reference

## 🚀 Quick Start (1 Minute)
```
1. Customer has mobile: +20 1234567890
2. SO → Click "Send via WhatsApp"
3. Select template, attach PDF
4. Send! Customer receives instantly ✅
```

## ⚠️ Installation Note

**Requires:** `pragtech_whatsapp_base` module  
**Status:** `installable: False` until pragtech installed  
**Setup Time:** 30 minutes (one-time)

## 🎯 Features (REQ-00027)

| Task | Feature | Benefit |
|------|---------|---------|
| 27 | WhatsApp API | Via pragtech |
| 28 | Templates | Dynamic messages |
| 29 | Auto-notify | SO/Project/Payment |

## 📍 Send Methods

**Manual:** SO → "Send via WhatsApp" button  
**Auto:** Settings → Enable notifications

## 📋 Templates

- `quotation_template`: Send quotes
- `so_confirmation`: Order confirmed
- `project_created`: Project started
- `payment_received`: Payment confirmed

## 📱 Phone Format

**Valid:** +20 1234567890  
**Minimum:** 8 digits  
**International:** Supported

## 🔄 Complete Flow

```
Create SO → Add Customer Mobile
→ Click "Send via WhatsApp"
→ Select Template + Attach PDF
→ Send → Customer Receives! ✅
```

## 🏢 Providers

**Meta (Official):**
- ✅ Verified badge
- ❌ Template approval needed

**1msg/Gupshup:**
- ✅ Quick setup
- ❌ Not official

## ⚡ Auto-Notifications

```
SO Confirmed → WhatsApp: "Order confirmed!" ✅
Project Created → WhatsApp: "Project started!" ✅
Payment Received → WhatsApp: "Payment received!" ✅
```

## 🔧 Troubleshooting

**No instance:** Configure pragtech first  
**Template error:** Create/approve template  
**Invalid mobile:** Format +20 1234567890  
**Not received:** Check customer number

## 📊 Integration

```
smart_view_whatsapp (Business Logic)
    ↓ uses
pragtech_whatsapp_base (API Infrastructure)
    ↓ connects to
Meta / 1msg / Gupshup (Provider)
    ↓ delivers to
Customer WhatsApp ✅
```

## ✅ Benefits

- ⚡ Instant delivery
- 📱 High open rate
- 📄 PDF attachments
- 🤖 Automation
- 📊 Tracking

**Module Version:** 19.0.1.0.0  
**Status:** ✅ Complete (needs pragtech)

📱 **Engage customers via their favorite app!**

