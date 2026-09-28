# 疑似防重配置变更管理-fcs_suspectset_chgbill

## 签署人单据体-子表 t_fcs_suspectchgconfirm

- **表名称：** 签署人单据体-子表
- **表名：** t_fcs_suspectchgconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisclaimercontent | 风险告知内容 | varchar | 255 |  | √ | ' ' | 风险告知内容 |
| 3 | fdisclaimername | 风险告知 | varchar | 255 |  | √ | ' ' | 风险告知 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdisclaimercontent_tag | 风险告知内容_详情 | text | 0 |  |  | null | 风险告知内容_详情 |
| 6 | fconfirmtime | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 7 | fconfirmuser | 签署人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fconfirmusetype | 签署人类型 | varchar | 30 |  | √ | ' ' | 签署人类型,枚举: A :签署人 B :知悉人 |
| 10 | fdisclaimerid | fdisclaimerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_suspectchgconfirm |  | fentryid |
| 2 | idx_fcs_suspectchgconfirm |  | fid |

---

## 单据体-多语言表 t_fcs_suspect_chgbill_e_l

- **表名称：** 单据体-多语言表
- **表名：** t_fcs_suspect_chgbill_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_suspect_chgbill_e_l |  | fpkid |
| 2 | idx_fcs_suspect_chgbill_e_l |  | fentryid,flocaleid |

---

## 疑似防重配置变更管理-多语言表 t_fcs_suspectset_chgbill_l

- **表名称：** 疑似防重配置变更管理-多语言表
- **表名：** t_fcs_suspectset_chgbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fchgreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_suspectset_chgbill_l |  | fpkid |
| 2 | idx_fcs_suspectset_chgbill_l |  | fid,flocaleid |

---

## 单据体-子表 t_fcs_suspect_chgbill_e

- **表名称：** 单据体-子表
- **表名：** t_fcs_suspect_chgbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finfotype | 信息类型 | varchar | 50 |  | √ | ' ' | 信息类型,枚举: S :字符 N :数值 D :日期 L :整数 B :布尔 Z :基础 A :附件 |
| 3 | fentryfieldname | 分录字段标识 | varchar | 255 |  | √ | ' ' | 分录字段标识 |
| 4 | fsrcentryid | 源单分录ID（序号） | varchar | 255 |  |  | ' ' | 源单分录ID（序号） |
| 5 | foldvalue_tag | 变更前内容_详情 | text | 0 |  |  | null | 变更前内容_详情 |
| 6 | fsrcbillid | 源单id | varchar | 255 |  | √ | ' ' | 源单id |
| 7 | ffieldname | 字段标识 | varchar | 255 |  |  | ' ' | 字段标识 |
| 8 | foldvalue | 变更前内容 | text | 0 |  |  | null | 变更前内容 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fentryname | 分录实体标识 | varchar | 255 |  |  | ' ' | 分录实体标识 |
| 12 | fchgfield | 变更项目 | varchar | 255 |  | √ | ' ' | 变更项目 |
| 13 | fsrcbillentryid | 源单分录id | varchar | 255 |  |  | ' ' | 源单分录id |
| 14 | fnewvalue | 变更后内容 | text | 0 |  |  | null | 变更后内容 |
| 15 | fnewvalue_tag | 变更后内容_详情 | text | 0 |  |  | null | 变更后内容_详情 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrychangetype | 分录修改类型 | varchar | 50 |  | √ | ' ' | 分录修改类型,枚举: add :新增 delete :删除 change :修改 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_suspect_chgbill_e |  | fid |
| 2 | pk_fcs_suspect_chgbill_e |  | fentryid |

---

## 疑似防重配置变更管理-主表 t_fcs_suspectset_chgbill

- **表名称：** 疑似防重配置变更管理-主表
- **表名：** t_fcs_suspectset_chgbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillpk | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsuspectsetid | 疑似防重方案 | int8 | 64 |  | √ | 0 | [疑似防重配置 fcs_suspectset](../fcs_files/fcs_suspectset.md) |
| 9 | fbeforechginfo | fbeforechginfo | varchar | 255 |  | √ | ' ' |  |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbeforechginfo_tag | fbeforechginfo_tag | text | 0 |  |  | null |  |
| 13 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fchgdate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fchgreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 16 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_suspectset_chgbill |  | fid |
| 2 | idx_fcs_suspectset_chgbill |  | fbillno |
