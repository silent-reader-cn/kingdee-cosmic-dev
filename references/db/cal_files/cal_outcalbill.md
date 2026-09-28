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
| 2 | fbizentityobjectid | 业务单业务对象 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 5 | fbizbillno | 业务单据编号 | varchar | 80 |  | √ | ' ' | 业务单据编号 |
| 6 | fprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 9 | finnerbilltype | 内部交易单据类别 | varchar | 30 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fbizdirection | 业务方向 | varchar | 5 |  | √ | ' ' | 业务方向,枚举: A :正向 B :反向 |
| 13 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fisinnervirtualbill | fisinnervirtualbill | bpchar | 1 |  | √ | '0' |  |
| 28 | finvorgid | 对方公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fcostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 33 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 34 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 35 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 38 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 39 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 42 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_outcalbill_bizbid |  | fbizbillid |
| 2 | t_cal_outcalbill_pkey |  | fid |
| 3 | idx_cal_outcalbill_org |  | forgid |

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
| 6 | fmainbillentity | 业务单核心单据实体 | varchar | 80 |  | √ | ' ' | 业务单核心单据实体 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fentrycostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsrcbillentryseq | 业务单来源单据分录序号 | int8 | 64 |  | √ | 0 | 业务单来源单据分录序号 |
| 11 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 13 | fmainbillid | 业务单核心单据ID | int8 | 64 |  | √ | 0 | 业务单核心单据ID |
| 14 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 17 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 19 | fsrcbillnumber | 业务单来源单据编号 | varchar | 80 |  | √ | ' ' | 业务单来源单据编号 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsrcbillid | 业务单来源单据ID | int8 | 64 |  | √ | 0 | 业务单来源单据ID |
| 23 | fmainbillnumber | 业务单核心单据编号 | varchar | 80 |  | √ | ' ' | 业务单核心单据编号 |
| 24 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fbalancecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | fentryadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 30 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 31 | fproductid | 产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fmainbillentryseq | 业务单核心单据分录序号 | int8 | 64 |  | √ | 0 | 业务单核心单据分录序号 |
| 34 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 35 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 36 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 38 | faudittime | 审核时间（废弃） | timestamp | 0 |  |  | null | 审核时间（废弃） |
| 39 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 40 | fentryprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 42 | fprojecttaskid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 43 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 44 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fcompanyorgid | 财务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fsrcbillentity | 业务单来源单据实体 | varchar | 80 |  | √ | ' ' | 业务单来源单据实体 |
| 47 | flocalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 48 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 49 | fislastentry | 是否全部结转 | bpchar | 1 |  | √ | '0' | 是否全部结转 |
| 50 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 51 | fsrcbillentryid | 业务单来源单据行ID | int8 | 64 |  | √ | 0 | 业务单来源单据行ID |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 53 | fmainbillentryid | 业务单核心单据行ID | int8 | 64 |  | √ | 0 | 业务单核心单据行ID |
| 54 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 55 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |

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
