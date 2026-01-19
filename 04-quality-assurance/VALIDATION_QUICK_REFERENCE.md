# Quick Reference: API & UI Validation

## 🎯 Golden Rule
**Every feature MUST pass both API validation AND UI validation before being marked as complete.**

---

## ✅ Validation Checklist (For All Features)

### Backend Developer
- [ ] API endpoint implemented
- [ ] Tested with Postman/curl
- [ ] All test cases pass
- [ ] Error handling works
- [ ] Postman collection created
- [ ] Handed off to QA

### Frontend Developer  
- [ ] UI component implemented
- [ ] All UI states work (empty, loading, success, error)
- [ ] Screenshots captured
- [ ] Responsive design tested
- [ ] Handed off to QA

### QA Engineer
- [ ] API tests pass (Postman)
- [ ] UI tests pass (manual)
- [ ] E2E flow works
- [ ] Bugs documented
- [ ] Feature marked complete

---

## 📋 Required Deliverables

### For API Validation
1. **Postman Collection** - All endpoints with test cases
2. **Test Results** - Screenshots of passing tests
3. **Error Scenarios** - Tested 400, 404, 500 responses

### For UI Validation
1. **Screenshots** - All UI states (typically 5-7 per feature)
2. **Test Report** - Manual testing checklist completed
3. **Responsive Test** - Works on desktop and mobile

### For E2E Validation
1. **Flow Documentation** - Step-by-step test execution
2. **Data Verification** - MongoDB data checked
3. **Performance Check** - Response times acceptable

---

## 🔍 Where to Find Details

| Need | Document | Section |
|------|----------|---------|
| **Task assignments** | TEAM_TASK_BREAKDOWN.md | Member sections |
| **Validation details** | API_UI_VALIDATION_MATRIX.md | Feature sections |
| **Validation workflow** | VALIDATION_STRATEGY.md | Workflow diagram |
| **Definition of Done** | TEAM_TASK_BREAKDOWN.md | Bottom of doc |

---

## 🚦 Validation Status Tracking

Use these labels in GitHub Issues/Projects:

- 🟡 **API: In Progress** - Backend dev working
- 🟢 **API: Validated** - QA approved API
- 🟡 **UI: In Progress** - Frontend dev working  
- 🟢 **UI: Validated** - QA approved UI
- 🟢 **E2E: Validated** - Complete flow works
- ✅ **Feature Complete** - All validations pass

---

## 📞 Who to Contact

| Question About | Contact |
|----------------|---------|
| API validation requirements | Member 9 (QA) |
| UI validation requirements | Member 9 (QA) |
| API implementation issues | Member 1 (Tech Lead) |
| UI implementation issues | Member 5 (Frontend Lead) |
| Integration issues | Member 1 (Tech Lead) |

---

## ⏱️ Validation Timeline

- **Week 3**: Ingestion feature
- **Week 4**: Search feature
- **Week 5**: Chat feature
- **Week 6**: Viability, Arguments, Clauses
- **Week 7**: Full regression

---

## 🛠️ Tools Setup

### Required Tools
1. **Postman** - Download from postman.com
2. **MongoDB Compass** - Download from mongodb.com
3. **Browser DevTools** - Built-in (F12)

### Optional Tools
1. **Playwright** - For E2E automation
2. **Newman** - For CI/CD API tests

---

## 📸 Screenshot Requirements

### Minimum Screenshots Per Feature
- Empty/initial state
- Loading state
- Success state
- Error state
- (Feature-specific states)

### Screenshot Naming Convention
```
feature_component_state.png

Examples:
- ingestion_upload_empty.png
- ingestion_upload_progress.png
- ingestion_upload_success.png
- search_results_loaded.png
- chat_message_sent.png
```

---

## 🐛 Bug Reporting

When validation fails:
1. Create GitHub issue
2. Use bug report template
3. Tag: `bug`, `validation-failed`
4. Assign to: Backend or Frontend dev
5. Link to: Validation matrix section

---

## 💡 Pro Tips

✅ **Start validation early** - Don't wait until the end

✅ **Test edge cases** - Empty inputs, large files, special characters

✅ **Document everything** - Screenshots, test results, bugs

✅ **Communicate blockers** - Don't wait for standup

✅ **Retest after fixes** - Ensure bugs are actually resolved

---

## 📊 Success Metrics

| Metric | Target |
|--------|--------|
| API Response Time | < 500ms (p95) |
| UI Load Time | < 2s |
| Test Coverage | > 80% |
| Bugs per Feature | < 5 |
| Validation Pass Rate | > 95% |

---

*Keep this reference handy throughout development. When in doubt, check the detailed validation matrix!*
