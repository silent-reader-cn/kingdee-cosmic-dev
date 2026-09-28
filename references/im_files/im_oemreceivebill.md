# 受托加工材料收料单-im_oemreceivebill

## 物料明细-分表 t_im_oemreceivebillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_oemreceivebillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foeminspect | 受托材料检验 | bpchar | 1 |  | √ | '0' | 受托材料检验 |
| 3 | fconcessionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 4 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | frelunquareturnbaseqty | 不合格关联退料基本数量 | numeric | 23 | 10 | √ | 0 | 不合格关联退料基本数量 |
| 7 | fconcessionbaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 8 | frelinspectbaseqty | 检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 检验关联基本数量 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | frelconcessionbaseqty | 让步接收关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收关联入库基本数量 |
| 11 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 12 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 13 | finspectedqty | 检验完成数量 | numeric | 23 | 10 | √ | 0 | 检验完成数量 |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 15 | frelinspectqty | 检验关联数量 | numeric | 23 | 10 | √ | 0 | 检验关联数量 |
| 16 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | frelqualifiedinbaseqty | 合格关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格关联入库基本数量 |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 20 | fqualifiedbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 21 | funqualifiedbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0 | 不合格基本数量 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 24 | finspectorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | funquareturnqty | 不合格已退料数量 | numeric | 23 | 10 | √ | 0 | 不合格已退料数量 |
| 26 | finspectedbaseqty | 检验完成基本数量 | numeric | 23 | 10 | √ | 0 | 检验完成基本数量 |
| 27 | funquaunreturnbaseqty | 不合格未退料基本数量 | numeric | 23 | 10 | √ | 0 | 不合格未退料基本数量 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | funquareturnbaseqty | 不合格已退料基本数量 | numeric | 23 | 10 | √ | 0 | 不合格已退料基本数量 |
| 30 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |
| 31 | funquaunreturnqty | 不合格未退料数量 | numeric | 23 | 10 | √ | 0 | 不合格未退料数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_oemreceivebillentry_r |  | fentryid |
| 2 | idx_im_oemreceivebillentry_r_fk |  | fid |

---

## 受托加工材料收料单-反写记录表 t_im_oemreceivebill_wb

- **表名称：** 受托加工材料收料单-反写记录表
- **表名：** t_im_oemreceivebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_oemreceivebill_wb_fk |  | fid |
| 2 | pk_im_oemreceivebill_wb |  | fentryid |

---

## 受托加工材料收料单-关联追踪表 t_im_oemreceivebill_tc

- **表名称：** 受托加工材料收料单-关联追踪表
- **表名：** t_im_oemreceivebill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_oemreceivebill_tc_tbill |  | ftbillid |
| 2 | idx_im_oemreceivebill_tc_tid |  | ftid |
| 3 | pk_im_oemreceivebill_tc |  | fid |

---

## 受托加工材料收料单-多语言表 t_im_oemreceivebill_l

- **表名称：** 受托加工材料收料单-多语言表
- **表名：** t_im_oemreceivebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_oemreceivebill_l |  | fpkid |
| 2 | idx_im_oemreceivebill_l_0 |  | fid,flocaleid |

---

## 关联子实体-子表 t_im_oemreceivebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_oemreceivebillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_oemreceivebillentry_lk |  | fentryid |
| 2 | idx_im_oemreceivebillentry_lk_fk |  | fentryid |

---

## 受托加工材料收料单-主表 t_im_oemreceivebill

- **表名称：** 受托加工材料收料单-主表
- **表名：** t_im_oemreceivebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fhandcloseflag | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 6 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fapplyuserid | fapplyuserid | int8 | 64 |  | √ | 0 |  |
| 13 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fasyncstatus | 异步状态 | varchar | 50 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 15 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 16 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 18 | fapplytype | fapplytype | varchar | 30 |  | √ | ' ' |  |
| 19 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 24 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 32 | fbillcretype | 单据生成类型 | varchar | 10 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 35 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 36 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 38 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 41 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_oemreceivebill |  | fid |
| 2 | idx_im_oemreceivebill_biztorgno |  | fbiztime,forgid,fbillno |
| 3 | idx_im_oemreceivebill_forgbillno |  | fbillno,forgid |
| 4 | idx_im_oemreceivebill_org |  | forgid |

---

## 物料明细-子表 t_im_oemreceivebillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_oemreceivebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | fsrcsystem | varchar | 50 |  | √ | ' ' |  |
| 3 | flogisticsbill | flogisticsbill | bpchar | 1 |  | √ | ' ' |  |
| 4 | frejectbaseqty | frejectbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funoutbaseqty | funoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 11 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 12 | fauditqty | fauditqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 14 | freceivebaseqty | freceivebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bd_customer :客户 |
| 16 | finbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 17 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fsrcbillnumber | fsrcbillnumber | varchar | 50 |  | √ | ' ' |  |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 25 | freceiveqtyunit2nd | freceiveqtyunit2nd | numeric | 23 | 10 | √ | 0 |  |
| 26 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 28 | frejectreason | frejectreason | varchar | 255 |  | √ | ' ' |  |
| 29 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 31 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 32 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 33 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 34 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 50 |  | √ | ' ' |  |
| 35 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 36 | freturntype | 退料类型 | varchar | 50 |  | √ | ' ' | 退料类型,枚举: A :退料 B :退补料 |
| 37 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 38 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 39 | funinbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 42 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 43 | frowclosestatus | 行关闭状态 | varchar | 50 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 44 | freceiveqty | freceiveqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | foutqty | foutqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | finqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 47 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 48 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 49 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 51 | funoutqty | funoutqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 54 | fcusmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 55 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 56 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 57 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 58 | frejectqtyunit2nd | frejectqtyunit2nd | numeric | 23 | 10 | √ | 0 |  |
| 59 | frelinbaseqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 60 | foutbaseqty | foutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 62 | frowterminatestatus | 行终止状态 | varchar | 50 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 63 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 64 | funinqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 65 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 66 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 67 | frelinqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 68 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 69 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 70 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 71 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 72 | frejectqty | frejectqty | numeric | 23 | 10 | √ | 0 |  |
| 73 | fsrcsysbillid | fsrcsysbillid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_oemreceivebillentry_fk |  | fid |
| 2 | pk_im_oemreceivebillentry |  | fentryid |
