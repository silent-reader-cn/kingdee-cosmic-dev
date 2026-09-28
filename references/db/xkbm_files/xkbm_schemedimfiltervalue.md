# 维度过滤值数据-xkbm_schemedimfiltervalue

## 维度过滤值数据-主表 t_xkbm_schemefiltervalue

- **表名称：** 维度过滤值数据-主表
- **表名：** t_xkbm_schemefiltervalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautorptschemeid | 自动方案id | int8 | 64 |  | √ | 0 | 自动方案id |
| 3 | fdata | 维度过滤字符串 | text | 0 |  |  | ' ' | 维度过滤字符串 |
| 4 | fschemeentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 5 | fsampleid | 模板id | varchar | 36 |  | √ | ' ' | 模板id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_schemefiltervalue |  | fid |
| 2 | idx_xkbm_schfiltervalue |  | fautorptschemeid,fsampleid,fschemeentryid |
