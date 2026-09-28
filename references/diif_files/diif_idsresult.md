# 智能销售预测结果-diif_idsresult

## 智能销售预测结果-主表 t_diif_idsresult

- **表名称：** 智能销售预测结果-主表
- **表名：** t_diif_idsresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcurrentdate | 当前期 | timestamp | 0 |  |  | null | 当前期 |
| 4 | fidsschemeid | 方案id | varchar | 50 |  | √ | ' ' | 方案id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_idsresult_schemeid |  | fidsschemeid |
| 2 | pk_t_diif_idsresult |  | fid |

---

## 单据体-子表 t_diif_idsresultentry

- **表名称：** 单据体-子表
- **表名：** t_diif_idsresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprevalue | 预测值 | numeric | 23 | 10 | √ | 0 | 预测值 |
| 3 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 销售部门 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性 |
| 6 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 |
| 7 | fprevaluetype | 预测值类型 | varchar | 50 |  | √ | ' ' | 预测值类型 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcustomergroupid | 客户分类 | int8 | 64 |  | √ | 0 | 客户分类 |
| 10 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 销售组织 |
| 11 | fforecastcycle | 预测时间 | timestamp | 0 |  |  | null | 预测时间 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 销售组 |
| 14 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_idsresultentry |  | fid |
| 2 | pk_t_diif_idsresultentry |  | fentryid |
