# 扩展节点基类-src_bidbillcomptpl_ext

## 扩展节点基类-多语言表 t_src_project_ext_l

- **表名称：** 扩展节点基类-多语言表
- **表名：** t_src_project_ext_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_ext_l_lid |  | flocaleid |
| 2 | pk_src_project_ext_l |  | fpkid |

---

## 扩展节点基类-主表 t_src_project_ext

- **表名称：** 扩展节点基类-主表
- **表名：** t_src_project_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsourceid | 项目立项 | int8 | 64 |  | √ | 0 | 项目立项查询 src_demandno |
| 4 | ftieredtype | 阶梯报价方式 | bpchar | 1 |  | √ | '1' | 阶梯报价方式,枚举: 1 :不启用阶梯报价 2 :采购清单分录阶梯报价 3 :采购清单子表阶梯报价 |
| 5 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止/流标 E :已废标 Z :无需处理 |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 8 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 9 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 9 :报价即开标(非密封报价) |
| 13 | fsceneid | 寻源场景名称 | int8 | 64 |  | √ | 0 | 采委会寻源场景F7 src_decisionscenereq |
| 14 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 15 | ftendertype | 招标方式 | bpchar | 1 |  | √ | ' ' | 招标方式,枚举: 1 :邀请招标 2 :公开招标 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fismultipackage | 是否多标段 | bpchar | 1 |  | √ | '0' | 是否多标段 |
| 18 | fsourceclassid | 寻源方式类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 19 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 20 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 21 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 23 | fbillno | 招标项目编号 | varchar | 30 |  | √ | ' ' | 招标项目编号 |
| 24 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |
| 25 | fterminalnode | 终止节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 29 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 30 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 31 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 32 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 35 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 36 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 38 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 39 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 40 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 41 | fnodename | 当前节点名称 | varchar | 50 |  | √ | ' ' | 当前节点名称 |
| 42 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 43 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 44 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 45 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_ext_sid |  | fsourceid |
| 2 | pk_src_project_ext |  | fid |
| 3 | idx_src_project_ext_pid |  | fparentid |
| 4 | idx_src_project_ext_fid |  | fsrctypeid |

---

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
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
| 2 | fbiznodeid | 关键业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 6 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
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
| 1 | fbiznodeid | 附属业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 5 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
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

## 扩展节点基类-分表 t_src_project_ext_a

- **表名称：** 扩展节点基类-分表
- **表名：** t_src_project_ext_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fprojectcreatetime | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
| 5 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | fsrcapplyid | 寻源申请 | int8 | 64 |  | √ | 0 | 寻源申请F7 src_applyf7 |
| 9 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 10 | fprojectcreatorid | 项目创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_ext_a |  | fid |
| 2 | idx_src_project_ext_a_cid |  | fcreatorid |

---

## 采购组织(多选)-多选基础资料表 t_src_projectpurorg

- **表名称：** 采购组织(多选)-多选基础资料表
- **表名：** t_src_projectpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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

## 中标金额汇总分录(MOV)-子表 t_src_decisionsumsup2

- **表名称：** 中标金额汇总分录(MOV)-子表
- **表名：** t_src_decisionsumsup2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fresult | 是否中标 | varchar | 30 |  | √ | ' ' | 是否中标,枚举: 1 :中标 2 :未中标 |
| 5 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 6 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 7 | fpreorderratio1 | 预定标含税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标含税占比(%) |
| 8 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 9 | floctaxamount | 报价含税金额 | numeric | 23 | 10 | √ | 0 | 报价含税金额 |
| 10 | fpreorderratio | 预定标未税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标未税占比(%) |
| 11 | forderratio | 中标未税占比(%) | numeric | 23 | 10 | √ | 0 | 中标未税占比(%) |
| 12 | fbudgetamount | fbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 13 | fpreamount | 预定标未税金额 | numeric | 23 | 10 | √ | 0 | 预定标未税金额 |
| 14 | fpretaxamount | 预定标含税金额 | numeric | 23 | 10 | √ | 0 | 预定标含税金额 |
| 15 | fcontracttype | fcontracttype | bpchar | 1 |  | √ | ' ' |  |
| 16 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 17 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 21 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 22 | flocamount | 报价未税金额 | numeric | 23 | 10 | √ | 0 | 报价未税金额 |
| 23 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | forderratio1 | 中标含税占比(%) | numeric | 23 | 10 | √ | 0 | 中标含税占比(%) |

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
