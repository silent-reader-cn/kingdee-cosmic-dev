# 差异分摊报告-calx_diffallocrpt

## 差异分摊报告-主表 t_cal_diffallocrpt

- **表名称：** 差异分摊报告-主表
- **表名：** t_cal_diffallocrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 10 | fallocrecordid | 分摊记录ID | int8 | 64 |  | √ | 0 | 分摊记录ID |
| 11 | fcarryrule | 差异结转规则 | varchar | 30 |  | √ | ' ' | 差异结转规则,枚举: A :按数量比例结转 B :按金额比例结转 |
| 12 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 13 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 14 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 15 | fcaldimensionvalue | 核算维度值 | varchar | 255 |  | √ | ' ' | 核算维度值 |
| 16 | fallocmodel | 分摊方式 | varchar | 30 |  | √ | ' ' | 分摊方式,枚举: A :按单据编号 B :按单据类型 |
| 17 | fcreatorid | 分摊人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 19 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 G :先进先出法 |
| 20 | falloctime | 分摊时间 | timestamp | 0 |  |  | null | 分摊时间 |
| 21 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 22 | fdividebasisvalue | 划分依据值 | varchar | 255 |  | √ | ' ' | 划分依据值 |
| 23 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_diffallocrpt_ca |  | fcostaccountid |
| 2 | idx_cal_diffallocrpt_mat |  | fmaterialid |
| 3 | pk_cal_diffallocrpt |  | fid |

---

## 单据体-子表 t_cal_diffallocrptentry

- **表名称：** 单据体-子表
- **表名：** t_cal_diffallocrptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | foutstr | 发出 | varchar | 255 |  | √ | ' ' | 发出 |
| 4 | fbalancestr | 结存 | varchar | 255 |  | √ | ' ' | 结存 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | foutamt | 发出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发出金额 |
| 8 | finstr | 收入 | varchar | 255 |  | √ | ' ' | 收入 |
| 9 | fsortseq | 排序序号 | int8 | 64 |  | √ | 0 | 排序序号 |
| 10 | fbilltypestr | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型 |
| 11 | fcreatetype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: B :实际成本 G :订单价差 H :发票价差 K :费用价差 P :材料耗用差异 Q :制造费用差异 R :未吸收费用 M :标准成本变更差异 S :成本更新差异 T :其他价差 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | foutbillqty | 出库单数量或金额 | numeric | 23 | 10 | √ | 0.0000000000 | 出库单数量或金额 |
| 14 | fbilltypeid | 单据类型ID | int8 | 64 |  | √ | 0 | 单据类型ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_diffallocrptentry |  | fentryid |
| 2 | idx_cal_diffallocrptentry_ct |  | fcreatetype |
| 3 | idx_cal_diffallocrptentry_eid |  | fentryid |
| 4 | idx_cal_diffallocrptentry_se |  | fsubelementid |

---

## 子单据体-子表 t_cal_diffallocrptentrydt

- **表名称：** 子单据体-子表
- **表名：** t_cal_diffallocrptentrydt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdtoutbillqty | 出库单数量或金额 | numeric | 23 | 10 | √ | 0.0000000000 | 出库单数量或金额 |
| 2 | fdtoutstr | 发出 | varchar | 255 |  | √ | ' ' | 发出 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fcostadjbillno | 成本调整单 | varchar | 80 |  | √ | ' ' | 成本调整单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_diffallocrptentrydt |  | fdetailid |
| 2 | idx_cal_diffalrptedt_eid |  | fentryid |
