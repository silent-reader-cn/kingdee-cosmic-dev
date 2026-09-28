# 考核管理-adm_examine

## 考核管理-多语言表 t_pur_examine_l

- **表名称：** 考核管理-多语言表
- **表名：** t_pur_examine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fsrcbillname | 数据来源 | varchar | 100 |  | √ | ' ' | 数据来源 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_examine_l_pkey |  | fpkid |
| 2 | idx_pur_examine_l_fid |  | fid,flocaleid |

---

## 考核管理-分表 t_pur_examine_a

- **表名称：** 考核管理-分表
- **表名：** t_pur_examine_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapproverid | 考核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapprovedate | 考核时间 | timestamp | 0 |  |  | null | 考核时间 |
| 4 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 7 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 10 | fcfmopinion | 反馈意见 | varchar | 255 |  | √ | ' ' | 反馈意见 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fcfmdate | 反馈时间 | timestamp | 0 |  |  | null | 反馈时间 |
| 13 | fauditopinion | 考核结果说明 | varchar | 255 |  | √ | ' ' | 考核结果说明 |
| 14 | fcfmid | 反馈人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 17 | finvalidid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_examine_a_ftime |  | fcreatetime |
| 2 | t_pur_examine_a_pkey |  | fid |

---

## 考核管理-主表 t_pur_examine

- **表名称：** 考核管理-主表
- **表名：** t_pur_examine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fexaminerid | 考核责任人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 4 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: C :已审核 Z :已作废 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :已确认 D :考核完成 |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 10 | famount | 实际考核金额(含税) | numeric | 19 | 6 | √ | 0.000000 | 实际考核金额(含税) |
| 11 | fdescription | 考核说明 | varchar | 510 |  |  | ' ' | 考核说明 |
| 12 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fexamtypeid | 考核类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 16 | fcfmstatus | 反馈结果 | bpchar | 1 |  | √ | ' ' | 反馈结果,枚举: A :待反馈 B :同意 C :驳回 |
| 17 | fauditstatus | 考核结果 | bpchar | 1 |  | √ | ' ' | 考核结果,枚举: A :待处理 B :考核完成 C :作废 |
| 18 | fsrcbillname | 数据来源 | varchar | 100 |  | √ | ' ' | 数据来源 |
| 19 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_examine_pkey |  | fid |
| 2 | idx_pur_examine_fbillno |  | fbillno |
| 3 | idx_pur_examine_fbilldate |  | fbilldate |
