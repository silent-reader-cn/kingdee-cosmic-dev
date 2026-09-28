# 质量整改（8D）-pur_qualityrectific

## 预防措施-子表 t_pur_recpmentry

- **表名称：** 预防措施-子表
- **表名：** t_pur_recpmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fdescribe | 措施描述 | varchar | 512 |  | √ | ' ' | 措施描述 |
| 4 | fhead | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcompletiontime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_recpmentry |  | fentryid |
| 2 | idx_pur_recpmentry_fid_fseq |  | fid,fseq |

---

## 问题描述-子表 t_pur_recdescentry

- **表名称：** 问题描述-子表
- **表名：** t_pur_recdescentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhowdiscover | 怎么发现的 | varchar | 512 |  | √ | ' ' | 怎么发现的 |
| 3 | fwhatproblem | 什么问题 | varchar | 512 |  | √ | ' ' | 什么问题 |
| 4 | foccurrencetime | 发生时间 | timestamp | 0 |  |  | null | 发生时间 |
| 5 | fdiscoveryperson | 发现人员 | varchar | 512 |  | √ | ' ' | 发现人员 |
| 6 | fquantityordegree | 数量/程度 | varchar | 50 |  | √ | ' ' | 数量/程度 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fwhyisaproblem | 为什么是问题 | varchar | 512 |  | √ | ' ' | 为什么是问题 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | foccurrencelocation | 发生地点 | varchar | 512 |  | √ | ' ' | 发生地点 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_recdescentry |  | fentryid |
| 2 | idx_pur_recdescentry_fid_fseq |  | fid,fseq |

---

## 执行验证-子表 t_pur_receventry

- **表名称：** 执行验证-子表
- **表名：** t_pur_receventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fisthrough | 是否通过 | bpchar | 1 |  | √ | ' ' | 是否通过,枚举: A :是 B :否 |
| 4 | fhead | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdescription | 验证描述 | varchar | 512 |  | √ | ' ' | 验证描述 |
| 7 | fcompletiontime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_receventry |  | fentryid |
| 2 | idx_pur_receventry_fid_fseq |  | fid,fseq |

---

## 原因分析-子表 t_pur_reccauseentry

- **表名称：** 原因分析-子表
- **表名：** t_pur_reccauseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fsuspiciousreason | 可疑原因 | varchar | 512 |  | √ | ' ' | 可疑原因 |
| 4 | fisrootcause | 是否根本原因 | bpchar | 1 |  | √ | ' ' | 是否根本原因,枚举: 1 :是 0 :否 |
| 5 | fverificationresult | 验证结果 | varchar | 512 |  | √ | ' ' | 验证结果 |
| 6 | fhead | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcompletiontime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_reccauseentry |  | fentryid |
| 2 | idx_pur_reccaentry_fid_fseq |  | fid,fseq |

---

## 明细信息-子表 t_pur_rectifyentry

- **表名称：** 明细信息-子表
- **表名：** t_pur_rectifyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainbillentryseq | 核心单据分录行号 | int4 | 32 |  | √ | 0 | 核心单据分录行号 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fquaproblem | 问题分类 | bpchar | 1 |  | √ | ' ' | 问题分类,枚举: A :尺寸不良 B :外观不良 C :异物 D :混料/错料 E :物理特性不良 F :力学特性不良 G :化学特性不良 H :其他 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frecurrence | 重复发生 | bpchar | 1 |  | √ | ' ' | 重复发生,枚举: 0 :否 1 :是 |
| 9 | fdetails | 问题说明 | varchar | 255 |  | √ | ' ' | 问题说明 |
| 10 | freceiptbillno | 收货单号 | varchar | 80 |  | √ | ' ' | 收货单号 |
| 11 | fsrcbillentryseq | 来源单据分录行号 | int4 | 32 |  | √ | 0 | 来源单据分录行号 |
| 12 | fdetails_tag | 问题说明_详情 | text | 0 |  |  | null | 问题说明_详情 |
| 13 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 14 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 17 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 18 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 20 | freceiptbillid | 收货单ID | varchar | 50 |  | √ | ' ' | 收货单ID |
| 21 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 26 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 27 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 31 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_rectifyentry_fid_fseq |  | fid,fseq |
| 2 | pk_pur_rectifyentry |  | fentryid |
| 3 | idx_pur_rectifyentry_fmatid |  | fmaterialid |

