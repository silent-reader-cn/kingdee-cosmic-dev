# 材料可用性分析-psw_cac

## 树形单据体-子表 t_psw_cacdetail

- **表名称：** 树形单据体-子表
- **表名：** t_psw_cacdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectedqty25 |  | numeric | 23 | 10 | √ | 0 |  |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fprojectedqty24 |  | numeric | 23 | 10 | √ | 0 |  |
| 4 | fprojectedqty23 |  | numeric | 23 | 10 | √ | 0 |  |
| 5 | fprojectedqty22 |  | numeric | 23 | 10 | √ | 0 |  |
| 6 | fprojectedqty21 |  | numeric | 23 | 10 | √ | 0 |  |
| 7 | fprojectedqty20 |  | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fprojectedqty29 |  | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprojectedqty28 |  | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprojectedqty27 |  | numeric | 23 | 10 | √ | 0 |  |
| 12 | fprojectedqty26 |  | numeric | 23 | 10 | √ | 0 |  |
| 13 | fsafetystock | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 18 | fprojectedqty58 |  | numeric | 23 | 10 | √ | 0 |  |
| 19 | fprojectedqty14 |  | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectedqty57 |  | numeric | 23 | 10 | √ | 0 |  |
| 21 | fprojectedqty13 |  | numeric | 23 | 10 | √ | 0 |  |
| 22 | fprojectedqty56 |  | numeric | 23 | 10 | √ | 0 |  |
| 23 | fprojectedqty12 |  | numeric | 23 | 10 | √ | 0 |  |
| 24 | fprojectedqty55 |  | numeric | 23 | 10 | √ | 0 |  |
| 25 | fprojectedqty11 |  | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprojectedqty54 |  | numeric | 23 | 10 | √ | 0 |  |
| 27 | fprojectedqty10 |  | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprojectedqty53 |  | numeric | 23 | 10 | √ | 0 |  |
| 29 | fprojectedqty52 |  | numeric | 23 | 10 | √ | 0 |  |
| 30 | fprojectedqty51 |  | numeric | 23 | 10 | √ | 0 |  |
| 31 | fprojectedqty19 |  | numeric | 23 | 10 | √ | 0 |  |
| 32 | fprojectedqty18 |  | numeric | 23 | 10 | √ | 0 |  |
| 33 | fprojectedqty17 |  | numeric | 23 | 10 | √ | 0 |  |
| 34 | fprojectedqty16 |  | numeric | 23 | 10 | √ | 0 |  |
| 35 | fprojectedqty59 |  | numeric | 23 | 10 | √ | 0 |  |
| 36 | fprojectedqty15 |  | numeric | 23 | 10 | √ | 0 |  |
| 37 | fmaterialcodeid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fprojectedqty60 |  | numeric | 23 | 10 | √ | 0 |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fprojectedqty47 |  | numeric | 23 | 10 | √ | 0 |  |
| 41 | fprojectedqty9 |  | numeric | 23 | 10 | √ | 0 |  |
| 42 | fprojectedqty46 |  | numeric | 23 | 10 | √ | 0 |  |
| 43 | fprojectedqty8 |  | numeric | 23 | 10 | √ | 0 |  |
| 44 | fprojectedqty45 |  | numeric | 23 | 10 | √ | 0 |  |
| 45 | fprojectedqty44 |  | numeric | 23 | 10 | √ | 0 |  |
| 46 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 47 | fprojectedqty43 |  | numeric | 23 | 10 | √ | 0 |  |
| 48 | fprojectedqty5 |  | numeric | 23 | 10 | √ | 0 |  |
| 49 | fprojectedqty42 |  | numeric | 23 | 10 | √ | 0 |  |
| 50 | fprojectedqty4 |  | numeric | 23 | 10 | √ | 0 |  |
| 51 | fprojectedqty41 |  | numeric | 23 | 10 | √ | 0 |  |
| 52 | fprojectedqty7 |  | numeric | 23 | 10 | √ | 0 |  |
| 53 | fprojectedqty40 |  | numeric | 23 | 10 | √ | 0 |  |
| 54 | fprojectedqty6 |  | numeric | 23 | 10 | √ | 0 |  |
| 55 | fprojectedqty49 |  | numeric | 23 | 10 | √ | 0 |  |
| 56 | fprojectedqty48 |  | numeric | 23 | 10 | √ | 0 |  |
| 57 | fprojectedqty50 |  | numeric | 23 | 10 | √ | 0 |  |
| 58 | fprojectedqty1 |  | numeric | 23 | 10 | √ | 0 |  |
| 59 | fprojectedqty0 |  | numeric | 23 | 10 | √ | 0 |  |
| 60 | fprojectedqty3 |  | numeric | 23 | 10 | √ | 0 |  |
| 61 | fprojectedqty2 |  | numeric | 23 | 10 | √ | 0 |  |
| 62 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 |
| 63 | fprojectedqty36 |  | numeric | 23 | 10 | √ | 0 |  |
| 64 | fprojectedqty35 |  | numeric | 23 | 10 | √ | 0 |  |
| 65 | fprojectedqty34 |  | numeric | 23 | 10 | √ | 0 |  |
| 66 | fqtytype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :预计可用库存 1 :需求 2 :供应 |
| 67 | fprojectedqty33 |  | numeric | 23 | 10 | √ | 0 |  |
| 68 | fprojectedqty32 |  | numeric | 23 | 10 | √ | 0 |  |
| 69 | fprojectedqty31 |  | numeric | 23 | 10 | √ | 0 |  |
| 70 | fprojectedqty30 |  | numeric | 23 | 10 | √ | 0 |  |
| 71 | fauxiliaryproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 72 | fprojectedqty39 |  | numeric | 23 | 10 | √ | 0 |  |
| 73 | fprojectedqty38 |  | numeric | 23 | 10 | √ | 0 |  |
| 74 | fprojectedqty37 |  | numeric | 23 | 10 | √ | 0 |  |
| 75 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 76 | finvqtyonhand | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_psw_cacdetail_fk |  | fid |
| 2 | pk_psw_cacdetail |  | fentryid |

---

## 材料可用性分析-主表 t_psw_cac

- **表名称：** 材料可用性分析-主表
- **表名：** t_psw_cac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fparauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fparmaterialmaster | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fmasterscheduleid | 计划编制id | int8 | 64 |  | √ | 0 | 计划编制id |
| 13 | fparmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_psw_cac_m0 |  | fbillno |
| 2 | pk_psw_cac |  | fid |
