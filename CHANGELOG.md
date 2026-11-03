# Changelog

## 1.0.1

### ✨ Added

- Adding comments to issues

### 🐛 Fixed

- Fixed crash when comment api returned empty authors

## 1.0.0

### 🔥 [BREAKING] 🔥

- finally commited to semantic versioning ;)
- changes in Team api may break compatibilty with older versions of gitea (see 2ba3378a)

### 🐛 Fixed

- Fixed typing for `create_issue`
- Fixed change in Gitea-Api for teams generation (curretnly limits to newes version of gitea) where "units" were renamed

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


