# 改善管理-adm_improve

## 改善管理-主表 t_pur_improve

- **表名称：** 改善管理-主表
- **表名：** t_pur_improve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freplydate | 要求回复时间 | timestamp | 0 |  |  | null | 要求回复时间 |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :改善中 D :改善提交 E :改善通过 F :改善驳回 |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fother | 改善要求（其他） | varchar | 510 |  |  | ' ' | 改善要求（其他） |
| 7 | ffinishstatus | 改善结果 | bpchar | 1 |  | √ | ' ' | 改善结果,枚举: A :待处理 B :同意 C :驳回 |
| 8 | fauditstatus | 审批结果 | bpchar | 1 |  | √ | ' ' | 审批结果,枚举: A :待处理 B :审批通过 C :驳回终止 |
| 9 | fenddate | 要求改善完成时间 | timestamp | 0 |  |  | null | 要求改善完成时间 |
| 10 | fquality | 改善要求（品质） | varchar | 510 |  |  | ' ' | 改善要求（品质） |
| 11 | fsrcbillname | fsrcbillname | varchar | 80 |  | √ | ' ' |  |
| 12 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :改善管理 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 15 | fsubject | 改善主题 | varchar | 255 |  | √ | ' ' | 改善主题 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: C :已审核 Z :已作废 |
| 17 | fsupservice | 供应商改善回复（服务） | varchar | 510 |  |  | ' ' | 供应商改善回复（服务） |
| 18 | fexpectdate | 预计完成时间 | timestamp | 0 |  |  | null | 预计完成时间 |
| 19 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdescription | 主题详述 | varchar | 510 |  |  | ' ' | 主题详述 |
| 21 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | ffinishdate | 改善完成时间 | timestamp | 0 |  |  | null | 改善完成时间 |
| 24 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 25 | fsupquality | 供应商改善回复（品质） | varchar | 510 |  |  | ' ' | 供应商改善回复（品质） |
| 26 | fcfmstatus | 反馈结果 | bpchar | 1 |  | √ | ' ' | 反馈结果,枚举: A :待处理 B :同意 C :驳回 |
| 27 | fservice | 改善要求（服务） | varchar | 510 |  |  | ' ' | 改善要求（服务） |
| 28 | flinkmanid | 采购方联系人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 29 | fimprovetypeid | 改善类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 30 | fsupreply | 供应商改善回复 | varchar | 510 |  |  | ' ' | 供应商改善回复 |
| 31 | fsupother | 供应商改善回复（其他） | varchar | 510 |  |  | ' ' | 供应商改善回复（其他） |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_improve_fbillno |  | fbillno |
| 2 | t_pur_improve_pkey |  | fid |
| 3 | idx_pur_improve_fbilldate |  | fbilldate |

---

## 改善管理-分表 t_pur_improve_a

- **表名称：** 改善管理-分表
- **表名：** t_pur_improve_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapproverid | 审批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapprovedate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 4 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fhandledate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 7 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 8 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 11 | fcfmopinion | 反馈说明 | varchar | 255 |  | √ | ' ' | 反馈说明 |
| 12 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fcfmdate | 反馈时间 | timestamp | 0 |  |  | null | 反馈时间 |
| 15 | fauditopinion | 审批结果说明 | varchar | 255 |  | √ | ' ' | 审批结果说明 |
| 16 | fcfmid | 反馈人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 19 | finvalidid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_improve_a_ftime |  | fcreatetime |
| 2 | t_pur_improve_a_pkey |  | fid |

---

## 改善管理-多语言表 t_pur_improve_l

- **表名称：** 改善管理-多语言表
- **表名：** t_pur_improve_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fsrcbillname | fsrcbillname | varchar | 80 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_improve_l_pkey |  | fpkid |
| 2 | idx_pur_improve_l_fid |  | fid,flocaleid |
