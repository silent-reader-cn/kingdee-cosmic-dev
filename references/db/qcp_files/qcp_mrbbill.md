# 来料MRB评审单-qcp_mrbbill

## 来料MRB评审单-主表 t_qcp_mrb

- **表名称：** 来料MRB评审单-主表
- **表名：** t_qcp_mrb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 来源单据分录内码 | varchar | 255 |  |  | null | 来源单据分录内码 |
| 3 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 4 | fsrcbillno | 来源单据编号 | varchar | 255 |  |  | null | 来源单据编号 |
| 5 | fmaterialid | 物料主数据 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 质检组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsettlement | 处理意见 | varchar | 255 |  |  | null | 处理意见 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbiztype | 业务类型 | int8 | 64 |  |  | null | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | flotno | 批号 | varchar | 80 |  |  | null | 批号 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpurchaseorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fsubinspector | 质检员 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fqty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fsrcbillid | 来源单据内码 | varchar | 255 |  |  | null | 来源单据内码 |
| 25 | fmaterialcfg | 物料编码 | int8 | 64 |  |  | null | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 26 | fsettlcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | funitid | 计量单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fmversion | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 29 | fstockid | 仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fdescription | 缺陷描述 | varchar | 255 |  |  | null | 缺陷描述 |
| 32 | fstocklocid | 仓位 | int8 | 64 |  |  | null | [仓位 bd_location](../sbd_files/bd_location.md) |
| 33 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 34 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fsupplierid | 供应商 | int8 | 64 |  |  | null | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 36 | fbaseunitqty | 基本单位数量 | numeric | 23 | 10 |  | null | 基本单位数量 |
| 37 | fscsystem | 来源系统 | varchar | 50 |  |  | null | 来源系统 |
| 38 | fextendvalue | 扩展值 | varchar | 50 |  | √ | ' ' | 扩展值,枚举: A :赠品 B :合并检验 |
| 39 | fstockorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fsrcbilltype | 来源单据类型 | int8 | 64 |  |  | null | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 41 | finspectdepid | 质检部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltype | 单据类型 | int8 | 64 |  |  | null | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_mrb |  | fid |

---

## 来料MRB评审单-分表 t_qcp_mrb_s

- **表名称：** 来料MRB评审单-分表
- **表名：** t_qcp_mrb_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furgentqty | 急料数量 | numeric | 23 | 10 |  | null | 急料数量 |
| 3 | fperformance | 性能 | bpchar | 1 |  | √ | '0' | 性能 |
| 4 | fresppersonid | 责任人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fiseffectprod | 退货是否影响生产 | bpchar | 1 |  | √ | '0' | 退货是否影响生产,枚举: 0 :否 1 :是 |
| 6 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 7 | fisliaison | 发供应商异常联络单 | bpchar | 1 |  | √ | ' ' | 发供应商异常联络单,枚举: 0 :否 1 :是 |
| 8 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 9 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | ffinishdate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fothersdesc | 其它方面 | varchar | 255 |  |  | null | 其它方面 |
| 13 | fsecurity | 安全 | bpchar | 1 |  | √ | '0' | 安全 |
| 14 | fprocessdeptid | 处理部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fissupplymeet | 后续供应是否满足计划 | bpchar | 1 |  | √ | '0' | 后续供应是否满足计划,枚举: 0 :否 1 :是 |
| 16 | fothers | 其它 | bpchar | 1 |  | √ | '0' | 其它 |
| 17 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fsize | 尺寸 | bpchar | 1 |  | √ | '0' | 尺寸 |
| 19 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 20 | fappearance | 外观 | bpchar | 1 |  | √ | '0' | 外观 |
| 21 | fcausation | 原因 | varchar | 255 |  |  | null | 原因 |
| 22 | flaunchdate | 上线日期 | timestamp | 0 |  |  | null | 上线日期 |
| 23 | fresponsibleparty | 来料异常责任方 | bpchar | 1 |  | √ | ' ' | 来料异常责任方,枚举: 1 :我方 2 :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_mrb_s |  | fid |

