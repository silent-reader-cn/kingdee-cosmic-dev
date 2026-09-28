# 生产成本差异结转单-sco_prodiffbill

## 单据体-子表 t_sco_prodiffbillentry

- **表名称：** 单据体-子表
- **表名：** t_sco_prodiffbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fentrycurdiffamt | 本期差异金额 | numeric | 23 | 10 | √ | 0 | 本期差异金额 |
| 4 | fentrycurcarryamt | 本期结转金额 | numeric | 23 | 10 | √ | 0 | 本期结转金额 |
| 5 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fsumrate | 累计结转比例 | numeric | 23 | 10 | √ | 0 | 累计结转比例 |
| 7 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 11 | fcarryrate | 规则结转比例 | numeric | 23 | 10 | √ | 0 | 规则结转比例 |
| 12 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: 4 :未吸收差异 3 :成本更新差异 1 :材料耗用差异 2 :制造费用耗用差异 |
| 13 | fentrysourcebill | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 14 | fentryendamt | 期末差异余额 | numeric | 23 | 10 | √ | 0 | 期末差异余额 |
| 15 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 16 | fexerate | 执行结转比例 | numeric | 23 | 10 | √ | 0 | 执行结转比例 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fentrystartamt | 期初差异余额 | numeric | 23 | 10 | √ | 0 | 期初差异余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_prodiffbillentry |  | fcostobjectid,felementid,fsubelementid |
| 2 | pk_sco_prodiffbillentry |  | fentryid |
| 3 | idx_sco_prodiffbillentry2 |  | fid |

---

## 生产成本差异结转单-主表 t_sco_prodiffbill

- **表名称：** 生产成本差异结转单-主表
- **表名：** t_sco_prodiffbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendamount | 期末差异余额 | numeric | 23 | 10 | √ | 0 | 期末差异余额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fdiffruleid | fdiffruleid | varchar | 255 |  | √ | ' ' |  |
| 6 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcurcarryamount | 本期结转金额 | numeric | 23 | 10 | √ | 0 | 本期结转金额 |
| 11 | fvoucher | fvoucher | varchar | 255 |  | √ | ' ' |  |
| 12 | fvouchernum | 凭证字号 | varchar | 80 |  | √ | ' ' | 凭证字号 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fsourcebill | 来源单据 | varchar | 255 |  | √ | ' ' | 来源单据,枚举: 0 :完工结算差异单 1 :未吸收差异单 |
| 15 | fdiffrule | 差异结转规则 | varchar | 255 |  | √ | ' ' | 差异结转规则,枚举: MANUAL :手工录入 MULTIINPUTAMT :综合销售出库金额/（期初库存余额+本期入库金额） PRODINPUTAMT :产品销售出库金额/（期初库存余额+本期入库金额） |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcurdiffamount | 本期差异金额 | numeric | 23 | 10 | √ | 0 | 本期差异金额 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 20 | fstartamount | 期初差异余额 | numeric | 23 | 10 | √ | 0 | 期初差异余额 |
| 21 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_prodiffbill |  | forgid,fcostaccountid,fcostcenterid |
| 2 | pk_sco_prodiffbill |  | fid |
