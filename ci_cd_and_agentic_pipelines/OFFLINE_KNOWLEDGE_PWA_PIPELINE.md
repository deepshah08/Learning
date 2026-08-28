# 📚 Offline Knowledge Center PWA & Scraping Pipeline

> **Context**: Single Source of Truth for the Offline Knowledge Center Progressive Web App (PWA), scraper engine, SPA router link rewriting, and GitHub Pages deployment.  
> **Repository**: [`deepshah08/antigravity_projects`](https://github.com/deepshah08/antigravity_projects)  
> **Live URL**: [https://deepshah08.github.io/antigravity_projects/](https://deepshah08.github.io/antigravity_projects/)  
> **Status**: 🟢 **Production (19,000+ Precached Offline Assets)**

---

## 1. Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               OFFLINE KNOWLEDGE CENTER ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                 │
│   ┌─────────────────────┐       Extracted Data       ┌─────────────────────────┐                │
│   │   Scraper Engine    │ ─────────────────────────> │   13,400+ Articles      │                │
│   │   (download.ts)     │   (Sanitized Hyperlinks)   │   (Public JSON Storage) │                │
│   └─────────────────────┘                            └───────────┬─────────────┘                │
│                                                                  │                              │
│                                                                  │ Ingestion                    │
│                                                                  ▼                              │
│   ┌─────────────────────┐      Offline Precache      ┌─────────────────────────┐                │
│   │ Service Worker (SW) │ <───────────────────────── │   React 19 + Vite PWA   │                │
│   │  (workbox-window)   │    (19,086 Cache Entries)  │      SPA Frontend       │                │
│   └─────────────────────┘                            └───────────┬─────────────┘                │
│                                                                  │                              │
│                                                                  │ GitHub Actions Deploy        │
│                                                                  ▼                              │
│                                                      ┌─────────────────────────┐                │
│                                                      │      GitHub Pages       │                │
│                                                      │  (Cloud Automated CI)   │                │
│                                                      └─────────────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Solved Issues & Technical Learnings

### A. SPA Hash Routing & `target="_blank"` Tab Popping Bug
- **Issue**: Clicking internal cross-references within scraped articles (e.g. `linux-001` $\rightarrow$ `devops-117`) opened an unwanted new browser tab pointing to an external site rather than navigating smoothly within the SPA hash router (`#/article/...`).
- **Root Cause**: The raw HTML extracted from external sites contained `target="_blank"` and `rel="noopener noreferrer"`. Even when the `href` was rewritten to `#/article/...`, browsers prioritized the `target="_blank"` attribute.
- **Two-Tier Fix**:
  1. **Scraper Extraction Level (`scraper/download.ts`)**:
     ```typescript
     a.setAttribute('href', `#/article/${topic.id}/${subDocId}`);
     a.removeAttribute('target');
     a.removeAttribute('rel');
     ```
  2. **Frontend Render Level (`offline-knowledge-center/src/App.tsx`)**:
     ```typescript
     const sanitizedHtml = article.contentHtml.replace(
       /<a\s+(?:[^>]*?\s+)?href=["'](#\/article\/[^"']+)["'][^>]*>/gi,
       '<a href="$1">'
     );
     ```

### B. Title Formatting Cleanliness
- **Issue**: Scraped article headers included trailing branding (e.g. `"Debian Linux - GeeksforGeeks"`).
- **Fix**: Added title cleaning in `App.tsx`:
  ```typescript
  const cleanTitle = (title: string) => title.replace(/\s*-\s*GeeksforGeeks$/i, '').trim();
  ```

### C. PWA Cache Invalidation Protocol
- Because Vite PWA precaches 19,000+ files (~700 MB), changes deployed to GitHub Pages will serve cached JSON in client browsers until a service worker update cycle completes or the user triggers a hard refresh (`Cmd + Shift + R`).

---

## 3. GitHub Actions CI/CD Deployment (`deploy.yml`)

The deployment workflow includes:
1. **Pull Request Trigger**: Executes `npm ci` and `npm run build` on all PRs to catch build and TypeScript errors before merge.
2. **Weekly Cron Schedule**: Scrapes newly updated articles and auto-commits data.
3. **Artifact Deployment**: Packages `dist/` and deploys to GitHub Pages environment.
