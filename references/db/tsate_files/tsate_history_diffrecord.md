# 税局版申报表比对记录-tsate_history_diffrecord

## 税局版申报表比对记录-主表 t_tsate_sbb_diff

- **表名称：** 税局版申报表比对记录-主表
- **表名：** t_tsate_sbb_diff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdetail | 比对详情 | varchar | 200 |  | √ | ' ' | 比对详情 |
| 4 | fhistorysbbid | 税局版申报表id | varchar | 50 |  | √ | ' ' | 税局版申报表id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fresult | 比对结果 | varchar | 50 |  | √ | ' ' | 比对结果,枚举: undo :未比对 comparing :比对中 diff :有差异 same :无差异 nodata :无比对数据 fail :比对失败 noneed :无需比对 |
| 7 | fdetail_tag | 比对详情_详情 | text | 0 |  |  | null | 比对详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_diff |  | fid |
| 2 | idx_tsatesbbdiff_1 |  | fhistorysbbid |
