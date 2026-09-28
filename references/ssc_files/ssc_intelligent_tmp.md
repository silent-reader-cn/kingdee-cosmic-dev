# 智能质检数据临时表-ssc_intelligent_tmp

## 智能质检数据临时表-主表 t_tk_intelligenttmp

- **表名称：** 智能质检数据临时表-主表
- **表名：** t_tk_intelligenttmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemtext | 费用项目 | varchar | 50 |  | √ | ' ' | 费用项目 |
| 3 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 4 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_intellittmp_fbillid |  | fbillid |
| 2 | pk_t_tk_intelligenttmp |  | fid |
