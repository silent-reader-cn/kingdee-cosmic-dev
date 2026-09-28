# 申报项目确认-tcvat_project_confirm

## 申报项目确认-主表 t_tcvat_project_confirm

- **表名称：** 申报项目确认-主表
- **表名：** t_tcvat_project_confirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | freportperiod | freportperiod | timestamp | 0 |  |  | null |  |
| 9 | ftaxplayeraptitude | 纳税人资质： | varchar | 30 |  | √ | ' ' | 纳税人资质：,枚举: zzsybnsr :一般纳税人 2 :小规模纳税人 3 :非增值税纳税人 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_project_confirm |  | fid |
| 2 | idx_tcvat_project_confirm |  | freportperiod,fstatus,forgid |

---

## 单据体-子表 t_tcvat_confirm_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_confirm_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxperiod | ftaxperiod | varchar | 50 |  | √ | ' ' |  |
| 3 | fname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 4 | fconfirmdecalare | 确认申报 | bpchar | 1 |  | √ | ' ' | 确认申报 |
| 5 | fprojectid | 项目id | varchar | 50 |  | √ | ' ' | 项目id |
| 6 | flevytype | 征收方式 | varchar | 30 |  | √ | ' ' | 征收方式,枚举: normal :一般计税 simple :简易计税 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fprepaytype | 预缴项目类型 | varchar | 30 |  | √ | ' ' | 预缴项目类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产预售 VAT_YJXMLX_004 :转让不动产 VAT_YJXMLX_005 :出租不动产 |
| 10 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 11 | fnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 12 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关(树) tpo_taxorgan_tree |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_confirm_entry_fk |  | fid |
| 2 | pk_tcvat_confirm_entry |  | fentryid |
