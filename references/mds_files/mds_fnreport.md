# 预测冲减记录-mds_fnreport

## 预测冲减记录-主表 t_mds_fnreport

- **表名称：** 预测冲减记录-主表
- **表名：** t_mds_fnreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 3 | ffordate | 预测时间 | timestamp | 0 |  |  | null | 预测时间 |
| 4 | fkqdate | 靠齐时间 | timestamp | 0 |  |  | null | 靠齐时间 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | foutstockqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计已出库数量 |
| 7 | fsetid | 预测冲减定义id | int8 | 64 |  | √ | 0 | 预测冲减定义 mds_setoffsetting |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fokdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexecqty | 运算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 运算数量 |
| 12 | fplanid | 预测ID | int8 | 64 |  | √ | 0 | 预测ID |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsrcmaterialid | 销售订单物料ID | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | forderstatus | 订单状态 | varchar | 5 |  | √ | ' ' | 订单状态,枚举: A :正常 B :已关闭 C :正常1 D :已关闭1 |
| 16 | fisqtysetoff | 是否进行过冲减 | bpchar | 1 |  | √ | '0' | 是否进行过冲减 |
| 17 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fhwremainqty | 预测剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预测剩余数量 |
| 19 | fsaleorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fforecastqty | 预测数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预测数量 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fqty | 订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单数量 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | frpddate | 要求交单日期 | timestamp | 0 |  |  | null | 要求交单日期 |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | ftoolid | 预测冲减运算ID | int8 | 64 |  | √ | 0 | 预测冲减运算 mds_setofftool |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fsalremainqty | 销售订单剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 销售订单剩余数量 |
| 31 | ffinishdate | 预计完工时间 | timestamp | 0 |  |  | null | 预计完工时间 |
| 32 | fsetoffverid | 冲减版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 33 | fsetoffdate | 冲减时间 | timestamp | 0 |  |  | null | 冲减时间 |
| 34 | fmanufactureid | 物料制造策略 | int8 | 64 |  | √ | 0 | 制造策略 bd_manustrategy |
| 35 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 36 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 37 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 38 | forderremainqty | 未关闭订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关闭订单数量 |
| 39 | fsendgoodsdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 40 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 41 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fepddate | 预计交单日期 | timestamp | 0 |  |  | null | 预计交单日期 |
| 43 | fplanentryid | 预测分录ID | int8 | 64 |  | √ | 0 | 预测分录ID |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 46 | fbilltype | 订单类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 47 | fremainqty | 本次剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次剩余数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_fnreport |  | fid |
| 2 | idx_mds_fnreport_setmid |  | fsetid |
| 3 | idx_mds_fnreport_mat |  | fmaterialid |
