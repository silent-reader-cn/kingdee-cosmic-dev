# 最大流水号表-fbd_maxserialnum

## 最大流水号表-主表 t_fbd_maxserialnum

- **表名称：** 最大流水号表-主表
- **表名：** t_fbd_maxserialnum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 3 | fprefix | 前缀 | varchar | 50 |  | √ | ' ' | 前缀 |
| 4 | fmaxserialnum | 最大号 | varchar | 50 |  | √ | ' ' | 最大号 |
| 5 | fpropkey | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_maxserialnum |  | fmaxserialnum |
| 2 | inx_fbd_maxserialnum |  | fentityname,fpropkey,fprefix |
| 3 | pk_t_fbd_maxserialnum |  | fid |
