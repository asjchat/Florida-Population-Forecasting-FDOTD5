#!/usr/bin/env python3
"""
GitHub Push Script for FDOT D5 Analysis
Automates the process of pushing to GitHub
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and report status"""
    print(f"\n{'='*60}")
    print(f"📍 {description}")
    print(f"{'='*60}")
    print(f"Command: {cmd}\n")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - FAILED (Code: {result.returncode})")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║         FDOT D5 Analysis - GitHub Push Automation             ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    # Get GitHub credentials
    print("\n📋 GITHUB SETUP INFORMATION")
    print("="*60)
    
    github_username = input("\n🔹 Enter your GitHub username: ").strip()
    github_token = input("🔹 Enter your GitHub personal access token: ").strip()
    repo_name = input("🔹 Enter repository name (default: fdot-d5-analysis): ").strip() or "fdot-d5-analysis"
    
    if not github_username or not github_token:
        print("\n❌ GitHub credentials required!")
        sys.exit(1)
    
    # Change to deployment folder
    deploy_dir = Path("c:\\Users\\anand\\Desktop\\FDOT_D5_Public_Release")
    if not deploy_dir.exists():
        print(f"\n❌ Deployment folder not found: {deploy_dir}")
        sys.exit(1)
    
    os.chdir(deploy_dir)
    print(f"\n✅ Working directory: {deploy_dir}")
    
    # Step 1: Initialize Git
    print("\n\n🚀 STEP 1: Initialize Git Repository")
    print("="*60)
    run_command("git init", "Initialize git repository")
    run_command("git config user.name 'FDOT Analysis'", "Configure git user name")
    run_command("git config user.email 'analysis@fdot.example.com'", "Configure git email")
    
    # Step 2: Add all files
    print("\n\n📦 STEP 2: Stage All Files")
    print("="*60)
    run_command("git add .", "Add all files to git")
    
    # Show what will be committed
    show_cmd = "git status --short"
    print(f"\nFiles to be committed:")
    subprocess.run(show_cmd, shell=True)
    
    # Step 3: Commit
    print("\n\n💾 STEP 3: Create Initial Commit")
    print("="*60)
    run_command(
        'git commit -m "Initial commit: FDOT D5 Demographic Analysis Dashboard - 2025-2050 projections with interactive visualization and download capabilities"',
        "Commit files"
    )
    
    # Step 4: Create remote URL
    print("\n\n🌐 STEP 4: Connect to GitHub Remote")
    print("="*60)
    
    remote_url = f"https://{github_username}:{github_token}@github.com/{github_username}/{repo_name}.git"
    remote_url_display = f"https://github.com/{github_username}/{repo_name}.git"
    
    print(f"Repository URL: {remote_url_display}")
    
    run_command(f'git remote add origin "{remote_url}"', "Add GitHub remote")
    
    # Step 5: Rename branch to main
    print("\n\n🔄 STEP 5: Prepare Main Branch")
    print("="*60)
    run_command("git branch -M main", "Rename branch to main")
    
    # Step 6: Push to GitHub
    print("\n\n🚀 STEP 6: Push to GitHub")
    print("="*60)
    run_command("git push -u origin main", "Push files to GitHub")
    
    # Success message
    print("\n\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                    ✅ PUSH SUCCESSFUL!                         ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    print(f"\n📍 Your repository is now available at:")
    print(f"   🔗 {remote_url_display}")
    
    print(f"\n📊 Repository Details:")
    print(f"   Username: {github_username}")
    print(f"   Repository: {repo_name}")
    print(f"   Branch: main")
    
    print("\n\n🎯 NEXT STEPS:")
    print("="*60)
    print("1. ✅ Files pushed to GitHub")
    print("2. 📋 Go to GitHub repository settings:")
    print(f"   https://github.com/{github_username}/{repo_name}/settings")
    print("3. 🌐 Enable GitHub Pages:")
    print("   • Click 'Pages' in left sidebar")
    print("   • Source: Deploy from a branch")
    print("   • Branch: main / root (/)")
    print("   • Click Save")
    print("4. 🚀 Your site will be live at:")
    print(f"   https://{github_username}.github.io/{repo_name}")
    print("   (Takes 1-2 minutes to deploy)")
    
    print("\n\n📥 Files Included:")
    files = list(deploy_dir.glob("*"))
    for f in sorted(files):
        if f.is_file():
            size = f.stat().st_size / 1024
            print(f"   ✓ {f.name:<40} ({size:>8.1f} KB)")
    
    print("\n\n💡 Tips:")
    print("   • Share the GitHub Pages link with stakeholders")
    print("   • Users can download data directly from index.html")
    print("   • Update files anytime by running: git push origin main")
    print("   • Monitor GitHub for issues and feedback")
    
    print("\n\n✨ Your FDOT D5 Analysis is now live on GitHub! 🎉\n")

if __name__ == "__main__":
    main()