---

## 附件-附件表 t_pur_recfmatta

- **表名称：** 附件-附件表
- **表名：** t_pur_recfmatta

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
| 1 | idx_pur_recfmatta_fbaseid |  | fbasedataid |
| 2 | idx_pur_recfmatta_fentryid |  | fentryid |
| 3 | pk_pur_recfmatta |  | fpkid |

---

## 附件-附件表 t_pur_recevatta

- **表名称：** 附件-附件表
- **表名：** t_pur_recevatta

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
| 1 | idx_pur_recevatta_fbaseid |  | fbasedataid |
| 2 | idx_pur_recevatta_fentryid |  | fentryid |
| 3 | pk_pur_recevatta |  | fpkid |

---

## 附件-附件表 t_pur_recdescatta

- **表名称：** 附件-附件表
- **表名：** t_pur_recdescatta

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
| 1 | idx_pur_recdescattr_fbaseid |  | fbasedataid |
| 2 | pk_pur_recdescatta |  | fpkid |
| 3 | idx_pur_recdescatta_fentryid |  | fentryid |

---

## 建立团队-子表 t_pur_recteamentry

- **表名称：** 建立团队-子表
- **表名：** t_pur_recteamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 80 |  | √ | ' ' | 姓名 |
| 3 | fphone | 手机号 | varchar | 255 |  | √ | ' ' | 手机号 |
| 4 | femail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fteamroles | 团队角色 | bpchar | 1 |  | √ | ' ' | 团队角色,枚举: 0 :组长 1 :组员 |
| 7 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |
| 8 | fprocess | 参与环节 | bpchar | 1 |  | √ | ' ' | 参与环节,枚举: A :问题全程 B :ICA阶段 C :PCA阶段 D :效果验证阶段 |
| 9 | frepresentative | 代表方 | bpchar | 1 |  | √ | ' ' | 代表方,枚举: A :采购方 B :供应商 |
| 10 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | fresponsibility | 职责 | varchar | 255 |  | √ | ' ' | 职责 |
| 12 | fdepartment | 部门 | varchar | 255 |  | √ | ' ' | 部门 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_recteamentry |  | fentryid |
| 2 | idx_pur_recteamentry_fid_fseq |  | fid,fseq |

---

## 附件-附件表 t_pur_recpmatta

- **表名称：** 附件-附件表
- **表名：** t_pur_recpmatta

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
| 1 | idx_pur_recpmatta_fentryid |  | fentryid |
| 2 | pk_pur_recpmatta |  | fpkid |
| 3 | idx_pur_recpmatta_fbaseid |  | fbasedataid |

---

## 质量整改（8D）-主表 t_pur_rectify

- **表名称：** 质量整改（8D）-主表
- **表名：** t_pur_rectify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpcaconfirmer | PCA确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpcafeedbacktime | PCA反馈时间 | timestamp | 0 |  |  | null | PCA反馈时间 |
| 4 | ficaconfirmer | ICA确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | forgid | 发起组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcancelstatus | 取消状态 | bpchar | 1 |  | √ | ' ' | 取消状态,枚举: A :未取消 Z :已取消 |
| 7 | fpcastatus | PCA状态 | bpchar | 1 |  | √ | ' ' | PCA状态,枚举: A :待反馈 B :待确认 C :已确认 D :待重新反馈 |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | ficafeedbacktime | ICA反馈时间 | timestamp | 0 |  |  | null | ICA反馈时间 |
| 10 | fverifyrequiretime | 验证要求时间 | timestamp | 0 |  |  | null | 验证要求时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpcarequiretime | PCA要求时间 | timestamp | 0 |  |  | null | PCA要求时间 |
| 13 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcancelid | 取消人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | ficastatus | ICA状态 | bpchar | 1 |  | √ | ' ' | ICA状态,枚举: A :待反馈 B :待确认 C :已确认 D :待重新反馈 |
| 18 | fpcaconfirmtime | PCA确认时间 | timestamp | 0 |  |  | null | PCA确认时间 |
| 19 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fverifyfeedbacktime | 验证反馈时间 | timestamp | 0 |  |  | null | 验证反馈时间 |
| 24 | fverifyconfirmtime | 验证确认时间 | timestamp | 0 |  |  | null | 验证确认时间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | ficaexplanation | ICA确认说明 | varchar | 512 |  | √ | ' ' | ICA确认说明 |
| 27 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 29 | fverifyconfirmer | 验证确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fpcaexplanation | PCA确认说明 | varchar | 512 |  | √ | ' ' | PCA确认说明 |
| 31 | fcanceldate | 取消日期 | timestamp | 0 |  |  | null | 取消日期 |
| 32 | fpersonid | 发起人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 33 | ficaconfirmtime | ICA确认时间 | timestamp | 0 |  |  | null | ICA确认时间 |
| 34 | ficarequiretime | ICA要求时间 | timestamp | 0 |  |  | null | ICA要求时间 |
| 35 | fsrcbilltype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 0 :新增 1 :质量问题通知 2 :纠正预防措施报告 |
| 36 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 37 | fverifyexplanation | 验证确认说明 | varchar | 512 |  | √ | ' ' | 验证确认说明 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fsummary | 问题总结 | varchar | 512 |  | √ | ' ' | 问题总结 |
| 40 | fverifystatus | 验证状态 | bpchar | 1 |  | √ | ' ' | 验证状态,枚举: A :待反馈 B :待确认 C :已确认 D :待重新反馈 |
| 41 | frectificationtitle | 整改标题 | varchar | 255 |  | √ | ' ' | 整改标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_rectify |  | fid |
| 2 | idx_pur_rectify_fbilldate |  | fbilldate |
| 3 | idx_pur_rectify_fbizid |  | fbizpartnerid |
| 4 | idx_pur_rectify_forgid |  | forgid |
| 5 | idx_pur_rectify_fbillno |  | fbillno |

