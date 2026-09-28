# 模板样式方案维度数据-xkrpt_wizarddimedata

## 模板样式方案维度数据-主表 t_xkrpt_wizarddimedata

- **表名称：** 模板样式方案维度数据-主表
- **表名：** t_xkrpt_wizarddimedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptid | 报表Id | varchar | 36 |  | √ | ' ' | 报表Id |
| 3 | forgid | 组织ID | int8 | 64 |  | √ | 0 | 组织ID |
| 4 | fschemeid | 模板样式方案ID | int8 | 64 |  | √ | 0 | 模板样式方案ID |
| 5 | fscopetypeid | 合并方案ID | int8 | 64 |  | √ | 0 | 合并方案ID |
| 6 | fdata | 数据 | text | 0 |  |  | ' ' | 数据 |
| 7 | fscopeid | 合并范围Id | int8 | 64 |  | √ | 0 | 合并范围Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizarddimedata |  | fid |
| 2 | idx_wd_schemeid_orgid |  | fschemeid,forgid |
