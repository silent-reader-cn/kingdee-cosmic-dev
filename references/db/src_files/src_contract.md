# 签约单-src_contract

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projecttpl_fscp |  | fsrctplid |
| 2 | idx_src_projecttpl_fobj |  | fbizobject |
| 3 | pk_src_projecttpl |  | fentryid |
| 4 | idx_src_projecttpl_fcom |  | fcomponentid |
| 5 | idx_src_projecttpl_fid |  | fid |
| 6 | idx_src_projecttpl_ftem |  | ftemplateid |

---

## 关键流程分录-子表 t_src_projectnode

- **表名称：** 关键流程分录-子表
- **表名：** t_src_projectnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiznodeid | 关键业务节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 4 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 6 | fbizobject | 关键业务对象 | varchar | 50 |  | √ | ' ' | 关键业务对象 |
| 7 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectnode_fobj |  | fbizobject |
| 2 | idx_src_projectnode_fid |  | fid |
| 3 | pk_src_projectnode |  | fentryid |
| 4 | idx_src_projectnode_feobj |  | fextobject |
| 5 | idx_src_projectnode_fnod |  | fbiznodeid |
| 6 | idx_src_projectnode_ftem |  | ftemplateid |

---

## 附属流程分录-子表 t_src_projectnodesub

- **表名称：** 附属流程分录-子表
- **表名：** t_src_projectnodesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbiznodeid | 附属业务节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 3 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 5 | fbizobject | 附属业务对象 | varchar | 50 |  | √ | ' ' | 附属业务对象 |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 9 | fisaudit | 是否需要审核 | bpchar | 1 |  | √ | '0' | 是否需要审核 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectnodesub_fobj |  | fbizobject |
| 2 | idx_src_projectnodesub_feid |  | fentryid |
| 3 | pk_src_projectnodesub |  | fdetailid |
| 4 | idx_src_projectnodesub_fnod |  | fbiznodeid |
| 5 | idx_src_projectnodesub_feobj |  | fextobject |
| 6 | idx_src_projectnodesub_ftem |  | ftemplateid |

---

## 采购清单分录-分表 t_src_contractentry_a

- **表名称：** 采购清单分录-分表
- **表名：** t_src_contractentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fsalorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 5 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 6 | fprecfmqty | fprecfmqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fsourceentryid | 上游源单分录ID | varchar | 50 |  | √ | ' ' | 上游源单分录ID |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fcontractbaseqty | 已签合同基本数量 | numeric | 23 | 10 | √ | 0 | 已签合同基本数量 |
| 10 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 12 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 13 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :未设置 1 :已设置 |
| 15 | fpurorderno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 16 | fcfmbaseqty | 定标基本数量 | numeric | 23 | 10 | √ | 0 | 定标基本数量 |
| 17 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fpreorderratio | fpreorderratio | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fisnew | 新增标的 | bpchar | 1 |  | √ | '0' | 新增标的 |
| 21 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 22 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbdsupplierid | 供应商库(bd_supplier) | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fprice5 | 定标价税合计 | numeric | 23 | 10 | √ | 0 | 定标价税合计 |
| 25 | fprice6 | 本币定标未税金额 | numeric | 23 | 10 | √ | 0 | 本币定标未税金额 |
| 26 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fprice4 | 定标未税金额 | numeric | 23 | 10 | √ | 0 | 定标未税金额 |
| 28 | fprice7 | 本币定标价税合计 | numeric | 23 | 10 | √ | 0 | 本币定标价税合计 |
| 29 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0 | 已订货基本数量 |
| 30 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 31 | fprotocolqty | 关联协议数量 | numeric | 23 | 10 | √ | 0 | 关联协议数量 |
| 32 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 33 | fxkpurorderno | 星空订单编号 | varchar | 2000 |  | √ | ' ' | 星空订单编号 |
| 34 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 35 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 38 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentry_a_fid |  | fid |
| 2 | pk_src_contractentry_a |  | fentryid |

---

## 签约单-关联追踪表 t_src_project_tc

- **表名称：** 签约单-关联追踪表
- **表名：** t_src_project_tc

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
| 1 | pk_src_project_tc |  | fid |
| 2 | idx_src_project_tc_tid |  | ftid |
| 3 | idx_src_project_tc_tbill |  | ftbillid |

---

## 采购清单分录-子表 t_src_contractentry

