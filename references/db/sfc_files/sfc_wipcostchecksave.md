# 车间在产品盘点(后台表)-sfc_wipcostchecksave

## 车间在产品盘点(后台表)-主表 t_sfc_wipcostcheck

- **表名称：** 车间在产品盘点(后台表)-主表
- **表名：** t_sfc_wipcostcheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fcheckprodqty | 实盘生产数量 | numeric | 23 | 10 | √ | 0 | 实盘生产数量 |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fwipmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 7 | fcheckbaseqty | 实盘基本数量 | numeric | 23 | 10 | √ | 0 | 实盘基本数量 |
| 8 | fwipcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fwipmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 10 | fcheckqty | 实盘数量 | numeric | 23 | 10 | √ | 0 | 实盘数量 |
| 11 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 12 | fwipcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_wipcostcheck_cpid |  | fcostaccountid,fperiodid,fproplanentryid |
| 2 | pk_sfc_wipcostcheck |  | fid |
