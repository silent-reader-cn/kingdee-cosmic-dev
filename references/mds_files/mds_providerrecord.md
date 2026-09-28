# 供方记录表-mds_providerrecord

## 供方记录表-主表 t_mds_providerrecord

- **表名称：** 供方记录表-主表
- **表名：** t_mds_providerrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 3 | ftransferid | 实体字段映射ID | int8 | 64 |  | √ | 0 | 实体字段映射ID |
| 4 | fsetid | 预测冲减定义 | int8 | 64 |  | √ | 0 | 预测冲减定义 mds_setoffsetting |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :正常 B :已关闭 |
| 7 | flogid | 冲减日志ID | int8 | 64 |  | √ | 0 | 冲减日志ID |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frecorddate | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 10 | fbno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fdefineconfig | 自定义配置字符 | varchar | 50 |  | √ | ' ' | 自定义配置字符 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fqty | 单据数量 | numeric | 23 | 10 | √ | 0.0000000000 | 单据数量 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbilltag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ftoolid | 预测冲减运算 | int8 | 64 |  | √ | 0 | 预测冲减运算 mds_setofftool |
| 21 | fbillunit | 单据计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbilltypename | 单据类型名称 | varchar | 50 |  | √ | ' ' | 单据类型名称 |
| 24 | ffcvrnnum | 预测版本ID | int8 | 64 |  | √ | 0 | 预测版本ID |
| 25 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 26 | fbillrowno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 27 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 28 | fbillorg | 单据组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_providerrecord_setmid |  | fsetid,fmateriel |
| 2 | idx_mds_providerrecord_mat |  | fmateriel |
| 3 | pk_mds_providerrecord |  | fid |
