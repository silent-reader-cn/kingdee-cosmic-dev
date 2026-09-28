# 报告撰写-dfa_frfreport

## 报告撰写-主表 t_dfa_frfreport

- **表名称：** 报告撰写-主表
- **表名：** t_dfa_frfreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdownloadurlext | 可下载的文档地址ext | varchar | 512 |  | √ | '{}' | 可下载的文档地址ext |
| 3 | fanalysisscene | 分析场景 | varchar | 20 |  | √ | ' ' | 分析场景,枚举: |
| 4 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fanalysisframemd | 分析框架markdown内容 | varchar | 255 |  | √ | ' ' | 分析框架markdown内容 |
| 6 | fdefaultparamext | 默认参数拓展 | varchar | 2000 |  | √ | '{}' | 默认参数拓展 |
| 7 | fmultilangext_tag | 多语言默认拓展字段_详情 | text | 0 |  |  | null | 多语言默认拓展字段_详情 |
| 8 | freportid | 报告id | int8 | 64 |  | √ | 0 | 报告id |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fchatsessionid | 关联会话id | varchar | 255 |  | √ | ' ' | 关联会话id |
| 11 | fmdurl | markdown文档地址 | varchar | 100 |  | √ | ' ' | markdown文档地址 |
| 12 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态 |
| 13 | ffilepaths_tag | 上传文件地址_详情 | text | 0 |  |  | null | 上传文件地址_详情 |
| 14 | ffilename | 文档名称 | varchar | 100 |  | √ | ' ' | 文档名称 |
| 15 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | ffilepaths | 上传文件地址 | varchar | 255 |  | √ | ' ' | 上传文件地址 |
| 17 | fanalysisframemd_tag | 分析框架markdown内容_详情 | text | 0 |  |  | null | 分析框架markdown内容_详情 |
| 18 | fhtmlurl | 互动网页地址 | varchar | 255 |  | √ | ' ' | 互动网页地址 |
| 19 | fmultilangext | 多语言默认拓展字段 | varchar | 255 |  | √ | ' ' | 多语言默认拓展字段 |
| 20 | fversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_frfreportid |  | freportid |
| 2 | pk_dfa_frfreport |  | fid |

---

## 报告撰写-多语言表 t_dfa_frfreport_l

- **表名称：** 报告撰写-多语言表
- **表名：** t_dfa_frfreport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilename | 文档名称 | varchar | 255 |  | √ | ' ' | 文档名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_frfreport_l_0 |  | fid,flocaleid |
| 2 | pk_dfa_frfreport_l |  | fpkid |
