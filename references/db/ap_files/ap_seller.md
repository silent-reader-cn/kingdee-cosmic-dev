# 往来单位匹配-ap_seller

## 往来单位匹配-主表 t_ap_seller

- **表名称：** 往来单位匹配-主表
- **表名：** t_ap_seller

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 工商登记名称 | varchar | 100 |  | √ | ' ' | 工商登记名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbiztype | 业务类型 | varchar | 5 |  | √ | ' ' | 业务类型,枚举: PUR :采购 FEE :费用 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 20 | fuseorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_seller_number |  | fnumber |
| 2 | t_ap_seller_pkey |  | fid |
| 3 | idx_t_ap_seller_createorg |  | fcreateorgid |
| 4 | idx_t_ap_seller_master |  | fmasterid |

---

## 往来单位匹配-使用范围位图表 t_ap_seller_m

- **表名称：** 往来单位匹配-使用范围位图表
- **表名：** t_ap_seller_m

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
| 1 | pk_t_ap_seller_m |  | forgid |

---

## 往来单位匹配-多语言表 t_ap_seller_l

- **表名称：** 往来单位匹配-多语言表
- **表名：** t_ap_seller_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工商登记名称 | varchar | 100 |  | √ | ' ' | 工商登记名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_seller_l_fid |  | fid,flocaleid |
| 2 | t_ap_seller_l_pkey |  | fpkid |

---

## 往来单位匹配-使用范围表 t_ap_seller_u

- **表名称：** 往来单位匹配-使用范围表
- **表名：** t_ap_seller_u

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
| 1 | idx_t_ap_seller_u_uo |  | fuseorgid |
| 2 | t_ap_seller_u_pkey |  | fdataid,fuseorgid |
