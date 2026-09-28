# 资产税务一般折旧摊销-tdm_assets_tgda

## 资产税务一般折旧摊销-主表 t_tdm_assets_tgda

- **表名称：** 资产税务一般折旧摊销-主表
- **表名：** t_tdm_assets_tgda

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnetsalvage | 预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 预计净残值 |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftotalallowance | 累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计折旧摊销额 |
| 8 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 9 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 10 | famortizetype | 折旧摊销方法 | varchar | 50 |  | √ | ' ' | 折旧摊销方法 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fassetsname | 资产名称 | varchar | 50 |  | √ | ' ' | 资产名称 |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fcurrentallowance | 当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 当期折旧摊销额 |
| 15 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 16 | fdepreciationtype | 折旧类型 | varchar | 30 |  | √ | ' ' | 折旧类型,枚举: accounting_depreciation :会计折旧 general_depreciation :税务一般折旧 accelerated_depreciation :税务加速折旧 |
| 17 | fpostingdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 18 | fassetsnumber | 资产编码 | varchar | 50 |  | √ | ' ' | 资产编码 |
| 19 | fthisyearallowance | 本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年折旧摊销额 |
| 20 | fuseperiods | 预计使用期数 | int8 | 64 |  | √ | 0 | 预计使用期数 |
| 21 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_assets_tgda |  | forgid |
| 2 | pk_tdm_assets_tgda |  | fid |
