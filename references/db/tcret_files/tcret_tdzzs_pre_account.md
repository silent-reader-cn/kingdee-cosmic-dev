# 土地增值税预征收入台账-tcret_tdzzs_pre_account

## 土地增值税预征收入台账-主表 t_tcret_tdzzs_pre_account

- **表名称：** 土地增值税预征收入台账-主表
- **表名：** t_tcret_tdzzs_pre_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftdzzsproject | 土地增值税项目 | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fpermethod | 计征依据确定方法 | varchar | 50 |  | √ | ' ' | 计征依据确定方法,枚举: jzzs :预收款减预缴增值税 jxxs :预收款减销项税 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fistax | 特定业态是否计税 | bpchar | 1 |  | √ | '0' | 特定业态是否计税 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 14 | fbqysksum | 本期预收款 | numeric | 23 | 10 | √ | 0 | 本期预收款 |
| 15 | fyyjsjsum | 应预缴税金 | numeric | 23 | 10 | √ | 0 | 应预缴税金 |
| 16 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_pre_fbillno |  | fbillno |
| 2 | pk_tcret_tdzzs_pre_account |  | fid |

---

## 土地增值税预征明细-子表 t_tcret_tdzzs_pre_acc_det

- **表名称：** 土地增值税预征明细-子表
- **表名：** t_tcret_tdzzs_pre_acc_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbqyyjsj | 4=2X3 | numeric | 23 | 10 | √ | 0 | 4=2X3 |
| 3 | fbqysk | 1 | numeric | 23 | 10 | √ | 0 | 1 |
| 4 | fyzl | 3 | numeric | 23 | 10 | √ | 0 | 3 |
| 5 | fjsyt | 计税业态 | varchar | 50 |  | √ | ' ' | 计税业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 6 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 7 | fjzyj | 2 | numeric | 23 | 10 | √ | 0 | 2 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fxsyt | 销售业态 | int8 | 64 |  | √ | 0 | [销售业态 bastax_saleformat](../bastax_files/bastax_saleformat.md) |
| 10 | froombasedata | 房间编码 | int8 | 64 |  | √ | 0 | [房间基础信息 bastax_room](../bastax_files/bastax_room.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_pre_acc_det_fk |  | fid |
| 2 | pk_tcret_tdzzs_pre_acc_det |  | fentryid |
