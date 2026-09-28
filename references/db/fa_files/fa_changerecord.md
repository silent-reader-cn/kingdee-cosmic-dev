# 变动记录-fa_changerecord

## 变动记录-主表 t_fa_changerecord

- **表名称：** 变动记录-主表
- **表名：** t_fa_changerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fdynamic | 是否动态 | bpchar | 1 |  | √ | '0' | 是否动态 |
| 5 | fchangebillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 6 | ftracedate | 追溯日期 | timestamp | 0 |  |  | null | 追溯日期 |
| 7 | fneedtrace | 是否需要追溯调整折旧 | bpchar | 1 |  | √ | '0' | 是否需要追溯调整折旧 |
| 8 | frealcardmasterid | 实物卡片master | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 9 | fdesc | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 10 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_changerecord_pkey |  | fid |
| 2 | idx_fa_changerecord |  | fassetbookid,fperiodid |
