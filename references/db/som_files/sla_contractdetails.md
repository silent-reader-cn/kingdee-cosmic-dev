# 合同明细-sla_contractdetails

## 合同明细-使用范围位图表 t_tk_sla_ctradetails_m

- **表名称：** 合同明细-使用范围位图表
- **表名：** t_tk_sla_ctradetails_m

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
| 1 | pk_t_tk_sla_ctradetails_m |  | forgid |

---

## 合同明细-多语言表 t_tk_sla_ctradetails_l

- **表名称：** 合同明细-多语言表
- **表名：** t_tk_sla_ctradetails_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 合同明细名称 | varchar | 50 |  | √ | ' ' | 合同明细名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_sla_ctradetails_l |  | fpkid |
| 2 | idx_ssc_sla_ctradetails_l |  | fid,flocaleid |

---

## 合同明细-使用范围表 t_tk_sla_ctradetails_u

- **表名称：** 合同明细-使用范围表
- **表名：** t_tk_sla_ctradetails_u

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
| 1 | pk_t_tk_sla_ctradetails_u |  | fdataid,fuseorgid |
| 2 | idx_t_tk_sla_ctradetails_u_uo |  | fuseorgid |

---

## 合同明细-子表 t_tk_sla_cdentry

- **表名称：** 合同明细-子表
- **表名：** t_tk_sla_cdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fservicestd | fservicestd | varchar | 255 |  | √ | ' ' |  |
| 3 | fserviceproject | 服务项目 | int8 | 64 |  | √ | 0 | [服务项目 sla_serviceproject](../som_files/sla_serviceproject.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fprice | 暂估单价 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估单价 |
| 6 | fcdremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fnorfixedamount | 结算固定价格 | numeric | 23 | 10 | √ | 0 | 结算固定价格 |
| 8 | fserviceclassify | 服务类别 | int8 | 64 |  | √ | 0 | [服务项目分类 sla_serviceclassify](../som_files/sla_serviceclassify.md) |
| 9 | fservicestandard | 服务标准 | int8 | 64 |  | √ | 0 | [服务标准 sla_servicelevel](../som_files/sla_servicelevel.md) |
| 10 | fbilling | 计费方式 | varchar | 10 |  | √ | ' ' | 计费方式,枚举: qty :数量单价 fixed :固定价格 |
| 11 | ffixedamount | 暂估固定价格 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估固定价格 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsettlementperiod | 结算周期 | varchar | 10 |  | √ | ' ' | 结算周期,枚举: MM :月度 QQ :季度 YY :年度 EL :其他 |
| 14 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fnorprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_sla_cdentry |  | fentryid |
| 2 | idx_ssc_sla_cdentry |  | fid |

---

## 合同明细-主表 t_tk_sla_ctradetails

- **表名称：** 合同明细-主表
- **表名：** t_tk_sla_ctradetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurrency | 合同币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_sla_ctradetails |  | fid |
| 2 | idx_t_tk_sla_ctradetails_createorg |  | fcreateorgid |
| 3 | idx_t_tk_sla_ctradetails_master |  | fmasterid |
| 4 | idx_ssc_sla_ctradetails |  | fnumber |
