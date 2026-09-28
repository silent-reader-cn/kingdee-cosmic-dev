# 模板评价-bos_nocode_tpl_comment

## 模板评价-主表 t_nocode_tpl_comment

- **表名称：** 模板评价-主表
- **表名：** t_nocode_tpl_comment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 4 | fcomment | 评价 | varchar | 500 |  | √ | ' ' | 评价 |
| 5 | fuid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fscore | 评分 | int4 | 32 |  | √ | 0 | 评分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_tpl_ftemplateid |  | ftemplateid |
| 2 | pk_nocode_tpl_comment |  | fid |
