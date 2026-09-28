# 试样结果-adm_sample_in

## 物料分录-子表 t_pur_sampleentry

- **表名称：** 物料分录-子表
- **表名：** t_pur_sampleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 3 | fphone | 签收人电话 | varchar | 20 |  | √ | ' ' | 签收人电话 |
| 4 | faddress | 送样地址 | varchar | 100 |  | √ | ' ' | 送样地址 |
| 5 | freceiver | 样品签收人 | varchar | 20 |  | √ | ' ' | 样品签收人 |
| 6 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fsendqty | 供方确认数量 | numeric | 19 | 6 | √ | 0.000000 | 供方确认数量 |
| 11 | ftestdate | 样品测试时间 | timestamp | 0 |  |  | null | 样品测试时间 |
| 12 | ftester | 测试负责人 | varchar | 20 |  | √ | ' ' | 测试负责人 |
| 13 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 14 | fsenddate | 要求送样时间 | timestamp | 0 |  |  | null | 要求送样时间 |
| 15 | ftestresult | 测试结果 | bpchar | 1 |  | √ | ' ' | 测试结果,枚举: 1 :合格 2 :不合格 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | farrivaldate | 预计到货时间 | timestamp | 0 |  |  | null | 预计到货时间 |
| 18 | funit | funit | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_sampleentry_pkey |  | fentryid |
| 2 | idx_pur_sample_fid_fseq |  | fid,fseq |

---

## 试样结果-主表 t_pur_sample

- **表名称：** 试样结果-主表
- **表名：** t_pur_sample

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 9 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 11 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :部分发货 E :全部发货 |
| 12 | fnotifynoid | fnotifynoid | int8 | 64 |  | √ | 0 |  |
| 13 | fcertifiapplyid | 认证申请单号 | int8 | 64 |  | √ | 0 | 供应商认证申请编号 pbd_certificationapplyno |
| 14 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 4 :样品确认 |
| 15 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 16 | faptitudenoid | 资审审查单号 | int8 | 64 |  | √ | 0 | 资质审查单号 srm_aptitudebillno |
| 17 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_sample_aptitudeid |  | faptitudenoid |
| 2 | t_pur_sample_pkey |  | fid |
| 3 | idx_pur_sample_fbillno |  | fbillno |
| 4 | idx_pur_sample_fbilldate |  | fbilldate |

---

## 试样结果-多语言表 t_pur_sample_l

- **表名称：** 试样结果-多语言表
- **表名：** t_pur_sample_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_sample_l_pkey |  | fpkid |
| 2 | idx_pur_sample_l_fid |  | fid,flocaleid |

---

## 试样结果-分表 t_pur_sample_a

- **表名称：** 试样结果-分表
- **表名：** t_pur_sample_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_sample_a_pkey |  | fid |
| 2 | idx_pur_sample_a_ftime |  | fcreatetime |
