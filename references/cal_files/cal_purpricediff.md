# 标准成本差异余额表-cal_purpricediff

## 标准成本差异余额表-主表 t_cal_purpricediff

- **表名称：** 标准成本差异余额表-主表
- **表名：** t_cal_purpricediff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出成本差异 |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fseqnum | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | fcreatetype | 差异类型 | bpchar | 1 |  | √ | ' ' | 差异类型,枚举: G :订单价差 H :发票价差 K :费用价差 M :标准成本变更差异 P :材料耗用差异 Q :制造费用差异 R :未吸收费用 S :成本更新差异 T :其他价差 |
| 10 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 12 | fmonth | 月 | int8 | 64 |  | √ | 0 | 月 |
| 13 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 16 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 结束期间 |
| 17 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fperiodid | 记账期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 21 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 24 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 25 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系（已作废） bd_accountingsys |
| 26 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 cal_bd_calpolicy |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 29 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 30 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 31 | fperiod | 导入期间 | int8 | 64 |  | √ | 0 | 导入期间 |
| 32 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_purpricediff_pkey |  | fid |
| 2 | idx_cal_purpricediff_mat |  | fmaterialid |
