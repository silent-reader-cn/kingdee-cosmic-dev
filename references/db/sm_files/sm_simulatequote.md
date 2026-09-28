# 模拟报价单-sm_simulatequote

## 组件明细-子表 t_sm_simulatedetailentry

- **表名称：** 组件明细-子表
- **表名：** t_sm_simulatedetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubmatpricesrc | 材料单价来源_下拉 | varchar | 20 |  | √ | ' ' | 材料单价来源_下拉,枚举: 999 :手工维护 101 :采购价目表 102 :当期加权平均价 103 :期初加权平均价 104 :最新采购订单价 105 :最新采购入库价 106 :最新应付单单价 301 :按BOM子项卷算 305 :最新存货核算入库单价 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fsuballmanufcost | 制造费用（含子项） | numeric | 23 | 10 | √ | 0 | 制造费用（含子项） |
| 4 | fsubmaterialamount | 材料金额 | numeric | 23 | 10 | √ | 0 | 材料金额 |
| 5 | fsubprocessrefpricesrc | 委外加工参考单价来源_下拉 | varchar | 20 |  | √ | ' ' | 委外加工参考单价来源_下拉,枚举: 999 :手工维护 101 :采购价目表 102 :当期加权平均价 103 :期初加权平均价 104 :最新采购订单价 105 :最新采购入库价 106 :最新应付单单价 301 :按BOM子项卷算 305 :最新存货核算入库单价 |
| 6 | fsubprocessrefprice | 委外加工参考单价 | numeric | 23 | 10 | √ | 0 | 委外加工参考单价 |
| 7 | fsubbaseprocpricesrc | 委外加工单价来源 | int8 | 64 |  | √ | 0 | 模拟报价取价来源类型 sm_simquotpricesrctype |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fsubpieceworkprice | 计件单价 | numeric | 23 | 10 | √ | 0 | 计件单价 |
| 10 | fsubsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 12 | fsubmaterialattr | 物料属性 | varchar | 20 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :委外件 10060 :内协件 |
| 13 | fsubqtydenominator | 用量:分母 | numeric | 23 | 10 | √ | 1 | 用量:分母 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 15 | fsubmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fsubmaterialrefprice | 材料参考单价 | numeric | 23 | 10 | √ | 0 | 材料参考单价 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | fisreplace | 替代件 | bpchar | 1 |  | √ | ' ' | 替代件 |
| 19 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | ' ' | 跳层 |
| 20 | fsubprocessamount | 委外加工金额 | numeric | 23 | 10 | √ | 0 | 委外加工金额 |
| 21 | fsubprocessprice | 委外加工单价 | numeric | 23 | 10 | √ | 0 | 委外加工单价 |
| 22 | fsubmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 23 | fmatpricesrcentitykey | 材料单价取价来源单据 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 24 | fsubbasematrefpricesrc | 材料参考单价来源 | int8 | 64 |  | √ | 0 | 模拟报价取价来源类型 sm_simquotpricesrctype |
| 25 | fsubbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 26 | fmatpricesrcentryid | 材料单价取价来源单据分录ID | int8 | 64 |  | √ | 0 | 材料单价取价来源单据分录ID |
| 27 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fsubqtynumerator | 用量:分子 | numeric | 23 | 10 | √ | 0 | 用量:分子 |
| 29 | fsubdatasource | 数据来源 | varchar | 20 |  | √ | ' ' | 数据来源,枚举: A :向导生成 B :手工增加 |
| 30 | fsubpricesrcbillid | 委外单价取价来源单据ID | int8 | 64 |  | √ | 0 | 委外单价取价来源单据ID |
| 31 | fneedcalc | 参与计算 | bpchar | 1 |  | √ | '1' | 参与计算 |
| 32 | fsuballlaborcost | 人工费用（含子项） | numeric | 23 | 10 | √ | 0 | 人工费用（含子项） |
| 33 | fsubpieceworkamount | 计件金额 | numeric | 23 | 10 | √ | 0 | 计件金额 |
| 34 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 35 | fsubunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | fsubqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 37 | fsuballprocessamount | 委外加工金额（含子项） | numeric | 23 | 10 | √ | 0 | 委外加工金额（含子项） |
| 38 | fsubremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 39 | fsubmatrefpricesrc | 材料参考单价来源_下拉 | varchar | 20 |  | √ | ' ' | 材料参考单价来源_下拉,枚举: 999 :手工维护 101 :采购价目表 102 :当期加权平均价 103 :期初加权平均价 104 :最新采购订单价 105 :最新采购入库价 106 :最新应付单单价 301 :按BOM子项卷算 305 :最新存货核算入库单价 |
| 40 | fmatpricesrcbillid | 材料单价取价来源单据ID | int8 | 64 |  | √ | 0 | 材料单价取价来源单据ID |
| 41 | fsubpricesrcentitykey | 委外单价取价来源单据 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 42 | fsubpricesrcentryid | 委外单价取价来源单据分录ID | int8 | 64 |  | √ | 0 | 委外单价取价来源单据分录ID |
| 43 | fsubauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 44 | fsubworkhours | 标准工时(小时) | numeric | 23 | 10 | √ | 0 | 标准工时(小时) |
| 45 | fsubmanufactureprice | 变动制造费用分配率 | numeric | 23 | 10 | √ | 0 | 变动制造费用分配率 |
| 46 | fsubprocesspricesrc | 委外加工单价来源_下拉 | varchar | 20 |  | √ | ' ' | 委外加工单价来源_下拉,枚举: 999 :手工维护 101 :采购价目表 102 :当期加权平均价 103 :期初加权平均价 104 :最新采购订单价 105 :最新采购入库价 106 :最新应付单单价 301 :按BOM子项卷算 305 :最新存货核算入库单价 |
| 47 | fsubbaseprocrefpricesrc | 委外加工参考单价来源 | int8 | 64 |  | √ | 0 | 模拟报价取价来源类型 sm_simquotpricesrctype |
| 48 | fsubworkprice | 标准工资率 | numeric | 23 | 10 | √ | 0 | 标准工资率 |
| 49 | fsublaborcost | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 50 | fsuballpcsamount | 计件金额（含子项） | numeric | 23 | 10 | √ | 0 | 计件金额（含子项） |
| 51 | fhourcoef | 工时数量系数 | numeric | 23 | 10 | √ | 0 | 工时数量系数 |
| 52 | fsubmaterialprice | 材料单价 | numeric | 23 | 10 | √ | 0 | 材料单价 |
| 53 | fqtyworkhours | 总工时 | numeric | 23 | 10 | √ | 0 | 总工时 |
| 54 | fsubmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 55 | fsubbasematpricesrc | 材料单价来源 | int8 | 64 |  | √ | 0 | 模拟报价取价来源类型 sm_simquotpricesrctype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_simulatedetailentry |  | fdetailid |
| 2 | idx_sm_simulatedetail_feid |  | fentryid |

