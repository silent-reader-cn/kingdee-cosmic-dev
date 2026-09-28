# 资产清单-tdm_asset_data

## 资产清单-主表 t_tdm_asset_data

- **表名称：** 资产清单-主表
- **表名：** t_tdm_asset_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcleaningdate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 4 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | faccdepreciationmethod | 折旧方法 | varchar | 200 |  | √ | ' ' | 折旧方法 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0 | 资产原值 |
| 13 | fstoragelocation | 存放地点 | varchar | 50 |  | √ | ' ' | 存放地点 |
| 14 | fassetcode | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 17 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | frdaddition | 是否研发形成 | varchar | 50 |  | √ | ' ' | 是否研发形成,枚举: 1 :是 0 :否 |
| 21 | faccresidualvalue | 预计净残值 | numeric | 23 | 10 | √ | 0 | 预计净残值 |
| 22 | fnodepreciation | 不允许列支折旧 | varchar | 50 |  | √ | ' ' | 不允许列支折旧,枚举: assetsUseRight :使用权资产 noTaxIncomeAssets :不征税收入形成资产 notApplicable :不适用 |
| 23 | faccamortizationperiods | 预计折旧摊销期数 | int8 | 64 |  | √ | 0 | 预计折旧摊销期数 |
| 24 | fassetclass | 资产类别 | varchar | 50 |  | √ | ' ' | 资产类别 |
| 25 | finitval | 初始资产原值 | numeric | 23 | 10 | √ | 0 | 初始资产原值 |
| 26 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 27 | fassetuse | 资产用途 | varchar | 50 |  | √ | ' ' | 资产用途,枚举: au_0 :用于研发投入 au_1 :用于高新投入 |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板引入 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_asset_data |  | fid |
| 2 | idx_tdm_asset_data_0 |  | ftaxorg |
| 3 | idx_tdm_asset_fassetcode |  | fassetcode,ftaxorg |
