# 资产清单-tdm_asset_data

## 资产清单-主表 t_tdm_asset_data

- **表名称：** 资产清单-主表
- **表名：** t_tdm_asset_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrccard | 卡片来源 | varchar | 100 |  | √ | ' ' | 卡片来源 |
| 3 | ftaxorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcleaningdate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 5 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finitaccumdepre | 初始累计折旧 | numeric | 23 | 10 | √ | 0 | 初始累计折旧 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccdepreciationmethod | 折旧方法 | varchar | 200 |  | √ | ' ' | 折旧方法 |
| 13 | fsourcetype | 税源标识 | varchar | 50 |  | √ | ' ' | 税源标识,枚举: fcssource :房产税源 tdssource :土地税源 carsource :车辆税源 shipsource :船舶税源 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0 | 资产原值 |
| 16 | fstoragelocation | 存放地点 | varchar | 50 |  | √ | ' ' | 存放地点 |
| 17 | fassetcode | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 20 | fsourcestatus | 税源状态 | varchar | 50 |  | √ | ' ' | 税源状态,枚举: 1 :已生成 0 :未生成 |
| 21 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | frdaddition | 是否研发形成 | varchar | 50 |  | √ | ' ' | 是否研发形成,枚举: 1 :是 0 :否 |
| 25 | faccresidualvalue | 预计净残值 | numeric | 23 | 10 | √ | 0 | 预计净残值 |
| 26 | fnodepreciation | 不允许列支折旧 | varchar | 50 |  | √ | ' ' | 不允许列支折旧,枚举: assetsUseRight :使用权资产 noTaxIncomeAssets :不征税收入形成资产 notApplicable :不适用 |
| 27 | faccamortizationperiods | 预计折旧摊销期数 | int8 | 64 |  | √ | 0 | 预计折旧摊销期数 |
| 28 | fassetclass | 资产类别 | varchar | 50 |  | √ | ' ' | 资产类别 |
| 29 | finitval | 初始资产原值 | numeric | 23 | 10 | √ | 0 | 初始资产原值 |
| 30 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 31 | fassetuse | 资产用途 | varchar | 50 |  | √ | ' ' | 资产用途,枚举: au_0 :用于研发投入 au_1 :用于高新投入 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板导入 |
| 34 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

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
