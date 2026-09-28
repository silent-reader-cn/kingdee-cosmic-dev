# 项目文档基础资料-mpm_document_basic

## 附件-附件表 t_mpm_docattach

- **表名称：** 附件-附件表
- **表名：** t_mpm_docattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_docattach |  | fpkid |

---

## 项目文档基础资料-多语言表 t_mpm_document_l

- **表名称：** 项目文档基础资料-多语言表
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

## 项目文档基础资料-主表 t_mpm_document

- **表名称：** 项目文档基础资料-主表
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
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未提交 B :已提交 C :待验收 D :部分验收 E :已验收 F :部分归档 G :已归档 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 项目文档单据编号 | varchar | 80 |  | √ | ' ' | 项目文档单据编号 |
| 14 | fdoctypeid | 文档类型 | int8 | 64 |  | √ | 0 | 文档类型 mpm_documenttype |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | ffolderid | 关联文件夹 | int8 | 64 |  | √ | 0 | 文件夹 mpm_folder |
| 18 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 19 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 21 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 22 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 23 | fdocname | 文档名称 | varchar | 2000 |  | √ | ' ' | 文档名称 |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fsrcformid | fsrcformid | varchar | 80 |  | √ | ' ' |  |
| 26 | ftaskid | 项目任务 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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