---

## 质量整改（8D）-关联追踪表 t_pur_rectify_tc

- **表名称：** 质量整改（8D）-关联追踪表
- **表名：** t_pur_rectify_tc

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
| 1 | pk_pur_rectify_tc |  | fid |
| 2 | idx_pur_rectify_tc_tbill |  | ftbillid |
| 3 | idx_pur_rectify_tc_tid |  | ftid |

---

## 永久措施-子表 t_pur_recfmentry

- **表名称：** 永久措施-子表
- **表名：** t_pur_recfmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fverify | 措施验证 | varchar | 512 |  | √ | ' ' | 措施验证 |
| 4 | fdescribe | 措施描述 | varchar | 512 |  | √ | ' ' | 措施描述 |
| 5 | fhead | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcompletiontime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_recfmentry |  | fentryid |
| 2 | idx_pur_recfmentry_fid_fseq |  | fid,fseq |

---

## 附件-附件表 t_pur_reccaatta

- **表名称：** 附件-附件表
- **表名：** t_pur_reccaatta

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
| 1 | idx_pur_reccaatta_fbaseid |  | fbasedataid |
| 2 | pk_pur_reccaatta |  | fpkid |
| 3 | idx_pur_reccaatta_fentryid |  | fentryid |

---

## 关联子实体-子表 t_pur_rectifyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_rectifyentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_rectifyentry_lk |  | fpkid |
| 2 | idx_pur_rectifyentry_lk_fk |  | fentryid |

---

## 临时措施-子表 t_pur_rectmentry

- **表名称：** 临时措施-子表
- **表名：** t_pur_rectmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fverify | 措施验证 | varchar | 512 |  | √ | ' ' | 措施验证 |
| 4 | fdescribe | 措施描述 | varchar | 512 |  | √ | ' ' | 措施描述 |
| 5 | fhead | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcompletiontime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 创建来源 | bpchar | 1 |  | √ | ' ' | 创建来源,枚举: A :采购方 B :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_rectmentry_fid_fseq |  | fid,fseq |
| 2 | pk_pur_rectmentry |  | fentryid |

---

## 附件-附件表 t_pur_rectmatta

- **表名称：** 附件-附件表
- **表名：** t_pur_rectmatta

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
| 1 | idx_pur_rectmatta_fentryid |  | fentryid |
| 2 | pk_pur_rectmatta |  | fpkid |
| 3 | idx_pur_rectmatta_fbaseid |  | fbasedataid |

---

## 质量整改（8D）-反写记录表 t_pur_rectify_wb

- **表名称：** 质量整改（8D）-反写记录表
- **表名：** t_pur_rectify_wb

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
| 1 | idx_pur_rectify_wb_fk |  | fid |
| 2 | pk_pur_rectify_wb |  | fentryid |
