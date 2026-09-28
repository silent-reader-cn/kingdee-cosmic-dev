# 弹性域测试单据-isc_demo_flex_test

## 单据体-子表 t_isc_demo_flex_testentry

- **表名称：** 单据体-子表
- **表名：** t_isc_demo_flex_testentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillino | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 3 | fentry_demo | 弹性域demo | int8 | 64 |  | √ | 0 | 弹性域配置测试 isc_demo_flex |
| 4 | fentry_flex | 弹性域 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_demo_flex_testentry |  | fentryid |
| 2 | i_t_isc_demo_flex_testentry |  | fid |

---

## 弹性域测试单据-主表 t_isc_demo_flex_test

- **表名称：** 弹性域测试单据-主表
- **表名：** t_isc_demo_flex_test

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fflex | 弹性域 | int8 | 64 |  | √ | 0 | null 002 |
| 3 | fflexfield | fflexfield | int8 | 64 |  | √ | 0 |  |
| 4 | fbasedatafield | 弹性域demo | int8 | 64 |  | √ | 0 | 弹性域配置测试 isc_demo_flex |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_demo_flex_test |  | fid |
| 2 | index_t_isc_demo_flex_test |  | fnumber |
