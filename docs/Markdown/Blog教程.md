# 基于Mkdocs+mkdocs-material





- 博客框架：Mkdocs+mkdocs-material（theme）

由于有了官方文档，所以操作几乎不需要记录了。

只记录基本操作：



## mkdocs

### 1. 安装

```bash
pip install mkdocs-material
# or
docker pull squidfunk/mkdocs-material
```

## 2. 使用

```bash
mkdocs new .
# or
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
```

文件组成：

```
.
├─ docs/
│  └─ index.md
└─ mkdocs.yml
```

## 3. 预览

```
mkdocs serve
# or
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

## 4. 打包

```
mkdocs build
or
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build
```

## 5. 发布

方法一：打包后发布pages

方法二：使用Github Actions(CI工具)

- 在仓库根目录创建/workflows/ci.yml

- 粘贴配置信息：

  ```yaml
  name: ci 
  on:
    push:
      branches:
        - master 
        - main
  permissions:
    contents: write
  jobs:
    deploy:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Configure Git Credentials
          run: |
            git config user.name github-actions[bot]
            git config user.email 41898282+github-actions[bot]@users.noreply.github.com
        - uses: actions/setup-python@v5
          with:
            python-version: 3.x
        - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
        - uses: actions/cache@v4
          with:
            key: mkdocs-material-${{ env.cache_id }}
            path: .cache
            restore-keys: |
              mkdocs-material-
        - run: pip install mkdocs-material 
        - run: mkdocs gh-deploy --force
  ```

  

评论功能在gitee中暂不可用
