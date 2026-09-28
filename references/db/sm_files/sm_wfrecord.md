# 委托代销结算记录-sm_wfrecord

## 单据体-子表 t_sm_wfrecordentry

- **表名称：** 单据体-子表
- **表名：** t_sm_wfrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fbillqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 4 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fverifybaseqty | 本次结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次结算基本数量 |
| 8 | fbillentryseq | 单据分录序号 | int8 | 64 |  | √ | 0 | 单据分录序号 |
| 9 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 10 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 11 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 13 | fwfinfo | 结算详情 | varchar | 512 |  |  | null | 结算详情 |
| 14 | fverifyqty | 本次结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次结算数量 |
| 15 | fwfinfo_tag | 结算详情_详情 | text | 0 |  |  | null | 结算详情_详情 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fbilltypeid | 单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_wfrecordentry_fbillno |  | fbillno |
| 2 | pk_t_sm_wfrecordentry |  | fentryid |
| 3 | idx_sm_wfrecordentry_fid |  | fid |

---

## 委托代销结算记录-主表 t_sm_wfrecord

- **表名称：** 委托代销结算记录-主表
- **表名：** t_sm_wfrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 结算批号 | varchar | 80 |  | √ | ' ' | 结算批号 |
| 3 | fcreatorid | 结算人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 6 | fheadwfinfo | 结算详情 | varchar | 512 |  |  | null | 结算详情 |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fwfnumber | 结算编码 | varchar | 80 |  | √ | ' ' | 结算编码 |
| 9 | fheadwfinfo_tag | 结算详情_详情 | text | 0 |  |  | null | 结算详情_详情 |
| 10 | fwriteofftypeid | 勾稽类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_wfrecord |  | fid |
| 2 | idx_sm_wfrecord_wfseq |  | fwfseq |
