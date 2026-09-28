# 文件夹-mpm_folder

## 文件夹-多语言表 t_mpm_folder_l

- **表名称：** 文件夹-多语言表
- **表名：** t_mpm_folder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 文件夹名称 | varchar | 255 |  | √ | ' ' | 文件夹名称 |
| 3 | ffullname | 长名称 | varchar | 512 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_folder_l |  | fpkid |
| 2 | idx_mpm_folder_fidflid |  | fid,flocaleid |

---

## 文件夹-使用范围表 t_mpm_folder_u

- **表名称：** 文件夹-使用范围表
- **表名：** t_mpm_folder_u

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
| 1 | pk_t_mpm_folder_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpm_folder_u_uo |  | fuseorgid |

---

## 附件-附件表 t_mpm_folattach

- **表名称：** 附件-附件表
- **表名：** t_mpm_folattach

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
| 1 | pk_mpm_folattach |  | fpkid |

---

## 文件夹-主表 t_mpm_folder

- **表名称：** 文件夹-主表
- **表名：** t_mpm_folder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 文件夹名称 | varchar | 255 |  | √ | ' ' | 文件夹名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 6 | fparentid | 上级基础资料 | int8 | 64 |  | √ | 0 | 文件夹 mpm_folder |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fprojectidid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 9 | ffullname | ffullname | varchar | 512 |  | √ | ' ' |  |
| 10 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | flongnumber | 长编码 | varchar | 512 |  | √ | ' ' | 长编码 |
| 12 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fisprojetfolder | 是否项目文件夹 | bpchar | 1 |  | √ | '0' | 是否项目文件夹 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 21 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_folder_number |  | fnumber |
| 2 | idx_t_mpm_folder_createorg |  | fcreateorgid |
| 3 | pk_mpm_folder |  | fid |
| 4 | idx_t_mpm_folder_master |  | fmasterid |

---

## 单据体-子表 t_mpm_folassign

- **表名称：** 单据体-子表
- **表名：** t_mpm_folassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fisdownload | 是否允许下载 | bpchar | 1 |  | √ | '0' | 是否允许下载 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_folassign_fid |  | fid |
| 2 | pk_t_mpm_folassign |  | fentryid |
