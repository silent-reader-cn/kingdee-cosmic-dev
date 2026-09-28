# 项目-bd_project_hr

## 关联子实体-子表 t_bd_project_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bd_project_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_project_lk_fk |  | fid |
| 2 | pk_bd_project_lk |  | fpkid |

---

## 项目-主表 t_bd_project

- **表名称：** 项目-主表
- **表名：** t_bd_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  |  | null |  |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fplanbegindate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 6 | fprojectmanagerid | fprojectmanagerid | int8 | 64 |  | √ | 0 |  |
| 7 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprocostindietrf | fprocostindietrf | bpchar | 1 |  | √ | '0' |  |
| 11 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcetype | fsourcetype | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fbudgetproname | fbudgetproname | varchar | 255 |  | √ | ' ' |  |
| 19 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fplanenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 23 | fname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 24 | fprostatus | 项目状态 | int8 | 64 |  | √ | 0 | [项目状态 bd_projectstatus](../basedata_files/bd_projectstatus.md) |
| 25 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [项目 bd_project_hr](../basedata_files/bd_project_hr.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | ffullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 28 | flongnumber | 长编码 | varchar | 810 |  | √ | ' ' | 长编码 |
| 29 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 30 | frefcheck | 是否反审核校验 | varchar | 30 |  | √ | '0' | 是否反审核校验,枚举: 0 :否 1 :是 |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 33 | fbudgetpronumber | fbudgetpronumber | varchar | 255 |  | √ | ' ' |  |
| 34 | fctrlstrategy | 控制策略 | varchar | 10 |  |  | null | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 35 | fsystemtype | fsystemtype | varchar | 30 |  | √ | 'SYS' |  |
| 36 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 37 | fissys | 是否系统创建 | bpchar | 1 |  | √ | '0' | 是否系统创建 |
| 38 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fproaddress | 项目地址 | varchar | 255 |  | √ | ' ' | 项目地址 |
| 40 | fnumber | 项目编码 | varchar | 80 |  |  | null | 项目编码 |
| 41 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fpmascreateorgid | fpmascreateorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 44 | ffullid | ffullid | varchar | 200 |  | √ | ' ' |  |
| 45 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 46 | fprojfinalaccount | fprojfinalaccount | varchar | 50 |  | √ | 'B' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_project_number |  | fnumber |
| 2 | idx_t_bd_project_ctrlstrategy |  | fctrlstrategy |
| 3 | idx_t_bd_project_master |  | fmasterid |
| 4 | t_bd_project_pkey |  | fid |
| 5 | idx_t_bd_project_createorg |  | fcreateorgid |

---

## 项目-多语言表 t_bd_project_l

- **表名称：** 项目-多语言表
- **表名：** t_bd_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 项目名称 | varchar | 255 |  |  | null | 项目名称 |
| 3 | ffullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 4 | fproaddress | 项目地址 | varchar | 255 |  | √ | ' ' | 项目地址 |
| 5 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_project_l_pkey |  | fpkid |
| 2 | idx_t_bd_project_l_fid |  | fid,flocaleid |

---

## 项目-使用范围位图表 t_bd_project_m

- **表名称：** 项目-使用范围位图表
- **表名：** t_bd_project_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_project_m |  | forgid |

---

## 项目-使用范围表 t_bd_project_u

- **表名称：** 项目-使用范围表
- **表名：** t_bd_project_u

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
| 1 | idx_t_bd_project_u_uo |  | fuseorgid |
| 2 | t_bd_project_u_pkey |  | fdataid,fuseorgid |
