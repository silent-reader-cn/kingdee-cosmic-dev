# 岗位汇报关系s-HR同步映射关系列表-xkbos_postreport_shrmap

## 岗位汇报关系s-HR同步映射关系列表-主表 t_sec_preportrelation

- **表名称：** 岗位汇报关系s-HR同步映射关系列表-主表
- **表名：** t_sec_preportrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 3 | fxksource | 数据来源 | int8 | 64 |  |  | 0 | [数据来源 xkbos_data_sources](../xkbase_files/xkbos_data_sources.md) |
| 4 | fpositionid | 岗位 | int8 | 64 |  | √ | 0 | [岗位 bos_position](../base_files/bos_position.md) |
| 5 | fsuperiorpositionid | 上级岗位 | int8 | 64 |  | √ | 0 | [岗位 bos_position](../base_files/bos_position.md) |
| 6 | fxkisshrpost | 是否存在s-HR同步映射关系 | bpchar | 1 |  |  | ' ' | 是否存在s-HR同步映射关系,枚举: 0 :否 1 :是 |
| 7 | fxkidstr | 内码id | varchar | 50 |  |  | ' ' | 内码id |
| 8 | freporttypeid | 汇报类型 | int8 | 64 |  | √ | 0 | [汇报类型 bos_reporttype](../base_files/bos_reporttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_preportrelation |  | fid |
| 2 | idx_sec_preportrela_typepos |  | freporttypeid,fpositionid |
