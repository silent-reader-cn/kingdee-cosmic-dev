# 分步调出单-im_transoutbill

## 分步调出单-反写记录表 t_im_transoutbill_wb

- **表名称：** 分步调出单-反写记录表
- **表名：** t_im_transoutbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transoutbill_wb_pkey |  | fentryid |
| 2 | idx_im_transoutbill_wb_fk |  | fid |

---

## 分步调出单-多语言表 t_im_transoutbill_l

- **表名称：** 分步调出单-多语言表
- **表名：** t_im_transoutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbill_l |  | fid,flocaleid |
| 2 | t_im_transoutbill_l_pkey |  | fpkid |

---

## 分步调出单-主表 t_im_transoutbill

- **表名称：** 分步调出单-主表
- **表名：** t_im_transoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettleroutedetailid | 结算路径明细ID | int8 | 64 |  | √ | 0 | 结算路径明细ID |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 11 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 20 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | froaddamageowner | 途损归属 | varchar | 10 |  | √ | ' ' | 途损归属,枚举: OutOwner :调出货主 InOwner :调入货主 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | ftransit | 在途归属 | varchar | 5 |  | √ | ' ' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 28 | frevconfirmnode | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 29 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 30 | finorgid | 调入组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 32 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 35 | fsettlescurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transoutbill_pkey |  | fid |
| 2 | idx_im_transoutbill_org |  | forgid |
| 3 | idx_im_transoutbill |  | fbilltypeid |
| 4 | idx_im_transoutbill_biztorgno |  | fbiztime,forgid,fbillno |
| 5 | idx_im_tobill_bktorgno |  | fbookdate,forgid,fbillno |
| 6 | idx_im_transoutbill_forgbillno |  | fbillno,forgid |
| 7 | idx_im_transoutbill_iorg |  | finorgid |

---

## 物料明细-子表 t_im_transoutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_transoutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finprojectid | 调入项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | foutownerid | int8 | 64 |  | √ | 0 |  |
| 7 | finvstatusid | 调入库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 9 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 10 | finlicenseno | 调入许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 11 | foutinvtypeid | foutinvtypeid | int8 | 64 |  | √ | 0 |  |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | finkeepertype | finkeepertype | varchar | 36 |  | √ | ' ' |  |
| 15 | fkeeperid | 调入保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | finownerid | finownerid | int8 | 64 |  | √ | 0 |  |
| 18 | foutkeeperid | foutkeeperid | int8 | 64 |  | √ | 0 |  |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 调出项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fkeepertype | 调入保管者类型 | varchar | 36 |  | √ | ' ' | 调入保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | froaddamageqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 25 | fwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 27 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 28 | ftransitownertype | 在途货主类型 | varchar | 30 |  | √ | ' ' | 在途货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 29 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 30 | fownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 32 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 33 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 34 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 35 | froaddamagebaseqty | 途损基本数量 | numeric | 23 | 10 | √ | 0 | 途损基本数量 |
| 36 | ftransitinvstatusid | ftransitinvstatusid | int8 | 64 |  | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | froaddamageqty2nd | 途损辅助数量 | numeric | 23 | 10 | √ | 0 | 途损辅助数量 |
| 40 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 41 | flicenseno | 调出许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 42 | fenterinvstatusid | fenterinvstatusid | int8 | 64 |  | √ | 0 |  |
| 43 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 44 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 45 | fsettleroute | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 46 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 50 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 51 | foutkeepertype | foutkeepertype | varchar | 36 |  | √ | ' ' |  |
| 52 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 53 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 54 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 55 | ftransitownerid | 在途货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | finkeeperid | finkeeperid | int8 | 64 |  | √ | 0 |  |
| 57 | finmpmtaskno | 调入项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | foutownertype | foutownertype | varchar | 36 |  | √ | ' ' |  |
| 60 | finvtypeid | 调入库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 61 | finlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 62 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 63 | flocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 64 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 65 | fentrycomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 66 | finorgid | finorgid | int8 | 64 |  | √ | 0 |  |
| 67 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 68 | fmpmtaskno | 调出项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 69 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 70 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 71 | fenterinvtypeid | fenterinvtypeid | int8 | 64 |  | √ | 0 |  |
| 72 | finownertype | finownertype | varchar | 36 |  | √ | ' ' |  |
| 73 | froaddamageqty3rd | 途损辅助数量(2) | numeric | 23 | 10 | √ | 0 | 途损辅助数量(2) |
| 74 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbill_e_mmt |  | fmaterialmasterid |
| 2 | idx_im_transoutbill_e_wh |  | fwarehouseid |
| 3 | t_im_transoutbillentry_pkey |  | fentryid |
| 4 | idx_im_transoutbillentry |  | fid |
| 5 | idx_im_transoutbill_e_oow |  | foutownerid |

---

