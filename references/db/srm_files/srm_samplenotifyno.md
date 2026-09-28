# 送样通知单号-srm_samplenotifyno

## 送样通知单号-多语言表 t_pur_samplenotify_l

- **表名称：** 送样通知单号-多语言表
- **表名：** t_pur_samplenotify_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 送样原因 | varchar | 255 |  | √ | ' ' | 送样原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_samplenotify_l_pkey |  | fpkid |
| 2 | idx_pur_notify_l_fid |  | fid,flocaleid |

---

## 送样通知单号-主表 t_pur_samplenotify

- **表名称：** 送样通知单号-主表
- **表名：** t_pur_samplenotify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fremark | 送样原因 | varchar | 255 |  | √ | ' ' | 送样原因 |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 4 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 7 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 9 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 11 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 C :已打回 D :部分发货 E :全部发货 |
| 12 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 13 | faptitudenoid | 资审单号 | int8 | 64 |  | √ | 0 | [资质审查单号 srm_aptitudebillno](../srm_files/srm_aptitudebillno.md) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_notify_fbilldate |  | fbilldate |
| 2 | idx_pur_notify_aptitudeid |  | faptitudenoid |
| 3 | t_pur_samplenotify_pkey |  | fid |
| 4 | idx_pur_notify_fbillno |  | fbillno |
