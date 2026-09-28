# 财务报表-dfa_fin_report

## 财务报表-主表 t_dfa_fin_report

- **表名称：** 财务报表-主表
- **表名：** t_dfa_fin_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrencycode | 币种编码 | varchar | 255 |  | √ | ' ' | 币种编码 |
| 3 | fpolicynumber | 会计政策编码 | varchar | 512 |  | √ | ' ' | 会计政策编码 |
| 4 | fpolicyname | 会计政策名称 | varchar | 50 |  | √ | ' ' | 会计政策名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fipoorgid | IPO编制组织 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcurrencyname | 币种名称 | varchar | 255 |  | √ | ' ' | 币种名称 |
| 9 | faccountingsysname | 核算体系名称 | varchar | 50 |  | √ | ' ' | 核算体系名称 |
| 10 | freportdate | 报表日期 | timestamp | 0 |  |  | null | 报表日期 |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 13 | ffinreporttype | IPO财务报表类型 | int8 | 64 |  | √ | 0 | [IPO财务报表类型 ipo_fin_report_type](../ipobase_files/ipo_fin_report_type.md) |
| 14 | faccountingsys | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 15 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 0 :数据同步-星空旗舰版 1 :数据同步-星空企业版 2 :手工引入 3 :数据同步-星瀚 |
| 16 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 18 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 19 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :合并报表 3 :报表 |
| 20 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 21 | forgname | 核算组织名称 | varchar | 50 |  | √ | ' ' | 核算组织名称 |
| 22 | famountunitname | 金额单位名称 | varchar | 255 |  | √ | ' ' | 金额单位名称 |
| 23 | facctsysnumber | 核算体系编码 | varchar | 512 |  | √ | ' ' | 核算体系编码 |
| 24 | famountunitcode | 金额单位编码 | varchar | 255 |  | √ | ' ' | 金额单位编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_fin_report |  | fid |
| 2 | idx_dfa_fin_report_m0 |  | fpolicy |
