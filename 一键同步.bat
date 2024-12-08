@echo off
setlocal

:: 设置项目路径（如果需要的话）
:: cd /d "path\to\your\project"

:: 复制文件
copy "./docs/readme.md" "readme.md" /y

:: 构建MkDocs项目（假设mkdocs.yml在项目根目录下）
python -m mkdocs build

:: 添加所有更改到Git暂存区
git add .

:: 获取当前日期并格式化为YYYY-MM-DD
for /f "tokens=2 delims==" %%i in ('wmic os get localdatetime /value') do set datetime=%%i
set datetime=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%

:: 提交更改到Git仓库
git commit -m "update at %datetime%"

:: 推送到远程仓库的master分支
git push origin master

endlocal