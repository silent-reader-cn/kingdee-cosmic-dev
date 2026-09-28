# 税收优惠统计历史记录表-tctrc_preference_record

## 单据体-子表 t_tctrc_prefer_record_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_prefer_record_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxationsysid | 税收制度 | varchar | 50 |  | √ | ' ' | 税收制度 |
| 3 | fstatisticprotid | 优惠项目 | varchar | 50 |  | √ | ' ' | 优惠项目 |
| 4 | ftaxcategoryid | 税种 | varchar | 50 |  | √ | ' ' | 税种 |
| 5 | famountincome | 所得额优惠 | varchar | 50 |  | √ | ' ' | 所得额优惠 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpreferenttax | 税额优惠 | varchar | 50 |  | √ | ' ' | 税额优惠 |
| 8 | famount | 优惠金额 | varchar | 50 |  | √ | ' ' | 优惠金额 |
| 9 | fskssqq | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 10 | fpreferenttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | forg | 税务组织 | varchar | 50 |  | √ | ' ' | 税务组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_prefer_record_djt |  | fentryid |
| 2 | idx_tctrc_prefer_record_djt_fk |  | fid |

---

## 税收优惠统计历史记录表-主表 t_tctrc_preference_record

- **表名称：** 税收优惠统计历史记录表-主表
- **表名：** t_tctrc_preference_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsbbid | 关联id | int8 | 64 |  | √ | 0 | 关联id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_preference_record |  | fid |
| 2 | idx_tctrc_precored_sbbid |  | fsbbid |
