# 需方记录表-mds_requestrecord

## 需方记录表-主表 t_mds_requestrecord

- **表名称：** 需方记录表-主表
- **表名：** t_mds_requestrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 原单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原单数量 |
| 3 | ftransferid | 实体字段映射ID | int8 | 64 |  | √ | 0 | 实体字段映射ID |
| 4 | fsetid | 预测冲减定义 | int8 | 64 |  | √ | 0 | 预测冲减定义 mds_setoffsetting |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :正常 B :已关闭 |
| 7 | fdeleverydate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 8 | flogid | 冲减日志ID | int8 | 64 |  | √ | 0 | 冲减日志ID |
| 9 | fsxh | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frecorddate | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 12 | fbno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | fepd | 预计交单日期 | timestamp | 0 |  |  | null | 预计交单日期 |
| 16 | faccoutqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计已出库数量 |
| 17 | fdefineconfig | 自定义配置字符 | varchar | 50 |  | √ | ' ' | 自定义配置字符 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fsaleorderoutid | 销售出库单ID | int8 | 64 |  | √ | 0 | 销售出库单ID |
| 21 | fqty | 单据数量 | numeric | 23 | 10 | √ | 0.0000000000 | 单据数量 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbilltag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | ftoolid | 预测冲减运算 | int8 | 64 |  | √ | 0 | 预测冲减运算 mds_setofftool |
| 27 | fbillunit | 单据计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fbilltypename | 单据类型名称 | varchar | 50 |  | √ | ' ' | 单据类型名称 |
| 30 | frpd | 要求交单日期 | timestamp | 0 |  |  | null | 要求交单日期 |
| 31 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 32 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 33 | fbillrowno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 34 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 35 | fbillorg | 单据组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_requestrecord_setmid |  | fsetid,fmateriel |
| 2 | pk_mds_requestrecord |  | fid |
| 3 | idx_mds_requestrecord_mat |  | fmateriel |