- **表名称：** 采购清单分录-子表
- **表名：** t_src_contractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliernumber | 供应商ID | varchar | 50 |  | √ | ' ' | 供应商ID |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | frebate | 返点(%) | numeric | 19 | 6 | √ | 0 | 返点(%) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | flocprice | 未税单价(本位币) | numeric | 23 | 10 | √ | 0 | 未税单价(本位币) |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fcontractqty | 关联合同数量 | numeric | 23 | 10 | √ | 0 | 关联合同数量 |
| 11 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 9 :预中标 7 :资审不合格 |
| 13 | fexchtypeid | 汇率(废弃) | int8 | 64 |  | √ | 0 | [汇率 bd_exrate_tree](../base_files/bd_exrate_tree.md) |
| 14 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 15 | fpricelistno | 价目表编号 | varchar | 50 |  | √ | ' ' | 价目表编号 |
| 16 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 17 | fsourcelistid | 货源清单分录ID | varchar | 50 |  | √ | ' ' | 货源清单分录ID |
| 18 | fpackageid | 标段ID | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 19 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 20 | fqtyfrom | 阶梯数量(从) | numeric | 23 | 10 | √ | 0 | 阶梯数量(从) |
| 21 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0 | 折扣率(%) |
| 25 | fname | fname | varchar | 300 |  | √ | ' ' |  |
| 26 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 29 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 30 | fdescription | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 31 | fsysresult | 系统推荐 | bpchar | 1 |  | √ | ' ' | 系统推荐,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 7 :资审不合格 |
| 32 | factprice | 实际未税单价 | numeric | 23 | 10 | √ | 0 | 实际未税单价 |
| 33 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 34 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 35 | fcontracttaxamt | 关联合同价税合计 | numeric | 23 | 10 | √ | 0 | 关联合同价税合计 |
| 36 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 37 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 40 | frank | 排名 | int4 | 32 |  | √ | 0 | 排名 |
| 41 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 42 | fsrcbillno | 上游源单单号 | varchar | 50 |  | √ | ' ' | 上游源单单号 |
| 43 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 44 | fmaxtaxprice | 起标价(含税) | numeric | 23 | 10 | √ | 0 | 起标价(含税) |
| 45 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标的 I :已废标 J :已终止 |
| 46 | fmaterialgroupid | fmaterialgroupid | int8 | 64 |  | √ | 0 |  |
| 47 | fsourcelistno | 货源清单编号 | varchar | 50 |  | √ | ' ' | 货源清单编号 |
| 48 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 49 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 50 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 51 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 52 | fmaxprice | 起标价(不含税) | numeric | 23 | 10 | √ | 0 | 起标价(不含税) |
| 53 | feffectdate | 价格生效时间 | timestamp | 0 |  |  | null | 价格生效时间 |
| 54 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 55 | freqsource | 需求来源 | bpchar | 1 |  | √ | '3' | 需求来源,枚举: 1 :寻源申请 2 :采购申请 3 :项目立项 4 :项目启动 5 :采购共享 |
| 56 | fbidmaterialid | 招标标的 | int8 | 64 |  | √ | 0 | [项目立项分录F7 src_demandf7two](../src_files/src_demandf7two.md) |
| 57 | ffeerate | 费率(%) | numeric | 19 | 6 | √ | 0 | 费率(%) |
| 58 | fpricelistid | 价目表分录ID | varchar | 50 |  | √ | ' ' | 价目表分录ID |
| 59 | fpkgamount | 标段未税金额 | numeric | 23 | 10 | √ | 0 | 标段未税金额 |
| 60 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | [片区与地区 pds_areadistrict](../pds_files/pds_areadistrict.md) |
| 61 | fpkgtaxamount | 标段价税合计 | numeric | 23 | 10 | √ | 0 | 标段价税合计 |
| 62 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 63 | forderqty | 关联订单数量 | numeric | 23 | 10 | √ | 0 | 关联订单数量 |
| 64 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 65 | fordertaxamt | 关联订单价税合计 | numeric | 23 | 10 | √ | 0 | 关联订单价税合计 |
| 66 | forderratio | 份额(%) | numeric | 19 | 6 | √ | 0 | 份额(%) |
| 67 | fprice_uom | 价格单位 | int4 | 32 |  | √ | 0 | 价格单位 |
| 68 | floctaxprice | 含税单价(本位币) | numeric | 23 | 10 | √ | 0 | 含税单价(本位币) |
| 69 | flgortid | 仓库代码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 70 | fcontractamt | 关联合同未税金额 | numeric | 23 | 10 | √ | 0 | 关联合同未税金额 |
| 71 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 72 | fduedate | 价格失效时间 | timestamp | 0 |  |  | null | 价格失效时间 |
| 73 | fdecrease | 降幅(%) | numeric | 19 | 6 | √ | 0 | 降幅(%) |
| 74 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 75 | flocamount | 未税金额(本位币) | numeric | 23 | 10 | √ | 0 | 未税金额(本位币) |
| 76 | fqtyto | 阶梯数量(至) | numeric | 23 | 10 | √ | 0 | 阶梯数量(至) |
| 77 | forderamt | 关联订单未税金额 | numeric | 23 | 10 | √ | 0 | 关联订单未税金额 |
| 78 | fsourcebillid | 上游源单ID | varchar | 50 |  | √ | ' ' | 上游源单ID |
| 79 | fareaid | 地区 | int8 | 64 |  | √ | 0 | [片区与地区 pds_areadistrict](../pds_files/pds_areadistrict.md) |
| 80 | fexchrate | 汇率值(废弃) | numeric | 19 | 6 | √ | 0 | 汇率值(废弃) |
| 81 | fbuyernote | 采购方备注 | varchar | 512 |  | √ | ' ' | 采购方备注 |
| 82 | fcurrencyid | 报价币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 83 | fvieamount | 竞价金额 | numeric | 23 | 10 | √ | 0 | 竞价金额 |
| 84 | fsuppliernote | 供应商备注 | varchar | 512 |  | √ | ' ' | 供应商备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentry_eid |  | fentrystatus |
| 2 | idx_src_contractentry_fid |  | fid |
| 3 | idx_src_contractentry_proid |  | fprojectid |
| 4 | idx_src_contractentry_sid |  | fsupplierid,fsuppliertype |
| 5 | pk_src_contractentry |  | fentryid |
| 6 | idx_src_contractentry_fpakid |  | fpackageid |
| 7 | idx_src_contractentry_pid |  | fpurlistid |

