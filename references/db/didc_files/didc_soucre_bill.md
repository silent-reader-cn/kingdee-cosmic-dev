# 取值来源单据-didc_soucre_bill

## 取值来源单据-主表 t_didc_soucre_bill

- **表名称：** 取值来源单据-主表
- **表名：** t_didc_soucre_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findexid | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_soucre_bill |  | findexid |
| 2 | pk_t_didc_soucre_bill |  | fid |
