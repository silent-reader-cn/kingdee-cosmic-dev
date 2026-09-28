# 资产重估单-fa_recalculate

## 单据体-子表 t_fa_recalculate_entry

- **表名称：** 单据体-子表
- **表名：** t_fa_recalculate_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbfaddupyeardepre | 重估前本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 重估前本年累计折旧 |
| 6 | faccumdep | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 7 | fdepredamount | 已折旧期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 已折旧期间数 |
| 8 | fbfpreresidualval | 重估前残值 | numeric | 19 | 6 | √ | 0.000000 | 重估前残值 |
| 9 | fbfyearorigvalchg | 重估前本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 重估前本年原值变动 |
| 10 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 11 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 12 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 13 | fbfdepredamount | 重估前已折旧期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 重估前已折旧期间数 |
| 14 | fbfnetamount | 重估前净额 | numeric | 19 | 6 | √ | 0.000000 | 重估前净额 |
| 15 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 16 | fbfaccumdepre | 重估前累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 重估前累计折旧 |
| 17 | fbfmonthdepre | 重估前本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 重估前本期折旧 |
| 18 | faddupyea | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 19 | fbfnetworth | 重估前净值 | numeric | 19 | 6 | √ | 0.000000 | 重估前净值 |
| 20 | fpreresidualval | 残值 | numeric | 19 | 6 | √ | 0.000000 | 残值 |
| 21 | fbforivalue | 重估前原值 | numeric | 19 | 6 | √ | 0.000000 | 重估前原值 |
| 22 | forivalue | 原值 | numeric | 19 | 6 | √ | 0.000000 | 原值 |
| 23 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 24 | fbfmonthorigvalchg | 重估前本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 重估前本期原值变动 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_recalculate_entry_pkey |  | fentryid |
| 2 | idx_fa_recalculate_entry |  | fid,frealcardid |

---

## 资产重估单-主表 t_fa_recalculate

- **表名称：** 资产重估单-主表
- **表名：** t_fa_recalculate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcoefficientf | 重估系数（%） | numeric | 23 | 10 | √ | 0.0000000000 | 重估系数（%） |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbizdate | 重估日期 | timestamp | 0 |  |  | null | 重估日期 |
| 11 | fbillno | 重估单号 | varchar | 30 |  | √ | ' ' | 重估单号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_recalculate |  | forgid,fdepreuseid |
| 2 | t_fa_recalculate_pkey |  | fid |
