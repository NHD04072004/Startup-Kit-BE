# Docker Management Script for Windows PowerShell

function Show-Help {
    Write-Host "Available commands:" -ForegroundColor Green
    Write-Host "  .\docker.ps1 build        - Build Docker images"
    Write-Host "  .\docker.ps1 up           - Start containers in development mode"
    Write-Host "  .\docker.ps1 up-prod      - Start containers in production mode"
    Write-Host "  .\docker.ps1 down         - Stop and remove containers"
    Write-Host "  .\docker.ps1 logs         - View container logs"
    Write-Host "  .\docker.ps1 shell        - Access app container shell"
    Write-Host "  .\docker.ps1 db-shell     - Access database shell"
    Write-Host "  .\docker.ps1 migrate      - Run database migrations"
    Write-Host "  .\docker.ps1 migration    - Create new migration"
    Write-Host "  .\docker.ps1 test         - Run tests"
    Write-Host "  .\docker.ps1 clean        - Remove all containers, volumes, and images"
    Write-Host "  .\docker.ps1 help         - Show this help message"
}

function Build-Images {
    Write-Host "Building Docker images..." -ForegroundColor Cyan
    docker-compose build
}

function Start-Dev {
    Write-Host "Starting containers in development mode..." -ForegroundColor Cyan
    docker-compose up -d
    Write-Host "Application started at http://localhost:8000" -ForegroundColor Green
}

function Start-Prod {
    Write-Host "Starting containers in production mode..." -ForegroundColor Cyan
    docker-compose -f docker-compose.prod.yml up -d
    Write-Host "Application started in production mode" -ForegroundColor Green
}

function Stop-Containers {
    Write-Host "Stopping containers..." -ForegroundColor Cyan
    docker-compose down
}

function Show-Logs {
    Write-Host "Showing container logs (Ctrl+C to exit)..." -ForegroundColor Cyan
    docker-compose logs -f
}

function Enter-Shell {
    Write-Host "Accessing app container shell..." -ForegroundColor Cyan
    docker-compose exec app /bin/bash
}

function Enter-DbShell {
    Write-Host "Accessing database shell..." -ForegroundColor Cyan
    docker-compose exec db mysql -u root -p
}

function Run-Migrate {
    Write-Host "Running database migrations..." -ForegroundColor Cyan
    docker-compose exec app alembic upgrade head
}

function Create-Migration {
    $message = Read-Host "Enter migration message"
    Write-Host "Creating new migration..." -ForegroundColor Cyan
    docker-compose exec app alembic revision --autogenerate -m "$message"
}

function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Cyan
    docker-compose exec app pytest
}

function Clean-All {
    Write-Host "WARNING: This will remove all containers, volumes, and images!" -ForegroundColor Yellow
    $confirm = Read-Host "Are you sure? (yes/no)"
    if ($confirm -eq "yes") {
        Write-Host "Cleaning up..." -ForegroundColor Cyan
        docker-compose down -v
        docker system prune -af
        Write-Host "Cleanup completed!" -ForegroundColor Green
    } else {
        Write-Host "Cleanup cancelled." -ForegroundColor Yellow
    }
}

# Main script logic
param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

switch ($Command.ToLower()) {
    "build"     { Build-Images }
    "up"        { Start-Dev }
    "up-prod"   { Start-Prod }
    "down"      { Stop-Containers }
    "logs"      { Show-Logs }
    "shell"     { Enter-Shell }
    "db-shell"  { Enter-DbShell }
    "migrate"   { Run-Migrate }
    "migration" { Create-Migration }
    "test"      { Run-Tests }
    "clean"     { Clean-All }
    "help"      { Show-Help }
    default     { 
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Show-Help 
    }
}
