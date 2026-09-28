# 价目表-pur_price

## 价目表-使用范围位图表 t_pur_price_m

- **表名称：** 价目表-使用范围位图表
- **表名：** t_pur_price_m

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
| 1 | pk_t_pur_price_m |  | forgid |

---

## 价目表-多语言表 t_pur_price_l

- **表名称：** 价目表-多语言表
- **表名：** t_pur_price_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_price_l_pkey |  | fpkid |
| 2 | idx_pur_price_l_fid_flocaleid |  | fid,flocaleid |

---

## 价目表-使用范围表 t_pur_price_u

- **表名称：** 价目表-使用范围表
- **表名：** t_pur_price_u

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
| 1 | idx_t_pur_price_u_uo |  | fuseorgid |
| 2 | t_pur_price_u_pkey |  | fdataid,fuseorgid |

---

## 分录信息-子表 t_pur_pricentry

- **表名称：** 分录信息-子表
- **表名：** t_pur_pricentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 3 | fdateto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fgoodsid | fgoodsid | int8 | 64 |  | √ | 0 |  |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fmatclassid | 物料分类 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fupprice | 价格上限 | numeric | 19 | 6 | √ | 0.000000 | 价格上限 |
| 10 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已禁用 |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 14 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 15 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 16 | frefprice | 参考价 | numeric | 23 | 10 | √ | 0.0000000000 | 参考价 |
| 17 | fminorderqty | 最小起订量 | numeric | 19 | 6 | √ | 0.000000 | 最小起订量 |
| 18 | fqtyto | 数量至 | numeric | 19 | 6 | √ | 0.000000 | 数量至 |
| 19 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 20 | fdatefrom | 有效期从 | timestamp | 0 |  |  | null | 有效期从 |
| 21 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 22 | flowprice | 价格下限 | numeric | 19 | 6 | √ | 0.000000 | 价格下限 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_pricentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_pricentry_fmaterialid |  | fmaterialid |
| 3 | t_pur_pricentry_pkey |  | fentryid |

---

## 收货组织-多选基础资料表 t_pur_price_rcv

- **表名称：** 收货组织-多选基础资料表
- **表名：** t_pur_price_rcv

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
| 1 | t_pur_price_rcv_pkey |  | fpkid |
| 2 | idx_pur_price_rcv_fid |  | fid,fbasedataid |

---

## 价目表-主表 t_pur_price

- **表名称：** 价目表-主表
- **表名：** t_pur_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbiztypescope | 业务类型范围 | varchar | 50 |  | √ | ' ' | 业务类型范围,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 A :样品采购 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcompareno | 比价单号 | varchar | 80 |  | √ | ' ' | 比价单号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fpurorgscope | 采购组织范围 | bpchar | 1 |  | √ | ' ' | 采购组织范围,枚举: 1 :所有采购组织 2 :限定采购组织 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 20 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fpriceobj | 定价对象 | bpchar | 1 |  | √ | ' ' | 定价对象,枚举: 1 :物料 2 :物料分类 |
| 23 | fsupscope | 供应商范围 | bpchar | 1 |  | √ | ' ' | 供应商范围,枚举: 1 :所有供应商 2 :限定供应商 |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | frcvorgscope | 收货组织范围 | bpchar | 1 |  | √ | ' ' | 收货组织范围,枚举: 1 :所有收货组织 2 :限定收货组织 |
| 27 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 28 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_price_pkey |  | fid |
| 2 | idx_pur_price_fmasterid |  | fmasterid |
| 3 | idx_t_pur_price_createorg |  | fcreateorgid |
| 4 | idx_t_pur_price_master |  | fmasterid |
| 5 | idx_pur_price_fnumber |  | fnumber |

---

## 采购组织-多选基础资料表 t_pur_price_org

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_pur_price_org

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
| 1 | t_pur_price_org_pkey |  | fpkid |
| 2 | idx_pur_price_org_fid |  | fid,fbasedataid |

---

## 供应商-多选基础资料表 t_pur_price_sup

- **表名称：** 供应商-多选基础资料表
- **表名：** t_pur_price_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_price_sup_pkey |  | fpkid |
| 2 | idx_pur_price_sup_fid |  | fid,fbasedataid |
