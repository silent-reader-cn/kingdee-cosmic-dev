# 附件关系表-rim_attach_relation

## 附件关系表-主表 t_rim_attach_relation

- **表名称：** 附件关系表-主表
- **表名：** t_rim_attach_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelation_id | 发票序列号 | varchar | 50 |  | √ | ' ' | 发票序列号 |
| 3 | frelation_type | 关系类型 | varchar | 10 |  | √ | ' ' | 关系类型,枚举: 1 :报销单 2 :发票 |
| 4 | fexpense_id | 报销单id | varchar | 50 |  | √ | ' ' | 报销单id |
| 5 | fattach_id | 附件id | varchar | 50 |  | √ | ' ' | 附件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_attach_relation |  | frelation_type,frelation_id |
| 2 | pk_rim_attach_relation |  | fid |
