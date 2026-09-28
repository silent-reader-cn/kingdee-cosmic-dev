# 资料变更管理-srm_supchange

## 资料变更管理-分表 t_pur_supplierchg_a

- **表名称：** 资料变更管理-分表
- **表名：** t_pur_supplierchg_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcfmopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_supplierchg_a_pkey |  | fid |
| 2 | idx_pur_supplierchg_ftime |  | fcreatetime |

---

## 变更分录-子表 t_pur_supplierchgentry

- **表名称：** 变更分录-子表
- **表名：** t_pur_supplierchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finfotype | 信息类型 | bpchar | 1 |  | √ | ' ' | 信息类型,枚举: S :字符 N :数值 D :日期 L :整数 B :布尔 Z :基础 A :附件 |
| 3 | fsrcentryid | 源单分录ID（序号） | varchar | 50 |  | √ | ' ' | 源单分录ID（序号） |
| 4 | fentryfieldname | 分录字段标识 | varchar | 100 |  | √ | ' ' | 分录字段标识 |
| 5 | fsrcbillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 6 | ffieldname | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 7 | foldvalue | 变更前内容 | varchar | 2000 |  | √ | ' ' | 变更前内容 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fother | 其他字段(多语言) | varchar | 2000 |  | √ | ' ' | 其他字段(多语言) |
| 11 | fentryname | 分录实体标识 | varchar | 50 |  | √ | ' ' | 分录实体标识 |
| 12 | fchgfield | 变更项目 | varchar | 200 |  | √ | ' ' | 变更项目 |
| 13 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :补充 2 :删除 3 :修改 |
| 14 | fsrcbillentryid | 源单分录ID | varchar | 50 |  | √ | '1' | 源单分录ID |
| 15 | fnewvalue | 变更后内容 | varchar | 2000 |  | √ | ' ' | 变更后内容 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_supplierchgentry_pkey |  | fentryid |
| 2 | idx_pur_supchgentry_fid_fseq |  | fid,fseq |

---

## 附件-附件表 t_pur_supchgentry_chgatt

- **表名称：** 附件-附件表
- **表名：** t_pur_supchgentry_chgatt

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
| 1 | t_pur_supchgentry_chgatt_pkey |  | fpkid |
| 2 | inx_chgentry_chgatt_fbdid |  | fbasedataid |
| 3 | inx_chgentry_chgatt_fentryid |  | fentryid |

---

## 资料变更管理-多语言表 t_pur_supplierchg_l

- **表名称：** 资料变更管理-多语言表
- **表名：** t_pur_supplierchg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_supplierchg_l_pkey |  | fpkid |
| 2 | idx_pur_supplierchg_l_fid |  | fid,flocaleid |

---

## 资料变更管理-主表 t_pur_supplierchg

- **表名称：** 资料变更管理-主表
- **表名：** t_pur_supplierchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 4 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmustcfm | 需要审批单位确认 | bpchar | 1 |  | √ | ' ' | 需要审批单位确认 |
| 8 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 10 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcfmstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :待处理 B :变更生效 C :不同意变更 |
| 12 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 13 | fparamchguser | 变更用户参数 | bpchar | 1 |  | √ | '3' | 变更用户参数,枚举: 3 :不同步变更供应商用户 1 :修改原有的供应商管理员用户 2 :新增一个供应商用管理员用户 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_supplierchg_fnumber |  | fsupplierid |
| 2 | t_pur_supplierchg_pkey |  | fid |

---

## 附件-附件表 t_pur_supchgentry_att

- **表名称：** 附件-附件表
- **表名：** t_pur_supchgentry_att

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
| 1 | inx_supchgentry_att_fbdid |  | fbasedataid |
| 2 | t_pur_supchgentry_att_pkey |  | fpkid |
| 3 | inx_supchgentry_att_fentryid |  | fentryid |
