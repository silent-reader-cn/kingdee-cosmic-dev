# 手动付款记录表-er_manualpay

## 手动付款记录表-主表 t_er_mannualpay

- **表名称：** 手动付款记录表-主表
- **表名：** t_er_mannualpay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatusbeforepay | 手动付款前状态 | varchar | 5 |  | √ | ' ' | 手动付款前状态 |
| 3 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 4 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mannualpay |  | fbillno,fformid |
| 2 | t_er_mannualpay_pkey |  | fid |
