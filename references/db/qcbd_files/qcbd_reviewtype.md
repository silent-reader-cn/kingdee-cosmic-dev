# 评审类型-qcbd_reviewtype

## 评审类型-主表 t_qcbd_reviewtype

- **表名称：** 评审类型-主表
- **表名：** t_qcbd_reviewtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_reviewtype |  | fid |
| 2 | idx_qcbd_revipe_fcreatetime |  | fcreatetime |
| 3 | idx_qcbd_revipe_fnumber |  | fnumber |
| 4 | idx_t_qcbd_reviewtype_createorg |  | fcreateorgid |
| 5 | idx_t_qcbd_reviewtype_master |  | fmasterid |

---

## 评审类型-使用范围表 t_qcbd_reviewtype_u

- **表名称：** 评审类型-使用范围表
- **表名：** t_qcbd_reviewtype_u

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
| 1 | idx_t_qcbd_reviewtype_u_uo |  | fuseorgid |
| 2 | pk_t_qcbd_reviewtype_u |  | fdataid,fuseorgid |

---

## 评审类型-使用范围位图表 t_qcbd_reviewtype_m

- **表名称：** 评审类型-使用范围位图表
- **表名：** t_qcbd_reviewtype_m

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
| 1 | pk_t_qcbd_reviewtype_m |  | forgid |

---

## 评审类型-多语言表 t_qcbd_reviewtype_l

- **表名称：** 评审类型-多语言表
- **表名：** t_qcbd_reviewtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_revipel_fid |  | fid,flocaleid |
| 2 | idx_qcbd_revipel_fname |  | fname |
| 3 | pk_qcbd_reviewtype_l |  | fpkid |
