# 未吸收费用差异单-sco_unabsorbdiff

## 单据体-子表 t_sco_unabsorbdiffentry

- **表名称：** 单据体-子表
- **表名：** t_sco_unabsorbdiffentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_unabsorbdiffentry2 |  | fid |
| 2 | pk_sco_unabsorbdiffentry |  | fentryid |
| 3 | idx_sco_unabsorbdiffentry |  | felementid,fsubelementid |

---

## 未吸收费用差异单-主表 t_sco_unabsorbdiff

- **表名称：** 未吸收费用差异单-主表
- **表名：** t_sco_unabsorbdiff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdifftotal | 差异总额 | numeric | 23 | 10 | √ | 0 | 差异总额 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fadjustbill | 成本调整单id | int8 | 64 |  | √ | 0 | 成本调整单id |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 10 | fsettlementobj | 结算对象 | varchar | 50 |  | √ | 'MAT' | 结算对象,枚举: MAT :物料 GL :总账 FAX :固定资产 |
| 11 | fadjustnum | 成本调整单编号 | varchar | 80 |  | √ | ' ' | 成本调整单编号 |
| 12 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdifftype | 差异类型 | varchar | 30 |  | √ | '0' | 差异类型,枚举: 4 :未吸收费用差异 3 :成本更新差异 |
| 21 | fcarrynumid | fcarrynumid | varchar | 80 |  | √ | ' ' |  |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fproallocgen | 期末成本计算生成 | varchar | 30 |  | √ | '0' | 期末成本计算生成 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_unabsorbdiff |  | forgid,fperiodid,fcostaccountid,fcostcenterid |
| 2 | pk_sco_unabsorbdiff |  | fid |
