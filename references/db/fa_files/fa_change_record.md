# 资产卡片变动记录-fa_change_record

## 资产卡片变动记录-主表 t_fa_change_record

- **表名称：** 资产卡片变动记录-主表
- **表名：** t_fa_change_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frealcardbakid | 变动前实物信息 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 3 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 4 | frecordtype | 账务处理类型 | bpchar | 1 |  | √ | ' ' | 账务处理类型,枚举: 0 :正常处理 1 :忽略变动数 2 :维度字段变动 |
| 5 | fvoucherdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 6 | frealcardmasterid | 实物信息masterID | int8 | 64 |  | √ | 0 | 实物信息masterID |
| 7 | fdepredecrease | 减值准备调减 | numeric | 19 | 6 | √ | 0 | 减值准备调减 |
| 8 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 9 | ffincardbakid | 变动后财务信息 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 10 | fdepreincrease | 减值准备调增 | numeric | 19 | 6 | √ | 0 | 减值准备调增 |
| 11 | forigvaldecrease | 原值调减 | numeric | 19 | 6 | √ | 0 | 原值调减 |
| 12 | forigvalincrease | 原值调增 | numeric | 19 | 6 | √ | 0 | 原值调增 |
| 13 | fsrcbillentity | 源单据标识 | varchar | 80 |  | √ | ' ' | 源单据标识 |
| 14 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 15 | faccumdepredecrease | 累计折旧调减 | numeric | 19 | 6 | √ | 0 | 累计折旧调减 |
| 16 | faccumdepreincrease | 累计折旧调增 | numeric | 19 | 6 | √ | 0 | 累计折旧调增 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_change_record_fsrc |  | fsrcbillid,fsrcbillentity |
| 2 | idx_fa_change_record_fcid |  | ffincardid |
| 3 | idx_fa_change_record_fmid |  | frealcardid,frealcardmasterid,frealcardbakid |
| 4 | pk_fa_change_record |  | fid |

---

## 卡片变动扩展-子表 t_fa_change_record_entry

- **表名称：** 卡片变动扩展-子表
- **表名：** t_fa_change_record_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifyfield | 变动字段 | varchar | 100 |  | √ | ' ' | 变动字段 |
| 3 | faftervalue | 变更后字段值 | varchar | 255 |  | √ | ' ' | 变更后字段值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbeforevalue | 变更前字段值 | varchar | 255 |  | √ | ' ' | 变更前字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_change_record_entry |  | fentryid |
| 2 | idx_fa_change_red_eny_fid |  | fid |
