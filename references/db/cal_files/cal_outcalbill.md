# 出库核算单-cal_outcalbill

## 单据体-分表 t_cal_outcalentry_a

- **表名称：** 单据体-分表
- **表名：** t_cal_outcalentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | fgroupnumber | 成组号 | varchar | 100 |  | √ | ' ' | 成组号 |
| 4 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 5 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 6 | fgroupseq | 成组行号 | varchar | 100 |  | √ | ' ' | 成组行号 |
| 7 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 8 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 9 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 10 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 11 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | funitfee | 单位采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位采购成本 |
| 14 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_outcalea_id |  | fid |
| 2 | idx_cal_outcalentry_groupno |  | fgroupnumber |
| 3 | t_cal_outcalentry_a_pkey |  | fentryid |
| 4 | idx_cal_outcalentey_groupseq |  | fgroupseq |

---

## 出库核算单-主表 t_cal_outcalbill

- **表名称：** 出库核算单-主表
- **表名：** t_cal_outcalbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizentityobjectid | 业务单业务对象 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fsettleroutedetailid | 结算路径明细ID | int8 | 64 |  | √ | 0 | 结算路径明细ID |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | fbizbillno | 业务单据编号 | varchar | 80 |  | √ | ' ' | 业务单据编号 |
| 7 | fprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | finnerbilltype | 内部交易单据类别 | varchar | 30 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fbizdirection | 业务方向 | varchar | 5 |  | √ | ' ' | 业务方向,枚举: A :正向 B :反向 |
| 14 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 26 | froaddamageowner | 途损归属 | varchar | 50 |  | √ | ' ' | 途损归属,枚举: OutOwner :调出货主 InOwner :调入货主 |
| 27 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fisinnervirtualbill | fisinnervirtualbill | bpchar | 1 |  | √ | '0' |  |
| 30 | finvorgid | 对方公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fcostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 35 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 36 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 37 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 39 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 40 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 41 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 44 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_outcalbill_bizbid |  | fbizbillid |
| 2 | t_cal_outcalbill_pkey |  | fid |
| 3 | idx_cal_outbill_customerid |  | fcustomerid |
| 4 | idx_cal_outcalbill_org |  | forgid |

---

## 出库核算单-多语言表 t_cal_outcalbill_l

- **表名称：** 出库核算单-多语言表
- **表名：** t_cal_outcalbill_l

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
| 1 | pk_cal_outcalbill_l |  | fpkid |
| 2 | idx_cal_outcalbill_l |  | fid,flocaleid |

---

## 单据体-子表 t_cal_outcalentry

- **表名称：** 单据体-子表
- **表名：** t_cal_outcalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaltaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 折扣率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣率(%) |
| 6 | fdevtrial | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 7 | fmainbillentity | 业务单核心单据实体 | varchar | 80 |  | √ | ' ' | 业务单核心单据实体 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fentrycostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsrcbillentryseq | 业务单来源单据分录序号 | int8 | 64 |  | √ | 0 | 业务单来源单据分录序号 |
| 12 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 13 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 14 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 15 | fmainbillid | 业务单核心单据ID | int8 | 64 |  | √ | 0 | 业务单核心单据ID |
| 16 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 19 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 21 | fsrcbillnumber | 业务单来源单据编号 | varchar | 80 |  | √ | ' ' | 业务单来源单据编号 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fsrcbillid | 业务单来源单据ID | int8 | 64 |  | √ | 0 | 业务单来源单据ID |
| 25 | fmainbillnumber | 业务单核心单据编号 | varchar | 80 |  | √ | ' ' | 业务单核心单据编号 |
| 26 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 27 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 28 | froaddamageqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | fbalancecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 31 | fentryadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 34 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 35 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 37 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 38 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 41 | fmainbillentryseq | 业务单核心单据分录序号 | int8 | 64 |  | √ | 0 | 业务单核心单据分录序号 |
| 42 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 43 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 44 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 46 | faudittime | 审核时间（废弃） | timestamp | 0 |  |  | null | 审核时间（废弃） |
| 47 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 48 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 49 | fentryprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 51 | fprojecttaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 52 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 53 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fcompanyorgid | 财务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fsrcbillentity | 业务单来源单据实体 | varchar | 80 |  | √ | ' ' | 业务单来源单据实体 |
| 56 | flocalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 57 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 58 | fislastentry | 是否全部结转 | bpchar | 1 |  | √ | '0' | 是否全部结转 |
| 59 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 60 | fsrcbillentryid | 业务单来源单据行ID | int8 | 64 |  | √ | 0 | 业务单来源单据行ID |
| 61 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 62 | fmainbillentryid | 业务单核心单据行ID | int8 | 64 |  | √ | 0 | 业务单核心单据行ID |
| 63 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 64 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_out_bizentry |  | fbizbillentryid |
| 2 | idx_cal_outcalet_whid |  | fwarehouseid,fid |
| 3 | t_cal_outcalentry_pkey |  | fentryid |
| 4 | idx_cal_outcalentry_srcid |  | fsrcbillentryid |
| 5 | idx_cal_incalentry_maineid |  | fmainbillentryid |
| 6 | idx_cal_outcalentry_ow |  | fownerid |
| 7 | idx_cal_outcalentry |  | fid |
| 8 | idx_cal_outcalet_matid |  | fmaterialid,fid |
