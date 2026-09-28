# 寻源效率分析-src_planitemf7

## 寻源效率分析-主表 t_src_sourceplan

- **表名称：** 寻源效率分析-主表
- **表名：** t_src_sourceplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftimediff | 耗时偏差(天) | numeric | 19 | 6 | √ | 0 | 耗时偏差(天) |
| 4 | fdiffrate | 耗时偏差率(%) | numeric | 19 | 6 | √ | 0 | 耗时偏差率(%) |
| 5 | fplanitemid | 寻源计划项 | int8 | 64 |  | √ | 0 | 寻源计划项 src_planitem |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fbegindate | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 8 | fbegindate2 | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | fhours2 | 实际耗时(天) | numeric | 19 | 6 | √ | 0 | 实际耗时(天) |
| 11 | fenddate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 12 | fenddate2 | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 13 | fhours | 预计耗时(天) | numeric | 19 | 6 | √ | 0 | 预计耗时(天) |
| 14 | fplandiff | 进度偏差(天) | numeric | 19 | 6 | √ | 0 | 进度偏差(天) |
| 15 | fsrcbilltype | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_sourceplan_fid |  | fid |
| 2 | pk_src_sourceplan |  | fentryid |

---

## 寻源效率分析-多语言表 t_src_sourceplan_l

- **表名称：** 寻源效率分析-多语言表
- **表名：** t_src_sourceplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
