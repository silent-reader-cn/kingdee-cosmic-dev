# 预测冲减历史记录-mds_fnreportbk

## 预测冲减历史记录-主表 t_mds_fnreportbk

- **表名称：** 预测冲减历史记录-主表
- **表名：** t_mds_fnreportbk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffordate | 预测时间 | timestamp | 0 |  |  | null | 预测时间 |
| 3 | foutstockqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计已出库数量 |
| 4 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbillentryseq | 预测单分录行号 | int4 | 32 |  | √ | 0 | 预测单分录行号 |
| 7 | fmodifytime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fplanid | 预测ID | int8 | 64 |  | √ | 0 | 预测ID |
| 9 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fsrcmaterialid | 销售订单物料ID | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | forderstatus | 订单状态 | varchar | 5 |  | √ | ' ' | 订单状态,枚举: A :正常 B :已关闭 C :正常1 D :已关闭1 |
| 12 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 13 | fforecastqty | 预测数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预测数量 |
| 14 | fsrcprojectid | 销售订单项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fsetofflogid | 冲减日志 | int8 | 64 |  | √ | 0 | [冲减日志 mds_setofflog](../mds_files/mds_setofflog.md) |
| 17 | fqty | 订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单数量 |
| 18 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | fsrctrackid | 销售订单跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsrcauxproperty | 销售订单辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 24 | fsrcbom | 销售订单BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 25 | fsrcmatverid | 销售订单物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 26 | fsetoffverid | 冲减版本 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 27 | fsetoffdate | 冲减时间 | timestamp | 0 |  |  | null | 冲减时间 |
| 28 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 29 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 30 | forderremainqty | 未关闭订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关闭订单数量 |
| 31 | fsendgoodsdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 32 | fsrcbonded | 销售订单保税 | bpchar | 1 |  | √ | '0' | 销售订单保税 |
| 33 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fplanentryid | 预测分录ID | int8 | 64 |  | √ | 0 | 预测分录ID |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fremainqty | 本次剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次剩余数量 |
| 37 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 38 | fsrccustomerid | 销售订单客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 39 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 40 | fsetoffqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 41 | fkqdate | 靠齐时间 | timestamp | 0 |  |  | null | 靠齐时间 |
| 42 | fsetid | 预测冲减定义id | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 43 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 44 | fokdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 45 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 46 | fexecqty | 运算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 运算数量 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fsourcetype | 来源 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 49 | fisqtysetoff | 是否进行过冲减 | bpchar | 1 |  | √ | '0' | 是否进行过冲减 |
| 50 | fhwremainqty | 预测剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预测剩余数量 |
| 51 | fsaleorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | fforecastbillno | 预测单编号 | varchar | 60 |  | √ | ' ' | 预测单编号 |
| 53 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | frpddate | 要求交单日期 | timestamp | 0 |  |  | null | 要求交单日期 |
| 55 | fsrclicenseno | 销售订单许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | ftoolid | 预测冲减运算ID | int8 | 64 |  | √ | 0 | [预测冲减运算 mds_setofftool](../mds_files/mds_setofftool.md) |
| 58 | fsalremainqty | 销售订单剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 销售订单剩余数量 |
| 59 | ffinishdate | 预计完工时间 | timestamp | 0 |  |  | null | 预计完工时间 |
| 60 | fmanufactureid | 物料制造策略 | int8 | 64 |  | √ | 0 | [制造策略 bd_manustrategy](../sbd_files/bd_manustrategy.md) |
| 61 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 62 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 63 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 64 | fepddate | 预计交单日期 | timestamp | 0 |  |  | null | 预计交单日期 |
| 65 | fsno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 66 | fbilltype | 订单类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_fnreportbk |  | fbillno |
| 2 | pk_t_mds_fnreportbk |  | fid |
