# 短信使用数量-wf_smsusingquantity

## 短信使用数量-主表 t_wf_smsusingquantity

- **表名称：** 短信使用数量-主表
- **表名：** t_wf_smsusingquantity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpermitenddate | 许可到期时间 | timestamp | 0 |  |  | null | 许可到期时间 |
| 3 | fsmsnumber | 已使用短信数量 | varchar | 500 |  | √ | ' ' | 已使用短信数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_smsusingquantity |  | fpermitenddate |
| 2 | pk_t_wf_smsusingquantity |  | fid |
