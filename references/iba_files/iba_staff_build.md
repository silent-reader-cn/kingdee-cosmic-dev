# 人员结构表-iba_staff_build

## 人员结构表-主表 t_iba_staff_build

- **表名称：** 人员结构表-主表
- **表名：** t_iba_staff_build

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fipoorg | 编制组织 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 1 :手工引入 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 11 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 12 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 1 :个 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_staff_build |  | fid |
| 2 | idx_iba_staff_build_id |  | fnumber |

---

## 单据体-子表 t_iba_staff_build_detail

- **表名称：** 单据体-子表
- **表名：** t_iba_staff_build_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | famount | 值 | numeric | 23 | 10 |  | null | 值 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fquota | 指标 | int8 | 64 |  | √ | 0 | 指标库 ipo_quota_info |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iba_staff_build_detail |  | fentryid |
| 2 | idx_iba__staff_build_detail |  | fid |
