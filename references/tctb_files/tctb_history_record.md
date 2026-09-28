# 纳税申报相关联记录-tctb_history_record

## 纳税申报相关联记录-主表 t_tctb_history_record

- **表名称：** 纳税申报相关联记录-主表
- **表名：** t_tctb_history_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecord_tag | 历史数据_详情 | text | 0 |  |  | null | 历史数据_详情 |
| 3 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 4 | ftype | 类型 | varchar | 100 |  | √ | ' ' | 类型 |
| 5 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 6 | frecord | 历史数据 | varchar | 510 |  | √ | ' ' | 历史数据 |
| 7 | fserialno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | forgid | 组织id | varchar | 100 |  | √ | ' ' | 组织id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_history_record_pkey |  | fid |
| 2 | idx_t_tctb_history_record |  | forgid |
