# 标准成本差异余额表-cal_purpricediff

## 标准成本差异余额表-主表 t_cal_purpricediff

- **表名称：** 标准成本差异余额表-主表
- **表名：** t_cal_purpricediff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出成本差异 |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fseqnum | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 9 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 10 | fcreatetype | 差异类型 | bpchar | 1 |  | √ | ' ' | 差异类型,枚举: G :订单价差 H :发票价差 K :费用价差 M :标准成本变更差异 P :材料耗用差异 Q :制造费用差异 R :未吸收费用 S :成本更新差异 T :其他价差 |
| 11 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fmonth | 月 | int8 | 64 |  | √ | 0 | 月 |
| 14 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 17 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 结束期间 |
| 18 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fperiodid | 记账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 22 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 24 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 27 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系（已作废） bd_accountingsys](../fibd_files/bd_accountingsys.md) |
| 28 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 29 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 31 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 32 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 33 | fperiod | 导入期间 | int8 | 64 |  | √ | 0 | 导入期间 |
| 34 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_purpricediff_pkey |  | fid |
| 2 | idx_cal_purpricediff_mat |  | fmaterialid |
