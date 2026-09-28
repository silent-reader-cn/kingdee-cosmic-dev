# 工程转固单-fa_engineeringbill

## 关联子实体-子表 t_fa_assetinfoaddentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_assetinfoaddentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_assetinfoaddentry_lk |  | fpkid |
| 2 | idx_fa_assetinfoaddentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_fa_assetinfochangeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_assetinfochangeentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assetinfochangeentry_lk_fk |  | fentryid |
| 2 | pk_fa_assetinfochangeentry_lk |  | fpkid |

---

## 资本化项目详情-子表 t_fa_engineeringbillentry

- **表名称：** 资本化项目详情-子表
- **表名：** t_fa_engineeringbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconstractamount | 施工费 | numeric | 19 | 6 | √ | 0.000000 | 施工费 |
| 3 | fequipmentamount | 设备费 | numeric | 19 | 6 | √ | 0.000000 | 设备费 |
| 4 | ftotalamount | 转固金额 | numeric | 19 | 6 | √ | 0.000000 | 转固金额 |
| 5 | fmaterialamount | 材料费 | numeric | 19 | 6 | √ | 0.000000 | 材料费 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fotheramount | 其他费用 | numeric | 19 | 6 | √ | 0.000000 | 其他费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_engineeringbillentry |  | fid |
| 2 | t_fa_engineeringbillentry_pkey |  | fentryid |

---

## 工程转固单-主表 t_fa_engineeringbill

- **表名称：** 工程转固单-主表
- **表名：** t_fa_engineeringbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fassetname | 资产名称 | varchar | 60 |  | √ | ' ' | 资产名称 |
| 5 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 10 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fassetqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 12 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 0 :新增 1 :变更 |
| 13 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fusedepartmentid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 20 | fbuildway | 建卡方式 | varchar | 30 |  | √ | ' ' | 建卡方式,枚举: 1 :按表体分录行建卡 2 :按数量拆分建卡 3 :按整单建卡 |
| 21 | fcurrencyfieldid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fassetqtycreate | 可生成数量 | int8 | 64 |  | √ | 1 | 可生成数量 |
| 23 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_engineeringbill_pkey |  | fid |
| 2 | idx_fa_engineeringbill |  | fbillno |

---

## 资本化项目详情-子表 t_fa_engineer_adddetail

- **表名称：** 资本化项目详情-子表
- **表名：** t_fa_engineer_adddetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconstractamount | 施工费 | numeric | 19 | 6 | √ | 0 | 施工费 |
| 2 | fequipmentamount | 设备费 | numeric | 19 | 6 | √ | 0 | 设备费 |
| 3 | ftotalamount | 转固金额 | numeric | 19 | 6 | √ | 0 | 转固金额 |
| 4 | fmaterialamount | 材料费 | numeric | 19 | 6 | √ | 0 | 材料费 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fotheramount | 其他费用 | numeric | 19 | 6 | √ | 0 | 其他费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_engineer_add_eid |  | fentryid |
| 2 | pk_fa_engineer_adddetail |  | fdetailid |

---

## 变更资产信息-子表 t_fa_assetinfochangeentry

- **表名称：** 变更资产信息-子表
- **表名：** t_fa_assetinfochangeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | foriginalvalchange | 原值变动金额 | numeric | 19 | 4 | √ | 0.0000 | 原值变动金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freason | 变更理由 | varchar | 255 |  | √ | ' ' | 变更理由 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftarget | 标的物 | varchar | 255 |  | √ | ' ' | 标的物 |
| 9 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_assetinfochangeentry |  | fentryid |
| 2 | idx_fa_assetinfochangeentry |  | fid |

---

## 工程转固单-关联追踪表 t_fa_engineeringbill_tc

- **表名称：** 工程转固单-关联追踪表
- **表名：** t_fa_engineeringbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_engineeringbill_tc_tbill |  | ftbillid |
| 2 | pk_fa_engineeringbill_tc |  | fid |
| 3 | idx_fa_engineeringbill_tc_tid |  | ftid |

---

## 资本化项目详情-子表 t_fa_engineer_chadetail

- **表名称：** 资本化项目详情-子表
- **表名：** t_fa_engineer_chadetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconstractamount | 施工费 | numeric | 19 | 6 | √ | 0 | 施工费 |
| 2 | fequipmentamount | 设备费 | numeric | 19 | 6 | √ | 0 | 设备费 |
| 3 | ftotalamount | 转固金额 | numeric | 19 | 6 | √ | 0 | 转固金额 |
| 4 | fmaterialamount | 材料费 | numeric | 19 | 6 | √ | 0 | 材料费 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fotheramount | 其他费用 | numeric | 19 | 6 | √ | 0 | 其他费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_engineer_cha_eid |  | fentryid |
| 2 | pk_fa_engineer_chadetail |  | fdetailid |

---

## 工程转固单-反写记录表 t_fa_engineeringbill_wb

- **表名称：** 工程转固单-反写记录表
- **表名：** t_fa_engineeringbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_engineeringbill_wb |  | fentryid |
| 2 | idx_fa_engineeringbill_wb_fk |  | fid |

---

## 新增资产信息-子表 t_fa_assetinfoaddentry

- **表名称：** 新增资产信息-子表
- **表名：** t_fa_assetinfoaddentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetname | 资产名称 | varchar | 255 |  | √ | ' ' | 资产名称 |
| 3 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 4 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fassetcat | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 7 | fassetqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 8 | faddassetqtycreate | 可生成数量 | numeric | 23 | 10 | √ | 0 | 可生成数量 |
| 9 | ftarget | 标的物 | varchar | 255 |  | √ | ' ' | 标的物 |
| 10 | fusedepartmentid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 12 | foriginalval | 资产原值 | numeric | 19 | 4 | √ | 0.0000 | 资产原值 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_assetinfoaddentry |  | fentryid |
| 2 | idx_fa_assetinfoaddentry |  | fid |
