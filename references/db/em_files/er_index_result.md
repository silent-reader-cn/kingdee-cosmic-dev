# 指标结果详情-er_index_result

## 指标结果详情-主表 t_er_index_result

- **表名称：** 指标结果详情-主表
- **表名：** t_er_index_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresult_tag | 结果集_详情 | text | 0 |  |  | ' ' | 结果集_详情 |
| 3 | forgid | 根组织id | varchar | 50 |  | √ | ' ' | 根组织id |
| 4 | fresult | 结果集 | varchar | 255 |  | √ | ' ' | 结果集 |
| 5 | fendtime | 页面结束日期 | timestamp | 0 |  |  | null | 页面结束日期 |
| 6 | fcachekey | 指标key | varchar | 255 |  | √ | ' ' | 指标key |
| 7 | fstarttime | 页面开始日期 | timestamp | 0 |  |  | null | 页面开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_index_result_cache |  | fcachekey |
| 2 | pk_t_er_index_result |  | fid |
| 3 | idx_er_index_result_time |  | fstarttime,fendtime,forgid |
