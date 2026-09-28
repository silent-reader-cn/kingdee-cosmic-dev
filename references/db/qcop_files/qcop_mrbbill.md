# 其他MRB评审单-qcop_mrbbill

## 其他MRB评审单-多语言表 t_qcop_mrb_l

- **表名称：** 其他MRB评审单-多语言表
- **表名：** t_qcop_mrb_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlement | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 缺陷描述 | varchar | 255 |  | √ | ' ' | 缺陷描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcop_mrb_l |  | fpkid |

---

## 其他MRB评审单-分表 t_qcop_mrb_s

- **表名称：** 其他MRB评审单-分表
- **表名：** t_qcop_mrb_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furgentqty | 急料数量 | numeric | 23 | 10 | √ | 0 | 急料数量 |
| 3 | fperformance | 性能 | bpchar | 1 |  | √ | '0' | 性能 |
| 4 | fresppersonid | fresppersonid | int8 | 64 |  | √ | 0 |  |
| 5 | fiseffectprod | 退货是否影响生产 | bpchar | 1 |  | √ | '0' | 退货是否影响生产,枚举: 0 :否 1 :是 |
| 6 | fisliaison | fisliaison | bpchar | 1 |  | √ | '0' |  |
| 7 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 8 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 10 | fothersdesc | 其它方面 | varchar | 255 |  | √ | ' ' | 其它方面 |
| 11 | fsecurity | 安全 | bpchar | 1 |  | √ | '0' | 安全 |
| 12 | fprocessdeptid | fprocessdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fissupplymeet | 后续供应是否满足计划 | bpchar | 1 |  | √ | '0' | 后续供应是否满足计划,枚举: 0 :否 1 :是 |
| 14 | fothers | 其它 | bpchar | 1 |  | √ | '0' | 其它 |
| 15 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fsize | 尺寸 | bpchar | 1 |  | √ | '0' | 尺寸 |
| 17 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 18 | fappearance | 外观 | bpchar | 1 |  | √ | '0' | 外观 |
| 19 | fcausation | fcausation | varchar | 255 |  | √ | ' ' |  |
| 20 | flaunchdate | 上线日期 | timestamp | 0 |  |  | null | 上线日期 |
| 21 | fresponsibleparty | fresponsibleparty | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcop_mrb_s |  | fid |

---

## 评审明细-子表 t_qcop_mrbentry

- **表名称：** 评审明细-子表
- **表名：** t_qcop_mrbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 处理数量 | numeric | 23 | 10 | √ | 0 | 处理数量 |
| 3 | fchkobjentryid | 检验对象行Id | int8 | 64 |  | √ | 0 | 检验对象行Id |
| 4 | finspfirstentrykey | 首检单分录标识 | varchar | 80 |  | √ | ' ' | 首检单分录标识 |
| 5 | frowtype | 分录行类型 | varchar | 5 |  | √ | ' ' | 分录行类型,枚举: A :来源分录行 B :复制分录行 |
| 6 | founqualitype | 原不良问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 7 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsrcsubentryid | 来源子分录 | varchar | 80 |  | √ | ' ' | 来源子分录 |
| 10 | fsrcentryidcp | 来源子分录关联复制 | varchar | 80 |  | √ | ' ' | 来源子分录关联复制 |
| 11 | fserialid | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 12 | fmemo | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fisdefect | 不良处理 | bpchar | 1 |  | √ | '0' | 不良处理 |
| 14 | fbaseunitqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 15 | fchkobjid | 检验对象Id | int8 | 64 |  | √ | 0 | 检验对象Id |
| 16 | fsrcinspectbillentryid | fsrcinspectbillentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fohandmode | 原处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 18 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 19 | fassqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fhandmode | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 22 | foqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcop_mrbentry |  | fentryid |

---

## 其他MRB评审单-主表 t_qcop_mrb

- **表名称：** 其他MRB评审单-主表
- **表名：** t_qcop_mrb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 来源单据分录内码 | varchar | 255 |  | √ | ' ' | 来源单据分录内码 |
| 3 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 4 | fsrcbillno | 来源单据编号 | varchar | 255 |  | √ | ' ' | 来源单据编号 |
| 5 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsettlement | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | flotno | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsrcbillid | 来源单据内码 | varchar | 255 |  | √ | ' ' | 来源单据内码 |
| 23 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 26 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fdescription | 缺陷描述 | varchar | 255 |  | √ | ' ' | 缺陷描述 |
| 29 | fstocklocid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | fbaseunitqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 32 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 33 | fstockorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 35 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcop_mrb_billno |  | fbillno |
| 2 | pk_t_qcop_mrb |  | fid |

---

## 其他MRB评审单-关联追踪表 t_qcop_mrb_tc

- **表名称：** 其他MRB评审单-关联追踪表
- **表名：** t_qcop_mrb_tc

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
| 1 | idx_qcop_mrb_tc_tbill |  | ftbillid |
| 2 | idx_qcop_mrb_tc_tid |  | ftid |
| 3 | pk_qcop_mrb_tc |  | fid |

---

## 关联子实体-子表 t_qcop_mrbentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcop_mrbentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseunitqty | 基本单位数量_确认携带值 | numeric | 23 | 10 | √ | 0 | 基本单位数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseunitqty_old | 基本单位数量_原始携带值 | numeric | 23 | 10 | √ | 0 | 基本单位数量_原始携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcop_mrbentry_lk |  | fpkid |

---

## 其他MRB评审单-反写记录表 t_qcop_mrb_wb

- **表名称：** 其他MRB评审单-反写记录表
- **表名：** t_qcop_mrb_wb

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
| 1 | idx_qcop_mrb_wb_fk |  | fid |
| 2 | pk_qcop_mrb_wb |  | fentryid |
