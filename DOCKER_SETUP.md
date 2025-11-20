# 🐳 Odoo 19 Docker Setup - Smart View Project

## ✅ Clean, Pre-configured Odoo 19 with No SCSS Issues!

---

## 📋 Prerequisites

```bash
# Install Docker and Docker Compose
sudo apt update
sudo apt install docker.io docker-compose -y

# Add your user to docker group (logout/login after)
sudo usermod -aG docker $USER
```

---

## 🚀 Quick Start

### Step 1: Start Odoo & PostgreSQL

```bash
cd /home/sabry3/smart_view
docker-compose up -d
```

**Wait 30 seconds for startup...**

### Step 2: Access Odoo

**URL:** http://localhost:8069

**First-time Setup:**
1. Create database: `smartview_docker`
2. Email: `admin`
3. Password: `admin`
4. Language: English
5. Load demo data: No
6. Click "Create Database"

### Step 3: Install Smart View Modules

After database creation:
1. Go to **Apps** menu
2. Click **⋮** → **"Update Apps List"**
3. Search for `smart_view`
4. Install in this order:
   - smart_view_base
   - smart_view_company_branding
   - smart_view_helpdesk
   - smart_view_sale_enhanced
   - smart_view_crm_enhanced
   - smart_view_project_sale
   - smart_view_project_enhanced
   - pragtech_whatsapp_base
   - smart_view_whatsapp

---

## 📊 Docker Services

```
╔════════════════════════════════════════════════════════╗
║  Service      │  Container           │  Port          ║
╠════════════════════════════════════════════════════════╣
║  Odoo 19      │  odoo19_smartview    │  8069          ║
║  PostgreSQL   │  postgres_smartview  │  5433 (host)   ║
╚════════════════════════════════════════════════════════╝
```

---

## 🛠️ Useful Commands

### View Logs
```bash
# All services
docker-compose logs -f

# Only Odoo
docker-compose logs -f web

# Only PostgreSQL
docker-compose logs -f db
```

### Stop Services
```bash
docker-compose stop
```

### Start Services
```bash
docker-compose start
```

### Restart Services
```bash
docker-compose restart
```

### Stop and Remove Everything
```bash
docker-compose down
```

### Stop and Remove Including Data
```bash
# ⚠️ WARNING: This deletes all data!
docker-compose down -v
```

### Check Status
```bash
docker-compose ps
```

### Access Odoo Shell
```bash
docker exec -it odoo19_smartview bash
```

### Access PostgreSQL
```bash
docker exec -it postgres_smartview psql -U odoo
```

---

## 📁 Project Structure

```
/home/sabry3/smart_view/
├── docker-compose.yml          # Docker services configuration
├── config/
│   └── odoo.conf              # Odoo configuration
├── modules/                    # Your Smart View modules (auto-mounted)
│   ├── smart_view_base/
│   ├── smart_view_sale_enhanced/
│   ├── smart_view_crm_enhanced/
│   ├── smart_view_project_sale/
│   ├── smart_view_project_enhanced/
│   ├── smart_view_helpdesk/
│   ├── smart_view_company_branding/
│   └── smart_view_whatsapp/
└── DOCKER_SETUP.md            # This file
```

---

## 🎯 What Docker Provides

✅ **Clean Odoo 19 installation**  
✅ **Pre-compiled assets** (no SCSS errors!)  
✅ **PostgreSQL 15** (latest stable)  
✅ **All dependencies included**  
✅ **Development mode enabled** (--dev=all)  
✅ **Persistent data** (volumes for database & filestore)  
✅ **Auto-restart** on failure  
✅ **Isolated environment** (no conflicts)

---

## ⚙️ Configuration

### Environment Variables

Edit `docker-compose.yml` to change:

**Database:**
```yaml
environment:
  - POSTGRES_USER=odoo
  - POSTGRES_PASSWORD=odoo
  - POSTGRES_DB=postgres
```

**Odoo:**
```yaml
environment:
  - HOST=db
  - USER=odoo
  - PASSWORD=odoo
```

### Ports

Change ports in `docker-compose.yml`:

```yaml
ports:
  - "8069:8069"  # Change first number: "YOUR_PORT:8069"
```

Example for port 8130:
```yaml
ports:
  - "8130:8069"
```

---

## 🔧 Advanced Configuration

### Custom Odoo Config

Edit `config/odoo.conf`:

```ini
[options]
# Your custom settings
workers = 4
max_cron_threads = 2
```

Then restart:
```bash
docker-compose restart web
```

### Add More Modules

Just add modules to `/home/sabry3/smart_view/modules/` and they'll be available!

```bash
# Example: Add a new module
cp -r /path/to/new_module /home/sabry3/smart_view/modules/

# Restart to detect new modules
docker-compose restart web

# Update apps list in Odoo UI
```

---

## 🐛 Troubleshooting

### Port Already in Use

**Error:** `Bind for 0.0.0.0:8069 failed: port is already allocated`

**Solution 1:** Stop existing service
```bash
# Find what's using port 8069
sudo lsof -i :8069

# Kill it
sudo kill -9 <PID>

# Or stop your old Odoo
pkill -f odoo-bin
```

**Solution 2:** Change port in `docker-compose.yml`
```yaml
ports:
  - "8070:8069"  # Use 8070 instead
```

### Database Connection Error

**Error:** `could not connect to server`

**Solution:**
```bash
# Check if PostgreSQL is running
docker-compose ps

# View logs
docker-compose logs db

# Restart database
docker-compose restart db
```

### Modules Not Showing

**Solution:**
```bash
# Restart Odoo
docker-compose restart web

# In Odoo UI:
# Apps → ⋮ → Update Apps List
```

### Clear All Data and Start Fresh

```bash
# Stop and remove everything
docker-compose down -v

# Start fresh
docker-compose up -d
```

---

## 📈 Performance Tips

### Production Settings

For production, edit `config/odoo.conf`:

```ini
[options]
workers = 4                    # CPU cores * 2
max_cron_threads = 2
db_maxconn = 64
limit_memory_hard = 2684354560 # 2.5GB
limit_memory_soft = 2147483648 # 2GB
limit_time_cpu = 600
limit_time_real = 1200
```

### Database Backup

```bash
# Backup
docker exec postgres_smartview pg_dump -U odoo smartview_docker > backup.sql

# Restore
cat backup.sql | docker exec -i postgres_smartview psql -U odoo -d smartview_docker
```

---

## 🎉 Benefits Over Manual Installation

| Feature | Manual Install | Docker |
|---------|---------------|---------|
| Setup Time | ~2 hours | ~5 minutes |
| SCSS Errors | ❌ Common | ✅ Pre-fixed |
| Dependencies | Manual | ✅ Included |
| Isolation | ❌ System-wide | ✅ Contained |
| Portability | ❌ Complex | ✅ Easy |
| Reproducible | ❌ Hard | ✅ Simple |
| Clean Removal | ❌ Messy | ✅ One command |

---

## 🔗 Useful Links

- **Odoo Docker Hub:** https://hub.docker.com/_/odoo
- **Odoo Documentation:** https://www.odoo.com/documentation/19.0/
- **Docker Compose Docs:** https://docs.docker.com/compose/

---

## ✅ Quick Reference

```bash
# Start everything
docker-compose up -d

# Stop everything
docker-compose stop

# View logs
docker-compose logs -f web

# Restart Odoo
docker-compose restart web

# Access shell
docker exec -it odoo19_smartview bash

# Remove everything
docker-compose down -v
```

---

**🚀 Your Odoo 19 is now running at: http://localhost:8069**

**No more CSS errors! No more SCSS issues! Just working Odoo!** 🎉

