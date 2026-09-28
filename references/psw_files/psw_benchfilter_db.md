# 工作台首页筛选落库-psw_benchfilter_db

## 工作台首页筛选落库-主表 t_psw_workbench

- **表名称：** 工作台首页筛选落库-主表
- **表名：** t_psw_workbench

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fproductionline | 生产线 | varchar | 500 |  |  | null | 生产线 |
| 4 | fbillstatus | 单据状态 | varchar | 500 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fwarehousetype | 库存类型 | varchar | 500 |  |  | null | 库存类型 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 8 | fwarehousestate | 库存状态 | varchar | 500 |  |  | null | 库存状态 |
| 9 | fplanmonth | 计划月数 | int8 | 64 |  |  | null | 计划月数 |
| 10 | fplanday | 计划日数 | int8 | 64 |  |  | null | 计划日数 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | freqiureorg | 需求组织 | varchar | 500 |  |  | null | 需求组织 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fwarehouse | 库存 | varchar | 500 |  |  | null | 库存 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fpredate | 前置时段 | int8 | 64 |  |  | null | 前置时段 |
| 17 | fplangroup | 计划分组 | varchar | 500 |  |  | null | 计划分组 |
| 18 | fstartdate | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 19 | fplanweek | 计划周数 | int8 | 64 |  |  | null | 计划周数 |
| 20 | fmaterial | 物料 | varchar | 500 |  |  | null | 物料 |
| 21 | fbillno | 单据编号 | varchar | 30 |  |  | null | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_wb_union |  | forgid |
| 2 | pk_t_psw_workbench |  | fid |
