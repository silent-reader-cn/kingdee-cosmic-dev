# 邀请函-tnd_inviteletter

## 供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 附件-附件表 t_pds_noticesup_sup_fj

- **表名称：** 附件-附件表
- **表名：** t_pds_noticesup_sup_fj

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
| 1 | idx_pds_noticesup_sup_fj_bid |  | fbasedataid |
| 2 | pk_pds_noticesup_sup_fj |  | fpkid |
| 3 | idx_pds_noticesup_sup_fj_eid |  | fentryid |

---

## 供应商回复附件-附件表 t_pds_noticesup_sup_fj2

- **表名称：** 供应商回复附件-附件表
- **表名：** t_pds_noticesup_sup_fj2

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
| 1 | idx_pds_noticesup_sup_fj2_bid |  | fbasedataid |
| 2 | pk_pds_noticesup_sup_fj2 |  | fpkid |
| 3 | idx_pds_noticesup_sup_fj2_fid |  | fentryid |

---

## 邀请函-主表 t_pds_noticesup_sup

- **表名称：** 邀请函-主表
- **表名：** t_pds_noticesup_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | faddress | faddress | varchar | 50 |  | √ | ' ' |  |
| 3 | freplydate | 要求回复时间 | timestamp | 0 |  |  | null | 要求回复时间 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentrystatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :暂存 B :已提交 C :已发布 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fcfmdate | 回复时间 | timestamp | 0 |  |  | null | 回复时间 |
| 8 | fsupletterstype | 函件类型 | bpchar | 1 |  | √ | ' ' | 函件类型,枚举: 4 :邀请函 |
| 9 | ffsstatus | ffsstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | femailstatus | femailstatus | varchar | 30 |  | √ | ' ' |  |
| 11 | fentryprojectid | 招标项目编号 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 12 | fpurpublisher | 采购方发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 14 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 15 | frefusenote | 拒绝原因 | varchar | 255 |  | √ | ' ' | 拒绝原因 |
| 16 | fissend | 是否发送 | bpchar | 1 |  | √ | '0' | 是否发送 |
| 17 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 18 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 20 | fduty | fduty | varchar | 50 |  | √ | ' ' |  |
| 21 | fcfmstatus | 回复状态 | bpchar | 1 |  | √ | ' ' | 回复状态,枚举: A :待回复 B :已回复 C :已拒绝 D :已终止/废标 E :已定标 |
| 22 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | fmainsend | fmainsend | bpchar | 1 |  | √ | '1' |  |
| 24 | fweixinstatus | fweixinstatus | bpchar | 1 |  | √ | 'A' |  |
| 25 | fsenddate | 函件发送时间 | timestamp | 0 |  |  | null | 函件发送时间 |
| 26 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 27 | fsystemtset | fsystemtset | bpchar | 1 |  | √ | ' ' |  |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fsmsstatus | fsmsstatus | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_noticesup_sup_fid |  | fid |
| 2 | idx_pds_noticesup_sup_feid |  | fentryprojectid |
| 3 | idx_pds_noticesup_sup_fsup |  | fsupplierid |
| 4 | idx_pds_noticesup_sup_ftpye |  | fsupletterstype |
| 5 | pk_pds_noticesup_sup |  | fentryid |
