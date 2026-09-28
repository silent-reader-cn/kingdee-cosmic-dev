# 描述大文本-plm_ipd_description

## 描述大文本-主表 t_plm_ipd_description

- **表名称：** 描述大文本-主表
- **表名：** t_plm_ipd_description

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flargetext | 大文本 | varchar | 255 |  | √ | ' ' | 大文本 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fabstracttext_tag | 摘要_详情 | text | 0 |  |  | null | 摘要_详情 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | flargetext_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 7 | fbillid | 所属单据 | varchar | 50 |  | √ | ' ' | 所属单据 |
| 8 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fabstracttext | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_description |  | fid |
| 2 | idx_plm_desc_number |  | fnumber |
