# 时段设置-mrp_dateset

## 时段设置-子表 t_mrp_datesetentry

- **表名称：** 时段设置-子表
- **表名：** t_mrp_datesetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnum | 个数 | int4 | 32 |  | √ | 0 | 个数 |
| 3 | fisnatural | 按自然周/月 | bpchar | 1 |  | √ | '0' | 按自然周/月 |
| 4 | ftype | 单位 | varchar | 10 |  | √ | ' ' | 单位,枚举: 1 :日 2 :周 3 :月 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_datesetentry |  | fentryid |
| 2 | idx_t_mrp_datesetentry |  | fid,fseq |

---

## 时段设置-主表 t_mrp_dateset

- **表名称：** 时段设置-主表
- **表名：** t_mrp_dateset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_dateset |  | fid |
| 2 | idx_t_mrp_dateset_fnum |  | fnumber |
