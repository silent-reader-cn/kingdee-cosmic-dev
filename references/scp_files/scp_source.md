# 客户物料对应表-scp_source

## 客户物料对应表-主表 t_pur_source

- **表名称：** 客户物料对应表-主表
- **表名：** t_pur_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbiztypescope | fbiztypescope | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcompareno | fcompareno | varchar | 80 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fpurorgscope | fpurorgscope | bpchar | 1 |  | √ | ' ' |  |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 25 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_source_fmasterid |  | fmasterid |
| 2 | t_pur_source_pkey |  | fid |
| 3 | idx_pur_source_fnumber |  | fnumber |
| 4 | idx_t_pur_source_master |  | fmasterid |
| 5 | idx_t_pur_source_createorg |  | fcreateorgid |

---

## 客户物料对应表-使用范围表 t_pur_source_u

- **表名称：** 客户物料对应表-使用范围表
- **表名：** t_pur_source_u

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
| 1 | pk_t_pur_source_u |  | fdataid,fuseorgid |
| 2 | idx_t_pur_source_u_uo |  | fuseorgid |

---

## 客户物料对应表-多语言表 t_pur_source_l

- **表名称：** 客户物料对应表-多语言表
- **表名：** t_pur_source_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_source_l_pkey |  | fpkid |
| 2 | idx_pur_source_l_fid_flocaleid |  | fid,flocaleid |

---

## 客户物料对应表-使用范围位图表 t_pur_source_m

- **表名称：** 客户物料对应表-使用范围位图表
- **表名：** t_pur_source_m

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
| 1 | pk_t_pur_source_m |  | forgid |

---

## 清单分录-子表 t_pur_sourcentry

- **表名称：** 清单分录-子表
- **表名：** t_pur_sourcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsid | 我方商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 3 | fmaxorderqty | 最大订货量 | numeric | 19 | 6 | √ | 0.000000 | 最大订货量 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | ftotalordqty | 累计订货量 | numeric | 19 | 6 | √ | 0.000000 | 累计订货量 |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已禁用 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 10 | fisprimary | fisprimary | bpchar | 1 |  | √ | ' ' |  |
| 11 | fminpackqty | 最小包装量 | numeric | 19 | 6 | √ | 0.000000 | 最小包装量 |
| 12 | fminorderqty | 最小订货量 | numeric | 19 | 6 | √ | 0.000000 | 最小订货量 |
| 13 | fdatefrom | 有效期从 | timestamp | 0 |  |  | null | 有效期从 |
| 14 | fquotaorder | fquotaorder | int8 | 64 |  | √ | 0 |  |
| 15 | fdateto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 16 | fmatclassid | fmatclassid | int8 | 64 |  | √ | 0 |  |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 pur_paycond |
| 19 | fgoodsdesc | 我方商品描述 | varchar | 255 |  | √ | ' ' | 我方商品描述 |
| 20 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 22 | fpurleadday | 采购提前期 | int8 | 64 |  | √ | 0 | 采购提前期 |
| 23 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 24 | fquotaratio | fquotaratio | numeric | 19 | 6 | √ | 0.000000 |  |
| 25 | fmaterialdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_sourcentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_sourcentry_fmaterialid |  | fmaterialid |
| 3 | idx_pur_sourcentry_fsupplierid |  | fsupplierid |
| 4 | t_pur_sourcentry_pkey |  | fentryid |
