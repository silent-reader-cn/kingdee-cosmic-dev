# 调度工作类型-fmm_dispatchwktp

## 调度工作类型-主表 t_fmm_dispatchwktp

- **表名称：** 调度工作类型-主表
- **表名：** t_fmm_dispatchwktp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | findependdisptch | findependdisptch | bpchar | 1 |  | √ | '0' |  |
| 15 | fbgcolor | 背颜色 | varchar | 50 |  | √ | ' ' | 背颜色 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fparentid | 上级工作类型 | int8 | 64 |  | √ | 0 | [调度工作类型 fmm_dispatchwktp](../fmm_files/fmm_dispatchwktp.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ffullname | ffullname | varchar | 50 |  | √ | ' ' |  |
| 22 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 23 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 25 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fmainwktp | 主工作类型 | bpchar | 1 |  | √ | '0' | 主工作类型 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | ffontcolor | 字体颜色 | varchar | 50 |  | √ | ' ' | 字体颜色 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_dispatchwktp_fct |  | fcreatetime |
| 2 | idx_fmm_dispatchwktp_fnum |  | fnumber |
| 3 | pk_fmm_dispatchwktp |  | fid |
| 4 | idx_t_fmm_dispatchwktp_createorg |  | fcreateorgid |
| 5 | idx_t_fmm_dispatchwktp_master |  | fmasterid |

---

## 调度工作类型-使用范围表 t_fmm_dispatchwktp_u

- **表名称：** 调度工作类型-使用范围表
- **表名：** t_fmm_dispatchwktp_u

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
| 1 | idx_t_fmm_dispatchwktp_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_dispatchwktp_u |  | fdataid,fuseorgid |

---

## 调度工作类型-多语言表 t_fmm_dispatchwktp_l

- **表名称：** 调度工作类型-多语言表
- **表名：** t_fmm_dispatchwktp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_dispatchwktp_l_fid |  | fid,flocaleid |
| 2 | idx_fmm_dispatchwktp_l_fna |  | fname |
| 3 | pk_fmm_dispatchwktp_l |  | fpkid |
