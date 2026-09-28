# 生产倒冲日志-im_mdc_backflushlog

## 单据体-子表 t_im_mdc_bflogentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_bflogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebillentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 3 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fstockid | 用料清单id | int8 | 64 |  | √ | 0 | 用料清单id |
| 6 | fmaterielmasterid | 子项编码(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fstockentryid | 用料清单分录id | int8 | 64 |  | √ | 0 | 用料清单分录id |
| 9 | fsourcebillentry | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型,枚举: A :完工入库单 B :工单汇报单 C :工序汇报单 D :工序转移单 E :委外完工入库单 F :完工退库单 H :委外收货单 SR :工序汇报单 SO :委外接收单 SI :内协接收单 |
| 10 | fbfres | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 11 | fproductid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 13 | fbfstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :倒冲成功 B :倒冲失败 C :反倒冲成功 D :反倒冲失败 E :部分倒冲 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fsourcebillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fbillseq | 单据行号 | varchar | 50 |  | √ | ' ' | 单据行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_bflogentry |  | fentryid |
| 2 | idx_im_mdc_bflogentry_fid |  | fid |

---

## 生产倒冲日志-主表 t_im_mdc_backflushlog

- **表名称：** 生产倒冲日志-主表
- **表名：** t_im_mdc_backflushlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_backflushlog_forgid |  | forgid |
| 2 | pk_im_mdc_backflushlog |  | fid |
