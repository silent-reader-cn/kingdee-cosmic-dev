# 专家库更新前数据-src_expertupdatelog

## 专家库更新前数据-主表 t_src_expertupdatelog

- **表名称：** 专家库更新前数据-主表
- **表名：** t_src_expertupdatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | [专家资料 src_expert](../src_files/src_expert.md) |
| 3 | fpausefrom | 暂停评标期间从 | timestamp | 0 |  |  | null | 暂停评标期间从 |
| 4 | fperiodid | 考评周期 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 5 | fevaluatescore | 考评得分 | numeric | 23 | 10 | √ | 0 | 考评得分 |
| 6 | fexpertawardid | 最近专家奖励 | int8 | 64 |  | √ | 0 | [专家奖励F7 src_expertawardf7](../src_files/src_expertawardf7.md) |
| 7 | fexpertpunishid | 最近专家处罚 | int8 | 64 |  | √ | 0 | [专家处罚F7 src_expertpunishf7](../src_files/src_expertpunishf7.md) |
| 8 | fevaluateid | 最近专家考评 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 9 | fevaluateto | 考评期间至 | timestamp | 0 |  |  | null | 考评期间至 |
| 10 | fevaluatedate | 最近更新时间 | timestamp | 0 |  |  | null | 最近更新时间 |
| 11 | fpauseto | 暂停评标期间至 | timestamp | 0 |  |  | null | 暂停评标期间至 |
| 12 | fevaluatefrom | 考评期间从 | timestamp | 0 |  |  | null | 考评期间从 |
| 13 | fevaluategradeid | 考评等级/结果 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 14 | fsrcbilltype | 最近更新来源 | bpchar | 1 |  | √ | ' ' | 最近更新来源,枚举: 1 :专家考评 2 :专家奖励 3 :专家处罚 |
| 15 | fevaluatetypeid | 考评类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertupdatelog |  | fid |
| 2 | idx_src_expertupdatelog_eid |  | fexpertid |
