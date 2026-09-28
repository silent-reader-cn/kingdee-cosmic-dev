# 知识库-gai_repo_info

## 知识库-多语言表 t_gai_repo_info_l

- **表名称：** 知识库-多语言表
- **表名：** t_gai_repo_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_info_l |  | fpkid |
| 2 | idx_t_gai_repo_info_l |  | fid |

---

## 文档管理-子表 t_gai_repo_doc_manage

- **表名称：** 文档管理-子表
- **表名：** t_gai_repo_doc_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilestatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: A :已上传 B :处理中(chunk) C :已完成 D :失败(chunk) E :暂存 F :处理中(embedding) G :失败(embedding) H :文档删除异常 |
| 3 | ffilesource | 文件来源 | varchar | 50 |  |  | ' ' | 文件来源,枚举: doc :文档型 html :社区HTML code :代码生成 |
| 4 | ffiletype | 文件类型 | varchar | 10 |  |  | ' ' | 文件类型 |
| 5 | fhitnum | 命中次数 | int8 | 64 |  | √ | 0 | 命中次数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fprogress | 进度 | numeric | 23 | 10 | √ | 0 | 进度 |
| 8 | flog | 日志 | varchar | 2000 |  |  | ' ' | 日志 |
| 9 | ftitle | 链接标题 | varchar | 500 |  |  | ' ' | 链接标题 |
| 10 | fcreatedate | 上传时间 | timestamp | 0 |  |  | null | 上传时间 |
| 11 | fstringnum | 字符数 | int8 | 64 |  | √ | 0 | 字符数 |
| 12 | ffilename | 文件名 | varchar | 500 |  |  | ' ' | 文件名 |
| 13 | ffilesize | 文件大小(KB) | int8 | 64 |  | √ | 0 | 文件大小(KB) |
| 14 | furl | HTML地址 | varchar | 500 |  |  | ' ' | HTML地址 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffilepath | 持久化文件 | varchar | 500 |  |  | ' ' | 持久化文件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_doc_manage |  | fentryid |
| 2 | idx_t_gai_repo_doc_manage |  | fid,ffilestatus |

---

## 知识库-主表 t_gai_repo_info

- **表名称：** 知识库-主表
- **表名：** t_gai_repo_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fchunkstrategy | 分块策略 | varchar | 50 |  | √ | 'base' | 分块策略,枚举: base :基础分块 identifier :标识符分块 customize :自定义分块 |
| 4 | fidentifiertype | 标识符按钮组 | varchar | 50 |  |  | null | 标识符按钮组,枚举: 1 :预置标识符 2 :自定义标识符 |
| 5 | fsource | 创建来源 | varchar | 50 |  | √ | 'dev' | 创建来源,枚举: dev :GPT开发平台 ms :微服务 |
| 6 | fcustomidentifier |  | varchar | 20 |  |  | null |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: A :新建 B :运行中 C :可用 D :失败 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ffiletotal | 文件总数 | int8 | 64 |  | √ | 0 | 文件总数 |
| 12 | fmetrictype | 向量计算类型 | varchar | 50 |  | √ | 'l2' | 向量计算类型,枚举: l2 :欧基里距离（L2） cosine :余弦相似度（COSINE） |
| 13 | fdeleteurl | 删除URL、电子邮件地址 | bpchar | 1 |  |  | '0' | 删除URL、电子邮件地址 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fchunklengthlimit | 分块最大长度 | int8 | 64 |  | √ | 50 | 分块最大长度 |
| 18 | findexmethod | 向量模型 | varchar | 50 |  |  | ' ' | 向量模型,枚举: |
| 19 | fisfulltext | 开启全文索引 | varchar | 50 |  | √ | '0' | 开启全文索引 |
| 20 | freplacesymbol | 替换连续空格、换行、制表符 | bpchar | 1 |  |  | '1' | 替换连续空格、换行、制表符 |
| 21 | ftype | 知识库类型 | varchar | 200 |  |  | 'qa' | 知识库类型,枚举: qa :文档问答 kd_code_gen :代码生成 |
| 22 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |
| 24 | fdesc | 说明 | varchar | 50 |  |  | ' ' | 说明 |
| 25 | fstringtotalnum | 字符总数 | int8 | 64 |  | √ | 0 | 字符总数 |
| 26 | fpresetidentifier |  | varchar | 50 |  |  | null | ,枚举: lineBreak :换行 lineBreak_double :双换行 lineBreak_triple :三换行 zh_period :中文句号 zh_qmark :中文问号 zh_emark :中文叹号 zh_comma :中文逗号 zh_semicolon :中文分号 en_period :英文句号 en_qmark :英文问号 en_emark :英文叹号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_repo_info |  | fnumber,fname |
| 2 | pk_t_gai_repo_info |  | fid |
