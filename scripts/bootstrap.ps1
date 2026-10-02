[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$secretDir = Join-Path $projectRoot 'secrets'
$envFile = Join-Path $projectRoot '.env'

if (-not (Test-Path -LiteralPath $secretDir)) {
    New-Item -ItemType Directory -Path $secretDir | Out-Null
}

function New-StrongSecret {
    param([int]$Length = 32)
    $bytes = New-Object byte[] $Length
    $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    try {
        $rng.GetBytes($bytes)
    }
    finally {
        $rng.Dispose()
    }
    return [Convert]::ToBase64String($bytes).Replace('+', 'A').Replace('/', 'B').Replace('=', 'C')
}

$secretFiles = @(
    'mysql_root_password',
    'mysql_wordpress_password',
    'mysql_exporter_password',
    'wp_admin_password',
    'grafana_admin_password'
)

foreach ($name in $secretFiles) {
    $path = Join-Path $secretDir $name
    if (-not (Test-Path -LiteralPath $path)) {
        [System.IO.File]::WriteAllText($path, (New-StrongSecret), (New-Object System.Text.UTF8Encoding($false)))
    }
}

$exporterPassword = [System.IO.File]::ReadAllText((Join-Path $secretDir 'mysql_exporter_password')).Trim()
$exporterConfig = "[client]`nuser=exporter`npassword=$exporterPassword`nhost=mysql`nport=3306`n"
[System.IO.File]::WriteAllText((Join-Path $secretDir 'mysql_exporter.cnf'), $exporterConfig, (New-Object System.Text.UTF8Encoding($false)))

if (-not (Test-Path -LiteralPath $envFile)) {
    Copy-Item -LiteralPath (Join-Path $projectRoot '.env.example') -Destination $envFile
}

Write-Host 'Da tao .env va cac tep secret cuc bo (khong duoc Git theo doi).'
Write-Host 'Hay doi WP_ADMIN_EMAIL trong .env truoc khi nop bai neu can.'

