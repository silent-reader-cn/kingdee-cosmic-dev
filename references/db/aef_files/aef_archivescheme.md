# 归档方案-aef_archivescheme

## 归档方案-主表 t_aef_archivescheme

- **表名称：** 归档方案-主表
- **表名：** t_aef_archivescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 归档分组 | int8 | 64 |  | √ | 0 | [归档分组 aef_archivegroup](../aef_files/aef_archivegroup.md) |
| 5 | fisxbrlpilot | 电子凭证 | bpchar | 1 |  | √ | '0' | 电子凭证 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmularchiveformat | 归档格式 | varchar | 50 |  | √ | ' ' | 归档格式,枚举: PDF :PDF EXCEL :Excel |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | farchivetype | 归档类型 | varchar | 30 |  | √ | ' ' | 归档类型,枚举: finance :财务 bill :单据 reportform :报表 tax :税务 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aef_archivescheme_createorg |  | fcreateorgid |
| 2 | idx_aef_archivescheme |  | fnumber |
| 3 | idx_t_aef_archivescheme_master |  | fmasterid |
| 4 | t_aef_archivescheme_pkey |  | fid |

---

## 归档方案-使用范围表 t_aef_archivescheme_u

- **表名称：** 归档方案-使用范围表
- **表名：** t_aef_archivescheme_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aef_archivescheme_u_uo |  | fuseorgid |
| 2 | pk_t_aef_archivescheme_u |  | fdataid,fuseorgid |

---

## 归档数据-子表 t_aef_archiveentry

- **表名称：** 归档数据-子表
- **表名：** t_aef_archiveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faiarchive | 智能方案归档 | bpchar | 1 |  | √ | '1' | 智能方案归档,枚举: 1 :上期 2 :上上期 |
| 3 | frptid | 报表模版 | varchar | 36 |  | √ | ' ' | [报表模板 xkrpt_rptsample](../xkrpt_files/xkrpt_rptsample.md) |
| 4 | fprinttemplate | 适用模板存储 | varchar | 500 |  |  | null | 适用模板存储 |
| 5 | fisneedprocessattachfile | 工作流附件归档 | bpchar | 1 |  | √ | ' ' | 工作流附件归档,枚举: 1 :是 0 :否 |
| 6 | farchiveperiod | 归档期间 | bpchar | 1 |  | √ | ' ' | 归档期间 |
| 7 | fprintsample | 适用模板ID | varchar | 100 |  | √ | ' ' | 适用模板ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | flargesamplejson_tag | 关联单据模板json（大文本）_详情 | text | 0 |  |  | null | 关联单据模板json（大文本）_详情 |
| 10 | fattachtabjson | 附件页签json | varchar | 2000 |  | √ | ' ' | 附件页签json |
| 11 | fdatefield | 归档日期字段 | varchar | 50 |  | √ | ' ' | 归档日期字段 |
| 12 | farchiverangereport | 归档范围 | varchar | 1000 |  | √ | ' ' | 归档范围 |
| 13 | farchiverangejson | 归档范围json | varchar | 2000 |  |  | null | 归档范围json |
| 14 | farchivetype | 归档类型 | varchar | 30 |  | √ | ' ' | 归档类型,枚举: finance :财务 bill :单据 |
| 15 | fprinttemplate_tag | 适用模板存储_详情 | text | 0 |  |  | null | 适用模板存储_详情 |
| 16 | fisneedattachfile | 附件归档 | bpchar | 1 |  | √ | ' ' | 附件归档,枚举: 1 :是 0 :否 |
| 17 | farchiverange | 归档范围 | varchar | 512 |  |  | null | 归档范围 |
| 18 | fattachtab | 附件页签 | varchar | 200 |  | √ | ' ' | 附件页签 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fprintsamplejson | 关联单据模板json | varchar | 1000 |  |  | ' ' | 关联单据模板json |
| 22 | flargesamplejson | 关联单据模板json（大文本） | varchar | 1000 |  | √ | ' ' | 关联单据模板json（大文本） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aef_archiveentry_pkey |  | fentryid |
| 2 | idx_aef_archiveentry_fid |  | fid |

---

## 归档方案-多语言表 t_aef_archivescheme_l

- **表名称：** 归档方案-多语言表
- **表名：** t_aef_archivescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aef_archivescheme_l_pkey |  | fpkid |
| 2 | idx_aef_archivescheme_l |  | fid,flocaleid |
