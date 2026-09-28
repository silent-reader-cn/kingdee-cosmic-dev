# LOCK控制单-pom_mrolockcontrol

## LOCK控制单-主表 t_pom_mrolockcontrol

- **表名称：** LOCK控制单-主表
- **表名：** t_pom_mrolockcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fborrowqty | 借用数量 | numeric | 23 | 10 | √ | 0 | 借用数量 |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fnotreturnqty | 未还数量 | numeric | 23 | 10 | √ | 0 | 未还数量 |
| 5 | fbizstatus | 业务状态（封存） | varchar | 50 |  | √ | ' ' | 业务状态（封存）,枚举: A :安装 B :移除 |
| 6 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 7 | flockindustry | LOCK创建人行业(封存) | varchar | 255 |  | √ | ' ' | LOCK创建人行业(封存) |
| 8 | flockpos | LOCK位置（封存） | varchar | 80 |  | √ | ' ' | LOCK位置（封存） |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fnotremoveqty | 未移除数量 | numeric | 23 | 10 | √ | 0 | 未移除数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | flockcreaterid | LOCK创建人(封存) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | flockinfoid | LOCK信息（封存） | int8 | 64 |  | √ | 0 | [LOCK信息 mpdm_lockinfo](../mpdm_files/mpdm_lockinfo.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注(封存) | varchar | 500 |  | √ | ' ' | 备注(封存) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | freturnqty | 已还数量 | numeric | 23 | 10 | √ | 0 | 已还数量 |
| 22 | ftagcount | 标识总数(封存) | int8 | 64 |  | √ | 0 | 标识总数(封存) |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | ftagcountdesc | 标识数量(封存) | varchar | 50 |  | √ | ' ' | 标识数量(封存) |
| 25 | fborrowerid | 借用人(封存) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrolockcontrol_pj |  | fprojectid |
| 2 | idx_pom_mrolockcontrol_lock |  | flockinfoid |
| 3 | pk_pom_mrolockcontrol |  | fid |

---

## 子单据体-子表 t_pom_mrolockcontrolentry

- **表名称：** 子单据体-子表
- **表名：** t_pom_mrolockcontrolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fisremove | 是否移除 | bpchar | 1 |  | √ | '0' | 是否移除 |
| 4 | ftag | 标识描述 | varchar | 255 |  | √ | ' ' | 标识描述 |
| 5 | fentrycreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fremovepersonid | 移除人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprofessionalid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 10 | fentryremovedate | 移除日期 | timestamp | 0 |  |  | null | 移除日期 |
| 11 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fpersonid | 员工工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrolockcontrolentry_fk |  | fid |
| 2 | pk_t_pom_mrolockcontrolentry |  | fdetailid |

---

## 单据体-子表 t_pom_mrolockentry

- **表名称：** 单据体-子表
- **表名：** t_pom_mrolockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fentindustry | LOCK创建人行业 | varchar | 50 |  | √ | ' ' | LOCK创建人行业 |
| 4 | fentcreater | LOCK创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fenttagcount | 标识总数 | int8 | 64 |  | √ | 0 | 标识总数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentbizstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :安装 B :移除 |
| 8 | fentborrower | 借用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | flockpos | LOCK位置 | varchar | 80 |  | √ | ' ' | LOCK位置 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flockid | LOCK信息 | int8 | 64 |  | √ | 0 | [LOCK信息 mpdm_lockinfo](../mpdm_files/mpdm_lockinfo.md) |
| 12 | ftagcdesc | 标识数量 | varchar | 50 |  | √ | ' ' | 标识数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrolry_fid |  | fid |
| 2 | pk_pom_mrolockentry |  | fentryid |
| 3 | idx_pom_mrolry_fseq |  | fseq |
