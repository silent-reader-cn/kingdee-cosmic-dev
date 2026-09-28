# 智能方案预置过滤-gl_intelloper_filter

## 智能方案预置过滤-主表 t_gl_intelloper_filter

- **表名称：** 智能方案预置过滤-主表
- **表名：** t_gl_intelloper_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizapp | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fbussiness | 业务类型 | varchar | 36 |  | √ | ' ' | 业务类型,枚举: |
| 4 | foper | 执行操作 | varchar | 36 |  | √ | ' ' | 执行操作,枚举: |
| 5 | ffilter | 过滤条件 | varchar | 36 |  | √ | ' ' | 过滤条件 |
| 6 | fhash | hash值 | int8 | 64 |  | √ | 0 | hash值 |
| 7 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | ' ' | 过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_intelloper_filter |  | fhash |
| 2 | t_gl_intelloper_filter_pkey |  | fid |