---

## 采购组织(多选)-多选基础资料表 t_src_projectpurorg

- **表名称：** 采购组织(多选)-多选基础资料表
- **表名：** t_src_projectpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectpurorg_bid |  | fbasedataid |
| 2 | idx_src_projectpurorg_fid |  | fid |
| 3 | pk_src_projectpurorg |  | fpkid |

---

## 签约单-主表 t_src_project

- **表名称：** 签约单-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | 项目立项 | int8 | 64 |  | √ | 0 | [项目立项查询 src_demandno](../src_files/src_demandno.md) |
| 8 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | 定标未税总价 | numeric | 23 | 10 | √ | 0 | 定标未税总价 |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | 招标项目编号 | varchar | 30 |  | √ | ' ' | 招标项目编号 |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | 当前节点名称 | varchar | 50 |  | √ | ' ' | 当前节点名称 |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 41 | ftieredtype | 阶梯报价方式 | bpchar | 1 |  | √ | '1' | 阶梯报价方式,枚举: 1 :不启用阶梯报价 2 :采购清单分录总量阶梯报价 3 :采购清单子分录总量阶梯报价 4 :采购清单子分录分段阶梯报价 |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | 招标时间 | timestamp | 0 |  |  | null | 招标时间 |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsystype | 来源类型 | bpchar | 1 |  | √ | '1' | 来源类型,枚举: 1 :项目启动 2 :手工新增 3 :外部系统 |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [采购业务组(封存) bd_pmoperatorgroup](../sbd_files/bd_pmoperatorgroup.md) |
| 54 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 55 | fismultipackage | 是否多标段 | bpchar | 1 |  | √ | '0' | 是否多标段 |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | 寻源方式类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 58 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |
| 62 | fterminalnode | 终止节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | 定标含税总价 | numeric | 23 | 10 | √ | 0 | 定标含税总价 |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 80 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_sourceid |  | fsourceid |
| 2 | idx_src_project_parentid |  | fparentid |
| 3 | pk_src_project |  | fid |
| 4 | idx_src_project_sourceclassid |  | fsourceclassid |
| 5 | idx_src_project_status |  | fopenstatus |
| 6 | idx_src_project_type |  | fsrctypeid |

---

## 采购方附件-附件表 t_src_contractentry_fj

- **表名称：** 采购方附件-附件表
- **表名：** t_src_contractentry_fj

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
| 1 | pk_src_contractentry_fj |  | fpkid |
| 2 | idx_src_contractentry_fj_fid |  | fentryid |
| 3 | idx_src_contractentry_fj_bid |  | fbasedataid |

---

## 签约单-分表 t_src_project_a

