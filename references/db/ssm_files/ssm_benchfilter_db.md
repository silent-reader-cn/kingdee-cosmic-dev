# 采购工作台首页筛选落库-ssm_benchfilter_db

## 采购工作台首页筛选落库-主表 t_ssm_workbench

- **表名称：** 采购工作台首页筛选落库-主表
- **表名：** t_ssm_workbench

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fasofdate | asofdate | timestamp | 0 |  |  | null | asofdate |
| 4 | fwarehousetype | 库存类型 | varchar | 50 |  | √ | ' ' | 库存类型 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fplanmonth | 计划月数 | int8 | 64 |  | √ | 0 | 计划月数 |
| 8 | fwarehousestate | 库存状态 | varchar | 50 |  | √ | ' ' | 库存状态 |
| 9 | fplanday | 计划日数 | int8 | 64 |  | √ | 0 | 计划日数 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | forg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fwarehouse | 库存 | varchar | 50 |  | √ | ' ' | 库存 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fpredate | 前置时段 | int8 | 64 |  | √ | 0 | 前置时段 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstartdate | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 17 | frange | frange | varchar | 50 |  | √ | ' ' |  |
| 18 | fplanweek | 计划周数 | int8 | 64 |  | √ | 0 | 计划周数 |
| 19 | fmaterial | 物料 | varchar | 50 |  | √ | ' ' | 物料 |
| 20 | fschemelist1 | fschemelist1 | varchar | 50 |  | √ | ' ' |  |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | freceiveorg | 库存组织 | varchar | 50 |  | √ | ' ' | 库存组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_workbench_m0 |  | fbillno |
| 2 | pk_ssm_workbench |  | fid |
