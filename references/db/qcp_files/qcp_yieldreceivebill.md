# 来料让步接收申请单-qcp_yieldreceivebill

## 来料让步接收申请单-多语言表 t_qcp_yieldrecbill_l

- **表名称：** 来料让步接收申请单-多语言表
- **表名：** t_qcp_yieldrecbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_yieldbillid_l |  | fpkid |

---

## 单据体-分表 t_qcp_ycbill_bad_a

- **表名称：** 单据体-分表
- **表名：** t_qcp_ycbill_bad_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 4 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_ycbill_a |  | fentryid |

---

## 来料让步接收申请单-关联追踪表 t_qcp_yieldrecbill_tc

- **表名称：** 来料让步接收申请单-关联追踪表
- **表名：** t_qcp_yieldrecbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_yieldrecbill_tc_tbill |  | ftbillid |
| 2 | pk_qcp_yieldrecbill_tc |  | fid |
| 3 | idx_qcp_yieldrecbill_tc_tid |  | ftid |

---

## 来料让步接收申请单-反写记录表 t_qcp_yieldrecbill_wb

- **表名称：** 来料让步接收申请单-反写记录表
- **表名：** t_qcp_yieldrecbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_yieldrecbill_wb |  | fentryid |
| 2 | idx_qcp_yieldrecbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_qcp_ycbill_bad_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_ycbill_bad_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fqyt | 让步接收申请数量_确认携带值 | numeric | 23 | 10 |  | null | 让步接收申请数量_确认携带值 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 8 | fqyt_old | 让步接收申请数量_原始携带值 | numeric | 23 | 10 |  | null | 让步接收申请数量_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_ycbill_bad_lk |  | fpkid |
| 2 | idx_qcp_ycbill_bad_lk_fk |  | fentryid |

---

## 单据体-子表 t_qcp_ycbill_bad

- **表名称：** 单据体-子表
- **表名：** t_qcp_ycbill_bad

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febaddegree | 不良程度 | varchar | 1 |  | √ | ' ' | 不良程度,枚举: 0 :轻微 5 :严重 |
| 3 | fsrcentryid | 来源单据体id | varchar | 50 |  | √ | ' ' | 来源单据体id |
| 4 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 5 | fchkobjentryid | 检验对象行id（上游带下来） | int8 | 64 |  | √ | 0 | 检验对象行id（上游带下来） |
| 6 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 7 | fdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryextf | 单据体扩展值 | varchar | 50 |  | √ | ' ' | 单据体扩展值,枚举: A :赠品 B :合并检验 |
| 10 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 11 | fresult | 让步接收申请结果 | varchar | 1 |  | √ | ' ' | 让步接收申请结果,枚举: Y :同意 N :不同意 |
| 12 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fdisprocureorgfield | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fdissettlementorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 17 | fbaseqyt | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 18 | fchkobjid | 检验对象id（上游带下来） | int8 | 64 |  | √ | 0 | 检验对象id（上游带下来） |
| 19 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 20 | fqyt | 让步接收申请数量 | numeric | 23 | 10 | √ | 0 | 让步接收申请数量 |
| 21 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 22 | fsourcebillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 23 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 25 | fsourcebilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fsrcbillid | 来源单据id | varchar | 50 |  | √ | ' ' | 来源单据id |
| 28 | fdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | freason | 让步接收申请理由 | varchar | 255 |  | √ | ' ' | 让步接收申请理由 |
| 32 | freturnnumber | 自动下推退料单编码 | varchar | 80 |  | √ | ' ' | 自动下推退料单编码 |
| 33 | fsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 34 | finstocknumber | 自动下推入库单编码 | varchar | 80 |  | √ | ' ' | 自动下推入库单编码 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_yield_bad |  | fentryid |

---

## 来料让步接收申请单-主表 t_qcp_yieldrecbill

- **表名称：** 来料让步接收申请单-主表
- **表名：** t_qcp_yieldrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcid | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 4 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fapplytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbaddegree | 不良程度 | varchar | 1 |  | √ | ' ' | 不良程度,枚举: 0 :轻微 5 :严重 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_yieldbillid |  | fid |