---

## 来料MRB评审单-多语言表 t_qcp_mrb_l

- **表名称：** 来料MRB评审单-多语言表
- **表名：** t_qcp_mrb_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlement | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fdescription | 缺陷描述 | varchar | 255 |  | √ | ' ' | 缺陷描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_mrb_l |  | fpkid |

---

## 评审明细-子表 t_qcp_mrbentry

- **表名称：** 评审明细-子表
- **表名：** t_qcp_mrbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fchkobjentryid | 检验对象行Id | int8 | 64 |  |  | null | 检验对象行Id |
| 3 | finspfirstentrykey | 首检单分录标识 | varchar | 80 |  |  | null | 首检单分录标识 |
| 4 | frowtype | 分录行类型 | varchar | 5 |  | √ | ' ' | 分录行类型,枚举: A :来源分录行 B :复制分录行 |
| 5 | fdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcentryidcp | 来源子分录关联复制 | varchar | 80 |  |  | null | 来源子分录关联复制 |
| 8 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 9 | fserialid | 序列号 | int8 | 64 |  |  | null | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 10 | fchkobjid | 检验对象Id | int8 | 64 |  |  | null | 检验对象Id |
| 11 | fohandmode | 原处理方式 | int8 | 64 |  |  | null | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 12 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 13 | fmrbmaterielid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 15 | fisdiscountold | 原是否折让 | bpchar | 1 |  | √ | '0' | 原是否折让 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fhandmode | 处理方式 | int8 | 64 |  |  | null | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 18 | foqty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 19 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 20 | fqty | 处理数量 | numeric | 23 | 10 |  | null | 处理数量 |
| 21 | founqualitype | 原不良问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 22 | funitid | 单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fsrcsubentryid | 来源子分录 | varchar | 80 |  |  | null | 来源子分录 |
| 24 | fmemo | 备注 | varchar | 255 |  |  | null | 备注 |
| 25 | fisdefect | 不良处理 | bpchar | 1 |  | √ | '0' | 不良处理 |
| 26 | fbaseunitqty | 基本单位数量 | numeric | 23 | 10 |  | null | 基本单位数量 |
| 27 | fsrcinspectbillentryid | 来源检验单单据行ID（冗余字段，方便查询反写） | int8 | 64 |  | √ | 0 | 来源检验单单据行ID（冗余字段，方便查询反写） |
| 28 | fdiscountamountold | 原折让金额 | numeric | 23 | 10 | √ | 0 | 原折让金额 |
| 29 | fassqty | 关联数量 | numeric | 23 | 10 |  | null | 关联数量 |
| 30 | fmrbmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 31 | freturnnumber | 自动下推退料单编码 | varchar | 80 |  | √ | ' ' | 自动下推退料单编码 |
| 32 | finstocknumber | 自动下推入库单编码 | varchar | 80 |  | √ | ' ' | 自动下推入库单编码 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 34 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_mrbentry |  | fentryid |

---

## 来料MRB评审单-关联追踪表 t_qcp_mrb_tc

- **表名称：** 来料MRB评审单-关联追踪表
- **表名：** t_qcp_mrb_tc

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
| 1 | idx_qcp_mrb_tc_tbill |  | ftbillid |
| 2 | pk_qcp_mrb_tc |  | fid |
| 3 | idx_qcp_mrb_tc_tid |  | ftid |

---

## 关联子实体-子表 t_qcp_mrbentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_mrbentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseunitqty | 基本单位数量_确认携带值 | numeric | 23 | 10 |  | null | 基本单位数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseunitqty_old | 基本单位数量_原始携带值 | numeric | 23 | 10 |  | null | 基本单位数量_原始携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_mrbentry_lk |  | fpkid |

---

## 来料MRB评审单-反写记录表 t_qcp_mrb_wb

- **表名称：** 来料MRB评审单-反写记录表
- **表名：** t_qcp_mrb_wb

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
| 1 | pk_qcp_mrb_wb |  | fentryid |
| 2 | idx_qcp_mrb_wb_fk |  | fid |
