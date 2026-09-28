# 企业项目结构-pmbd_orgpros

## 企业项目结构-主表 t_pmbd_orgpros

- **表名称：** 企业项目结构-主表
- **表名：** t_pmbd_orgpros

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fdutypersonid | 责任人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdutydeptid | 责任部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 15 | fname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 企业项目结构 pmbd_orgpros |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 20 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 22 | fselfid | 列表传递过来的id | varchar | 50 |  | √ | ' ' | 列表传递过来的id |
| 23 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 节点编码 | varchar | 30 |  | √ | ' ' | 节点编码 |
| 25 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_orgpros |  | fid |
| 2 | idx_t_pmbd_orgpros_createorg |  | fcreateorgid |
| 3 | idx_t_pmbd_orgpros_master |  | fmasterid |
| 4 | idx_pmbd_orgpos_fcreatetime |  | fcreatetime |
| 5 | idx_pmbd_orgpos_fnumber |  | fnumber |

---

## 企业项目结构-使用范围表 t_pmbd_orgpros_u

- **表名称：** 企业项目结构-使用范围表
- **表名：** t_pmbd_orgpros_u

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
| 1 | idx_t_pmbd_orgpros_u_uo |  | fuseorgid |
| 2 | pk_t_pmbd_orgpros_u |  | fdataid,fuseorgid |

---

## 企业项目结构-多语言表 t_pmbd_orgpros_l

- **表名称：** 企业项目结构-多语言表
- **表名：** t_pmbd_orgpros_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_orgposl_fid |  | fid,flocaleid |
| 2 | idx_pmbd_orgposl_fname |  | fname |
| 3 | pk_pmbd_orgpros_l |  | fpkid |

---

## 企业项目结构-使用范围位图表 t_pmbd_orgpros_m

- **表名称：** 企业项目结构-使用范围位图表
- **表名：** t_pmbd_orgpros_m

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
| 1 | pk_t_pmbd_orgpros_m |  | forgid |

---

## PMO信息-子表 t_pmbd_orgprosentry

- **表名称：** PMO信息-子表
- **表名：** t_pmbd_orgprosentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fpnumber | 工号 | int8 | 64 |  | √ | 0 | 企业人力资源池 pmbd_enterprise_hm_res_po |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_orgpry_fid |  | fid |
| 2 | idx_pmbd_orgpry_fseq |  | fseq |
| 3 | pk_pmbd_orgprosentry |  | fentryid |
