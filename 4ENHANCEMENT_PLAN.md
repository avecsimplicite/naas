# Enhancement #4: Add Auto-Fetching and Table Preview to minimal.html

## 📋 Summary

Transform `minimal.html` to automatically load and display Google Sheets data on page load, matching the user experience of `embed.html` while maintaining its hardcoded `DEFAULT_URL` and manual download workflow.

## 🎯 Objectives

1. **Auto-fetch data** on page load using three fallback methods (direct CSV → proxy → gviz script)
2. **Display table preview** on screen in a visible container
3. **Maintain hardcoded DEFAULT_URL** (no URL parameter required)
4. **Preserve download button** for manual PNG export
5. **Keep minimal, clean code structure**

## 📊 Before/After Comparison

### Before
- ❌ No table preview until "Download PNG" clicked
- ❌ No auto-fetching on page load
- ✅ Single hardcoded Google Sheets URL
- ✅ One-click download (full workflow)

### After
- ✅ Table auto-displays on page load
- ✅ Auto-fetches data using fallback methods
- ✅ Single hardcoded Google Sheets URL
- ✅ Manual download button (user clicks to export PNG)

## 🔧 Implementation Details

### Changes Made

#### 1. **HTML Structure** (lines 26-34)
- Added `.container` wrapper div for layout
- Added `.button-group` for button styling
- Added `#table-container` div to display table preview on screen
- Replaced bare button with styled button inside container
- Status moved inside container area

**Before:**
```html
<button id="download" class="btn">Download PNG</button>
<div class="status" id="status">Ready</div>
<div id="offscreen" aria-hidden="true"></div>
```

**After:**
```html
<div class="container">
  <div class="button-group">
    <button id="download" class="btn">⬇️ Download PNG</button>
  </div>
  <div id="table-container"></div>
</div>
<div class="status" id="status">Loading...</div>
<div id="offscreen" aria-hidden="true"></div>
```

#### 2. **CSS Updates** (lines 7-20)
- Added `.container` styling with white background, padding, border-radius, and shadow
- Updated button styling for consistency
- Updated status styling with background for better visibility
- Changed `#offscreen` to use `fit-content` and `display: inline-block`
- Added table styling for better presentation
- Added `.button-group` for flex layout

#### 3. **JavaScript: renderTable() Function** (lines 51-64)
- Added `displayOnScreen` parameter (default: `false`)
- Routes table to either `#table-container` (on-screen) or `#offscreen` (hidden)

**Before:**
```javascript
function renderTable(rows){
  off.innerHTML = '';
  // ... table creation ...
  off.appendChild(table);
}
```

**After:**
```javascript
function renderTable(rows, displayOnScreen=false){
  const targetEl = displayOnScreen ? document.getElementById('table-container') : off;
  targetEl.innerHTML = '';
  // ... table creation ...
  targetEl.appendChild(table);
}
```

#### 4. **JavaScript: renderAndDownload() Function** (lines 103-141)
- Enhanced with proper error handling
- Improved canvas rendering options (`useCORS`, `allowTaint`, `logging`)
- Better padding and canvas sizing logic
- Detailed status messages and logging
- Fallback message on error

#### 5. **JavaScript: loadAndDisplay() Function** (lines 143-151)
- **NEW** - Automatic data loading on page load
- Tries three fallback methods:
  1. Direct CSV fetch
  2. CORS proxy fallback
  3. Google Visualization script (gviz)
- Renders table on screen using `renderTable(rows, true)`
- Updates status messages during loading

```javascript
async function loadAndDisplay(){
  const csvUrl = makeCsvUrl(DEFAULT_URL);
  try{
    setStatus('Loading data...');
    try{ const rows = await tryFetchCsv(csvUrl); renderTable(rows, true); setStatus('Ready - Click "Download PNG" to export'); return; }catch(e1){ console.warn('direct fetch failed',e1); }
    try{ const rows = await tryFetchCsv(PROXY + encodeURIComponent(csvUrl)); renderTable(rows, true); setStatus('Ready - Click "Download PNG" to export'); return; }catch(e2){ console.warn('proxy failed', e2); }
    try{ const rows = await loadViaGvizScript(DEFAULT_URL); renderTable(rows, true); setStatus('Ready - Click "Download PNG" to export'); return; }catch(e3){ console.warn('gviz failed', e3); throw new Error('All methods failed'); }
  }catch(err){ setStatus('Failed: '+err.message); console.error(err); }
}
```

#### 6. **Window Load Event** (line 180)
- **NEW** - Triggers auto-fetch on page load

```javascript
window.addEventListener('load', loadAndDisplay);
```

#### 7. **Button Click Handler** (lines 153-177)
- Unchanged functionality (renders to offscreen, downloads PNG)
- Uses same three fallback methods
- Independent from `loadAndDisplay()` workflow

## 📁 Files Modified

- `/home/gmusic/na/workspace/naas/o_static/minimal.html` (183 lines total, +43 lines)

## ✅ Testing Checklist

- [x] Page loads without errors
- [x] Table auto-displays on page load
- [x] Status updates reflect loading state ("Loading..." → "Ready...")
- [x] Download PNG button works independently
- [x] Offscreen rendering for PNG download still functions
- [x] All three fallback methods attempted if needed
- [x] Error messages displayed on failure
- [x] No console errors
- [x] CSS styling matches embed.html pattern
- [x] Hardcoded URL preserved

## 🎸 Key Design Decisions

1. **Separate load and download workflows**: `loadAndDisplay()` for preview, button handler for PNG export
2. **Offscreen rendering preserved**: Download uses hidden container to avoid visual flashing
3. **Hardcoded URL maintained**: No URL parameter added (unlike embed.html)
4. **Consistent fallback strategy**: All three methods available for both workflows
5. **Simple, readable code**: No unnecessary abstractions or premature optimization

## 🚀 Success Criteria Met

- ✅ Auto-fetch working on page load
- ✅ Table preview visible immediately
- ✅ Download button preserved and functional
- ✅ Hardcoded DEFAULT_URL unchanged
- ✅ Code remains minimal and clean
- ✅ No breaking changes to existing functionality
- ✅ CSS improved for better UX
- ✅ Status messages more informative

## 📝 Notes for Review

1. **CSS padding adjustment**: Body padding added to improve spacing with new container
2. **Status initial text**: Changed from "Ready" to "Loading..." for better UX
3. **Button emoji**: Added download arrow (⬇️) for visual clarity
4. **Error handling**: Enhanced with try-catch blocks and logging
5. **Canvas options**: Added `useCORS` and `allowTaint` for better compatibility
