# 待考评的专家-src_evaluateexpert

## 待考评的专家-主表 t_src_evaluateexperthead

- **表名称：** 待考评的专家-主表
- **表名：** t_src_evaluateexperthead

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fschemeid | 待考评专家批量获取方案 | int8 | 64 |  | √ | 0 | 扩展过滤 pds_extfilter |
| 5 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 6 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateexperthead_pid |  | fparentid |
| 2 | pk_src_evaluateexperthead |  | fid |

---

## 专家分录-子表 t_src_evaluateexpert

- **表名称：** 专家分录-子表
- **表名：** t_src_evaluateexpert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliertype | 专家类别 | varchar | 50 |  | √ | ' ' | 专家类别,枚举: src_expert :评标专家 |
| 3 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisevaluatepush | 下达否 | bpchar | 1 |  | √ | '0' | 下达否 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsupplierid | 专家编码 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 9 | fentryparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluateexpert |  | fentryid |
| 2 | idx_src_evaluateexpert_sid |  | fsupplierid |
| 3 | idx_src_evaluateexpert_pid |  | fentryparentid |
| 4 | idx_src_evaluateexpert_fid |  | fid |
