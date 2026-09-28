# 质量问题通知-scp_problemnotice

## 质量问题通知-主表 t_pur_prob_notice

- **表名称：** 质量问题通知-主表
- **表名：** t_pur_prob_notice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 发起方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 16 | fhopendate | 要求反馈日期 | timestamp | 0 |  |  | null | 要求反馈日期 |
| 17 | fsrcbilltype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 1 :质量问题通知 2 :采购收货 |
| 18 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_probnotice_fbizid |  | fbizpartnerid |
| 2 | pk_pur_prob_notice |  | fid |
| 3 | idx_pur_probnotice_fbdate |  | fbilldate |
| 4 | idx_pur_probnotice_forgid |  | forgid |
| 5 | idx_pur_probnotice_fbillno |  | fbillno |

---

## 反馈附件-附件表 t_pur_prob_feedbackatta

- **表名称：** 反馈附件-附件表
- **表名：** t_pur_prob_feedbackatta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_probentry_fbasedataid |  | fbasedataid |
| 2 | idx_pur_probentry_fentryid |  | fentryid |
| 3 | pk_pur_prob_feedbackatta |  | fpkid |

---

## 明细信息-子表 t_pur_prob_entryentity

- **表名称：** 明细信息-子表
- **表名：** t_pur_prob_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fquaproblem | 问题分类 | bpchar | 1 |  | √ | ' ' | 问题分类,枚举: A :尺寸不良 B :外观不良 C :异物 D :混料/错料 E :物理特性不良 F :力学特性不良 G :其他 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 8 | ffeedbackdesc_tag | 反馈说明_详情 | text | 0 |  |  | null | 反馈说明_详情 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | frecurrence | 重复发生 | bpchar | 1 |  | √ | ' ' | 重复发生,枚举: 0 :否 1 :是 |
| 11 | fdetails | 问题说明 | varchar | 255 |  | √ | ' ' | 问题说明 |
| 12 | ffeedbackstatus | 反馈状态 | bpchar | 1 |  | √ | ' ' | 反馈状态,枚举: A :待反馈 B :已反馈 |
| 13 | freceiptbillno | 收货单号 | varchar | 80 |  | √ | ' ' | 收货单号 |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 15 | fdetails_tag | 问题说明_详情 | text | 0 |  |  | null | 问题说明_详情 |
| 16 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 17 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 23 | freceiptbillid | 收货单ID | varchar | 50 |  | √ | ' ' | 收货单ID |
| 24 | ffeedbackdesc | 反馈说明 | varchar | 255 |  | √ | ' ' | 反馈说明 |
| 25 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 30 | ffeedbackerid | 反馈人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 32 | ffacebacktime | 反馈时间 | timestamp | 0 |  |  | null | 反馈时间 |
| 33 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 34 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 38 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_probentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_probentry_fmaterialid |  | fmaterialid |
| 3 | pk_pur_prob_entryentity |  | fentryid |
