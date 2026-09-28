# 动态安全库存计算单-invp_dynamicinv_cal

## 明细信息-子表 t_invp_dynamicinv_cal_e

- **表名称：** 明细信息-子表
- **表名：** t_invp_dynamicinv_cal_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 5 | fadvicesafeqty | 建议安全库存数量 | numeric | 23 | 10 | √ | 0 | 建议安全库存数量 |
| 6 | fadoptsafeqty | 采纳安全库存数量 | numeric | 23 | 10 | √ | 0 | 采纳安全库存数量 |
| 7 | fdesireservice | 期望服务水平（%） | int8 | 64 |  | √ | 0 | 期望服务水平（%） |
| 8 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 9 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fcursafeinvcost | 当前安全库存成本 | numeric | 23 | 10 | √ | 0 | 当前安全库存成本 |
| 12 | fdayconsume | 日均消耗 | numeric | 23 | 10 | √ | 0 | 日均消耗 |
| 13 | fadoptsafeinvcost | 采纳安全库存成本 | numeric | 23 | 10 | √ | 0 | 采纳安全库存成本 |
| 14 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fcursaftyinvqty | 系统当前安全库存 | numeric | 23 | 10 | √ | 0 | 系统当前安全库存 |
| 16 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 18 | favalialeday | 安全库存可用天数 | int8 | 64 |  | √ | 0 | 安全库存可用天数 |
| 19 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 20 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | fpuravgleadtime | 采购平均提前期（天） | int8 | 64 |  | √ | 0 | 采购平均提前期（天） |
| 23 | frefrenceservice | 参考服务水平（%） | numeric | 23 | 10 | √ | 0 | 参考服务水平（%） |
| 24 | fsafeinvupdatetime | 安全库存更新时间 | timestamp | 0 |  |  | null | 安全库存更新时间 |
| 25 | fadoptfixleadtime | 采纳固定提前期（天） | int8 | 64 |  | √ | 0 | 采纳固定提前期（天） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_dynamicinv_cal_e_fk |  | fid |
| 2 | pk_invp_dynamicinv_cal_e |  | fentryid |

---

## 动态安全库存计算单-主表 t_invp_dynamicinv_cal

- **表名称：** 动态安全库存计算单-主表
- **表名：** t_invp_dynamicinv_cal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcalstatus | 计算状态 | varchar | 50 |  | √ | ' ' | 计算状态,枚举: wait :待计算 doing :计算中 complete :计算完成 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcalscheme | 计算方案 | int8 | 64 |  | √ | 0 | [动态安全库存计算方案 invp_dynamicinv_scheme](../invp_files/invp_dynamicinv_scheme.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 计算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fstatisticsunitrange | 统计周期范围 | varchar | 80 |  | √ | ' ' | 统计周期范围 |
| 10 | fprocessrate | 计算进度 | int8 | 64 |  | √ | 0 | 计算进度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcaldate | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillsource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: manual :手工创建 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_dynamicinv_cal |  | fid |
| 2 | idx_invp_dynamicinv_cal_m0 |  | fbillno |
