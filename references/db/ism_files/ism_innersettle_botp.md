# 内部交易单据生成转换规则记录-ism_innersettle_botp

## 内部交易单据生成转换规则记录-主表 t_ism_innersettle_botp

- **表名称：** 内部交易单据生成转换规则记录-主表
- **表名：** t_ism_innersettle_botp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbotpid | 转换规则 | varchar | 50 |  | √ | ' ' | 转换规则 |
| 3 | fcreatetime | 生成日期 | timestamp | 0 |  |  | null | 生成日期 |
| 4 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 5 | fentitynumber | 元数据编码 | varchar | 50 |  | √ | ' ' | 元数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_innersettle_botp |  | fid |
| 2 | idx_t_ism_innersettle_botp_0 |  | fbillid,fentitynumber |
