# 费用项目与子要素对应表-sca_expenseitemsubelemen

## 费用项目与子要素对应表-主表 t_sca_expenseitemsubeleme

- **表名称：** 费用项目与子要素对应表-主表
- **表名：** t_sca_expenseitemsubeleme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmfgfeealloccoid | 制造费用分配（成本中心）id | int8 | 64 |  | √ | 0 | 制造费用分配（成本中心）id |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fallocamt | 费用项目金额累计 | numeric | 23 | 10 | √ | 0.0000000000 | 费用项目金额累计 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 17 | fbenefcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_expenseitemsubeleme |  | forgid,fcostaccountid |
| 2 | pk_t_sca_expenseitemsubeleme |  | fid |
