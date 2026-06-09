param(
    [Parameter(Mandatory = $true)]
    [string]$TargetProjectPath
)

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceFiles = @('AGENTS.md', 'SKILL.md')

if (-not (Test-Path -LiteralPath $TargetProjectPath)) {
    throw "Target project path does not exist: $TargetProjectPath"
}

foreach ($name in $sourceFiles) {
    $source = Join-Path $scriptRoot $name
    $destination = Join-Path $TargetProjectPath $name

    if (-not (Test-Path -LiteralPath $source)) {
        throw "Missing source file: $source"
    }

    Copy-Item -LiteralPath $source -Destination $destination -Force
    Write-Host "Copied $name -> $destination"
}
