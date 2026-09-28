# 折旧记录分录实体-fa_depre_entry

## 折旧记录分录实体-主表 t_fa_depreentry

- **表名称：** 折旧记录分录实体-主表
- **表名：** t_fa_depreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 折旧头 | int8 | 64 |  | √ | 0 | 折旧头 |
| 2 | fshouldamount | 本期应提折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期应提折旧额 |
| 3 | fdeprerate | 本期折旧率 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧率 |
| 4 | fleftworkload | 剩余工作量 | numeric | 19 | 6 | √ | 0.000000 | 剩余工作量 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbgndepreamount | 期初折旧 | numeric | 19 | 6 | √ | 0.000000 | 期初折旧 |
| 7 | ftotalworkload | 工作总量 | numeric | 19 | 6 | √ | 0.000000 | 工作总量 |
| 8 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fentrystatus | fentrystatus | varchar | 50 |  | √ | 'A' |  |
| 11 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 12 | fdepreamount | 本期折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧额 |
| 13 | fsumworkload | 累计工作量 | numeric | 19 | 6 | √ | 0.000000 | 累计工作量 |
| 14 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 15 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fusedeptid | fusedeptid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenddepreamount | 期末折旧 | numeric | 19 | 6 | √ | 0.000000 | 期末折旧 |
| 20 | fdepreworkload | 本期工作量 | numeric | 19 | 6 | √ | 0.000000 | 本期工作量 |
| 21 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 22 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 23 | fentryid | 单据编号 | int8 | 64 |  | √ | 0 | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depreentry_fid |  | fid |
| 2 | t_fa_depreentry_pkey |  | fentryid |
