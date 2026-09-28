# 待修复的发票数据-sim_repair_invoice

## 待修复的发票数据-主表 t_sim_repair_invoice

- **表名称：** 待修复的发票数据-主表
- **表名：** t_sim_repair_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoicepk | 发票主键 | int8 | 64 |  | √ | 0 | 发票主键 |
| 3 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 4 | fbusinesstype | 业务类型 | varchar | 10 |  | √ | ' ' | 业务类型,枚举: 0 :PDF发票重新生成 |
| 5 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 6 | forderno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_repair_invoice |  | fid |
| 2 | idx_sim_repair_invoice |  | finvoicepk |
