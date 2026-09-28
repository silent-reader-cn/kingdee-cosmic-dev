# 会计折旧-tdm_account_depreciation

## 会计折旧-主表 t_tdm_account_depre

- **表名称：** 会计折旧-主表
- **表名：** t_tdm_account_depre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 3 | fresidualvalue | 会计预计净残值 | numeric | 23 | 10 | √ | 0 | 会计预计净残值 |
| 4 | fmodifier | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fyearorivaluedecr | 本年原值调减 | numeric | 23 | 10 | √ | 0 | 本年原值调减 |
| 6 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 7 | famortizationmethod | 会计折旧摊销方法 | varchar | 50 |  | √ | ' ' | 会计折旧摊销方法 |
| 8 | famortizationperiods | 会计预计折旧摊销期数 | int8 | 64 |  | √ | 0 | 会计预计折旧摊销期数 |
| 9 | famortizedperiods | 会计已折旧摊销期数 | int8 | 64 |  | √ | 0 | 会计已折旧摊销期数 |
| 10 | fcumulativeamount | 会计累计折旧摊销额 | numeric | 23 | 10 | √ | 0 | 会计累计折旧摊销额 |
| 11 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 13 | fyearamount | 会计本年折旧摊销额 | numeric | 23 | 10 | √ | 0 | 会计本年折旧摊销额 |
| 14 | fassetsvalue | fassetsvalue | numeric | 23 | 10 | √ | 0 |  |
| 15 | fassetcode | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 16 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板引入 |
| 17 | fassetorivalue | 资产原值 | numeric | 23 | 10 | √ | 0 | 资产原值 |
| 18 | fcurrentamount | 会计当期折旧摊销额 | numeric | 23 | 10 | √ | 0 | 会计当期折旧摊销额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_account_depre_0 |  | forg |
| 2 | idx_tdm_account_depre_1 |  | fassetcode,faccountingperiod,forg |
| 3 | pk_tdm_account_depre |  | fid |