- **表名称：** 签约单-分表
- **表名：** t_src_project_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 255 |  |  | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 5 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fisbidnotice | fisbidnotice | bpchar | 1 |  | √ | '0' |  |
| 9 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 10 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fversion | 版本号 | int8 | 64 |  | √ | 1 | 版本号 |
| 12 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 16 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 17 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 18 | fprojectcreatorid | 项目创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fotherwinrule | fotherwinrule | varchar | 255 |  |  | ' ' |  |
| 24 | fdecisionname | fdecisionname | varchar | 100 |  | √ | ' ' |  |
| 25 | fispaper | fispaper | bpchar | 1 |  | √ | '0' |  |
| 26 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 27 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 28 | freasonremark_tag | freasonremark_tag | text | 0 |  |  | null |  |
| 29 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 30 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 31 | faftertalkrule | faftertalkrule | varchar | 255 |  |  | ' ' |  |
| 32 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
| 33 | fsolereason | fsolereason | bpchar | 1 |  | √ | ' ' |  |
| 34 | forderrule | forderrule | varchar | 255 |  | √ | ' ' |  |
| 35 | freasonremark | freasonremark | varchar | 255 |  | √ | ' ' |  |
| 36 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 37 | fdecisionbillno | fdecisionbillno | varchar | 50 |  | √ | ' ' |  |
| 38 | fcontractcycle | fcontractcycle | varchar | 50 |  | √ | ' ' |  |
| 39 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 42 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fbidaddress | fbidaddress | varchar | 50 |  | √ | ' ' |  |
| 45 | fsourcestate | fsourcestate | varchar | 30 |  | √ | ' ' |  |
| 46 | fsrcapplyid | 寻源申请 | int8 | 64 |  | √ | 0 | [寻源申请F7 src_applyf7](../src_files/src_applyf7.md) |
| 47 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 48 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 49 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 50 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 51 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 52 | fprojectcreatetime | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
| 53 | fismustapply | fismustapply | bpchar | 1 |  | √ | '0' |  |
| 54 | fdiscardrule | fdiscardrule | varchar | 255 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_a |  | fid |
| 2 | idx_src_project_a_fcreatorid |  | fcreatorid |
| 3 | idx_src_project_a_fsrcapplyid |  | fsrcapplyid |

---

## 签约单-分表 t_src_project_x

- **表名称：** 签约单-分表
- **表名：** t_src_project_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 5 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止/流标 E :已废标 Z :无需处理 |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 14 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_x |  | fid |
| 2 | idx_src_project_x_fcreatorid |  | fcreatorid |

---

## 签约单-多语言表 t_src_project_l

- **表名称：** 签约单-多语言表
- **表名：** t_src_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | 当前节点名称 | varchar | 100 |  | √ | ' ' | 当前节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_l_flocaleid |  | flocaleid,fid |
| 2 | pk__src_project_l |  | fpkid |

---

## 签约单-反写记录表 t_src_project_wb

- **表名称：** 签约单-反写记录表
- **表名：** t_src_project_wb

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
| 1 | idx_src_project_wb_fk |  | fid |
| 2 | pk_src_project_wb |  | fentryid |

---

## 商务条款分录-子表 t_src_contractitem

- **表名称：** 商务条款分录-子表
- **表名：** t_src_contractitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freply | 供应商回复 | varchar | 510 |  | √ | ' ' | 供应商回复 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdemandvalue | 采购方要求值 | varchar | 510 |  | √ | ' ' | 采购方要求值 |
| 6 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 7 | frequest | 商务条款名称 | varchar | 510 |  | √ | ' ' | 商务条款名称 |
| 8 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | [寻源商务条款 src_bizitem](../src_files/src_bizitem.md) |
| 9 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 10 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 11 | freplyvalue | 回复值 | varchar | 510 |  | √ | ' ' | 回复值 |
| 12 | fdemand | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractitem_fid |  | fid |
| 2 | idx_src_contractitem_fsid |  | fsupplierid |
| 3 | pk_src_contractitem |  | fentryid |

---

## 中标金额汇总分录(MOV)-子表 t_src_decisionsumsup2

