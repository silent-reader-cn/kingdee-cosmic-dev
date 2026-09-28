# 供应商业务员-pbd_supbizperson

## 供应商业务员-主表 t_pur_supbizperson

- **表名称：** 供应商业务员-主表
- **表名：** t_pur_supbizperson

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsupgroupid | 供应商分组 | int8 | 64 |  | √ | 0 | 供应商分类 bd_suppliergroup |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fscpuserid | 供应商用户 | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 14 | fbizscope | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :订单 2 :收货 3 :退货 4 :对账 5 :收票 6 :付款 7 :询价 8 :招标 A :全部 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fuserid | 对应人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fbizpartnerid | 供应商 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 28 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_supbizperson_fmasterid |  | fmasterid |
| 2 | idx_t_pur_supbizperson_createorg |  | fcreateorgid |
| 3 | t_pur_supbizperson_pkey |  | fid |
| 4 | idx_t_pur_supbizperson_master |  | fmasterid |
| 5 | idx_pur_supbizperson_fnumber |  | fnumber |

---

## 采购方(影响：订单&#x2f;发货&#x2f;收货&#x2f;入库&#x2f;退货)-多选基础资料表 t_pur_supbiz_purorg

- **表名称：** 采购方(影响：订单&#x2f;发货&#x2f;收货&#x2f;入库&#x2f;退货)-多选基础资料表
- **表名：** t_pur_supbiz_purorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_supbiz_purorg_fid |  | fid,fbasedataid |
| 2 | t_pur_supbiz_purorg_pkey |  | fpkid |

---

## 供应商业务员-多语言表 t_pur_supbizperson_l

- **表名称：** 供应商业务员-多语言表
- **表名：** t_pur_supbizperson_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_supbizperson_l_fid |  | fid,flocaleid |
| 2 | t_pur_supbizperson_l_pkey |  | fpkid |

---

## 供应商业务员-使用范围位图表 t_pur_supbizperson_m

- **表名称：** 供应商业务员-使用范围位图表
- **表名：** t_pur_supbizperson_m

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
| 1 | pk_t_pur_supbizperson_m |  | forgid |

---

## 供应商业务员-使用范围表 t_pur_supbizperson_u

- **表名称：** 供应商业务员-使用范围表
- **表名：** t_pur_supbizperson_u

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
| 1 | idx_t_pur_supbizperson_u_uo |  | fuseorgid |
| 2 | t_pur_supbizperson_u_pkey |  | fdataid,fuseorgid |

---

## 收货方(影响：订单&#x2f;发货&#x2f;收货&#x2f;入库&#x2f;退货)-多选基础资料表 t_pur_supbiz_rcvorg

- **表名称：** 收货方(影响：订单&#x2f;发货&#x2f;收货&#x2f;入库&#x2f;退货)-多选基础资料表
- **表名：** t_pur_supbiz_rcvorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_supbiz_rcvorg_fid |  | fid,fbasedataid |
| 2 | t_pur_supbiz_rcvorg_pkey |  | fpkid |

---

## 核算方(影响：对账&#x2f;开票&#x2f;收款)-多选基础资料表 t_pur_supbiz_setorg

- **表名称：** 核算方(影响：对账&#x2f;开票&#x2f;收款)-多选基础资料表
- **表名：** t_pur_supbiz_setorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_supbiz_setorg_pkey |  | fpkid |
| 2 | idx_pur_supbiz_setorg_fid |  | fid,fbasedataid |
