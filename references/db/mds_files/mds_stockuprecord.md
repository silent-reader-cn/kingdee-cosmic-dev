# 备货信息记录表-mds_stockuprecord

## 备货信息记录表-主表 t_mds_stockuprecord

- **表名称：** 备货信息记录表-主表
- **表名：** t_mds_stockuprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fconfiguration | 客舱构型 | int8 | 64 |  | √ | 0 | 客舱构型 mpdm_cabinconfig |
| 4 | fpolarisstatus | 客舱改装状态 | int8 | 64 |  | √ | 0 | 客舱改装状态 mds_polarisstatus |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 6 | fsourcebilltype | 来源单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fstockupmode | 备货方式 | varchar | 50 |  | √ | ' ' | 备货方式,枚举: 0 :按BOM备货 1 :按历史用量备货 2 :按客户需求备货 |
| 10 | fbackuphis | 按历史用量备货状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 11 | fbackupcustmor | 按客户需求备货状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fplanid | 计划id | int8 | 64 |  | √ | 0 | 计划id |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fqueryindex | 查找索引 | varchar | 80 |  | √ | ' ' | 查找索引 |
| 17 | fbackupbom | 按BOM备货状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 18 | fplancode | 计划号 | varchar | 80 |  | √ | ' ' | 计划号 |
| 19 | fbillno | 计划号 | varchar | 80 |  | √ | ' ' | 计划号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_stockuprecord |  | fid |
| 2 | idx_mds_stockuprecord |  | fplanid,fprojectid |
