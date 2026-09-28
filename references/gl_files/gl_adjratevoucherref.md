# 调汇凭证关系-gl_adjratevoucherref

## 调汇凭证关系-主表 t_gl_adjratevoucherref

- **表名称：** 调汇凭证关系-主表
- **表名：** t_gl_adjratevoucherref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 3 | fadjrateid | 调汇方案id | int8 | 64 |  | √ | 0 | 调汇方案id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_adjratevoucher_adjid |  | fadjrateid |
| 2 | t_gl_adjratevoucherref_pkey |  | fid |
