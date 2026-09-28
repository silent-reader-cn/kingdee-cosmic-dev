# 预测冲减历史记录-mds_fnreportbk

## 预测冲减历史记录-主表 t_mds_fnreportbk

- **表名称：** 预测冲减历史记录-主表
- **表名：** t_mds_fnreportbk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 3 | ffordate | 预测时间 | timestamp | 0 |  |  | null | 预测时间 |
| 4 | fkqdate | 靠齐时间 | timestamp | 0 |  |  | null | 靠齐时间 |
| 5 | fsetid | 预测冲减定义id | int8 | 64 |  | √ | 0 | 预测冲减定义 mds_setoffsetting |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | foutstockqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计已出库数量 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fokdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fmodifytime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
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
| 22 | fsetofflogid | 冲减日志 | int8 | 64 |  | √ | 0 | 冲减日志 mds_setofflog |
| 23 | fqty | 订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单数量 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | frpddate | 要求交单日期 | timestamp | 0 |  |  | null | 要求交单日期 |
| 26 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | ftoolid | 预测冲减运算ID | int8 | 64 |  | √ | 0 | 预测冲减运算 mds_setofftool |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fsalremainqty | 销售订单剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 销售订单剩余数量 |
| 32 | ffinishdate | 预计完工时间 | timestamp | 0 |  |  | null | 预计完工时间 |
| 33 | fsetoffverid | 冲减版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 34 | fsetoffdate | 冲减时间 | timestamp | 0 |  |  | null | 冲减时间 |
| 35 | fmanufactureid | 物料制造策略 | int8 | 64 |  | √ | 0 | 制造策略 bd_manustrategy |
| 36 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 37 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 38 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 39 | forderremainqty | 未关闭订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关闭订单数量 |
| 40 | fsendgoodsdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 41 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 42 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fplanentryid | 预测分录ID | int8 | 64 |  | √ | 0 | 预测分录ID |
| 44 | fepddate | 预计交单日期 | timestamp | 0 |  |  | null | 预计交单日期 |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fsno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 47 | fbilltype | 订单类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 48 | fremainqty | 本次剩余数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次剩余数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_fnreportbk |  | fbillno |
| 2 | pk_t_mds_fnreportbk |  | fid |
