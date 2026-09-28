# 财务报表-ipo_fin_report

## 财务报表-主表 t_fin_report

- **表名称：** 财务报表-主表
- **表名：** t_fin_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fpolicyname | 会计政策名称 | varchar | 50 |  | √ | ' ' | 会计政策名称 |
| 4 | fipoorgid | IPO编制组织 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | freportdate | 报表日期 | timestamp | 0 |  |  | null | 报表日期 |
| 7 | faccountingsysname | 核算体系名称 | varchar | 50 |  | √ | ' ' | 核算体系名称 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | ffinreporttype | IPO财务报表类型 | int8 | 64 |  | √ | 0 | IPO财务报表类型 ipo_fin_report_type |
| 10 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 1 :手工引入 2 :数据同步-旗舰版 3 :数据同步-企业版 |
| 11 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :合并报表 |
| 14 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 15 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 16 | forgname | 核算组织名称 | varchar | 50 |  | √ | ' ' | 核算组织名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fin_report |  | fipoorgid,freporttype,freportdate |
| 2 | pk_fin_report |  | fid |
