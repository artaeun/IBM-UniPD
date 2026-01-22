# Link Check Summary - IBM-UniPD Repository

**Date:** 2026-01-22  
**Repository:** artaeun/IBM-UniPD  
**Branch:** copilot/check-wiki-links-consistency

## Overview

This document summarizes the comprehensive link consistency check performed on all markdown files in the repository.

## Scan Results

- **Total Markdown Files Scanned:** 63
- **Total Internal Links Checked:** 275
- **Broken Links Found:** 60 (initially)
- **Fixable Links:** 13 (links with incorrect paths but files exist)
- **Missing Files:** 47 (links to files that don't exist in repository)

## Actions Taken

### 1. Fixed Broken Links (13 files)

All links with incorrect paths have been corrected:

| File | Issues Fixed | Type of Fix |
|------|-------------|-------------|
| `Dati/Studio/III_Anno/BEM/README.md` | 2 links | Removed malformed `<>` syntax from absolute paths |
| `Dati/Studio/III_Anno/ESB/README.md` | 1 link | Removed malformed `<>` syntax from absolute path |
| `Dati/Studio/III_Anno/SGEIA/README.md` | 1 link | Removed malformed `<>` syntax from absolute path |
| `Dati/Studio/III_Anno/TSB/README.md` | 2 links | Removed malformed `<>` syntax from absolute paths |
| `Dati/Studio/II_Anno/EIP/README.md` | 5 links | Fixed case sensitivity (II_anno → II_Anno) |
| `Dati/Studio/II_Anno/FDE/README.md` | 1 link | Fixed typo (Materiale_0vario → Materiale_vario) |
| `Dati/Studio/I_Anno/AM1/README.md` | 1 link | Added missing .pdf extension |

### 2. Documented Missing Files

Created two comprehensive reports:

#### MISSING_FILES_REPORT.md
Detailed report organizing all 47 missing files by:
- Course/Topic
- Academic Year (I, II, III Anno)
- Folder location
- Referenced location and line number
- Credited contributors

#### MISSING_FILES_ISSUES.md
18 ready-to-use GitHub issue templates for tracking missing files, organized by course.

## Missing Files by Category

### Course Materials (Notes, Summaries)
- **Count:** 18 files
- **Courses Affected:** BEM, Biomeccanica, ESB, InfoMed, TSB, Biomateriali, F2, FDE, S&S, TDC, AM1, BFA, F1
- **Primary Contributors:** Davide Bosco, Matilde Franceschi, Matteo Grigolon, Andrea Fogale, Jun Hao Zhou, Arianna Zuanazzi, Mattia Campagnolo, Matteo Cuzzolin

### Exercise Materials & Solutions
- **Count:** 19 files/folders
- **Courses Affected:** FAMP (13 weekly quizzes), FDE (3 exercise solutions + 1 folder), EIP (1 folder)

### Lab Materials
- **Count:** 2 folders
- **Course:** EIP
- **Content:** Prof. Di Camillo and Prof. Ceccarello lab materials

### Exam Materials
- **Count:** 1 folder
- **Course:** DF (Dispositivi Fotonici)
- **Content:** Academic Year 2020/2021 exam papers

### Other Materials
- **Count:** 7 files
- **Includes:** STI presentation materials, self-assessment documents, reference materials (periodic table)

## Verification

After fixes:
- ✅ All 13 fixable links now resolve correctly
- ✅ 0 fixable links remaining
- ✅ 47 broken links properly documented with detailed context
- ✅ All changes reviewed and committed

## Next Steps for Repository Maintainers

1. **Create GitHub Issues**
   - Use the templates in `MISSING_FILES_ISSUES.md`
   - Create one issue per course/topic area
   - Assign appropriate labels (e.g., "missing-content", "help-wanted")

2. **Contact Contributors**
   - Reach out to credited individuals for each missing file
   - Priority contacts:
     - Matteo Grigolon (multiple courses, 13+ files)
     - Matilde Franceschi (multiple courses, 6+ files)
     - Davide Bosco (BEM, ESB, TDC)

3. **Add Files as Located**
   - Maintain the exact filenames referenced in the links
   - Preserve file extensions and formatting
   - Place files in the correct folders as documented

4. **Re-run Link Checker**
   - After adding files, run the link checker script again
   - Verify all links resolve correctly
   - Update documentation as needed

## Link Checker Script

A Python script was created to perform this analysis: `/tmp/check_links_v2.py`

The script:
- Scans all `.md` files recursively
- Extracts internal links (excluding external URLs, mailto:, tel:, etc.)
- Resolves relative and absolute paths
- Identifies files that exist elsewhere in the repo
- Generates detailed reports

To run again in the future:
```bash
python3 /tmp/check_links_v2.py
```

## Files Changed in This PR

1. `Dati/Studio/III_Anno/BEM/README.md` - Fixed 2 links
2. `Dati/Studio/III_Anno/ESB/README.md` - Fixed 1 link
3. `Dati/Studio/III_Anno/SGEIA/README.md` - Fixed 1 link
4. `Dati/Studio/III_Anno/TSB/README.md` - Fixed 2 links
5. `Dati/Studio/II_Anno/EIP/README.md` - Fixed 5 links
6. `Dati/Studio/II_Anno/FDE/README.md` - Fixed 1 link
7. `Dati/Studio/I_Anno/AM1/README.md` - Fixed 1 link
8. `MISSING_FILES_REPORT.md` - NEW: Comprehensive report
9. `MISSING_FILES_ISSUES.md` - NEW: Issue templates
10. `LINK_CHECK_SUMMARY.md` - NEW: This summary document

## Conclusion

✅ **Task Completed Successfully**

All broken links that could be fixed have been corrected. All missing files have been thoroughly documented with actionable next steps for repository maintainers. The repository now has a clear path forward to resolve all remaining broken links by locating and adding the missing files.

---

**Generated by:** GitHub Copilot  
**PR Branch:** copilot/check-wiki-links-consistency  
**Commits:** 4
