# 收货信息-pbd_receiptinfo

## 收货信息-使用范围表 t_mal_receiptinfo_u

- **表名称：** 收货信息-使用范围表
- **表名：** t_mal_receiptinfo_u

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
| 1 | idx_t_mal_receiptinfo_u_uo |  | fuseorgid |
| 2 | t_mal_receiptinfo_u_pkey |  | fdataid,fuseorgid |

---

## 收货信息-使用范围位图表 t_mal_receiptinfo_m

- **表名称：** 收货信息-使用范围位图表
- **表名：** t_mal_receiptinfo_m

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
| 1 | pk_t_mal_receiptinfo_m |  | forgid |

---

## 收货信息-多语言表 t_mal_receiptinfo_l

- **表名称：** 收货信息-多语言表
- **表名：** t_mal_receiptinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 收货人 | varchar | 100 |  | √ | ' ' | 收货人 |
| 4 | fmapaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 5 | fwholeaddress | 全地址 | varchar | 255 |  | √ | ' ' | 全地址 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_receiptinfo_l_pkey |  | fpkid |
| 2 | idx_mal_receiptinfo_l_fid |  | fid,flocaleid |

---

## 收货信息-主表 t_mal_receiptinfo

- **表名称：** 收货信息-主表
- **表名：** t_mal_receiptinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftel | 固定电话 | varchar | 50 |  | √ | ' ' | 固定电话 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | faddressid | 省市区 | varchar | 50 |  | √ | ' ' | 省市区 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdefault | 默认交货地址 | bpchar | 1 |  | √ | ' ' | 默认交货地址 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fpostalcode | 邮政编码 | varchar | 10 |  | √ | ' ' | 邮政编码 |
| 14 | fmapaddress | fmapaddress | varchar | 255 |  | √ | ' ' |  |
| 15 | fwholeaddress | fwholeaddress | varchar | 255 |  | √ | ' ' |  |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 20 | fphone | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 25 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 26 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | fjdaddressnum | fjdaddressnum | varchar | 100 |  | √ | ' ' |  |
| 30 | farea | farea | varchar | 50 |  | √ | ' ' |  |
| 31 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_receiptinfo_createorg |  | fcreateorgid |
| 2 | idx_t_mal_receiptinfo_master |  | fmasterid |
| 3 | t_mal_receiptinfo_pkey |  | fid |
| 4 | idx_mal_receiptinfo_fnumber |  | fnumber |
