# 抵质押物f7-gm_pledgebill_f7

## 单据体-子表 t_gm_pledgebill_shareorg

- **表名称：** 单据体-子表
- **表名：** t_gm_pledgebill_shareorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_pledgebill_shareorg |  | fentryid |
| 2 | ind_gm_pledgebill_shareorg_fd |  | fid |

---

## 抵质押物f7-主表 t_gm_pledgebill

- **表名称：** 抵质押物f7-主表
- **表名：** t_gm_pledgebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpledgename | 抵质押物名称 | varchar | 255 |  | √ | ' ' | 抵质押物名称 |
| 3 | fusablerange | 使用范围 | varchar | 80 |  | √ | ' ' | 使用范围,枚举: org :本组织 share :共享 specifyshare :指定共享 |
| 4 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstoppledgedate | fstoppledgedate | timestamp | 0 |  |  | null |  |
| 6 | fpledgestatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: unpledge :待押 pledging :在押 releasepledge :解押 cacelpledge :注销 |
| 7 | fpledgetextno | fpledgetextno | varchar | 255 |  | √ | ' ' |  |
| 8 | frealrightpersonid | 物权人ID | int8 | 64 |  | √ | 0 | 物权人ID |
| 9 | frealright | 物权属性 | varchar | 80 |  | √ | ' ' | 物权属性,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 12 | fpledgerate | fpledgerate | int4 | 32 |  | √ | 0 |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fpledgeno | fpledgeno | int8 | 64 |  | √ | 0 |  |
| 15 | frealrightpersontext | 物权人 | varchar | 80 |  | √ | ' ' | 物权人 |
| 16 | fbaseedittype | fbaseedittype | varchar | 80 |  | √ | ' ' |  |
| 17 | ftotalpledgevalue | 累计抵押价值 | numeric | 19 | 4 | √ | 0 | 累计抵押价值 |
| 18 | fpledgevalue | 可抵押价值 | numeric | 19 | 4 | √ | 0 | 可抵押价值 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 24 | fbegindate | fbegindate | timestamp | 0 |  |  | null |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fpledgetypeid | fpledgetypeid | int8 | 64 |  | √ | 0 |  |
| 27 | foriginalvalue | foriginalvalue | numeric | 19 | 4 | √ | 0 |  |
| 28 | fcurrentappraisedvalue | fcurrentappraisedvalue | numeric | 19 | 4 | √ | 0 |  |
| 29 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 30 | fbillsource | fbillsource | varchar | 80 |  | √ | ' ' |  |
| 31 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 32 | finitialappraisedvalue | finitialappraisedvalue | numeric | 19 | 4 | √ | 0 |  |
| 33 | fattribute | 属性 | varchar | 80 |  | √ | ' ' | 属性,枚举: mortgage :抵押 pledge :质押 counter_guarantee :反担保 |
| 34 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_pledgebill_fsource |  | fsourcebillid,fbillsource |
| 2 | pk_t_gm_pledgebill |  | fid |
| 3 | idx_gm_pledgebill_billno |  | fbillno |