## 物料明细-分表 t_im_transoutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_transoutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 100 |  | √ | ' ' | 核心单据实体 |
| 7 | finremainreturnqty | 调入未退回数量 | numeric | 23 | 10 | √ | 0 | 调入未退回数量 |
| 8 | freltransinbaseqty | 关联调入基本数量 | numeric | 23 | 10 | √ | 0 | 关联调入基本数量 |
| 9 | freturnbaseqty | 调出已退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调出已退回基本数量 |
| 10 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | frelreturnbaseqty | 关联调出已退回基本数量 | numeric | 23 | 10 | √ | 0 | 关联调出已退回基本数量 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 15 | fremaintransinbaseqty | 未调入基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调入基本数量 |
| 16 | fremainreturnbaseqty | 调出未退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调出未退回基本数量 |
| 17 | finremainreturnbaseqty | 调入未退回基本数量 | numeric | 23 | 10 | √ | 0 | 调入未退回基本数量 |
| 18 | finreturnbaseqty | 调入已退回基本数量 | numeric | 23 | 10 | √ | 0 | 调入已退回基本数量 |
| 19 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 20 | freloutqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 21 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 24 | freturnqty | 调出已退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调出已退回数量 |
| 25 | ftransinbaseqty | 已调入基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入基本数量 |
| 26 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 27 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 28 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 29 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 30 | freloutbaseqty | 出库基本数量 | numeric | 23 | 10 | √ | 0 | 出库基本数量 |
| 31 | ftransinqty | 已调入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入数量 |
| 32 | fremaintransinqty | 未调入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调入数量 |
| 33 | fremainreturnqty | 调出未退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调出未退回数量 |
| 34 | frelreturnqty | 关联调出已退回数量 | numeric | 23 | 10 | √ | 0 | 关联调出已退回数量 |
| 35 | finreturnqty | 调入已退回数量 | numeric | 23 | 10 | √ | 0 | 调入已退回数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | freltransinqty | 关联调入数量 | numeric | 23 | 10 | √ | 0 | 关联调入数量 |
| 38 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbillentry_r_id |  | fid |
| 2 | t_im_transoutbillentry_r_pkey |  | fentryid |

---

## 物料明细-分表 t_im_transoutbillentry_x

- **表名称：** 物料明细-分表
- **表名：** t_im_transoutbillentry_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 3 | fenterinvstatusid | fenterinvstatusid | int8 | 64 |  | √ | 0 |  |
| 4 | finprojectid | finprojectid | int8 | 64 |  | √ | 0 |  |
| 5 | finlocationid | finlocationid | int8 | 64 |  | √ | 0 |  |
| 6 | foutkeepertype | 调出保管者类型 | varchar | 36 |  | √ | ' ' | 调出保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 7 | foutinvstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | finwarehouseid | finwarehouseid | int8 | 64 |  | √ | 0 |  |
| 10 | finkeeperid | finkeeperid | int8 | 64 |  | √ | 0 |  |
| 11 | foutinvtypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 12 | finorgid | finorgid | int8 | 64 |  | √ | 0 |  |
| 13 | finkeepertype | finkeepertype | varchar | 36 |  | √ | ' ' |  |
| 14 | finownerid | finownerid | int8 | 64 |  | √ | 0 |  |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fenterinvtypeid | fenterinvtypeid | int8 | 64 |  | √ | 0 |  |
| 17 | finownertype | finownertype | varchar | 36 |  | √ | ' ' |  |
| 18 | foutkeeperid | 调出保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbillentry_x_id |  | fid |
| 2 | idx_im_transoutbill_e_x_oow |  | foutownerid |
| 3 | t_im_transoutbillentry_x_pkey |  | fentryid |

---

## 物料明细-分表 t_im_transoutbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_transoutbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 6 | fincostaccountid | 调入成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 7 | fincostcurrencyid | 调入成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | finunitactualcost | 调入单位实际成本 | numeric | 23 | 10 | √ | 0 | 调入单位实际成本 |
| 10 | finactualcost | 调入实际成本 | numeric | 23 | 10 | √ | 0 | 调入实际成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbillentry_c |  | fid |
| 2 | pk_im_transoutbillentry_c |  | fentryid |

---

## 关联子实体-子表 t_im_transoutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transoutbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbillentry_lk_fk |  | fentryid |
| 2 | t_im_transoutbillentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_transoutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transoutbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transoutbill_lk_fk |  | fid |
| 2 | t_im_transoutbill_lk_pkey |  | fpkid |

---

## 分步调出单-关联追踪表 t_im_transoutbill_tc

- **表名称：** 分步调出单-关联追踪表
- **表名：** t_im_transoutbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_im_transoutbill_tc_tid |  | ftid |
| 2 | idx_im_transout_tc_ftbidtid |  | ftbillid,ftid |
| 3 | idx_im_transoutbill_tc_tbill |  | ftbillid |
| 4 | t_im_transoutbill_tc_pkey |  | fid |
