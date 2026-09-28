# 初始化子任务单据-ipop_init_bill_itemcfg

## 初始化子任务单据-主表 t_ipop_init_item

- **表名称：** 初始化子任务单据-主表
- **表名：** t_ipop_init_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomer | 甲方负责人 | varchar | 100 |  | √ | ' ' | 甲方负责人 |
| 3 | fmarkfinished | 标记完成 | varchar | 50 |  | √ | ' ' | 标记完成 |
| 4 | fmarkstatus | 标记状态 | varchar | 10 |  | √ | ' ' | 标记状态,枚举: 1 :已完成 0 :未完成 |
| 5 | findex | 事项顺序 | int4 | 32 |  | √ | 0 | 事项顺序 |
| 6 | fitemname | 事项名称 | varchar | 200 |  | √ | ' ' | 事项名称 |
| 7 | fknowledge | 社区知识 | varchar | 255 |  | √ | ' ' | 社区知识 |
| 8 | fadviser | 实施顾问 | varchar | 100 |  | √ | ' ' | 实施顾问 |
| 9 | fitemid | 事项ID | varchar | 30 |  | √ | ' ' | 事项ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_item |  | fid |
| 2 | idx_ipop_init_item_itid |  | fitemid |