---

## 报价物料-子表 t_sm_simulatequoteentry

- **表名称：** 报价物料-子表
- **表名：** t_sm_simulatequoteentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotedbaseqty | 累计报价基本数量 | numeric | 23 | 10 | √ | 0 | 累计报价基本数量 |
| 3 | frowclosestatus | 行关闭状态 | bpchar | 1 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 4 | fbomversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 7 | fmaterialcommonid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 8 | fquotecost | 报价金额 | numeric | 23 | 10 | √ | 0 | 报价金额 |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fquotenoratecost | 报价成本 | numeric | 23 | 10 | √ | 0 | 报价成本 |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fprodpcsamount | 计件金额（父项） | numeric | 23 | 10 | √ | 0 | 计件金额（父项） |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | fquotedqty | 累计报价数量 | numeric | 23 | 10 | √ | 0 | 累计报价数量 |
| 15 | fpieceworkamount | 计件金额 | numeric | 23 | 10 | √ | 0 | 计件金额 |
| 16 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 17 | fprodsubprice | 委外加工单价（父项） | numeric | 23 | 10 | √ | 0 | 委外加工单价（父项） |
| 18 | fjoinquotedbaseqty | 关联报价基本数量 | numeric | 23 | 10 | √ | 0 | 关联报价基本数量 |
| 19 | fprodstdhour | 标准工时（父项） | numeric | 23 | 10 | √ | 0 | 标准工时（父项） |
| 20 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 22 | fjoinquotedqty | 关联报价数量 | numeric | 23 | 10 | √ | 0 | 关联报价数量 |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fcostuprate | 成本上浮率(%) | numeric | 23 | 10 | √ | 0 | 成本上浮率(%) |
| 25 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 26 | fqty | 报价数量 | numeric | 23 | 10 | √ | 0 | 报价数量 |
| 27 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 28 | fprodqtyhours | 总工时（父项） | numeric | 23 | 10 | √ | 0 | 总工时（父项） |
| 29 | flaborcost | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 30 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fprodpcsprice | 计件单价（父项） | numeric | 23 | 10 | √ | 0 | 计件单价（父项） |
| 32 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 33 | fprodhourcoef | 工时数量系数 | numeric | 23 | 10 | √ | 0 | 工时数量系数 |
| 34 | fprodcustomfee | 自定义待摊费用 | numeric | 23 | 10 | √ | 0 | 自定义待摊费用 |
| 35 | fprodstdwage | 标准工资率（父项） | numeric | 23 | 10 | √ | 0 | 标准工资率（父项） |
| 36 | fmaterialtype | 物料类型 | varchar | 30 |  | √ | ' ' | 物料类型,枚举: 10710 :主产品 10720 :联产品 10730 :副产品 |
| 37 | fprodmanucostrate | 变动制造费用分配率（父项） | numeric | 23 | 10 | √ | 0 | 变动制造费用分配率（父项） |
| 38 | fprodsubpricesrc | 委外加工单价来源（父项） | varchar | 20 |  | √ | ' ' | 委外加工单价来源（父项）,枚举: 101 :采购价目表 104 :最新采购订单价 106 :最新应付单价 999 :手工维护 |
| 39 | fprodprocesscost | 委外加工费（父项） | numeric | 23 | 10 | √ | 0 | 委外加工费（父项） |
| 40 | fprodmanufacturecost | 制造费用（父项） | numeric | 23 | 10 | √ | 0 | 制造费用（父项） |
| 41 | fprocesscost | 委外加工费 | numeric | 23 | 10 | √ | 0 | 委外加工费 |
| 42 | fprodlaborcost | 人工费用（父项） | numeric | 23 | 10 | √ | 0 | 人工费用（父项） |
| 43 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 44 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0 | 材料成本 |
| 45 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 47 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 48 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_simulateentry_fid |  | fid |
| 2 | pk_t_sm_simulatequoteentry |  | fentryid |

