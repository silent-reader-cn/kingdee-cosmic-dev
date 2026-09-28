# 凭证冲销关系-gl_reverserelation

## 单据体-子表 t_gl_reverserelationentry

- **表名称：** 单据体-子表
- **表名：** t_gl_reverserelationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frdebitamount | 冲销借 | numeric | 19 | 6 | √ | 0.000000 | 冲销借 |
| 3 | frecreditamount | 冲销贷 | numeric | 19 | 6 | √ | 0.000000 | 冲销贷 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsdebitamount | 源借 | numeric | 19 | 6 | √ | 0.000000 | 源借 |
| 6 | fscreditamount | 源贷 | numeric | 19 | 6 | √ | 0.000000 | 源贷 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_reverserelationentry_pkey |  | fentryid |
| 2 | idx_gl_reverserelationentry |  | fid |

---

## 凭证冲销关系-主表 t_gl_reverserelation

- **表名称：** 凭证冲销关系-主表
- **表名：** t_gl_reverserelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentityid | 源凭证(冲销)ID | int8 | 64 |  | √ | 0 | 源凭证(冲销)ID |
| 3 | ftargentityid | 目标凭证ID | int8 | 64 |  | √ | 0 | 目标凭证ID |
| 4 | fiseffective | 是否生效 | bpchar | 1 |  | √ | ' ' | 是否生效 |
| 5 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reverserelation |  | fsrcentityid |
| 2 | t_gl_reverserelation_pkey |  | fid |
