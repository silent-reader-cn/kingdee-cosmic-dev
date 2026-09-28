# 费用明细数据同步记录-er_expensedata_syncrecord

## 费用明细数据同步记录-多语言表 t_er_expdata_syncrecord_l

- **表名称：** 费用明细数据同步记录-多语言表
- **表名：** t_er_expdata_syncrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 费用明细数据同步记录-主表 t_er_expdata_syncrecord

- **表名称：** 费用明细数据同步记录-主表
- **表名：** t_er_expdata_syncrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmessage | 错误信息 | text | 0 |  |  | null | 错误信息 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fcount | 同步数量 | int8 | 64 |  | √ | 0 | 同步数量 |
| 8 | fsyncrange | 同步数据范围 | bpchar | 1 |  | √ | '0' | 同步数据范围,枚举: 1 :全量 0 :增量 |
| 9 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 10 | fmessage_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_expdata_syncrecord |  | fid |
| 2 | idx_er_syncrecord_fbegintime |  | fbegintime |