---

## 模拟报价单-主表 t_sm_simulatequote

- **表名称：** 模拟报价单-主表
- **表名：** t_sm_simulatequote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  |  | null | 联系地址 |
| 3 | forgid | 报价组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 9 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fgettaxprice | 获取含税价 | bpchar | 1 |  | √ | ' ' | 获取含税价 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 20 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 21 | fbizdate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 22 | fsessionid | 生成进程ID | varchar | 100 |  | √ | ' ' | 生成进程ID |
| 23 | fcalcbomloss | 报价数量计算BOM损耗 | bpchar | 1 |  | √ | ' ' | 报价数量计算BOM损耗 |
| 24 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 25 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 26 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 27 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fsettlecurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_uniq_simulate_billnoorg |  | fbillno,forgid |
| 2 | pk_t_sm_simulatequote |  | fid |

---

## 取价组织-多选基础资料表 t_sm_simqguidepriceorg

- **表名称：** 取价组织-多选基础资料表
- **表名：** t_sm_simqguidepriceorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_simqguidepriceorg |  | fpkid |
| 2 | idx_sm_sqguidepriceorg |  | fentryid |

---

## 向导价目表取价来源单据体（隐藏）-子表 t_sm_guidepricesrc

- **表名称：** 向导价目表取价来源单据体（隐藏）-子表
- **表名：** t_sm_guidepricesrc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fguidepricesrcset | 取价选项 | varchar | 20 |  | √ | ' ' | 取价选项,枚举: A :最高价 B :最低价 C :审核日期最近 D :生效日期最近 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fguidepricesrctype | 取价来源类型 | varchar | 20 |  | √ | ' ' | 取价来源类型,枚举: A :单价来源、自制单价来源 B :参考单价来源、委外单价来源 |
| 5 | fguidepricesrcgroup | 取价来源种类 | varchar | 20 |  | √ | ' ' | 取价来源种类,枚举: A :外购材料单价 B :委外加工费 C :自制委外件材料单价 |
| 6 | fguidepricesrc | 取价来源 | varchar | 20 |  | √ | ' ' | 取价来源,枚举: 101 :采购价目表 102 :当期加权平均价 103 :期初加权平均价 104 :最新采购订单价 105 :最新采购入库价 106 :最新应付单单价 301 :按BOM子项卷算 305 :最新存货核算入库单价 999 :手工维护 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fguideseq | 取价序号 | int4 | 32 |  | √ | 0 | 取价序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_guidepricesrc |  | fentryid |
| 2 | idx_sm_guidepricesrc_id |  | fid |

---

## 自定义费用明细-子表 t_sm_simulatefeedetail

- **表名称：** 自定义费用明细-子表
- **表名：** t_sm_simulatefeedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcustomfeeqty | 待摊数量 | numeric | 23 | 10 | √ | 0 | 待摊数量 |
| 2 | fcustompricetype | 自定义价格类型 | varchar | 30 |  | √ | ' ' | 自定义价格类型,枚举: A :自定义待摊费用 B :自定义不计入成本费用 |
| 3 | ffeeitemname | 费用名称 | varchar | 100 |  | √ | ' ' | 费用名称 |
| 4 | fcustomcostuprate | 自定义待摊费用成本上浮率(%) | numeric | 23 | 10 | √ | 0 | 自定义待摊费用成本上浮率(%) |
| 5 | fcustomcostupamount | 自定义待摊费用成本上浮比率金额 | numeric | 23 | 10 | √ | 0 | 自定义待摊费用成本上浮比率金额 |
| 6 | fcustomprodfeeamount | 本次分摊的成本 | numeric | 23 | 10 | √ | 0 | 本次分摊的成本 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | ffeeitem | 费用项目（基础资料） | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 11 | fcustomfeeamount | 待摊成本 | numeric | 23 | 10 | √ | 0 | 待摊成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_simulatefeedetail |  | fdetailid |
| 2 | idx_sm_simulatefeedetail |  | fentryid |

---

## 价目表-多选基础资料表 t_sm_simqguidepricelist

- **表名称：** 价目表-多选基础资料表
- **表名：** t_sm_simqguidepricelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购价目表 pm_purpricelist |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_simqguidepricelist |  | fpkid |
| 2 | idx_sm_sqguidepricelist |  | fentryid |
