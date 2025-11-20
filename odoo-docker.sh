#!/bin/bash

# Odoo 19 Docker Management Script
# Smart View Project

set -e

PROJECT_DIR="/home/sabry3/smart_view"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.yml"

cd "$PROJECT_DIR"

show_help() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Odoo 19 Docker Manager - Smart View"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Usage: ./odoo-docker.sh [command]"
    echo ""
    echo "Commands:"
    echo "  start       - Start Odoo & PostgreSQL"
    echo "  stop        - Stop services"
    echo "  restart     - Restart services"
    echo "  status      - Show service status"
    echo "  logs        - Show live logs"
    echo "  logs-odoo   - Show Odoo logs only"
    echo "  logs-db     - Show PostgreSQL logs only"
    echo "  shell       - Access Odoo shell"
    echo "  db-shell    - Access PostgreSQL shell"
    echo "  backup      - Backup database"
    echo "  clean       - Stop and remove containers (keeps data)"
    echo "  nuke        - ⚠️  Remove EVERYTHING including data"
    echo "  help        - Show this help"
    echo ""
    echo "Quick start:"
    echo "  ./odoo-docker.sh start"
    echo "  Open: http://localhost:8069"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

case "$1" in
    start)
        echo "🚀 Starting Odoo 19 & PostgreSQL..."
        docker-compose up -d
        echo "✅ Services started!"
        echo "📍 Odoo: http://localhost:8069"
        echo "📍 PostgreSQL: localhost:5433"
        echo ""
        echo "💡 View logs: ./odoo-docker.sh logs"
        ;;
    
    stop)
        echo "⏹️  Stopping services..."
        docker-compose stop
        echo "✅ Services stopped!"
        ;;
    
    restart)
        echo "🔄 Restarting services..."
        docker-compose restart
        echo "✅ Services restarted!"
        ;;
    
    status)
        echo "📊 Service Status:"
        echo ""
        docker-compose ps
        ;;
    
    logs)
        echo "📋 Showing live logs (Ctrl+C to exit)..."
        docker-compose logs -f
        ;;
    
    logs-odoo)
        echo "📋 Showing Odoo logs (Ctrl+C to exit)..."
        docker-compose logs -f web
        ;;
    
    logs-db)
        echo "📋 Showing PostgreSQL logs (Ctrl+C to exit)..."
        docker-compose logs -f db
        ;;
    
    shell)
        echo "🐚 Accessing Odoo shell..."
        docker exec -it odoo19_smartview bash
        ;;
    
    db-shell)
        echo "🐚 Accessing PostgreSQL shell..."
        docker exec -it postgres_smartview psql -U odoo
        ;;
    
    backup)
        BACKUP_FILE="backup_$(date +%Y%m%d_%H%M%S).sql"
        echo "💾 Creating database backup: $BACKUP_FILE"
        docker exec postgres_smartview pg_dumpall -U odoo > "$BACKUP_FILE"
        echo "✅ Backup created: $BACKUP_FILE"
        ;;
    
    clean)
        echo "🧹 Stopping and removing containers (data preserved)..."
        docker-compose down
        echo "✅ Containers removed! Data is safe."
        echo "💡 Start again with: ./odoo-docker.sh start"
        ;;
    
    nuke)
        echo "⚠️  WARNING: This will delete ALL data!"
        echo "Are you sure? Type 'yes' to confirm:"
        read -r confirmation
        if [ "$confirmation" = "yes" ]; then
            echo "💥 Removing everything..."
            docker-compose down -v
            echo "✅ Everything removed!"
            echo "💡 Start fresh with: ./odoo-docker.sh start"
        else
            echo "❌ Cancelled."
        fi
        ;;
    
    help|--help|-h|"")
        show_help
        ;;
    
    *)
        echo "❌ Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac

