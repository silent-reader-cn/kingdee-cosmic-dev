# 采购订单变更单-scp_xorder

## 采购订单变更单-分表 t_pur_xorder_a

- **表名称：** 采购订单变更单-分表
- **表名：** t_pur_xorder_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumsaloutamount | fsumsaloutamount | numeric | 23 | 10 | √ | 0 |  |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 5 | fbillversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 8 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 9 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 13 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 14 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 15 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 19 | frejectreason | 打回原因 | varchar | 512 |  | √ | '0' | 打回原因 |
| 20 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | freason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 23 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 26 | fcloseid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fsumdiffamount | fsumdiffamount | numeric | 23 | 10 | √ | 0 |  |
| 29 | fsrcbilltype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 1 :自建商城 2 :京东商城 3 :ERP系统 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fsumsettleamount | fsumsettleamount | numeric | 23 | 10 | √ | 0 |  |
| 32 | fcheckstatus | fcheckstatus | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_xorder_a_fcreatetime |  | fcreatetime |
| 2 | pk_pur_xorder_a |  | fid |

---

## 订单分录-子表 t_pur_xorderentry

- **表名称：** 订单分录-子表
- **表名：** t_pur_xorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | frowlogstatus | 行物流状态 | bpchar | 1 |  | √ | ' ' | 行物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fsrcbillentryseq | fsrcbillentryseq | bpchar | 20 |  | √ | ' ' |  |
| 10 | fpromiseday | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 13 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 14 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fschedulebaseqty | 关联交货计划基本数量 | numeric | 23 | 10 | √ | 0 | 关联交货计划基本数量 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 20 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fjointdatachannelid | 对接渠道主键 | varchar | 50 |  | √ | ' ' | 对接渠道主键 |
| 22 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 23 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 24 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 25 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 26 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fexecutesdate | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 28 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 E :变更中 |
| 33 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 34 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 35 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 36 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 37 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 38 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 39 | fdeliaddr | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 40 | fscheduledetail | 进度详情 | varchar | 512 |  | √ | ' ' | 进度详情 |
| 41 | fexecuteschedule | 执行进度 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 42 | fscheduleqty | 关联交货计划数量 | numeric | 23 | 10 | √ | 0 | 关联交货计划数量 |
| 43 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 46 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :折扣额 NULL :无 |
| 47 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 48 | freqbillno | freqbillno | varchar | 80 |  | √ | ' ' |  |
| 49 | fpayentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 50 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_xorderentry_fmatlid |  | fmaterialid |
| 2 | pk_pur_xorderentry |  | fentryid |
| 3 | idx_pur_xorderentry_fid_fseq |  | fid,fseq |

---

## 用料信息-子表 t_pur_xorderentry_s

- **表名称：** 用料信息-子表
- **表名：** t_pur_xorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freturnsubbaseqty | 已退料基本数量 | numeric | 23 | 10 | √ | 0 | 已退料基本数量 |
| 2 | fconsumesubbaseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 3 | fissuemode | 领送料方式 | bpchar | 1 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fextraratiobasicqty | 发料上限基本数量 | numeric | 23 | 10 | √ | 0 | 发料上限基本数量 |
| 6 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0 | 变动损耗率 |
| 7 | fsubsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fparentmaterialid | 父项物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 10 | fsubconfiguredcodeid | 用料配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fwasteformula | 损耗计算公式 | bpchar | 1 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 12 | fparententryid | 父级行主键 | varchar | 50 |  | √ | '0' | 父级行主键 |
| 13 | fsubmaterialid | 用料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 16 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 17 | freturnsubqty | 已退料数量 | numeric | 23 | 10 | √ | 0 | 已退料数量 |
| 18 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 19 | fsubsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 20 | fsubrequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 21 | fsubbaseqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 22 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fsubsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 24 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 27 | fjointdatachannelid | fjointdatachannelid | varchar | 80 |  | √ | ' ' |  |
| 28 | fsupplymode | 货主类型 | varchar | 80 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 29 | foutstocksubqty | 已发料数量 | numeric | 23 | 10 | √ | 0 | 已发料数量 |
| 30 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fextraratioqty | 发料上限数量 | numeric | 23 | 10 | √ | 0 | 发料上限数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fsubremarks | fsubremarks | varchar | 512 |  | √ | ' ' |  |
| 34 | fsubrequirebaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 35 | frowid | 行主键 | varchar | 50 |  | √ | ' ' | 行主键 |
| 36 | fsubunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fsubqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 38 | foverissuecontrl | 控制发料数量 | bpchar | 1 |  | √ | ' ' | 控制发料数量,枚举: A :可超发 B :不可超发 |
| 39 | foutstocksubbaseqty | 已发料基本数量 | numeric | 23 | 10 | √ | 0 | 已发料基本数量 |
| 40 | fqtytype | 用量类型 | bpchar | 1 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 |
| 41 | fqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 42 | fconsumesubqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 43 | freceiptsubbaseqty | 已收料基本数量 | numeric | 23 | 10 | √ | 0 | 已收料基本数量 |
| 44 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 45 | fsubstitute | 替代料 | bpchar | 1 |  | √ | '0' | 替代料 |
| 46 | freceiptsubqty | 已收料数量 | numeric | 23 | 10 | √ | 0 | 已收料数量 |
| 47 | fsubsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 48 | fisbackflushnew | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 49 | fsubsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 50 | fsubmaterialnametext | 用料名称 | varchar | 255 |  | √ | ' ' | 用料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorderentry_s |  | fdetailid |
| 2 | idx_pur_xorderentry_s_fid |  | fentryid,fseq |

---

## 采购订单变更单-多语言表 t_pur_xorder_l

- **表名称：** 采购订单变更单-多语言表
- **表名：** t_pur_xorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fchangereason | fchangereason | varchar | 512 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorder_l |  | fpkid |
| 2 | idx_pur_xorder_l_fid_flocaleid |  | fid,flocaleid |

---

## 订单分录-分表 t_pur_xorderentry_a

- **表名称：** 订单分录-分表
- **表名：** t_pur_xorderentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 3 | fsumrefundqty | 退货需补数量 | numeric | 23 | 10 | √ | 0 | 退货需补数量 |
| 4 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '1' | 控制发货数量 |
| 5 | fsaloutqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0 | 发货上限数量 |
| 6 | fsuminstockretqty | 已退库数量 | numeric | 23 | 10 | √ | 0 | 已退库数量 |
| 7 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 8 | frcvpersonname | 收货人 | varchar | 200 |  | √ | ' ' | 收货人 |
| 9 | fsaloutratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0 | 发货欠发比率(%) |
| 10 | ferpsourceid | ferpsourceid | varchar | 255 |  | √ | ' ' |  |
| 11 | frowcloseid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 13 | frowclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 14 | fsumreturnqty | fsumreturnqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | frcvpersonid | 收货人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 16 | fsumreceiptqty | 已收货数量 | numeric | 23 | 10 | √ | 0 | 已收货数量 |
| 17 | fsaloutqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0 | 发货下限数量 |
| 18 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fsumreturnreqqty | 已退货申请数量 | numeric | 23 | 10 | √ | 0 | 已退货申请数量 |
| 20 | flockprepayamt | 已锁定付款金额 | numeric | 23 | 10 | √ | 0 | 已锁定付款金额 |
| 21 | fsumreceiveqty | 已通知数量 | numeric | 23 | 10 | √ | 0 | 已通知数量 |
| 22 | fsumrejqty | 已拒收数量 | numeric | 23 | 10 | √ | 0 | 已拒收数量 |
| 23 | fprepayamt | 预付金额 | numeric | 23 | 10 | √ | 0 | 预付金额 |
| 24 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 25 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 26 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 27 | fsuminstockbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 28 | frelateoutstockqty | 关联发货数量 | numeric | 23 | 10 | √ | 0 | 关联发货数量 |
| 29 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 30 | fjdorder | fjdorder | int8 | 64 |  | √ | 0 |  |
| 31 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 32 | fsumoutstockqty | 已发货数量 | numeric | 23 | 10 | √ | 0 | 已发货数量 |
| 33 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 34 | fsuminstockqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 35 | fsaloutrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0 | 发货超发比率(%) |
| 36 | fsumrecretbaseqty | 已退货基本数量 | numeric | 23 | 10 | √ | 0 | 已退货基本数量 |
| 37 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsaloutbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0 | 发货下限基本数量 |
| 40 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 41 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 42 | fpayprepayamt | 已付预付金额 | numeric | 23 | 10 | √ | 0 | 已付预付金额 |
| 43 | fsaloutbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0 | 发货上限基本数量 |
| 44 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 45 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | frelateoutstockbaseqty | 关联发货基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货基本数量 |
| 47 | fsumaccepttaxamount | 已验收金额 | numeric | 23 | 10 | √ | 0 | 已验收金额 |
| 48 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 49 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 50 | fpayableamt | 关联对账金额 | numeric | 23 | 10 | √ | 0 | 关联对账金额 |
| 51 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 52 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0 | 已开票数量 |
| 53 | fsumrefundbaseqty | 退货需补基本数量 | numeric | 23 | 10 | √ | 0 | 退货需补基本数量 |
| 54 | fsuminstockretbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 55 | fvmistockqty | VMI在库数量 | numeric | 23 | 10 | √ | 0 | VMI在库数量 |
| 56 | fsumreceiptbaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0 | 已收货基本数量 |
| 57 | frelateinvoiceamt | 关联开票金额 | numeric | 23 | 10 | √ | 0 | 关联开票金额 |
| 58 | frowclosereason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 59 | fsumoutstockbaseqty | 已发货基本数量 | numeric | 23 | 10 | √ | 0 | 已发货基本数量 |
| 60 | fsumapaccepttaxamount | 已申请验收金额 | numeric | 23 | 10 | √ | 0 | 已申请验收金额 |
| 61 | fpayableqty | 关联对账数量 | numeric | 23 | 10 | √ | 0 | 关联对账数量 |
| 62 | fpayamt | 已付款金额 | numeric | 23 | 10 | √ | 0 | 已付款金额 |
| 63 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 64 | ferpsourceentryid | ferpsourceentryid | varchar | 255 |  | √ | ' ' |  |
| 65 | frelateapaccepttaxamount | 关联验收申请金额 | numeric | 23 | 10 | √ | 0 | 关联验收申请金额 |
| 66 | frelateinvoiceqty | 关联开票数量 | numeric | 23 | 10 | √ | 0 | 关联开票数量 |
| 67 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 68 | fsumrecretqty | 已退货数量 | numeric | 23 | 10 | √ | 0 | 已退货数量 |
| 69 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 70 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0 | 已开票金额 |
| 71 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 72 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorderentry_a |  | fentryid |
| 2 | idx_pur_xorderentry_a_fid |  | fid |

---

## 订单分录-分表 t_pur_xorderentry_o

- **表名称：** 订单分录-分表
- **表名：** t_pur_xorderentry_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foproperation | 工序编码 | varchar | 80 |  | √ | ' ' | 工序编码 |
| 3 | fmftorderid | 委外工单ID | varchar | 50 |  | √ | ' ' | 委外工单ID |
| 4 | fmftsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 5 | fmftorderentryid | 委外工单行ID | varchar | 50 |  | √ | ' ' | 委外工单行ID |
| 6 | foprdescription | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 8 | fmftdirect | 委外直送 | bpchar | 1 |  | √ | '0' | 委外直送 |
| 9 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 10 | foproperationname | 工序名称 | varchar | 100 |  | √ | ' ' | 工序名称 |
| 11 | foprentryid | 工序计划工序号ID | varchar | 50 |  | √ | ' ' | 工序计划工序号ID |
| 12 | ftechno | 工序计划编码 | varchar | 80 |  | √ | ' ' | 工序计划编码 |
| 13 | foproperationid | 工序ID | varchar | 50 |  | √ | ' ' | 工序ID |
| 14 | foprentryseq | 工序计划工序号 | varchar | 20 |  | √ | ' ' | 工序计划工序号 |
| 15 | fmftorderentryseq | 委外工单分录序号 | varchar | 20 |  | √ | ' ' | 委外工单分录序号 |
| 16 | ftechid | 工序计划ID | varchar | 50 |  | √ | ' ' | 工序计划ID |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 19 | fprocessseq | 工序计划序列号 | varchar | 50 |  | √ | ' ' | 工序计划序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorderentry_o |  | fentryid |
| 2 | idx_pur_xorderentry_o_fid |  | fid |

---

## 采购订单变更单-主表 t_pur_xorder

- **表名称：** 采购订单变更单-主表
- **表名：** t_pur_xorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentity | fsourcebillentity | varchar | 80 |  | √ | ' ' |  |
| 3 | fdelidate | 最早交货日期 | timestamp | 0 |  |  | null | 最早交货日期 |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fvalider | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | fsumpayableamt | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 10 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 11 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fsumpayamt | 已付款金额 | numeric | 23 | 10 | √ | 0 | 已付款金额 |
| 13 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 15 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 E :变更中 |
| 17 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 18 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fchangebillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fissyn | fissyn | bpchar | 1 |  | √ | '0' |  |
| 22 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 23 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 24 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 25 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fcontacterid | 供应商业务员 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fprepayrate | 预付比例(%) | numeric | 23 | 10 | √ | 0 | 预付比例(%) |
| 29 | foperatorid | 采购员 | int8 | 64 |  |  | null | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 30 | fbilldate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 31 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | fpaystatus | 收款状态 | bpchar | 1 |  | √ | ' ' | 收款状态,枚举: A :待开票 B :部分开票 C :待收款 D :部分收款 E :已收款 |
| 33 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 34 | fcentersettle | 集中结算 | bpchar | 1 |  | √ | '0' | 集中结算 |
| 35 | fsupgroupid | fsupgroupid | int8 | 64 |  | √ | 0 |  |
| 36 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 37 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 38 | fsuminvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0 | 已开票金额 |
| 39 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 41 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fchangereason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 43 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 44 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 45 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fchangebizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 47 | fdelisupid | 发货方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 48 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 50 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 51 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 52 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 53 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 54 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 55 | fsumprepayamt | 预付金额 | numeric | 23 | 10 | √ | 0 | 预付金额 |
| 56 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 57 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 58 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 59 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorder |  | fid |
| 2 | idx_pur_xorder_fbillno |  | fbillno |
| 3 | idx_pur_xorder_fbizpartnerid |  | fbilldate,fbizpartnerid |
| 4 | idx_pur_xorder_forgid |  | forgid |
| 5 | idx_pur_xorder_fsupplierid |  | fsupplierid |

---

## 采购方附件-附件表 t_pur_order_feedbackatta

- **表名称：** 采购方附件-附件表
- **表名：** t_pur_order_feedbackatta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_orderentry_fentryid |  | fentryid |
| 2 | idx_pur_orderentry_fbasedataid |  | fbasedataid |
| 3 | pk_t_pur_order_feedbackatta |  | fpkid |

---

## 附件-附件表 t_pur_orderejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_orderejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orderrejectatt_fbasedataid |  | fbasedataid |
| 2 | pk_t_pur_orderejectreasonatt |  | fpkid |

---

## 交货计划-子表 t_pur_xorderentry_delsub

- **表名称：** 交货计划-子表
- **表名：** t_pur_xorderentry_delsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 计划交货数量 | numeric | 23 | 10 | √ | 0 | 计划交货数量 |
| 2 | fplandeliverdate | 计划交货日期 | timestamp | 0 |  |  | null | 计划交货日期 |
| 3 | fplanentryseq | 交货计划分录序号 | int4 | 32 |  | √ | 0 | 交货计划分录序号 |
| 4 | fchasedeliverdate | 追料计划日期 | timestamp | 0 |  |  | null | 追料计划日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fplanunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdelentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdelentrycreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fplanbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fplanbasicqty | 计划交货基本数量 | numeric | 23 | 10 | √ | 0 | 计划交货基本数量 |
| 11 | fplanpoentryid | 订单分录id | varchar | 50 |  | √ | ' ' | 订单分录id |
| 12 | fdelentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fplancomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fplanlocation | 交货地点 | varchar | 512 |  | √ | ' ' | 交货地点 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fplanaddress | 交货地址 | varchar | 512 |  | √ | ' ' | 交货地址 |
| 18 | fplanentryid | 交货计划分录id | varchar | 50 |  | √ | ' ' | 交货计划分录id |
| 19 | fdelentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_xorderentry_delsub |  | fentryid,fseq |
| 2 | idx_pur_xorderentry_delsupoeid |  | fplanpoentryid |
| 3 | pk_pur_xorderentry_delsub |  | fdetailid |

---

## 物流信息-子表 t_pur_order_log

- **表名称：** 物流信息-子表
- **表名：** t_pur_order_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 3 | fdelidate | 预计到货日期 | timestamp | 0 |  |  | null | 预计到货日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flogbillno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 pur_logsupplier](../pbd_files/pur_logsupplier.md) |
| 9 | frecphone | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_order_log_flogbillno |  | flogbillno |
| 2 | t_pur_order_log_pkey |  | fentryid |
| 3 | idx_pur_order_log_fid_fseq |  | fid,fseq |

---

## 用料信息-多语言表 t_pur_xorderentry_s_l

- **表名称：** 用料信息-多语言表
- **表名：** t_pur_xorderentry_s_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fsubremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_xorderentry_s_l |  | fpkid |
| 2 | idx_pur_xorderentry_s_l |  | fdetailid,flocaleid |
