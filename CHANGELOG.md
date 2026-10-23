# Changelog

## 0.3.3

### ✨ Added


### 🐛 Fixed

- Fixed typing for `create_issue`
- Fixed change in Gitea-Api for teams generation (curretnly limits to newes version of gitea) where "units" were renamed

### 🧹 Internal / Maintenance




## 0.3.3

### ✨ Added

- Added changelog \o/
- First attempt to add branch protections using `repo.create_branch_protection` and `repo.get_branch_protections`

### 🧹 Internal / Maintenance

- Added typing annotations to disable field population tests that cannot be supported in older versions on some API objects
- Removed testing support for gitea 1.23

## 0.3.2

### 🐛 Fixed

- Requrests ignoring disabled certificate validation (#51)
- Just wrong typing parameters in `Commit`-class


