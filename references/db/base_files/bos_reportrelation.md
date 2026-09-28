# 汇报关系-bos_reportrelation

## 汇报关系-主表 t_sec_preportrelation

- **表名称：** 汇报关系-主表
- **表名：** t_sec_preportrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 3 | fpositionid | 岗位 | int8 | 64 |  | √ | 0 | 岗位 bos_position |
| 4 | fsuperiorpositionid | 上级岗位 | int8 | 64 |  | √ | 0 | 岗位 bos_position |
| 5 | freporttypeid | 汇报类型 | int8 | 64 |  | √ | 0 | 汇报类型 bos_reporttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_preportrelation |  | fid |
| 2 | idx_sec_preportrela_typepos |  | freporttypeid,fpositionid |
