# 产能调整-psw_adjcap

## 产能调整-主表 t_psw_adjcap

- **表名称：** 产能调整-主表
- **表名：** t_psw_adjcap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_adjcap_line |  | flineid |
| 2 | pk_t_psw_adjcap |  | fid |

---

## 调整明细-子表 t_psw_adjcapentry

- **表名称：** 调整明细-子表
- **表名：** t_psw_adjcapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 3 | fremarks | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fshiftselect | 班次 | varchar | 50 |  | √ | ' ' | 班次,枚举: |
| 7 | fadjustworkhour | 调整工时 | numeric | 23 | 10 | √ | 0 | 调整工时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_adjcapentry |  | fentryid |
| 2 | idx_t_psw_adjcapentry |  | fid |
