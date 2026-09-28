# 项目文档-mpm_document

## 文档单据体-多语言表 t_mpm_docentry_l

- **表名称：** 文档单据体-多语言表
- **表名：** t_mpm_docentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fabstract | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 2 | fdocname | 文档名称 | varchar | 2000 |  | √ | ' ' | 文档名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_docentry_l |  | fpkid |
| 2 | idx_mpm_docel_fenflid |  | fentryid,flocaleid |

---

## 文档单据体-子表 t_mpm_docentry

- **表名称：** 文档单据体-子表
- **表名：** t_mpm_docentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcformid | 来源业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fuploadtime | 上传时间 | timestamp | 0 |  |  | null | 上传时间 |
| 4 | fwebsite | 网址 | varchar | 2000 |  | √ | ' ' | 网址 |
| 5 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 6 | fabstract | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fuploaduserid | 上传人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdocname | 文档名称 | varchar | 2000 |  | √ | ' ' | 文档名称 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_docentry |  | fentryid |
| 2 | idx_mpm_docentry_fid |  | fid |

---

## 项目文档-多语言表 t_mpm_document_l

- **表名称：** 项目文档-多语言表
- **表名：** t_mpm_document_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwebsite | fwebsite | varchar | 2000 |  | √ | ' ' |  |
| 3 | fabstract | fabstract | varchar | 2000 |  | √ | ' ' |  |
| 4 | fdocname | 文档名称 | varchar | 2000 |  | √ | ' ' | 文档名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_document_fidflid |  | fid,flocaleid |
| 2 | pk_mpm_document_l |  | fpkid |

---

## 项目文档-主表 t_mpm_document

- **表名称：** 项目文档-主表
- **表名：** t_mpm_document

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuploadtime | fuploadtime | timestamp | 0 |  |  | null |  |
| 3 | fwebsite | fwebsite | varchar | 2000 |  | √ | ' ' |  |
| 4 | frowtype | 行类型 | bpchar | 1 |  | √ | ' ' | 行类型,枚举: A :计划行 B :文档行 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fabstract | fabstract | varchar | 2000 |  | √ | ' ' |  |
| 7 | fplandatetime | 计划提交时间 | timestamp | 0 |  |  | null | 计划提交时间 |
| 8 | fcheckdoc | 验收文档 | bpchar | 1 |  | √ | '0' | 验收文档 |
| 9 | fuploaduserid | fuploaduserid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未提交 B :已提交 C :待验收 D :部分验收 E :已验收 F :部分归档 G :已归档 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fdoctypeid | 文档类型 | int8 | 64 |  | √ | 0 | 文档类型 mpm_documenttype |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | ffolderid | 关联文件夹 | int8 | 64 |  | √ | 0 | 文件夹 mpm_folder |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fparentid | 计划行 | int8 | 64 |  | √ | 0 | 项目文档基础资料 mpm_document_basic |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 23 | fdocname | 文档名称 | varchar | 2000 |  | √ | ' ' | 文档名称 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fsrcformid | fsrcformid | varchar | 80 |  | √ | ' ' |  |
| 26 | ftaskid | 项目任务 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_document_fprj |  | fprojectid |
| 2 | idx_mpm_document_fbillno |  | fbillno |
| 3 | idx_mpm_document_fparent |  | fparentid |
| 4 | idx_mpm_document_ftask |  | ftaskid |
| 5 | pk_mpm_document |  | fid |

---

## 附件-附件表 t_mpm_docentryattach

- **表名称：** 附件-附件表
- **表名：** t_mpm_docentryattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_docentryattach |  | fpkid |
| 2 | idx_mpm_docentryatt_fid |  | fentryid |
