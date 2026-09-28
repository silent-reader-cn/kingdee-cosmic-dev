# 监控设置-fa_riskmonitoring_setting

## 分录-子表 t_fa_risksettingentry

- **表名称：** 分录-子表
- **表名：** t_fa_risksettingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 值 | int8 | 64 |  | √ | 0 | 值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcondition | 条件 | varchar | 2 |  | √ | ' ' | 条件,枚举: = :等于 <> :不等于 >= :大于等于 > :大于 <= :小于等于 < :小于 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fassetcategoryid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 7 | fwarningvalue | 预警 | varchar | 255 |  | √ | ' ' | 预警 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_risksettingentry |  | fid |
| 2 | t_fa_risksettingentry_pkey |  | fentryid |

---

## 监控设置-主表 t_fa_risksetting

- **表名称：** 监控设置-主表
- **表名：** t_fa_risksetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_risksetting_pkey |  | fid |
| 2 | idx_fa_risksetting |  | forgid,fcreaterid |
