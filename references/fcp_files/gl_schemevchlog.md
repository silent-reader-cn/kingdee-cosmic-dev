# 期末方案生成凭证记录-gl_schemevchlog

## 期末方案生成凭证记录-主表 t_gl_schemevchlog

- **表名称：** 期末方案生成凭证记录-主表
- **表名：** t_gl_schemevchlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证 | int8 | 64 |  | √ | 0 | 凭证 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 4 | fschemeid | 期末方案执行记录 | int8 | 64 |  | √ | 0 | 期末方案执行记录 |
| 5 | fvchsource | 凭证来源 | varchar | 30 |  | √ | ' ' | 凭证来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_schemevchlog_fsid |  | fschemeid |
| 2 | pk_gl_schemevchlog |  | fid |