- **表名称：** 中标金额汇总分录(MOV)-子表
- **表名：** t_src_decisionsumsup2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 3 | fmaxamount | 标杆未税金额 | numeric | 23 | 10 | √ | 0 | 标杆未税金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresult | 是否中标 | varchar | 30 |  | √ | ' ' | 是否中标,枚举: 1 :中标 2 :未中标 |
| 6 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 7 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 8 | fpreorderratio1 | 预定标含税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标含税占比(%) |
| 9 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 10 | floctaxamount | 报价含税金额 | numeric | 23 | 10 | √ | 0 | 报价含税金额 |
| 11 | fpreorderratio | 预定标未税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标未税占比(%) |
| 12 | forderratio | 中标未税占比(%) | numeric | 23 | 10 | √ | 0 | 中标未税占比(%) |
| 13 | fbudgetamount | fbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fpreamount | 预定标未税金额 | numeric | 23 | 10 | √ | 0 | 预定标未税金额 |
| 15 | ftaxamountrate | 含税价差率(%) | numeric | 23 | 10 | √ | 0 | 含税价差率(%) |
| 16 | fpretaxamount | 预定标含税金额 | numeric | 23 | 10 | √ | 0 | 预定标含税金额 |
| 17 | fcontracttype | fcontracttype | bpchar | 1 |  | √ | ' ' |  |
| 18 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 19 | famountrate | 未税价差率(%) | numeric | 23 | 10 | √ | 0 | 未税价差率(%) |
| 20 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 21 | fmaxtaxamount | 标杆含税金额 | numeric | 23 | 10 | √ | 0 | 标杆含税金额 |
| 22 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 23 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 24 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 25 | fbidcount | 中标标的数 | int4 | 32 |  | √ | 0 | 中标标的数 |
| 26 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 27 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 29 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 30 | flocamount | 报价未税金额 | numeric | 23 | 10 | √ | 0 | 报价未税金额 |
| 31 | ftaxamountdiff | 含税价差 | numeric | 23 | 10 | √ | 0 | 含税价差 |
| 32 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 33 | famountdiff | 未税价差 | numeric | 23 | 10 | √ | 0 | 未税价差 |
| 34 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | forderratio1 | 中标含税占比(%) | numeric | 23 | 10 | √ | 0 | 中标含税占比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsup2_fpid |  | fparentid |
| 2 | pk_src_decisionsumsup2 |  | fentryid |
| 3 | idx_src_decisionsumsup2_fpag |  | fpackageid |
| 4 | idx_src_decisionsumsup2_fid |  | fid |
| 5 | idx_src_decisionsumsup2_fcid |  | fcategoryid |
| 6 | idx_src_decisionsumsup2_fsup |  | fsupplierid |
| 7 | idx_src_decisionsumsup2_fpro |  | fprojectid |

---

## 阶梯报价分录-子表 t_src_contractentrysub

- **表名称：** 阶梯报价分录-子表
- **表名：** t_src_contractentrysub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftieredprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 2 | ftieredunitid | 阶梯计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | ftieredtaxamount | 阶梯价税合计 | numeric | 23 | 10 | √ | 0 | 阶梯价税合计 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftieredprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 6 | ftieredamount | 阶梯未税金额 | numeric | 23 | 10 | √ | 0 | 阶梯未税金额 |
| 7 | ftieredqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 8 | ftieredqty | 阶梯数量 | numeric | 23 | 10 | √ | 0 | 阶梯数量 |
| 9 | ftieredtaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | ftierednote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | ftieredcurrid | 阶梯报价币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | ftieredqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentrysub_eid |  | fentryid |
| 2 | pk_src_contractentrysub |  | fdetailid |
| 3 | idx_src_contractentrysub_pid |  | ftieredprojectid |

---

## 关联子实体-子表 t_src_contractentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_contractentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcontracttaxamt_old | 关联合同价税合计_原始携带值 | numeric | 23 | 10 |  | null | 关联合同价税合计_原始携带值 |
| 2 | fcontracttaxamt | 关联合同价税合计_确认携带值 | numeric | 23 | 10 |  | null | 关联合同价税合计_确认携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 4 | fcontractamt | 关联合同未税金额_确认携带值 | numeric | 23 | 10 |  | null | 关联合同未税金额_确认携带值 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 6 | fcontractqty_old | 关联合同数量_原始携带值 | numeric | 23 | 10 |  | null | 关联合同数量_原始携带值 |
| 7 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcontractqty | 关联合同数量_确认携带值 | numeric | 23 | 10 |  | null | 关联合同数量_确认携带值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 11 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 12 | fcontractamt_old | 关联合同未税金额_原始携带值 | numeric | 23 | 10 |  | null | 关联合同未税金额_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_contractentry_lk |  | fpkid |
| 2 | idx_src_contractentry_lk_fk |  | fentryid |

---

## 供应商附件-附件表 t_src_contractentry_supfj

- **表名称：** 供应商附件-附件表
- **表名：** t_src_contractentry_supfj

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
| 1 | idx_src_contractentry_sfj_fid |  | fentryid |
| 2 | idx_src_contractentry_sfj_bid |  | fbasedataid |
| 3 | pk_src_contractentry_supfj |  | fpkid |
