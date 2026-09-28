# MRP子项冲减明细表-mrp_atosetoffrecord

## MRP子项冲减明细表-主表 t_mrp_atosetoffrecord

- **表名称：** MRP子项冲减明细表-主表
- **表名：** t_mrp_atosetoffrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffbaseqty | 冲减数量 | numeric | 23 | 10 | √ | 0 | 冲减数量 |
| 3 | fdemandstartdate | 冲减开始日期 | timestamp | 0 |  |  | null | 冲减开始日期 |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | forgid | 冲减组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ffomatverid | 预测单物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 9 | fbillentryseq | 冲减单据序号 | int4 | 32 |  | √ | 0 | 冲减单据序号 |
| 10 | ftracknumid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 11 | ffobonded | 预测单保税 | bpchar | 1 |  | √ | '0' | 预测单保税 |
| 12 | ffoprojectid | 预测单项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 15 | ffocustomerid | 预测单客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 16 | ffodremainbaseqty | 预测单剩余需求数量 | numeric | 23 | 10 | √ | 0 | 预测单剩余需求数量 |
| 17 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 19 | ffobillentryid | 预测单据分录ID | int8 | 64 |  | √ | 0 | 预测单据分录ID |
| 20 | ffobillid | 预测单据ID | int8 | 64 |  | √ | 0 | 预测单据ID |
| 21 | fdemandbaseqty | 原始需求数量 | numeric | 23 | 10 | √ | 0 | 原始需求数量 |
| 22 | fdemandenddate | 冲减结束日期 | timestamp | 0 |  |  | null | 冲减结束日期 |
| 23 | ffobillentryseq | 预测单据序号 | int4 | 32 |  | √ | 0 | 预测单据序号 |
| 24 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fcaculatelogid | 运算日志 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 26 | fbillno | 冲减单据编号 | varchar | 80 |  | √ | ' ' | 冲减单据编号 |
| 27 | ffoorgid | 预测单组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | ffobillname | 预测单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | forderseq | 冲减顺序 | int4 | 32 |  | √ | 0 | 冲减顺序 |
| 30 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fplanflex | 冲减单据计划维度 | varchar | 255 |  | √ | ' ' | 冲减单据计划维度 |
| 32 | ffoplanflex | 预测单据计划维度 | varchar | 255 |  | √ | ' ' | 预测单据计划维度 |
| 33 | ffoauxpropid | 预测单辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 34 | fdremainbaseqty | 剩余需求数量 | numeric | 23 | 10 | √ | 0 | 剩余需求数量 |
| 35 | ffolicenseno | 预测单许可证编码 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 36 | ffobeforemainqty | 预测冲减前剩余数量 | numeric | 23 | 10 | √ | 0 | 预测冲减前剩余数量 |
| 37 | fbillname | 冲减单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 38 | ffobillno | 预测单据编号 | varchar | 80 |  | √ | ' ' | 预测单据编号 |
| 39 | ffodemandbaseqty | 预测单原始需求数量 | numeric | 23 | 10 | √ | 0 | 预测单原始需求数量 |
| 40 | fbillentryid | 冲减单据分录ID | int8 | 64 |  | √ | 0 | 冲减单据分录ID |
| 41 | fbeforemainqty | 冲减前剩余数量 | numeric | 23 | 10 | √ | 0 | 冲减前剩余数量 |
| 42 | fbillid | 冲减单据ID | int8 | 64 |  | √ | 0 | 冲减单据ID |
| 43 | ffotracknumid | 预测单跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 44 | ffobomid | 预测单BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 45 | fchildsetid | 子项冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 46 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 47 | flicenseno | 许可证编码 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 48 | ffodemanddate | 预测需求日期 | timestamp | 0 |  |  | null | 预测需求日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_atosetoffrecord_cid |  | fcaculatelogid |
| 2 | pk_t_mrp_atosetoffrecord |  | fid |
