# 预缴税源信息(暂存)-tcret_tdzzs_yjsyxx_tp

## 预缴税源信息(暂存)-主表 t_tcret_tdzzs_yjsyxx_tp

- **表名称：** 预缴税源信息(暂存)-主表
- **表名：** t_tcret_tdzzs_yjsyxx_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsbbbillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fsblimit | 税源期限 | varchar | 50 |  | √ | ' ' | 税源期限,枚举: month :月 season :季 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | ftdzzsxm | 项目名称 | int8 | 64 |  | √ | 0 | 土地增值税项目 tdm_tdzzs_clearing_unit |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fenddate | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 13 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 14 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 15 | fssbsylx | 申报表适用类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fstartdate | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 18 | fsbbbillno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 19 | fbillno | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_tdzzs_tp_fbillno |  | fbillno |
| 2 | pk_tcret_tdzzs_yjsyxx_tp |  | fid |

---

## 单据体-子表 t_tcret_tdzzs_yjsyxx_entp

- **表名称：** 单据体-子表
- **表名：** t_tcret_tdzzs_yjsyxx_entp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemno |  | varchar | 50 |  | √ | ' ' |  |
| 3 | fbuildingtype | 1 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 4 | fswjqtsr | 5 | numeric | 23 | 10 | √ | 0 | 5 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fyssr | 3=4+5+6 | numeric | 23 | 10 | √ | 0 | 3=4+5+6 |
| 7 | fbqybtse | 10=8-9 | numeric | 23 | 10 | √ | 0 | 10=8-9 |
| 8 | fupdaco | 触发更新字段 | varchar | 50 |  | √ | ' ' | 触发更新字段 |
| 9 | fhbsr | 4 | numeric | 23 | 10 | √ | 0 | 4 |
| 10 | fstxssr | 6 | numeric | 23 | 10 | √ | 0 | 6 |
| 11 | fyzl | 7 | numeric | 23 | 10 | √ | 0 | 7 |
| 12 | fynse | 8=3*7 | numeric | 23 | 10 | √ | 0 | 8=3*7 |
| 13 | fsubbuildingtype | 2 | int8 | 64 |  | √ | 0 | 房产类型子目 tcret_tdzzs_fclxzm |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fbqyjse | 9 | numeric | 23 | 10 | √ | 0 | 9 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_yjsyxx_entp_fk |  | fid |
| 2 | pk_tcret_tdzzs_yjsyxx_entp |  | fentryid |
